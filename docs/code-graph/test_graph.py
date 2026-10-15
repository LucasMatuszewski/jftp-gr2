"""Behavior checks for stale-index rejection without changing real JFTP source."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import graph


class FreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.here = self.root / "docs" / "code-graph"
        self.here.mkdir(parents=True)
        self.java = self.root / "src" / "Demo.java"
        self.java.parent.mkdir()
        self.java.write_text("class Demo {}", encoding="utf-8")
        (self.root / "pom.xml").write_text("<project/>", encoding="utf-8")
        self.graph_path = self.here / "jftp.graph.json"
        self.graph_path.write_text('{"nodes": [], "edges": []}', encoding="utf-8")
        for name, value in (("ROOT", self.root), ("HERE", self.here)):
            mocked = patch.object(graph, name, value)
            mocked.start()
            self.addCleanup(mocked.stop)
        self.rev = patch.object(graph, "revision", return_value="revision-A")
        self.rev_mock = self.rev.start()
        self.addCleanup(self.rev.stop)
        graph.write_json(self.here / "provenance.json", {
            "revision": "revision-A", "graph_sha256": graph.digest(self.graph_path),
            "source_sha256": graph.fingerprints()})

    def test_unchanged_snapshot_is_usable(self):
        self.assertEqual(graph.load()[0]["nodes"], [])

    def test_edited_java_is_rejected(self):
        self.java.write_text("class Demo { void changed() {} }", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Stale"):
            graph.load()

    def test_added_java_is_rejected(self):
        (self.java.parent / "New.java").write_text("class New {}", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Stale"):
            graph.load()

    def test_deleted_java_is_rejected(self):
        self.java.unlink()
        with self.assertRaisesRegex(ValueError, "Stale"):
            graph.load()

    def test_changed_build_descriptor_is_rejected(self):
        (self.root / "pom.xml").write_text("<project>changed</project>", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Stale"):
            graph.load()

    def test_switched_revision_is_rejected(self):
        self.rev_mock.return_value = "revision-B"
        with self.assertRaisesRegex(ValueError, "Stale"):
            graph.load()

    def test_modified_graph_is_rejected(self):
        self.graph_path.write_text('{"nodes": [{"id": "invented"}]}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "hash differs"):
            graph.load()


if __name__ == "__main__":
    unittest.main()
