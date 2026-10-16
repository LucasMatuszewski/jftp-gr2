# JFTP graph for agent navigation

> **Original reference snapshot — do not regenerate in place.** These existing generated outputs are preserved in the [immutable original snapshot](../context-snapshots/original-initial-context/README.md). Follow the [versioned refresh workflow](../context-snapshots/workflow.md) after major application changes; publish a new change-labelled set instead of replacing these files. Historical refresh commands below use fixed destinations and must not be run against the original outputs.

Use [graph.py](graph.py) for bounded symbol, caller, callee and impact queries. It reads the portable [JFTP graph](jftp.graph.json) locally using Python's standard library. No Graphify installation, model endpoint, database service or MCP registration is needed for queries. Use the existing [RepoMap](../repo-maps/README.md) for orientation and [full-source Repomix](../RepoMix/README.md) for broader implementation context; verify original bodies before edits.

The 2026-10-15 snapshot covers revision `cdc95025ac74098f129bfd9cdcd613fa6348c8d0`: 189 Java files, 2,372 nodes and 7,609 relationships, including 2,095 `calls` edges. Extraction and provenance capture took 9.810 seconds on this machine. Nodes include files, classes, methods and external placeholders; node count is not a count of Java definitions. The graph file is 3,301,974 bytes. These are local measurements, not comparative speed or token-savings claims.

This is a working-tree snapshot made before the granular commits. The helper
requires an exact match to its recorded `HEAD`, even when source hashes still
match. Recording these changes therefore makes queries reject this snapshot;
generate and validate a new change-labelled snapshot before querying the new HEAD; do not refresh this original reference in place.
Committing a refreshed snapshot changes HEAD again and triggers the same guard.
The snapshot's revision is retained as provenance rather than relabeled without
regeneration.

## Query it

From the repository root, use a working Python 3.10+ interpreter. This Windows session's `python` alias is broken; its working interpreter is:

```powershell
$graphPython = 'C:\Users\BiuroEdukey\AppData\Local\Python\pythoncore-3.14-64\python.exe'
& $graphPython -B docs/code-graph/graph.py status
& $graphPython -B docs/code-graph/graph.py find 'ftpsession_ftpsession_connect' --limit 10
& $graphPython -B docs/code-graph/graph.py callers src_main_java_com_myjavaworld_jftp_ftpsession_ftpsession_connect
& $graphPython -B docs/code-graph/graph.py impact src_main_java_com_myjavaworld_jftp_ftpsession_ftpsession_connect --depth 2 --limit 20
& $graphPython -B docs/code-graph/graph.py callees src_main_java_com_myjavaworld_jftp_jftpapplication_jftpapplication_jftpapplication
```

On other machines, substitute a working `python`/`python3`. `find` matches a substring across node records; select the exact node ID before traversal. IDs distinguish source contexts but are extractor-generated and are not stable semantic Java IDs across arbitrary edits. Callers/callees use direct `calls` relationships; impact walks inbound calls only, at depth 1–3. Results state total and truncation; `--limit` defaults to 20 and is capped at 100. Increase it for a truncated bounded question or narrow the target. The helper loads the local graph file, but returns only bounded records to the agent.

All queries reject a changed Java file, added/deleted Java file, changed `pom.xml`, changed Git HEAD or altered graph bytes. Resource/configuration changes outside that fingerprint are not detected: inspect their wiring directly and refresh after relevant changes. Git must be available and trust the checkout. `source_review` marks the three inspected connection edges as `source-checked`; other edges are `unreviewed`. The known false worker edge is returned as `rejected` and is not expanded into further traversal. Review annotations are ignored when their graph hash differs.

## What the pilot established

| Question | Current evidence |
| --- | --- |
| Who calls `FTPSession.connect(RemoteHost)`? | Three graph edges match inspected original calls: `ConnectAction.actionPerformed` at L73, `FavoritesDlg.connectButtonPressed` at L249, and `FTPSession.reconnect` at L703. |
| What needs review for a signature change? | Those three direct call sites. Depth-2 graph traversal returns six relationships, including transitive handlers; it is not proof of all possible compatibility impact. |
| Is GUI startup complete in the graph? | Partial. `main -> JFTPApplication()` and `newSession` are present; the constructor's preference call at L41, `new JFTP()` at L55 and frame visibility at L61 have no outgoing call edges. |
| Can unused classes be identified from graph degree? | No. `ImageCellRenderer` has no incoming `calls` edges here but explicit constructions exist in FavoritesDlg and PreferencesDlg. ThreadVar and both transferables also have source constructor references. |
| Is every extracted edge correct? | No. The `SwingWorker` construction at FTPSession L617 points to disconnect's anonymous worker at L1500. That target is explicitly rejected by the helper. |
| Does it understand the FTP implementation? | It identifies application navigation, not the absent external `ftpapi` implementation. Reflective client/parser construction and worker lifecycle need original-source inspection. |

[validation.json](validation.json) records exact graph edges and gaps. [evidence.json](evidence.json) contains 14 original-source citation cards with byte hashes, inclusive line ranges and exact quotations. The skill citation checker validated all 14 cards. The caller assertion compares graph sites with inspected Java sites; it does not prove an exhaustive whole-program caller search. No class is designated dead code.

All 189 Java paths are represented, including three `package-info.java` files with no extracted symbols. `pom.xml` is staged and also yields no symbols. Extraction reported these four warnings; it did not report parser failures. File representation is not semantic completeness. Source resources, XML/properties wiring, dependency implementations, dynamic dispatch, reflection, OS integration and external consumers remain outside the graph's guarantees.

## Historical refresh recipe (do not run in place)

Graphify `graphifyy==0.9.91` generates the graph; queries do not require it. Refresh requires `uv`, Git and the provisioned cache. The explicit `provision` command downloads packages; it does not install an agent skill, hooks or client configuration.

```powershell
& $graphPython -B docs/code-graph/graph.py provision
& $graphPython -B docs/code-graph/graph.py refresh
& $graphPython -B docs/code-graph/validate.py
& $graphPython -B .agents/skills/legacy-codebase-workflows/scripts/check_citations.py . docs/code-graph/evidence.json
& $graphPython -B -m unittest discover -s docs/code-graph -p test_graph.py -v
```

The default runtime/cache location is the external temporary directory `jftp-code-graph`; pass `--cache <external-directory>` consistently to provision and refresh for a durable machine-local location. Temporary storage may be cleaned by Windows. The saved graph and standard-library queries remain usable independently. The tested Python version is 3.14.3; other supported interpreters were not exercised. Graphify's top-level version is pinned and the actual 30-package inventory is recorded in [provenance.json](provenance.json); dependency resolution on a fresh machine can differ. Preserve the provisioned environment for exact comparisons.

Refresh stages only `src/**/*.java` plus `pom.xml` in a new external directory. It runs `extract --code-only --no-cluster --force` with `uv --offline`; it never scans the original repository root or sends source through hosted Context7. It checks source fingerprints before publication. Raw extraction warnings remain in ignored `artifacts/extract.log`. Machine-specific paths, extracted packages and staging copies stay outside primary reports. Keep that external cache private; it contains source snapshots. No socket-denial test was performed: `uv --offline` controls package resolution and is not a network sandbox.

The current `validate.py` contains regression expectations and line ranges for this snapshot. After intentional source edits, update them from the new original source; a failing expectation requires investigation. Refresh does not invent new source-review findings. Never mechanically preserve the rejected worker edge after regeneration.

The freshness suite passed seven checks: unchanged snapshot, edited/added/deleted Java, changed build descriptor, switched revision and changed graph bytes. No application build, behavior tests or GUI launch were required or performed. That original graph pilot did not modify application source. The startup refresh includes seven test/helper files and the changed Maven descriptor; production Java remains unchanged.

## How agents should use the graph

Start with a bounded question and exact symbol. Inspect callers or a shallow impact trace, check `source_review`, and open the original call sites and callee. Follow anonymous worker bodies, listeners, resources and dependency wiring manually. Use characterization tests before behavior changes. A complete graph dump is unnecessary agent context; small queries plus verified source are the useful interface.

See the [source-checked architecture sketch](architecture.md) and [open-source tool comparison](tool-comparison.md). For later Java API refactoring, evaluate JDT-backed navigation once the project and dependencies import correctly. The current AST graph is useful now but cannot certify overload resolution, virtual dispatch or safe deletion.

Only `artifacts/` is ignored. Primary graph, evidence, provenance and helper files remain Git-visible, with scoped LF attributes. No persistent process, watcher, server, MCP entry, hook or AGENTS.md instruction was installed. The Beads bridge could not run because its WSL launch returned `Wsl/Service/E_ACCESSDENIED`; no shared issue was created or updated from this session.


## Sygnity UI refresh, 2026-10-16

A new [change-labelled snapshot](../context-snapshots/sygnity-ui-90f300211437/README.md) records the agreed styling step. Use its per-file source manifest and stated scope when navigating that implementation. The original outputs in this directory remain historical and unchanged.
