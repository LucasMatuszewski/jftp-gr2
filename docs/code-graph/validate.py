"""Recheck bounded JFTP graph questions against original-source citation cards.

Known extraction gaps are reported, not disguised as passing semantic checks.
"""
import collections
import json
from pathlib import Path

import graph


def main():
    data, provenance = graph.load()
    nodes = {n["id"]: n for n in data["nodes"]}
    edges = data["edges"]
    session = "src_main_java_com_myjavaworld_jftp_ftpsession_ftpsession_connect"
    app = "src_main_java_com_myjavaworld_jftp_jftpapplication_jftpapplication_jftpapplication"
    callers = [e for e in edges if e["target"] == session and e["relation"] == "calls"]
    expected = {
        ("src/main/java/com/myjavaworld/jftp/actions/ConnectAction.java", "L73"),
        ("src/main/java/com/myjavaworld/jftp/FavoritesDlg.java", "L249"),
        ("src/main/java/com/myjavaworld/jftp/FTPSession.java", "L703"),
    }
    assert {(e["source_file"], e["source_location"]) for e in callers} == expected
    assert all(nodes[e["source"]].get("_callable") and not nodes[e["source"]].get("_callable_class") for e in callers)
    files = {n.get("source_file") for n in nodes.values()}
    assert all(p in files for p in provenance["source_sha256"] if p.endswith(".java"))
    citations = []
    prefix = "src/main/java/com/myjavaworld/"
    specs = [
        ("connect-action", prefix+"jftp/actions/ConnectAction.java", 70, 75, "ConnectAction calls session.connect(remoteHost)."),
        ("connect-favorite", prefix+"jftp/FavoritesDlg.java", 232, 250, "FavoritesDlg resolves a session and connects the selected host."),
        ("reconnect", prefix+"jftp/FTPSession.java", 701, 705, "reconnect calls connect(this.remoteHost)."),
        ("startup", prefix+"jftp/JFTPApplication.java", 32, 67, "main constructs JFTPApplication; constructor configures preferences, constructs and shows JFTP, creates a session."),
        ("new-session", prefix+"jftp/JFTP.java", 148, 157, "JFTP.newSession creates FTPSession."),
        ("panes", prefix+"jftp/FTPSession.java", 287, 295, "FTPSession creates local/remote panes and status window."),
        ("worker", prefix+"jftp/FTPSession.java", 617, 653, "Connection work creates a SwingWorker, reflectively loads FTP classes, then calls client.connect/login."),
        ("worker-other", prefix+"jftp/FTPSession.java", 1495, 1508, "The graph's L617 SwingWorker target at L1500 belongs to disconnect, so that target is rejected."),
        ("renderer-favorites", prefix+"jftp/FavoritesDlg.java", 265, 270, "ImageCellRenderer has a constructor reference in FavoritesDlg."),
        ("renderer-preferences", prefix+"jftp/PreferencesDlg.java", 170, 173, "ImageCellRenderer has a constructor reference in PreferencesDlg."),
        ("thread-var", prefix+"gui/SwingWorker.java", 143, 147, "ThreadVar is instantiated by SwingWorker."),
        ("transferables", prefix+"jftp/DnDTransferHandler.java", 73, 84, "Both transferables have explicit constructor calls."),
        ("ftp-default", prefix+"jftp/RemoteHost.java", 34, 39, "Default FTP implementation and parser class names are stored as strings."),
        ("dependency", "pom.xml", 70, 88, "ftpapi 3.0.0 and JavaHelp are declared external dependencies."),
    ]
    for key, relative, start, end, claim in specs:
        path = graph.ROOT / relative
        lines = path.read_text(encoding="utf-8").splitlines()
        assert len(lines) >= end
        citations.append({"id": key, "claim": claim, "status": "observed",
                          "path": relative, "sha256": graph.digest(path),
                          "start_line": start, "end_line": end,
                          "quote": "\n".join(lines[start-1:end])})
    app_edges = [e for e in edges if e["source"] == app and e["relation"] == "calls"]
    missing_startup = [line for line in ("L41", "L55", "L61") if not any(e.get("source_location") == line for e in app_edges)]
    bad_worker = [e for e in edges if e["source"] == session and e.get("source_location") == "L617" and nodes.get(e["target"], {}).get("source_location") == "L1500"]
    renderer_ids = {i for i in nodes if "imagecellrenderer" in i}
    renderer_calls = [e for e in edges if e["relation"] == "calls" and e["target"] in renderer_ids and e["source"] not in renderer_ids]
    findings = {
        "revision": provenance["revision"], "graph_sha256": provenance["graph_sha256"],
        "java_paths_represented": provenance["java_files"],
        "relation_counts": dict(collections.Counter(e["relation"] for e in edges)),
        "questions": [
            {"question": "Who calls FTPSession.connect(RemoteHost)?", "result": "3 graph callers match the 3 inspected source call sites", "edges": callers},
            {"question": "What changes if its signature changes?", "result": "3 direct call sites require review; inbound depth-2 traversal is navigation only. External/reflection compatibility remains unknown."},
            {"question": "Does GUI startup resolve completely?", "result": "Partial", "missing_call_site_lines": missing_startup, "source": "JFTPApplication.java", "citations": ["startup", "new-session"]},
            {"question": "Can zero incoming edges establish dead classes?", "result": "No", "ImageCellRenderer_incoming_calls": len(renderer_calls), "citations": ["renderer-favorites", "renderer-preferences", "thread-var", "transferables"], "scope": "All src/**/*.java extracted; named constructor sites inspected. Resources and reflection are outside graph scope. No dead-code conclusion."},
            {"question": "Can the graph establish FTP library implementation and architecture?", "result": "Partial architecture navigation; ftpapi internals absent", "citations": ["new-session", "panes", "worker", "ftp-default", "dependency"]},
        ],
        "rejected_edges": [{"edge": e, "reason": "Anonymous worker at L617 incorrectly targets disconnect's worker at L1500", "citations": ["worker", "worker-other"]} for e in bad_worker],
        "source_reviewed_edges": callers,
        "notes": ["EXTRACTED is an extraction label, not proof that Java receiver resolution is correct", "Coverage includes file nodes for package-info.java; these have no extracted symbols", "No application behavior or offline socket-denial test was run"],
    }
    graph.write_json(graph.HERE / "evidence.json", {"revision": provenance["revision"], "citations": citations})
    graph.write_json(graph.HERE / "validation.json", findings)
    print(json.dumps({"citations": len(citations), "verified_direct_callers": len(callers),
                      "missing_startup_call_lines": missing_startup, "rejected_worker_edges": len(bad_worker),
                      "renderer_incoming_calls": len(renderer_calls)}, indent=2))


if __name__ == "__main__":
    main()
