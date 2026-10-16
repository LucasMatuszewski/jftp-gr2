"""Unrelated events must return before starting Bash or the audit backend."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import types
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("fast_pom_launch", HERE / "launch.py")
launch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launch)


class FastFilterTests(unittest.TestCase):
    def call(self, tool="Bash", data=None, raw=None):
        if raw is None:
            raw = json.dumps({"hook_event_name": "PreToolUse", "cwd": str(HERE.parents[1]),
                              "tool_name": tool, "tool_input": data or {"command": "git status --short"}}).encode()
        output = io.StringIO()
        with patch.object(launch.sys, "stdin", types.SimpleNamespace(buffer=io.BytesIO(raw))), \
                patch.object(launch.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)) as run, \
                contextlib.redirect_stdout(output), contextlib.redirect_stderr(io.StringIO()):
            code = launch.main()
        return code, output.getvalue(), run.call_args_list, raw

    def test_unrelated_inputs_do_not_start_bash(self):
        cases = [("Bash", {"command": "git status --short"}),
                 ("Bash", {"command": "cat pom.xml"}),
                 ("Bash", {"command": "Get-Content pom.xml"}),
                 ("Bash", {"command": "git diff -- pom.xml"}),
                 ("Write", {"file_path": "README.md", "content": "See pom.xml"}),
                 ("Edit", {"file_path": "src/Main.java", "old_string": "pom.xml", "new_string": "POM.XML"}),
                 ("apply_patch", {"command": "*** Begin Patch\n*** Add File: README.md\n+Document pom.xml\n*** End Patch"}),
                 ("mcp__context7__query_docs", {"query": "Java collection classes"})]
        for tool, data in cases:
            with self.subTest(tool=tool, data=data):
                code, output, calls, _ = self.call(tool, data)
                self.assertEqual([], calls, "Unrelated input must not start Bash")
                self.assertEqual(0, code)
                self.assertEqual("", output)

    def test_candidates_forward_the_exact_payload_once(self):
        cases = [("Bash", {"command": "echo bad > pom.xml"}),
                 ("Bash", {"command": "mvn versions:use-latest-versions"}),
                 ("Bash", {"command": "mvn release:prepare"}),
                 ("Bash", {"command": "mvn -f build.xml validate"}),
                 ("Bash", {"command": "cat pom.xml | Set-Content pom.xml"}),
                 ("Write", {"file_path": "module\\POM.XML", "content": "<project/>"}),
                 ("Edit", {"file_path": "pom.xml", "old_string": "1", "new_string": "2"}),
                 ("apply_patch", {"command": "*** Begin Patch\n*** Update File: candidate.xml\n*** Move to: module/pom.xml\n@@\n-a\n+b\n*** End Patch"}),
                 ("apply_patch", {"command": "*** Begin Patch\n*** Delete File: module/pom.xml\n*** End Patch"}),
                 ("mcp__fs__write", {"path": "pom.xml", "content": "<project/>"})]
        for tool, data in cases:
            with self.subTest(tool=tool, data=data):
                code, output, calls, raw = self.call(tool, data)
                self.assertEqual(1, len(calls))
                self.assertEqual(raw, calls[0].kwargs.get("input"), "Forward JSON unchanged after inspection")
                self.assertEqual(0, code)

    def test_invalid_payloads_are_not_silently_ignored(self):
        for raw in (b"not JSON", b"{}", b"[]", b"x" * (1024 * 1024 + 1)):
            with self.subTest(raw_length=len(raw)):
                code, output, calls, _ = self.call(raw=raw)
                self.assertEqual([], calls)
                self.assertEqual(0, code)
                self.assertEqual("deny", json.loads(output)["hookSpecificOutput"]["permissionDecision"])

    def test_escaped_filename_is_inspected(self):
        raw = json.dumps({"hook_event_name": "PreToolUse", "cwd": str(HERE.parents[1]),
                          "tool_name": "Write", "tool_input": {"file_path": "pom.xml", "content": "<project/>"}}).replace("pom.xml", "pom\\u002exml").encode()
        self.assertEqual(1, len(self.call(raw=raw)[2]))

    def test_matcher_excludes_non_file_tools_but_keeps_shell_and_mcp(self):
        configuration = json.loads((HERE.parent / "hooks.json").read_text(encoding="utf-8"))
        matcher = configuration["hooks"]["PreToolUse"][0]["matcher"]
        for tool in ("update_plan", "spawn_agent", "Agent", "wait", "read_mcp_resource"):
            self.assertIsNone(re.search(matcher, tool), tool)
        for tool in ("Bash", "apply_patch", "Edit", "Write", "mcp__fs__write_file", "mcp__context7__query_docs"):
            self.assertIsNotNone(re.search(matcher, tool), tool)


if __name__ == "__main__":
    unittest.main()
