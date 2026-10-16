"""Skip unrelated events before launching Bash and the full POM validator."""
import os
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

MAX_BYTES = 1024 * 1024
SHELL_TOOLS = ("Bash", "exec_command", "shell", "shell_command")
MAVEN_MUTATION = re.compile(r"\b(?:versions|release):|\b(?:flatten|moditect):|\b(?:mvn|mvnw)(?:\.cmd)?\b.*(?:\s)(?:-f|--file)(?:\s|=|$)", re.I)


def is_pom(name):
    return name.replace("\\", "/").rsplit("/", 1)[-1].lower() == "pom.xml"


def shell_candidate(command):
    return "pom.xml" in command.lower() or bool(MAVEN_MUTATION.search(command))


def simple_read(command):
    # Shared with the full validator: never allow pipes or command substitution.
    if re.search(r"[;|&<>`$\r\n]", command):
        return False
    return bool(re.fullmatch(
        r"\s*(?:(?:cat|Get-Content|type)\s+(?:--\s+)?[\w./\\:\- ]*pom\.xml|"
        r"git\s+diff(?:\s+--(?:stat|numstat|name-only|cached))*\s+--\s+[\w./\\:\- ]*pom\.xml)\s*",
        command, re.I))


def should_inspect(event):
    """Cheap input-only gate: no POM reads, XML parsing, Bash or Codex calls."""
    if (not isinstance(event, dict) or event.get("hook_event_name") != "PreToolUse"
            or not isinstance(event.get("cwd"), str) or not isinstance(event.get("tool_name"), str)
            or not isinstance(event.get("tool_input"), dict)):
        raise ValueError("Invalid PreToolUse event; cannot inspect its arguments")
    tool, data = event["tool_name"], event["tool_input"]
    if tool in ("Edit", "Write"):
        path = data.get("file_path")
        return not isinstance(path, str) or is_pom(path)
    if tool == "apply_patch":
        command = data.get("command")
        if not isinstance(command, str):
            return True
        paths = [match.group(1) for line in command.splitlines()
                 if (match := re.fullmatch(r"\*\*\* (?:(?:Add|Update|Delete) File|Move to): (.+)", line))]
        if paths:
            return any(is_pom(path) for path in paths)
        return "pom.xml" in command.lower()  # Malformed POM patch needs full validation.
    if tool in SHELL_TOOLS:
        command = data.get("command", data.get("cmd"))
        return not isinstance(command, str) or (shell_candidate(command) and not simple_read(command))
    return "pom.xml" in json.dumps(data).lower()


def main():
    try:
        raw = sys.stdin.buffer.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("Hook input is too large")
        event = json.loads(raw.decode("utf-8-sig"))
        if not should_inspect(event):
            return 0
        if sys.platform == "win32":
            bash = str(Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/bin/bash.exe")
        else:
            bash = shutil.which("bash")
        if not bash or not Path(bash).is_file():
            raise OSError("Git Bash (Windows) or Bash (Linux/WSL) is required")
        script = Path(__file__).resolve().with_name("pom-security.sh")
        completed = subprocess.run([bash, str(script)], input=raw, timeout=515)
        if completed.returncode:
            raise OSError(f"Bash hook process exited {completed.returncode}")
        return 0
    except (OSError, ValueError, RecursionError, subprocess.SubprocessError) as exc:
        print(f"POM hook launcher blocked this tool: {exc}", file=sys.stderr)
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                         "permissionDecision": "deny", "permissionDecisionReason": str(exc)}}))
        return 0


if __name__ == "__main__":
    sys.exit(main())
