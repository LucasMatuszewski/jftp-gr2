"""Opt-in real-model hook smoke: python -B .codex/hooks/tests/live_smoke.py risky|removal.

Uses existing Codex login and real web search. Costs model usage. Never edits the
application POM. The synthetic fixture is removed; audit evidence stays in TEMP.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[3]
MODE = sys.argv[1] if len(sys.argv) == 2 else ""
if MODE not in ("risky", "removal"):
    raise SystemExit("Usage: live_smoke.py risky|removal")

shell = Path("C:/Program Files/Git/bin/bash.exe") if sys.platform == "win32" else "bash"
head = ('<project xmlns="http://maven.apache.org/POM/4.0.0">\n'
        '<modelVersion>4.0.0</modelVersion>\n'
        '<groupId>example.synthetic</groupId><artifactId>security-hook-smoke</artifactId><version>1</version>\n'
        '<dependencies>\n')
dependency = ('<dependency><groupId>org.apache.logging.log4j</groupId>'
              '<artifactId>log4j-core</artifactId><version>2.14.1</version></dependency>\n')
tail = '</dependencies>\n</project>\n'
before = head + (dependency if MODE == "removal" else "") + tail
after = head + (dependency if MODE == "risky" else "") + tail

with tempfile.TemporaryDirectory(prefix="live-pom-", dir=Path(__file__).parent) as fixture:
    path = Path(fixture) / "pom.xml"
    path.write_text(before, encoding="utf-8")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    payload = {"hook_event_name": "PreToolUse", "tool_name": "Write", "cwd": fixture,
               "tool_input": {"file_path": "pom.xml", "content": after}}
    completed = subprocess.run([str(shell), str(ROOT / ".codex/hooks/pom-security.sh")],
                               input=json.dumps(payload), text=True, encoding="utf-8",
                               capture_output=True, timeout=520, cwd=ROOT)
    print(completed.stdout)
    if completed.stderr:
        print(completed.stderr, file=sys.stderr)
    if completed.returncode:
        raise SystemExit(f"Hook failed: exit {completed.returncode}")
    output = json.loads(completed.stdout)["hookSpecificOutput"]
    expected = "deny" if MODE == "risky" else None
    if output.get("permissionDecision") != expected:
        raise SystemExit(f"Unexpected verdict for {MODE}")
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise SystemExit("Hook modified the synthetic source POM")
    if MODE == "risky" and "high risk" not in output.get("permissionDecisionReason", "") and "critical risk" not in output.get("permissionDecisionReason", ""):
        raise SystemExit("A research failure is not a demonstrated vulnerability block")
    print(f"PASS: {MODE}, two real Codex reviews, source POM unchanged")
