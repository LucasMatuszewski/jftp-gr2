# Full and compressed JFTP Repomix comparison

Historical comparison of the original artifacts. The startup exercise subsequently refreshed the descriptor in both packs; the Java compression analysis remains applicable. Current hashes, exact sizes and tokens are in [compression-comparison.json](compression-comparison.json). Tables and review/context measurements below are retained as historical evidence and do not describe the refreshed artifact bytes.

Examined revision: `cdc95025ac74098f129bfd9cdcd613fa6348c8d0`. Comparison generated on 2026-10-15 with Repomix 1.18.1. Both complete XML files were read together by the comparison program; representative source and compressed sections were inspected to verify the conclusions below. This orchestrator analysis does **not** claim that both complete raw files were injected into the model's context. A separately requested built-in Luna subagent is reviewing that direct-loading requirement.

**The compressed pack retains all 466 file entries and useful class/method navigation, but loses important information. It is insufficient on its own for reliable behavior analysis, API usage, debugging, refactoring, security review or rebuilding the application.**

## Sizes

| Measurement | Full, without supported comments | Compressed, same comment policy | Reduction |
| --- | ---: | ---: | ---: |
| UTF-8 bytes | 1,171,503 | 878,499 | 293,004 (25.01%) |
| KiB (1,024 bytes) | 1,144.05 | 857.91 | 286.14 |
| Whole-file `o200k_base` tokens | 329,742 | 244,509 | 85,233 (25.85%) |
| File entries | 466 | 466 | 0 |
| Changed / unchanged decoded entries | — | 183 / 283 | — |

Files: [full pack](jftp.full-no-comments.xml), [compressed pack](jftp.compressed-no-comments.xml). Combined: **574,251 measured tokens**, or 2,050,002 bytes. The original full-pack CLI report said 329,743 tokens; direct recount of the persisted bytes differs by one token. This table uses direct on-disk recounts consistently, without universal-newline conversion.

The full pack's SHA-256 remains `2a4c7dc55631758e13615a2e8c3c9dd75cb4f3271a46ee5f856064215a4bef11`; the compressed pack's is `264abb7d24e8606c86e28dd472acebcdac04c842bbac7999e0a4db47e101621d`. All 466 original source hashes remain unchanged. Compression generation wall time was not retained, so no timing comparison is claimed.

## Why the reduction is about 26%

The compressed variant was generated from the verified full pack's decoded file contents. Only `output.compress` was changed. Code/comment scope, file allowlist, token encoding and security policy were preserved. Unsupported source comments had already remained in both variants; no additional Java comment removal explains these savings.

| Entry type | Files | Changed | Full content tokens | Compressed content tokens |
| --- | ---: | ---: | ---: | ---: |
| Java | 182 | 182 | 169,274 | 85,814 |
| CSS | 1 | 1 | 644 | 78 |
| HTML help | 95 | 0 | 61,710 | 61,710 |
| Properties | 172 | 0 | 28,580 | 28,580 |
| XML, including Maven/assembly | 7 | 0 | 6,520 | 6,520 |
| DTD | 5 | 0 | 1,795 | 1,795 |
| Text/license files | 3 | 0 | 4,638 | 4,638 |
| README | 1 | 0 | 1,410 | 1,410 |

These are tokens of individual XML-decoded, newline/boundary-normalized contents. They exclude XML escaping, file wrappers and the pack overview, so they must not be added to or substituted for the whole-file counts above. Java content shrank by 49.30%, while the unchanged resources limit overall savings. The 41 German properties files preserved by the full pack remain present with the same decoded text.

## What survived and what was removed

The following checks search normalized original declarations/fragments within the **same** compressed file. A repeated fragment can produce a match in another location; presence therefore does not prove retained ownership, ordering, reachability or behavior. The source AST is parsed from the full pack; no claim is made that the compressed sketch is valid Java.

| Original element | Original count | Present in compressed text | Interpretation |
| --- | ---: | ---: | --- |
| Class names, including nested classes | 186 | 186 | Useful navigation survives |
| Interface names | 6 | 6 | Useful navigation survives |
| Method name/declaration lines | 1,394 | 1,394 | A name is not its complete contract |
| Full method declaration prefixes, ignoring `@Override` | 1,394 | 1,334 | 60 lose more than an `@Override` annotation |
| Full method prefixes including annotations/throws | 1,394 | 1,127 | 267 differ under this stricter check |
| Constructor declaration prefixes | 254 | 0 | Constructor calls may survive without constructor definitions |
| Complete field declarations | 998 | 10 | Most state/defaults/constants disappear |
| Complete import declarations | 1,764 | 0 | Import-based dependency information disappears |
| Complete package declarations | 182 | 0 | Paths remain; package statements do not |

Some calls, object creation, selected condition lines and returns survive because they share lines with captured identifiers. Other returns, assignments, constructor setup, branch guards, loop headers, exception handling, cleanup and multiline declaration continuations disappear. The extraction inserts 3,742 gap markers into Java and 14 into CSS; gaps do not encode the missing logic. Repeated captures may also be deduplicated. Do not interpret the remaining calls as a complete call graph or preserved execution sequence.

## Important omissions, checked against original source

Each example is present in the full pack and original source, and absent from the compressed entry. The source revision, byte hashes, quotations and original lines are recorded in [the comparison data](compression-comparison.json); the skill's citation checker validated all ten evidence cards.

| Area | Concrete omitted information | Practical implication |
| --- | --- | --- |
| Resource loading | `ClassLoader loader` in [ResourceLoader.java:46](../../src/main/java/com/myjavaworld/util/ResourceLoader.java#L46) | The ClassLoader overload's complete parameter list cannot be reconstructed from its header |
| Filtering | `return exclusionFilter ? false : true;` in [LocalFileFilter.java:139](../../src/main/java/com/myjavaworld/jftp/LocalFileFilter.java#L139) | Remaining condition/call lines do not tell whether a file is accepted or rejected |
| Favorites persistence/encryption | `if (cipher == null)` in [FavoritesManager.java:122](../../src/main/java/com/myjavaworld/jftp/FavoritesManager.java#L122) | Both serialization calls survive, but the guard separating plaintext fallback from encryption is missing |
| SSL API contract | Checked-exception continuation in [JFTPSSLContext.java:39](../../src/main/java/com/myjavaworld/jftp/ssl/JFTPSSLContext.java#L39) | The complete `throws` contract is missing |
| SSL initialization | Third `ctx.init` argument, `null`, in [JFTPSSLContext.java:43](../../src/main/java/com/myjavaworld/jftp/ssl/JFTPSSLContext.java#L43) | A surviving method call does not guarantee all arguments survive |
| Transfers | Selected-file loop headers in [FTPSession.java:723](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L723) and line 851 | Upload/download calls remain, but batch iteration structure is lost |
| Preferences and cleanup | `return prefs;` in [JFTP.java:566](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L566) | Cleanup calls alone do not expose the method's unusual result/error-control behavior |
| Reflection/default implementation | FTP implementation class-name constant in [RemoteHost.java:36](../../src/main/java/com/myjavaworld/jftp/RemoteHost.java#L36) | Reflection call names remain without the default implementation's complete wiring |
| Styling | CSS property declarations in `src/main/help/helpset/content/default.css` | Selector names survive, but property/value choices needed to reproduce styling disappear |

Useful retained examples include `SwingUtilities.invokeLater(doFinished);` in [SwingWorker.java:141](../../src/main/java/com/myjavaworld/gui/SwingWorker.java#L141) and `jftp.newSession();` in [JFTPApplication.java:62](../../src/main/java/com/myjavaworld/jftp/JFTPApplication.java#L62). These reveal scheduling and startup operations, but do not prove their surrounding conditions, constructor initialization, callbacks or lifecycle were preserved.

The implications above are source-based analysis, not observed GUI/FTP behavior. No application build, tests, GUI launch or network transfers were run.

## Is it sufficient?

| Task | Compressed pack alone |
| --- | --- |
| Find file, class/interface and method names | Useful, with declaration/constructor limitations |
| Sketch broad module ownership | Partly useful; verify imports, state and wiring in full source |
| Use precise APIs or overloads | Insufficient: some parameters, arguments, exceptions and constructors are missing |
| Explain full application workflows or logic | Insufficient: control flow, results and initialization are incomplete |
| Debug or refactor behavior | Insufficient: read the relevant full implementation and callers |
| Review security, SSL, persistence or concurrency | Insufficient: missing guards/cleanup/state can change the conclusion |
| Reproduce UI styling | Insufficient: CSS properties are removed |
| Compile or rebuild from the packed sketch | Insufficient; it is not source-equivalent Java |

**Not all important information is preserved.** Use RepoMap or the compressed pack for orientation, then fetch the relevant full implementation. The preserved HTML, properties and XML help with configuration discovery but cannot restore omitted Java logic.

## Can both whole packs fit together?

The project requests 1,000,000 context tokens and automatic compaction at 800,000. The actual session token event at **2026-10-15 08:29:16 UTC** reported an **828,400-token runtime window** and **246,336 input tokens**, including cached input. Cached input still occupies context.

| Budget calculation | Tokens |
| --- | ---: |
| Both complete packs | 574,251 |
| Fresh-context allowance below configured 800,000 compaction point | 225,749 |
| Fresh-context allowance below observed 828,400 runtime limit | 254,149 |
| Existing observed input plus both packs | 820,587 |
| Remaining nominal runtime space in that projection | 7,813 |

**A fresh sufficiently large context has room for both packs plus instructions. This already long conversation would exceed the configured compaction point when both are added and leave very little runtime headroom.** The projection is a point-in-time estimate: tokenizer differences, prompts, tool metadata, new messages, reasoning/output reserves and client clamping can reduce the margin. Configuration values alone do not prove the active window or successful loading.

The orchestrator processed both complete files together in one program and inspected source-backed examples. It has not injected all 574,251 raw file tokens into this chat. The completed [built-in Luna direct review](luna-direct-review.md) used a fresh uninterrupted turn, reports both complete texts available before semantic analysis, and reports no visible truncation or compaction. Its exact internal window/usage remains unexposed. Earlier interrupted/resumed attempts are documented separately and do not substantiate that successful review.

## Complete changes and reproduction evidence

- [Machine-readable comparison](compression-comparison.json): all 466 per-file rows, configuration, hashes, counts, ten source evidence cards and context snapshot.
- [Per-file CSV](artifacts/compression-changes.csv): exact normalized-entry line counts and size/token changes for every path.
- [Complete unified diff](artifacts/full-vs-compressed.diff): every changed decoded file entry, including omitted lines and inserted gap markers.
- [Whole-XML diff](artifacts/whole-xml.diff): complete raw artifact differences, including XML framing/serialization and original line endings.
- `artifacts/callable-signatures.json`: per-callable signature preservation checks.
- `artifacts/compression-evidence.json`: citation-checker input.
- `artifacts/compare_compression.py`, `artifacts/measure_tokens.mjs`, `artifacts/repomix.compressed.config.json`: generator, tokenizer and exact pinned configuration.

Only supporting `artifacts/` are ignored. Both packs, this report and the machine-readable comparison remain Git-visible. The original full pack and RepoMap reports were not rewritten.
