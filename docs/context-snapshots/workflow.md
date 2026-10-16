# Preserve, refresh and compare application context

Read this when implementing a feature, refactoring, or changing Java, libraries, build configuration or resources. Use the [Legacy Skill](../../.agents/skills/legacy-codebase-workflows/SKILL.md) for extraction, source verification and tooling. This document adds the repository's immutable snapshot and coordinated-publication policy; it does not authorize application changes beyond the agreed exercise.

## When a snapshot is required

A major step is a verified feature or refactoring slice, a Java/runtime or library migration stage, or a substantial change to module boundaries, build/dependency wiring, resources or reflective configuration. After integrating and verifying that step, refresh all three context products: RepoMap, the selected Repomix profiles and the code graph. Do this before marking the step complete or handing its results to another agent. Record the new snapshot with the same logical application change when committing is authorized.

Intermediate failing experiments do not replace a verified snapshot. Do not generate on every save or let independent agents regenerate shared outputs while other agents are still editing their inputs. Documentation-only work without analysed input changes can reuse the prior snapshot, with source-match evidence and any existing freshness limitation stated explicitly.

## Coordinate contributors

For substantial work, the coordinator assigns independent modules/files to implementing agents and names one snapshot publisher and a reviewer. Workers preserve each other's edits and report changed inputs and unresolved effects. Serialize work on shared files. The publisher waits for integrated source and the required verification results; the reviewer checks scope, provenance, coverage and representative source relationships. These roles may be combined when parallel agents would not help a small task.

Freeze the examined source while extracting. Record HEAD, dirty state and byte hashes of every selected source input, including untracked files deliberately included in the step. If any input changes before publication, discard that candidate and regenerate all affected products against the new state. A shared HEAD alone does not establish equal source inputs or equal scope.

## Preserve the original and name each new result

`original-initial-context/` is the preserved initial reference set. Its manifest records exact copies, their original paths and original generation metadata. Never edit, delete, regenerate or relabel its files or replace its manifest. Corrections belong in a new snapshot with an explanation. The original directory is application-context evidence, not an executable checkout or a live freshness index.

For a new result, create a previously nonexistent directory under `docs/context-snapshots/` named `<change-slug>-<source-id>`, for example `java-21-stage-1-<source-id>` or `passive-mode-fix-<source-id>`. Use a source commit abbreviation after a source commit exists; otherwise use a digest of the selected input manifest and explicitly record the dirty working tree. These are naming examples, not an agreed Java target. If the name is already present, verify/reuse its exact source state or choose a new distinct ID; never overwrite it. Preserve earlier steps as well as the original.

Keep `repo-maps/`, `RepoMix/` and `code-graph/` beneath that directory, plus a short `README.md`, `manifest.json` and `comparison.md`. Use readable labels in the catalogue, including the feature/refactor or upgrade stage. A documentation commit can change HEAD after generation: retain the real examined revision and source hashes rather than inventing a generation against the new commit.

## Generate and validate a complete set

1. Read the existing [RepoMap](../repo-maps/README.md), [Repomix](../RepoMix/README.md) and [graph](../code-graph/README.md) guides and the Legacy Skill references appropriate to those products. Check pinned native mapper readiness first; document any supported fallback. Preserve the existing scope, resource encodings and comment/compression choices unless the agreed change requires a documented adjustment.
2. Choose a fresh external staging directory and explicit source allowlist. Exclude all saved context recursively, including `docs/context-snapshots/**`, `docs/repo-maps/**`, `docs/RepoMix/**` and `docs/code-graph/**`, plus caches, build output, agent configuration and protected inputs. Never map previously generated source packs into themselves. Keep runtime/cache data outside the checkout.
3. Produce a RepoMap overview and complete captured-definition index when the previous set includes one; retain coverage, omitted/clipped definitions, skipped files and parse warnings. Export named reports and necessary inventory/metadata evidence using the skill's exporter.
4. Regenerate the selected full-code Repomix pack; if a compressed comparison profile is retained, regenerate it from the same chosen source input. Preserve explicit comment handling and resource encoding policies. Validate source/pack coverage and byte hashes; identify implementation lost by compression.
5. Extract the code graph against the same source state, recording its own narrower/wider scope. Recheck representative callers, startup, constructors, anonymous workers and dependency/reflection boundaries from original source. Regenerate citation cards and review findings; never copy old `source-checked` labels or rejected edges onto a different graph without reviewing them again.
6. Capture a manifest with the change label, parent snapshot, original baseline, actual source revision, dirty/untracked input state, per-product source hashes and scope, tool/configuration versions, output paths/hashes, generation measurements, coverage/warnings and validation evidence. A graph may include tests excluded by a pack; record the scope difference rather than describing them as identical corpora. Record the generator version/hash needed to reproduce the set.
7. Verify the before/after source fingerprints match and recheck the original snapshot against its unchanged manifest. Publish the new directory only when all three products and their validations are complete. A tool failure leaves a candidate, not a current snapshot: report the missing check and keep prior references intact.
8. Write `comparison.md` against both the previous step and the original baseline. Describe actual source/configuration changes, added/removed/moved declarations, reviewed caller/impact differences, scope differences and validation limits. Separate code changes from changes caused by the extractor, tool version, token budget, comment policy or classpath. Keep the catalogue and relevant guide links current, preserving the original row.

Keep primary snapshots and required provenance visible to Git. Only disposable `artifacts/` directories may be ignored by default; never hide an entire snapshot. Follow explicit-path staging and the existing commit/push rules. Do not install automatic refresh hooks or change MCP registrations as part of this workflow.

## Existing helper limitations

The current `docs/repo-maps/artifacts/build_context.py` and `docs/code-graph/graph.py refresh` write to fixed legacy destinations. **Do not run these in-place refresh recipes against the original reference outputs.** Use the skill's low-level tools with explicit external staging/output and export/copy validated products into the new named directory. If adapting a helper is necessary, add explicit source/output selection and no-overwrite checks before using it; test that separately from the application. Moving a root-relative helper into a snapshot directory does not make it snapshot-aware.

The existing graph query helper reads a fixed adjacent graph and requires an exact HEAD match. Do not change an archived graph/provenance or remove the guard just to make a historical query run. For historical inspection, use bounded graph-file queries against the selected graph and source evidence from its recorded state; describe any source mismatch. Any future snapshot-aware wrapper must select source and snapshot explicitly and preserve these distinctions. This documentation change does not implement that wrapper or run a fresh application analysis.

## Legacy Skill assessment

The installed skill already provides native-first setup, scope/budget accounting, external staging, named exports, original-source citation checks, Repomix policy choices, graph acceptance questions and refresh triggers. Its `references/saved-context.md` recommends current primary outputs at the top level and does not define an immutable multi-step history; `references/code-graphs.md` does not establish a coordinated three-product publication transaction. Following only those refresh recipes can overwrite the initial reference set.

This repository policy supplies the missing naming, preservation, ownership and comparison rules without expanding always-loaded agent instructions. A reusable upstream enhancement could add an optional "immutable baselines and change snapshots" section to `saved-context.md`, linked from the modernization and graph references: honor repository policy, create a new destination, record source/tool fingerprints, validate all required products before promotion, and compare against baseline and parent. Such an enhancement belongs in the skill's source repository through its normal reviewed change process. Installed `.agents/skills/` copies remain untouched.
