# Original initial context — immutable reference

These are byte-for-byte copies of the analysis available when the snapshot-preservation policy was adopted. They were archived, not regenerated. Keep this entire directory unchanged; create a separately named snapshot for subsequent application steps or corrected analysis.

| Product | Preserved files |
| --- | --- |
| RepoMap | [Overview](repo-maps/jftp.overview.python.md), [complete captured-definition index](repo-maps/jftp.definitions.python.md), raw maps and inventory/metadata in `repo-maps/evidence/`. |
| Repomix | [Full-code pack](RepoMix/jftp.full-no-comments.xml), [compressed pack](RepoMix/jftp.compressed-no-comments.xml), [provenance](RepoMix/provenance.json), [compression measurements](RepoMix/compression-comparison.json). |
| Code graph | [Graph JSON](code-graph/jftp.graph.json), [provenance](code-graph/provenance.json), [source citation cards](code-graph/evidence.json), [validation findings](code-graph/validation.json). |

[manifest.json](manifest.json) records all 16 preserved payload files, original paths, archive paths, byte sizes and SHA-256 hashes. `.gitattributes` disables text conversion here to retain the archived bytes across checkouts. Historical paths inside the files retain their original meaning; resolve their archived counterparts using the manifest. Runtime caches and ignored experiment logs are not part of this snapshot.

The generators recorded base revision `cdc95025ac74098f129bfd9cdcd613fa6348c8d0` with working-tree changes. The maps and graph contain 189 Java files, including seven startup test/helper sources; Repomix's selected scope includes 182 Java files. Earlier startup changes include the Maven descriptor. **This is the original reference set for the new preservation workflow, not an assertion that the files describe pristine upstream or the earliest pre-startup working tree.** Preserve the historical hashes and limitations instead of changing that provenance.

Use this snapshot to compare later stages and investigate regressions. For current-code navigation, validate source fingerprints or use an appropriately regenerated later snapshot. The historical graph helper is fixed-path and exact-HEAD guarded; copying it here would not make it a historical-source query tool.

The [catalogue](../README.md) and [workflow](../workflow.md) describe selecting and publishing later snapshots. Archived evidence is never an instruction to rerun a fixed-destination refresh command.
