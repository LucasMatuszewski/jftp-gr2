"""Opt-in native app-server smoke using the existing Codex login.

Requires user trust in /hooks. Uses the project's existing permissions.
No stored trust or user/project configuration is changed.
"""
import argparse
import json
import os
from pathlib import Path
import tempfile
from inspect_hooks import AppServer

ROOT = Path(__file__).resolve().parents[3]
parser = argparse.ArgumentParser()
parser.add_argument("--reviewed-hook", action="store_true",
                    help="Test the sole reviewed project hook for this invocation without persisting trust")
parser.add_argument("--case", choices=("shell", "risky"), default="shell")
options = parser.parse_args()
evidence = Path(tempfile.mkdtemp(prefix="jftp-pom-native-"))
environment = os.environ.copy()
for name in ("CODEX_THREAD_ID", "CODEX_SESSION_ID", "CODEX_DAEMON_SHUTDOWN_SOCKET", "CODEX_PERMISSION_PROFILE", "CODEX_CI"):
    environment.pop(name, None)
environment["JFTP_POM_TRACE_FILE"] = str(evidence / "hook-launch.log")
print("Evidence:", evidence, flush=True)

with AppServer(environment=environment, evidence=evidence) as server:
    metadata = server.rpc(2, "hooks/list", {"cwds": [str(ROOT)]})["data"][0]
    matches = [hook for hook in metadata["hooks"]
               if Path(hook["sourcePath"]) == ROOT / ".codex/hooks.json"]
    if metadata["errors"] or metadata["warnings"] or len(matches) != 1:
        raise SystemExit("Expected exactly one project hook without load errors")
    hook = matches[0]
    if not hook["enabled"] or (hook["trustStatus"] not in ("trusted", "managed") and not options.reviewed_hook):
        raise SystemExit("Trust and enable .codex/hooks.json in /hooks before native validation")
    if options.reviewed_hook and len(metadata["hooks"]) != 1:
        raise SystemExit("Reviewed-hook test requires this project hook to be the only discovered hook")
    settings = {"bypass_hook_trust": True} if options.reviewed_hook else {}
    thread = server.rpc(3, "thread/start", {"cwd": str(ROOT), "approvalPolicy": "never", "ephemeral": True, "config": settings})
    thread_id = thread["thread"]["id"]
    with tempfile.TemporaryDirectory(prefix="native-pom-", dir=Path(__file__).parent) as fixture:
        target = Path(fixture) / "pom.xml"
        command = "echo native-hook-probe > " + target.as_posix()
        before = None
        if options.case == "risky":
            before = ('<project xmlns="http://maven.apache.org/POM/4.0.0">\n'
                      '<modelVersion>4.0.0</modelVersion>\n'
                      '<groupId>example.synthetic</groupId><artifactId>hook</artifactId><version>1</version>\n'
                      '<dependencies/>\n</project>\n')
            target.write_text(before, encoding="utf-8")
            path = target.relative_to(ROOT).as_posix()
            patch = ('*** Begin Patch\n*** Update File: ' + path + '\n@@\n-<dependencies/>\n'
                     '+<dependencies><dependency><groupId>org.apache.logging.log4j</groupId>'
                     '<artifactId>log4j-core</artifactId><version>2.14.1</version></dependency></dependencies>\n'
                     '*** End Patch')
            action = "Then call apply_patch with exactly this patch:\n" + patch + "\n"
        else:
            action = "Then run one separate shell call: " + command + ". "
        prompt = ("Run exactly two action calls. First run a shell call: echo JFTP_HOOK_BASELINE . "
                  + action + "The PreToolUse hook should allow the first and deny the second. "
                  "If code mode yields a running cell, use wait calls until the actual final tool "
                  "result arrives; the security audit can take several minutes. A running cell is "
                  "not a completed action. Stop only after that result. Do not inspect files, "
                  "retry, delegate, alter the provided patch or make any other action call. "
                  "This is authorized validation in an isolated synthetic fixture.")
        server.rpc(4, "turn/start", {"threadId": thread_id, "input": [{"type": "text", "text": prompt}]})
        denied, baseline, turn_done = False, False, False
        active_hooks = set()
        while True:
            message = server.receive(timeout=530)
            if message.get("method") == "hook/started":
                active_hooks.add(message["params"]["run"]["id"])
            if message.get("method") == "hook/completed":
                run = message["params"]["run"]
                active_hooks.discard(run["id"])
                if run["status"] == "blocked":
                    text = json.dumps(message)
                    if options.case == "shell" and "POM-related shell command cannot be previewed safely" in text:
                        denied = True
                    if options.case == "risky" and any(label in text for label in ("critical risk", "high risk")):
                        denied = True
            if message.get("method") == "item/completed":
                item = message.get("params", {}).get("item", {})
                if item.get("type") == "commandExecution" and "JFTP_HOOK_BASELINE" in item.get("aggregatedOutput", ""):
                    baseline = True
            if message.get("method") == "turn/completed":
                turn_done = True
            if turn_done and not active_hooks:
                break
        if options.case == "shell" and target.exists():
            raise SystemExit("FAIL: synthetic POM was created")
        if options.case == "risky" and target.read_text(encoding="utf-8") != before:
            raise SystemExit("FAIL: synthetic POM was changed")
        if not denied or not (evidence / "hook-launch.log").exists():
            raise SystemExit("FAIL: no native completed hook with the expected denial")
        if not baseline:
            raise SystemExit("FAIL: the unrelated shell command was not allowed")
        if len((evidence / "hook-launch.log").read_text(encoding="utf-8").splitlines()) != 1:
            raise SystemExit("FAIL: unrelated shell call started Bash, or the candidate was launched repeatedly")
        print(f"PASS: native PreToolUse allowed a normal command and denied {options.case} POM change")
