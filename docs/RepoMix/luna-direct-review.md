# Luna direct full-context review

This review was produced by the fresh built-in Codex subagent `/root/luna_preloaded_direct`, explicitly using `gpt-6-luna` with low reasoning effort. It loaded both complete raw packs before semantic analysis, then returned its report in that same uninterrupted turn. It did not use Python, XML/AST parsing, generated comparisons, counters or diffs to derive its conclusions. The coordinator edited the report for clarity and corrected overbroad statements about filtering decisions, overload signatures, transfer loop headers, `finally` structure and resource values using the already verified original-source evidence. The earlier failed/resumed report is retained separately and is not this review.

The [unedited Luna response](artifacts/luna-direct-raw.md) is retained for transparency.

## Loading and context

Luna reported that both complete raw texts were available together before analysis. The fixed loader delivered 239 separate small raw-text notifications covering all bytes of both files. It used two raw I/O reads for the full file and one for the compressed file, because a single whole-file tool read of the larger file had returned incomplete data. It did not parse or infer anything about repository content. Packetization was a delivery mechanism; Luna did not analyze separate chunks as independent inputs.

No visible missing range, truncation or intervening compaction was reported in this fresh run. The model's internal token accounting and exact per-subagent window are not exposed by the built-in tool, so those remain unverified. The project requests 1,000,000 context tokens and compaction at 800,000; those settings alone do not prove the child's actual runtime limit.

| Supplied measurement | Full pack | Compressed pack |
| --- | ---: | ---: |
| Bytes | 1,171,503 | 878,499 |
| Whole-file `o200k_base` tokens | 329,742 | 244,509 |
| Combined tokens | 574,251 | — |

These are supplied, previously measured values, not values recomputed by Luna. Both files describe revision `cdc95025ac74098f129bfd9cdcd613fa6348c8d0` with the same 466-file scope. Both already remove supported comments; properties, DTD and plain-text comments remain. Structural compression is lossy extraction, not reversible archive compression.

## Retained information

The compressed pack retains file paths, class/interface names, method-name lines and selected calls. It remains useful for finding major components such as `FTPSession`, `RemoteHost`, action classes and GUI helpers. It suggests broad responsibilities and shows many connection, upload, download, command and directory-operation calls.

Startup still contains `jftp.setVisible(true);` and `jftp.newSession();`. `SwingWorker` still contains `SwingUtilities.invokeLater(doFinished);`. These are useful orientation clues, but the presence of an operation does not establish its complete lifecycle or surrounding conditions.

Properties bundles, Maven/assembly XML and HTML help preserve configuration and user-facing documentation. The help topics explain connection settings, SSL modes and transfer procedures. These resources support feature discovery but do not restore omitted Java implementation.

## Important losses

### Constructors, fields and defaults

Constructor signatures, many field declarations and default values disappear. `RemoteHost` illustrates why surviving initialization calls are insufficient: the full file exposes constructor overloads, the default port, passive mode and data-channel defaults. The compressed sketch does not preserve the complete constructor contracts or all constants used by them.

The full `FTPSession` declares connection state, filters, timers, counters, transfer settings and abort-related state. The compressed pack shows many usages without the complete state model. `JFTPPreferences` likewise contains defaults and transfer-extension mappings whose full relationships cannot be recovered from a structural sketch. This weakens state tracing and behavior-sensitive refactoring.

### Imports, packages and exact APIs

Import and package declarations are omitted, making precise dependency/type interpretation less reliable even though paths remain. Multiline signatures may lose parameters, checked exceptions and annotations.

For example, the full `ResourceLoader` overload includes `ClassLoader loader`; the compressed entry retains its first declaration line but loses that parameter continuation. Other overload declaration lines survive, so it would be inaccurate to say every overload signature disappears. What is missing is the complete contract of the affected overload.

The full `FavoritesManager.getFavorites()` declares `IOException`, `ClassNotFoundException`, `IllegalBlockSizeException` and `BadPaddingException`; compression retains only the start of its declaration. Similar continuation loss affects `JFTPSSLContext.getSSLContext`. Callers cannot safely infer the full exception obligations from the sketch.

### Filtering results and transfer iteration

`LocalFileFilter.accept` retains selected condition lines involving hidden files, regex matching and dates. Its decisive return expressions are absent. The full implementation returns `exclusionFilter ? true : false` for failed criteria and `exclusionFilter ? false : true` after a file passes. Without those results, the remaining conditions do not establish acceptance/rejection polarity.

The full `FTPSession.download()` and `upload()` iterate over selected entries. The selected-file `for` loop headers are absent from the compressed entries, even though transfer calls and some condition lines remain. The complete sequencing of iteration, abort/disconnection handling, refreshes and exception/finalization paths is not preserved. This matters when reviewing recursive or destructive operations.

### Favorites persistence and encryption branching

The full `FavoritesManager` distinguishes serialized legacy `List` data from encrypted `SealedObject` data. Its write path chooses plaintext serialization when cipher creation fails and sealed serialization otherwise. The compressed file contains fragments of both paths but omits the `if (cipher == null)` guard.

An analyst seeing the surviving serialization calls alone could miss both the migration path and the plaintext fallback. The complete version is required for a dependable review of storage and error behavior. Numeric embedded key material is intentionally not reproduced here.

### Preferences and `finally`

The full `JFTP.loadPreferences` closes streams and returns `prefs` from its `finally` block. The compressed entry retains read/close operations but omits `return prefs;`. A return inside `finally` can affect exception propagation; its absence materially changes the apparent control flow.

Other cleanup and return paths are similarly incomplete. A list of surviving calls is insufficient to establish which failures are propagated, suppressed or followed by UI cleanup.

### Reflection and client selection

The full code connects preference-derived host settings, reflective client/parser instantiation, passive mode, timeouts, buffering, SSL/data-channel options and implicit SSL port selection. Compression retains many operation names and calls while removing some defaults, constructor context, guards and error paths. The default FTP implementation class-name constant in `RemoteHost` is one concrete lost piece of reflective wiring.

### Worker scheduling and SSL arguments

`SwingWorker` retains calls such as thread-reference clearing and `SwingUtilities.invokeLater(doFinished)`, but not their complete `try`/`finally` relationship. In the full implementation, `invokeLater` follows the `try`/`finally`: an unchecked exception from `construct()` clears the reference but can skip scheduling `finished()`. The compressed call fragments do not establish that the completion callback is guaranteed.

The full SSL initialization is `ctx.init(new KeyManager[] {...}, new TrustManager[] {...}, null)`. The compressed excerpt retains the manager-array portions but loses the final `null` argument and part of the exception contract. The high-level intent survives; the exact call contract does not.

### Styling and execution evidence

The full help `default.css` specifies fonts, margins, colors, padding, borders and spacing. Compression retains selectors such as `body`, `p.note` and `code`, while removing their property values. That cannot reproduce the styling. This CSS loss should not be generalized to all resources: properties, XML and HTML entries remain unchanged under the comparison's normalization.

Neither pack proves a working build or GUI/FTP behavior. Entry-point and POM references are static evidence; this review did not execute the application.

## Suitability

| Use | Compressed pack alone |
| --- | --- |
| File/class navigation | Useful |
| Broad architecture | Useful with gaps; verify wiring and state |
| Exact APIs and exception contracts | Insufficient |
| Complete behavior and edge cases | Insufficient |
| Debugging or behavior-sensitive refactoring | Insufficient |
| Security and threading review | Insufficient |
| Styling reproduction | Insufficient |
| Rebuilding or proving startup | Insufficient evidence |

## Conclusion

The compressed pack preserves recognizable structure, selected calls and substantial supporting documentation. It removes important constructor/state information, declaration continuations, results, guards, iteration structure, cleanup relationships and CSS values. Those omissions can change conclusions about filtering, persistence, transfer safety, SSL and asynchronous cleanup.

Use the [full pack](jftp.full-no-comments.xml) for behavior-sensitive analysis and the [compressed pack](jftp.compressed-no-comments.xml) for orientation. This semantic summary is not an exhaustive list of every deleted line; the [existing comparison report](COMPARISON.md) links the separately produced exact change records.

## Why the earlier attempt failed

The earlier brief wrongly mixed direct model reading with Python-generated analysis and an excessive per-chunk workflow. Luna initially stopped after only a small read. It later completed streamed loading, but interrupting and resuming it replaced that raw context with a summary before semantic analysis. That history is not evidence of a too-small model window.

The successful retry used a new built-in subagent, a fixed raw-text delivery program and one uninterrupted preload-to-analysis turn. Programs transported text only; the model performed the semantic comparison. The exact internal context limit remains unknown, while complete same-turn raw delivery and the absence of visible truncation/compaction are reported by the successful delegate.
