"""Real Bash/Windows command wiring checks; no model calls or app POM edits."""
import json
import contextlib
import importlib.util
import io
import os
import os
from pathlib import Path
import shutil
import subprocess
import types
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / ".codex/hooks/pom-security.sh"
BASH = Path("C:/Program Files/Git/bin/bash.exe") if os.name == "nt" else shutil.which("bash")


class LauncherTests(unittest.TestCase):
    def test_candidate_invokes_preview_backend_once(self):
        # Unit process double counts backend invocations; no endpoint is mocked.
        with tempfile.TemporaryDirectory() as directory:
            stub = Path(directory) / "backend.sh"
            log = Path(directory) / "calls.log"
            stub.write_text('python3() {\n'
                            '  printf "backend\\n" >> "$JFTP_BACKEND_CALL_LOG"\n'
                            '  if [[ " $* " == *" --classify "* ]]; then printf "inspect\\n"; else cat >/dev/null; fi\n'
                            '}\n', encoding="utf-8", newline="\n")
            environment = os.environ.copy()
            environment.update(BASH_ENV=stub.as_posix(), JFTP_BACKEND_CALL_LOG=log.as_posix())
            payload = json.dumps({"hook_event_name": "PreToolUse", "cwd": str(ROOT),
                                  "tool_name": "Write", "tool_input": {"file_path": "pom.xml", "content": "<project/>"}})
            result = subprocess.run([str(BASH), str(SCRIPT)], input=payload, text=True, capture_output=True,
                                    cwd=ROOT, env=environment, timeout=30)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertEqual(["backend"], log.read_text(encoding="utf-8").splitlines())

    def test_bootstrap_failures_are_explicit_denials(self):
        spec = importlib.util.spec_from_file_location("pom_launch", SCRIPT.with_name("launch.py"))
        launch = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(launch)
        for failure in (OSError("synthetic spawn failure"), subprocess.TimeoutExpired("bash", 515)):
            output = io.StringIO()
            event = json.dumps({"hook_event_name": "PreToolUse", "cwd": str(ROOT), "tool_name": "Bash",
                                "tool_input": {"command": "echo bad > pom.xml"}}).encode()
            with patch.object(launch.sys, "stdin", types.SimpleNamespace(buffer=io.BytesIO(event))), patch.object(launch.subprocess, "run", side_effect=failure), contextlib.redirect_stdout(output), contextlib.redirect_stderr(io.StringIO()):
                code = launch.main()
            self.assertEqual(0, code)
            self.assertEqual("deny", json.loads(output.getvalue())["hookSpecificOutput"]["permissionDecision"])

    def invoke(self, tool, data, configured=False, cwd=None):
        payload = json.dumps({"hook_event_name": "PreToolUse", "cwd": str(cwd or ROOT),
                              "tool_name": tool, "tool_input": data})
        if configured:
            config = json.loads((ROOT / ".codex/hooks.json").read_text(encoding="utf-8"))
            hook = config["hooks"]["PreToolUse"][0]["hooks"][0]
            if os.name == "nt":
                return subprocess.run(hook.get("commandWindows", hook["command"]), input=payload, text=True,
                                      capture_output=True, shell=True, cwd=cwd or ROOT, timeout=30)
            command = [BASH, "-c", hook["command"]]
        else:
            command = [str(BASH), str(SCRIPT)]
        return subprocess.run(command, input=payload, text=True, capture_output=True,
                              cwd=cwd or ROOT, timeout=30)

    def test_unrelated_tool_does_not_launch_models(self):
        completed = self.invoke("Bash", {"command": "git status --short"})
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("", completed.stdout)

    def test_shell_write_is_blocked_before_execution(self):
        completed = self.invoke("Bash", {"command": "echo never-run > pom.xml"})
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("deny", json.loads(completed.stdout)["hookSpecificOutput"]["permissionDecision"])
        self.assertIn("apply_patch", json.loads(completed.stdout)["hookSpecificOutput"]["permissionDecisionReason"])

    def test_invalid_json_blocks(self):
        completed = subprocess.run([str(BASH), str(SCRIPT)], input="not JSON", text=True,
                                   capture_output=True, cwd=ROOT, timeout=30)
        self.assertEqual(0, completed.returncode)
        self.assertEqual("deny", json.loads(completed.stdout)["hookSpecificOutput"]["permissionDecision"])

    def test_configured_windows_or_unix_command_from_subdirectory(self):
        completed = self.invoke("Bash", {"command": "git status --short"}, configured=True, cwd=ROOT / "src")
        self.assertEqual(0, completed.returncode, completed.stderr)

    def test_configured_command_preserves_block(self):
        completed = self.invoke("Bash", {"command": "echo never-run > pom.xml"}, configured=True)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("deny", json.loads(completed.stdout)["hookSpecificOutput"]["permissionDecision"])


if __name__ == "__main__":
    unittest.main()
