"""Behavior tests for the POM gate. All POMs and verdicts are synthetic."""
import importlib.util
import json
from pathlib import Path
import tempfile
import sys
import unittest
from unittest.mock import patch
import subprocess


MODULE = Path(__file__).resolve().parents[1] / "pom_security.py"
sys.path.insert(0, str(MODULE.parent))
spec = importlib.util.spec_from_file_location("pom_security", MODULE)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


def pom(version="1.0", extra=""):
    return ("<project>\n<modelVersion>4.0.0</modelVersion>\n"
            "<groupId>example</groupId><artifactId>demo</artifactId><version>1</version>\n"
            f"<properties><library.version>{version}</library.version></properties>\n"
            "<dependencies><dependency><groupId>example</groupId><artifactId>library</artifactId>"
            "<version>${library.version}</version></dependency></dependencies>\n"
            f"{extra}\n</project>\n")


def verdict(role="vulnerabilities", status="allow", severity=None):
    return {"role": role, "status": status, "summary": "Synthetic unit verdict",
            "checked_at": guard.today(),
            "sources": ["https://example.org/synthetic-advisory"],
            "findings": [] if severity is None else [{
                "severity": severity, "coordinate": "example:library:2.0",
                "risk": "Synthetic risk", "advisory_ids": ["SYNTHETIC-001"],
                "introduced_by_change": True, "recommendation": "Do not add",
                "urls": ["https://example.org/synthetic-advisory"]}]}


class PomGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "pom.xml").write_text(pom(), encoding="utf-8")

    def event(self, tool, data, **extra):
        return {"hook_event_name": "PreToolUse", "cwd": str(self.root),
                "tool_name": tool, "tool_input": data, **extra}

    def patch(self, old="1.0", new="2.0", path="pom.xml"):
        return self.event("apply_patch", {"command": (
            f"*** Begin Patch\n*** Update File: {path}\n@@\n"
            f"-<properties><library.version>{old}</library.version></properties>\n"
            f"+<properties><library.version>{new}</library.version></properties>\n"
            "*** End Patch")})

    def test_unrelated_patch_does_not_start_review(self):
        event = self.event("apply_patch", {"command": "*** Begin Patch\n*** Add File: a.txt\n+hello\n*** End Patch"})
        self.assertEqual([], guard.prepare(event, self.root))

    def test_property_change_is_reviewed_before_any_write(self):
        changes = guard.prepare(self.patch(), self.root)
        self.assertEqual(1, len(changes))
        self.assertIn("2.0", changes[0]["after"])
        self.assertIn("1.0", changes[0]["before"])
        self.assertEqual(pom(), (self.root / "pom.xml").read_text(encoding="utf-8"))

    def test_nested_pom_from_subdirectory(self):
        folder = self.root / "module"
        folder.mkdir()
        (folder / "pom.xml").write_text(pom(), encoding="utf-8")
        event = self.patch()
        event["cwd"] = str(folder)
        self.assertEqual("module/pom.xml", guard.prepare(event, self.root)[0]["path"])

    def test_new_pom_is_reviewed(self):
        patch = "*** Begin Patch\n*** Add File: new/pom.xml\n" + "\n".join("+" + line for line in pom().splitlines()) + "\n*** End Patch"
        change = guard.prepare(self.event("apply_patch", {"command": patch}), self.root)[0]
        self.assertIsNone(change["before"])
        self.assertEqual("new/pom.xml", change["path"])

    def test_delete_and_move_pom_are_reviewed(self):
        deletion = "*** Begin Patch\n*** Delete File: pom.xml\n*** End Patch"
        self.assertIsNone(guard.prepare(self.event("apply_patch", {"command": deletion}), self.root)[0]["after"])
        moved = self.patch()
        moved["tool_input"]["command"] = moved["tool_input"]["command"].replace("*** Update File: pom.xml", "*** Update File: pom.xml\n*** Move to: moved/pom.xml")
        self.assertEqual("moved/pom.xml", guard.prepare(moved, self.root)[0]["path"])

    def test_move_non_pom_to_pom_is_reviewed(self):
        (self.root / "candidate.xml").write_text(pom(), encoding="utf-8")
        event = self.patch(path="candidate.xml")
        event["tool_input"]["command"] = event["tool_input"]["command"].replace("*** Update File: candidate.xml", "*** Update File: candidate.xml\n*** Move to: module/pom.xml")
        self.assertEqual(1, len(guard.prepare(event, self.root)))

    def test_comments_and_formatting_do_not_start_review(self):
        self.assertEqual([], guard.prepare(self.event("Write", {"file_path": "pom.xml", "content": pom().replace("<project>", "<project>\n<!-- comment -->")}), self.root))

    def test_edit_and_write_compatibility(self):
        edit = self.event("Edit", {"file_path": "pom.xml", "old_string": "<library.version>1.0", "new_string": "<library.version>2.0"})
        write = self.event("Write", {"file_path": "pom.xml", "content": pom("2.0")})
        self.assertEqual(guard.prepare(edit, self.root)[0]["after"], guard.prepare(write, self.root)[0]["after"])

    def test_multiple_poms_in_one_patch(self):
        (self.root / "module").mkdir()
        (self.root / "module/pom.xml").write_text(pom(), encoding="utf-8")
        first = self.patch()["tool_input"]["command"]
        second = self.patch(path="module/pom.xml")["tool_input"]["command"]
        combined = first.replace("*** End Patch", second.replace("*** Begin Patch\n", ""))
        self.assertEqual(2, len(guard.prepare(self.event("apply_patch", {"command": combined}), self.root)))

    def test_parent_repository_profile_plugin_and_bom_changes_are_reviewed(self):
        extras = ["<parent><groupId>x</groupId><artifactId>parent</artifactId><version>2</version></parent>",
                  "<repositories><repository><url>http://bad.example</url></repository></repositories>",
                  "<profiles><profile><id>test</id><properties><v>2</v></properties></profile></profiles>",
                  "<build><plugins><plugin><artifactId>unknown</artifactId><version>2</version></plugin></plugins></build>",
                  "<dependencyManagement><dependencies><dependency><artifactId>bom</artifactId><version>2</version></dependency></dependencies></dependencyManagement>"]
        for extra in extras:
            with self.subTest(extra=extra):
                self.assertEqual(1, len(guard.prepare(self.event("Write", {"file_path": "pom.xml", "content": pom(extra=extra)}), self.root)))

    def test_unpreviewable_shell_and_mcp_pom_writes_are_blocked(self):
        for tool, data in [("Bash", {"command": "python change.py pom.xml"}),
                           ("Bash", {"command": "mvn versions:set -DnewVersion=2"}),
                           ("Bash", {"command": "mvn -f build.xml validate"}),
                           ("Bash", {"command": "Set-Content POM.XML 'bad'"}),
                           ("mcp__fs__write_file", {"path": "pom.xml", "content": pom("2.0")})]:
            with self.subTest(tool=tool, data=data):
                with self.assertRaises(guard.Block):
                    guard.prepare(self.event(tool, data), self.root)

    def test_simple_read_and_unrelated_shell_are_allowed(self):
        for command in ["git status --short", "cat pom.xml", "Get-Content pom.xml", "git diff -- pom.xml"]:
            self.assertEqual([], guard.prepare(self.event("Bash", {"command": command}), self.root))

    def test_read_command_with_side_effects_is_not_allowlisted(self):
        for command in ["cat pom.xml; echo bad > pom.xml", "Get-Content pom.xml | Set-Content pom.xml", "git diff --output=pom.xml", "cat $(touch pom.xml)"]:
            with self.assertRaises(guard.Block):
                guard.prepare(self.event("Bash", {"command": command}), self.root)

    def test_malformed_xml_and_entity_expansion_are_blocked(self):
        for content in ["<project>", '<!DOCTYPE project [<!ENTITY x "bad">]><project>&x;</project>', "<not-a-pom/>"]:
            with self.assertRaises(guard.Block):
                guard.prepare(self.event("Write", {"file_path": "pom.xml", "content": content}), self.root)

    def test_missing_and_ambiguous_patch_context_are_blocked(self):
        for old in ["nonexistent", "1.0"]:
            if old == "1.0":
                (self.root / "pom.xml").write_text(pom().replace("</project>", "<properties><library.version>1.0</library.version></properties>\n</project>"), encoding="utf-8")
            with self.assertRaises(guard.Block):
                guard.prepare(self.patch(old=old), self.root)

    def test_outside_root_is_blocked(self):
        with self.assertRaises(guard.Block):
            guard.prepare(self.patch(path="../pom.xml"), self.root)

    def test_duplicate_pom_operations_are_blocked(self):
        patch = self.patch()["tool_input"]["command"]
        duplicate = patch.replace("*** End Patch", patch.replace("*** Begin Patch\n", ""))
        with self.assertRaises(guard.Block):
            guard.prepare(self.event("apply_patch", {"command": duplicate}), self.root)

    def test_invalid_event_is_blocked(self):
        for data in [None, {}, {"hook_event_name": "PreToolUse", "tool_name": "apply_patch"}]:
            with self.assertRaises(guard.Block):
                guard.prepare(data, self.root)

    def test_valid_verdict_allows(self):
        self.assertEqual("allow", guard.validate_verdict(verdict(), "vulnerabilities")["status"])

    def test_current_utc_timestamp_is_accepted(self):
        report = verdict()
        report["checked_at"] = guard.today() + "T00:00:00Z"
        self.assertEqual("allow", guard.validate_verdict(report, "vulnerabilities")["status"])

    def test_invalid_or_timezone_ambiguous_timestamps_block(self):
        for timestamp in [guard.today() + "Tinvalid", guard.today() + "T00:00:00"]:
            report = verdict()
            report["checked_at"] = timestamp
            with self.assertRaises(guard.Block):
                guard.validate_verdict(report, "vulnerabilities")

    def test_unknown_without_dependency_coordinates_is_fail_closed(self):
        report = verdict(status="unknown")
        report["findings"] = []
        with self.assertRaises(guard.Block):
            guard.validate_verdict(report, "vulnerabilities")

    def test_high_risk_blocks_even_if_agent_says_allow(self):
        with self.assertRaises(guard.Block):
            guard.validate_verdict(verdict(severity="high"), "vulnerabilities")

    def test_missing_evidence_unknown_and_stale_verdicts_block(self):
        for field, value in [("status", "unknown"), ("status", "block"), ("sources", []),
                             ("sources", ["invented"]), ("checked_at", "2000-01-01"),
                             ("findings", "none"), ("role", "other")]:
            report = verdict()
            report[field] = value
            with self.subTest(field=field, value=value):
                with self.assertRaises(guard.Block):
                    guard.validate_verdict(report, "vulnerabilities")

    def test_source_change_during_review_blocks(self):
        changes = guard.prepare(self.patch(), self.root)
        (self.root / "pom.xml").write_text(pom("3.0"), encoding="utf-8")
        with self.assertRaises(guard.Block):
            guard.check_unchanged(changes, self.root)

    def test_cli_reviews_are_isolated_and_read_only(self):
        command = guard.review_command("codex", self.root, self.root / "schema.json", self.root / "out.json", "selected-model")
        self.assertIn("--ignore-user-config", command)
        self.assertIn("--ephemeral", command)
        self.assertEqual("read-only", command[command.index("--sandbox") + 1])
        self.assertEqual("hooks", command[command.index("--disable") + 1])
        self.assertEqual("selected-model", command[command.index("--model") + 1])
        self.assertNotIn("--dangerously-bypass-hook-trust", command)

    def test_cli_errors_timeouts_and_malformed_reports_block(self):
        # Process failures, not endpoint/database doubles: no HTTP mock is created.
        scenarios = [subprocess.CompletedProcess([], 1, "", "synthetic process failure"),
                     subprocess.CompletedProcess([], 0, "not JSONL", ""),
                     subprocess.TimeoutExpired("codex", 240)]
        for outcome in scenarios:
            evidence = self.root / str(len(list(self.root.iterdir())))
            evidence.mkdir()
            with self.subTest(outcome=outcome), patch.object(guard.shutil, "which", return_value="codex"), patch.object(guard.subprocess, "run") as run:
                if isinstance(outcome, Exception):
                    run.side_effect = outcome
                else:
                    run.return_value = outcome
                with self.assertRaises(guard.Block):
                    guard.run_reviews({}, guard.prepare(self.patch(), self.root), evidence)
                self.assertEqual(2, run.call_count)

    def test_live_search_requires_completed_tool_event(self):
        self.assertFalse(guard.live_search_completed('{"type":"item.started","item":{"type":"web_search"}}'))
        self.assertFalse(guard.live_search_completed('{"type":"item.completed","item":{"type":"agent_message","text":"I searched"}}'))
        self.assertTrue(guard.live_search_completed('{"type":"item.completed","item":{"type":"web_search","query":"synthetic"}}'))

    def test_success_does_not_override_existing_approval_policy(self):
        output = guard.result("context", "reviews passed")["hookSpecificOutput"]
        self.assertNotIn("permissionDecision", output)
        self.assertEqual("deny", guard.result("deny", "risk")["hookSpecificOutput"]["permissionDecision"])


if __name__ == "__main__":
    unittest.main()
