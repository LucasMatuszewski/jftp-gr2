# JFTP Repomix packs

> **Original reference snapshot — do not regenerate in place.** These existing generated outputs are preserved in the [immutable original snapshot](../context-snapshots/original-initial-context/README.md). Follow the [versioned refresh workflow](../context-snapshots/workflow.md) after major application changes; publish a new change-labelled set instead of replacing these files. Historical refresh commands below use fixed destinations and must not be run against the original outputs.

Two profiles are available: the original [full-code pack](jftp.full-no-comments.xml) and the [compressed structural pack](jftp.compressed-no-comments.xml), both with the same 466-file scope and supported-comment removal policy. See the [detailed comparison](COMPARISON.md) for measured sizes, precise losses, source examples, use-case suitability and context-budget analysis.

| Pack | Bytes | Direct whole-file `o200k_base` tokens |
| --- | ---: | ---: |
| Full | 1,172,053 | 329,919 |
| Compressed | 879,049 | 244,686 |

Compression reduces tokens by 25.85%; both packs together require approximately 574,605 tokens before instructions/history. The compressed pack omits important implementation and API details and is a navigation aid. The [built-in Luna direct review](luna-direct-review.md) used a fresh, uninterrupted preload-to-analysis turn with both complete raw texts; it reports no visible truncation or compaction. Its exact internal runtime window is not exposed by the tool.

The full-pack measurements below preserve its original CLI report; that token total differs from the direct persisted-file recount by one token.

[jftp.full-no-comments.xml](jftp.full-no-comments.xml) is a parsable XML pack of 466 tracked text files at revision `cdc95025ac74098f129bfd9cdcd613fa6348c8d0`, refreshed on 2026-10-15 with Repomix 1.18.1. It preserves selected implementation bodies and signatures without structural compression.

| Measurement | Value |
| --- | --- |
| Selected / packed text files | 466 / 466 |
| Java files | 182 |
| File size | 1,172,053 bytes |
| Measured tokens, `o200k_base` | 329,920 |
| Repomix generation wall time | 2.904 s |
| Pack SHA-256 | `09716675ece1ca18ffa153dd5a85ca89c184cf4442332bad729e9e95c16c461d` |

Generation time excludes setup, snapshot preparation, validation and map generation. The pack is large: locate relevant sections instead of loading it wholesale. Start with [RepoMap](../repo-maps/README.md) to identify paths.

The startup refresh changes the Maven descriptor only. The compressed pack received the same verified descriptor entry; compressed Java bodies are unchanged. The earlier Luna reviews and detailed narrative comparison describe the original pair; current exact hashes and measurements are in `compression-comparison.json`.

## Included and omitted

The explicit tracked-file allowlist includes Java source, all 172 properties bundles, Maven configuration and assembly XML, JavaHelp XML/DTD/HTML/CSS/text, README, LICENSE and NOTICE. At generation time, the seven new test/helper sources were untracked and were excluded by that allowlist; committing them afterward does not add them to these saved packs. The refreshed RepoMaps and code graph do include them. FTP protocol-library and JavaHelp dependency implementations are not packed.

Binary images, fonts and other binary assets, Sygnity design assets/guidelines, IDE configuration, local agent configuration, protected paths and generated context are excluded. Thus this is the full code for the selected application text scope, not the whole repository or its external dependencies.

Java, HTML, XML and CSS comments are removed. Properties, DTD and plain-text comments/documentation remain because they have no supported comment manipulator in this pinned version; standalone license and notice text is intentionally retained. Empty lines and implementation code are preserved, apart from Repomix's documented boundary/trailing-whitespace normalization.

Repomix retained one Javadoc because it mentioned `licenseAgreed`. To honor the selected profile, the generator removes only Tree-sitter-identified Java comment ranges in the temporary input before packing. It leaves original files unchanged and compares the actual packed syntax and tokens against the originals.

## Legacy encoding and safe input

41 German properties files contain non-UTF-8 bytes. They are decoded as ISO-8859-1 and transcoded to UTF-8 only in the external staging snapshot. `ResourceLoader.java` delegates to `ResourceBundle.getBundle`; the legacy resource-loading convention is documented in [Oracle's Java 8 PropertyResourceBundle reference](https://docs.oracle.com/javase/8/docs/api/java/util/PropertyResourceBundle.html). All original byte hashes and per-file decoding choices are in [provenance.json](provenance.json). No original resource encoding was changed.

Repomix's root discovery tried to scan protected directories despite the explicit include list. Generation therefore uses an external snapshot containing only the reviewed tracked-file allowlist, preserving repository-relative paths. Protected data is never copied or read. Root discovery failure details remain in local artifacts.

## Verification and refresh

The actual output passed XML parsing and exact selected-file coverage. All 182 Java files and the CSS file passed non-comment token and syntax-tree comparisons, with no parser errors or remaining comment nodes. HTML elements, attributes and normalized text matched across 95 files; XML elements, attributes and text matched across seven files. The remaining 181 files matched their decoded originals after boundary/newline normalization. 912 original Java comment nodes were removed. All 466 original source byte hashes remained unchanged. Repomix's security check reported no suspicious files.

These checks validate packing and code preservation, not a working build or application runtime. No build, tests, GUI or FTP operations were run.

[Provenance](provenance.json) is Git-visible and contains the exact include list, full configuration, original source hashes and encodings, output hashes, profile and validation metrics. Local configuration, logs, detailed audits and helpers are under ignored `artifacts/`. The primary XML has a scoped `-text` Git attribute so checkout conversion does not change its recorded hash.

Use the [shared refresh instructions](../repo-maps/README.md#refresh) to regenerate both maps and this pack. Refresh after relevant source changes; configuration changes also require regeneration. Never use this comment-stripped pack to infer original documentation or code outside its declared scope.


## Sygnity UI refresh, 2026-10-16

A new [change-labelled snapshot](../context-snapshots/sygnity-ui-90f300211437/README.md) records the agreed styling step. Use its per-file source manifest and stated scope when navigating that implementation. The original outputs in this directory remain historical and unchanged.
