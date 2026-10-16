"""Measure the configured hook on synthetic inputs; never starts model reviews.

python -B .codex/hooks/tests/benchmark_hook.py --samples 9 --output <outside-repo.json>
"""
import argparse
import json
import os
from pathlib import Path
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
parser = argparse.ArgumentParser()
parser.add_argument("--samples", type=int, default=9)
parser.add_argument("--output", type=Path, required=True)
options = parser.parse_args()
if options.samples < 3 or options.output.resolve().is_relative_to(ROOT):
    raise SystemExit("Use at least three samples and an output path outside the checkout")
handler = json.loads((ROOT / ".codex/hooks.json").read_text(encoding="utf-8"))["hooks"]["PreToolUse"][0]["hooks"][0]
command = handler.get("commandWindows", handler["command"]) if os.name == "nt" else handler["command"]
cases = {
    "unrelated_shell": ("Bash", {"command": "git status --short"}),
    "unrelated_patch": ("apply_patch", {"command": "*** Begin Patch\n*** Add File: sample.txt\n+Document pom.xml here\n*** End Patch"}),
    "unrelated_mcp": ("mcp__docs__query", {"query": "Java collections"}),
}
results = {}
for name, (tool, data) in cases.items():
    payload = json.dumps({"hook_event_name": "PreToolUse", "cwd": str(ROOT),
                          "tool_name": tool, "tool_input": data})
    elapsed = []
    for sample in range(options.samples + 1):
        start = time.perf_counter()
        completed = subprocess.run(command, input=payload, text=True, capture_output=True,
                                   shell=True, cwd=ROOT, timeout=30)
        duration = (time.perf_counter() - start) * 1000
        if completed.returncode or completed.stdout.strip():
            raise SystemExit(f"Unexpected result for unrelated input {name}: {completed.stderr}")
        if sample:  # Exclude one warm-up run per input; include process startup.
            elapsed.append(round(duration, 2))
    results[name] = {"samples_ms": elapsed, "median_ms": round(statistics.median(elapsed), 2)}
report = {"measurement": "configured hook command, including process startup; one warm-up excluded",
          "samples_per_case": options.samples, "results": results}
options.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report, indent=2))
