"""Bounded agent navigation over a pinned, local Graphify Java graph.

No application build, model API, server, hooks, or agent registration.
Runtime provisioning is explicit; graph queries use only the standard library.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
VERSION = "0.9.91"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_files():
    # Deliberately never enumerate the checkout root or secret/config trees.
    return sorted((ROOT / "src").rglob("*.java")) + [ROOT / "pom.xml"]


def fingerprints():
    return {p.relative_to(ROOT).as_posix(): digest(p) for p in source_files()}


def revision():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def runtime_env(cache):
    env = os.environ.copy()
    env.update(UV_CACHE_DIR=str(cache / "uv-cache"), UV_TOOL_DIR=str(cache / "uv-tools"),
               PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    return env


def run_graphify(cache, args, online=False):
    command = ["uv"] + ([] if online else ["--offline"])
    command += ["tool", "run", "--python", sys.executable, "--from",
                f"graphifyy=={VERSION}", "graphify"] + args
    result = subprocess.run(command, env=runtime_env(cache), cwd=cache,
                            capture_output=True, text=True, encoding="utf-8",
                            errors="replace", timeout=55)
    if result.returncode:
        raise RuntimeError(result.stdout[-3000:] + result.stderr[-3000:])
    return result.stdout + result.stderr


def load():
    graph_path = HERE / "jftp.graph.json"
    provenance = json.loads((HERE / "provenance.json").read_text(encoding="utf-8"))
    if digest(graph_path) != provenance["graph_sha256"]:
        raise ValueError("Graph hash differs from provenance; refresh before querying.")
    if fingerprints() != provenance["source_sha256"] or revision() != provenance["revision"]:
        raise ValueError("Stale source/revision. Run graph.py refresh before querying.")
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    return graph, provenance


def edge_review(edge, graph_hash):
    path = HERE / "validation.json"
    if not path.exists():
        return {"status": "unreviewed"}
    review = json.loads(path.read_text(encoding="utf-8"))
    if review.get("graph_sha256") != graph_hash:
        return {"status": "unreviewed", "note": "Saved source review is for a different graph"}
    for rejected in review.get("rejected_edges", []):
        if rejected["edge"] == edge:
            return {"status": "rejected", "reason": rejected["reason"], "citations": rejected["citations"]}
    if edge in review.get("source_reviewed_edges", []):
        return {"status": "source-checked", "evidence": "evidence.json"}
    return {"status": "unreviewed"}


def refresh(cache):
    before, head = fingerprints(), revision()
    started = time.perf_counter()
    # Unique staging avoids stale semantic layers and never deletes a live cache.
    stage = Path(tempfile.mkdtemp(prefix="jftp-source-", dir=cache))
    for relative in before:
        target = stage / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)
    output = stage / "extracted"
    log = run_graphify(cache, ["extract", str(stage), "--code-only", "--no-cluster",
                               "--force", "--out", str(output)])
    candidates = list(output.rglob("graph.json"))
    if len(candidates) != 1:
        raise ValueError(f"Expected one graph.json, found {candidates}")
    graph = json.loads(candidates[0].read_text(encoding="utf-8"))
    if not graph.get("nodes") or not graph.get("edges", graph.get("links")):
        raise ValueError("Extraction produced an empty graph")
    # Preserve raw extractor output; its node IDs use repository-relative paths.
    if before != fingerprints() or head != revision():
        raise ValueError("Source changed during extraction; repeat refresh")
    artifacts = HERE / "artifacts"
    artifacts.mkdir(exist_ok=True)
    (artifacts / "extract.log").write_text(log, encoding="utf-8")
    graph_path = HERE / "jftp.graph.json"
    shutil.copyfile(candidates[0], graph_path)
    dependencies = subprocess.check_output(
        ["uv", "--offline", "tool", "run", "--python", sys.executable,
         "--from", f"graphifyy=={VERSION}", "python", "-c",
         "import importlib.metadata,json; print(json.dumps({d.metadata['Name']:d.version for d in importlib.metadata.distributions()}))"],
        env=runtime_env(cache), cwd=cache, text=True, encoding="utf-8", timeout=20)
    provenance = {"revision": head, "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                  "tool": "graphifyy", "version": VERSION,
                  "mode": "code-only, no-cluster; no model or server",
                  "scope": "src/**/*.java plus pom.xml staged; Java graph extraction only",
                  "excluded": "resources, dependencies, generated docs, agent config, secrets",
                  "java_files": len(before)-1, "source_sha256": before,
                  "graph_sha256": digest(graph_path), "nodes": len(graph["nodes"]),
                  "edges": len(graph.get("edges", graph.get("links", []))),
                  "elapsed_seconds": round(time.perf_counter()-started, 3),
                  "runtime_packages": json.loads(dependencies),
                  "source_tracked_diff": subprocess.check_output(["git", "diff", "--name-only", "HEAD", "--", "src", "pom.xml"], cwd=ROOT, text=True).splitlines(),
                  "limitations": ["Heuristic Java resolution, not javac/JDT", "Missing edges do not imply dead code", "Verify receivers and original bodies before changes", "No network-denial test was performed; uv offline only controls package resolution"]}
    write_json(HERE / "provenance.json", provenance)
    return {k: provenance[k] for k in ("revision", "java_files", "nodes", "edges", "elapsed_seconds")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["provision", "refresh", "status", "find", "callers", "callees", "impact"])
    parser.add_argument("symbol", nargs="?", help="Substring for find; exact node ID for traversals")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--depth", type=int, choices=[1, 2, 3], default=1)
    parser.add_argument("--cache", type=Path, default=Path(tempfile.gettempdir()) / "jftp-code-graph")
    args = parser.parse_args()
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")
    if args.command in ("provision", "refresh"):
        cache = args.cache.resolve()
        if cache == ROOT or ROOT in cache.parents:
            parser.error("Cache/staging must be outside the repository")
        cache.mkdir(parents=True, exist_ok=True)
        if args.command == "provision":
            run_graphify(cache, ["--help"], online=True)
            result = {"provisioned": f"graphifyy=={VERSION}", "cache": str(cache)}
        else:
            result = refresh(cache)
    else:
        graph, provenance = load()
        nodes = {n["id"]: n for n in graph["nodes"]}
        edges = graph.get("edges", graph.get("links", []))
        if args.command == "status":
            result = {k: provenance[k] for k in ("revision", "java_files", "nodes", "edges", "generated_utc")}
            result["fresh"] = True
        elif args.command == "find":
            if not args.symbol:
                parser.error("find requires a symbol substring")
            rows = [n for n in nodes.values() if args.symbol.casefold() in json.dumps(n).casefold()]
            result = {"total": len(rows), "truncated": len(rows)>args.limit, "nodes": rows[:args.limit]}
        else:
            if args.symbol not in nodes:
                parser.error("Use find first, then pass an exact returned node ID")
            inbound = args.command != "callees"
            visited, frontier, rows = {args.symbol}, {args.symbol}, []
            depth = args.depth if args.command == "impact" else 1
            for level in range(1, depth+1):
                following = set()
                for edge in edges:
                    if edge.get("relation") != "calls":
                        continue
                    near, far = (edge["target"], edge["source"]) if inbound else (edge["source"], edge["target"])
                    if near in frontier:
                        review = edge_review(edge, provenance["graph_sha256"])
                        rows.append({"depth": level, "node": nodes.get(far, {"id": far}),
                                     "edge": edge, "source_review": review})
                        if far not in visited and review["status"] != "rejected":
                            following.add(far)
                visited.update(following)
                frontier = following
                if not frontier:
                    break
            result = {"target": nodes[args.symbol], "relation": "calls", "depth": depth,
                      "total": len(rows), "truncated": len(rows)>args.limit, "results": rows[:args.limit],
                      "warning": "Heuristic navigation only. Check original source; zero edges is not proof of no callers."}
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f"graph: {exc}", file=sys.stderr)
        sys.exit(1)
