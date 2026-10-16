"""Locate Bash explicitly on Windows and pass the native hook stdin unchanged."""
import os
import json
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    try:
        if sys.platform == "win32":
            bash = str(Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/bin/bash.exe")
        else:
            bash = shutil.which("bash")
        if not bash or not Path(bash).is_file():
            raise OSError("Git Bash (Windows) or Bash (Linux/WSL) is required")
        script = Path(__file__).resolve().with_name("pom-security.sh")
        completed = subprocess.run([bash, str(script)], timeout=515)
        if completed.returncode:
            raise OSError(f"Bash hook process exited {completed.returncode}")
        return 0
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"POM hook launcher blocked this tool: {exc}", file=sys.stderr)
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                         "permissionDecision": "deny", "permissionDecisionReason": str(exc)}}))
        return 0


if __name__ == "__main__":
    sys.exit(main())
