# Versioned application context

This catalogue identifies saved analysis inputs for agents. Snapshots preserve evidence about source, not task status or proof of application behavior. Use a snapshot whose recorded source fingerprints match the question; consult original source and resources before implementation.

| Snapshot | Purpose | Recorded source state |
| --- | --- | --- |
| [original-initial-context](original-initial-context/README.md) | Immutable reference copy of the RepoMap, Repomix and code graph available when this convention was adopted. | Earlier working-tree analysis, based on `cdc95025ac74098f129bfd9cdcd613fa6348c8d0`, including startup changes. Exact scope and byte hashes are in its manifest; it is not a pristine upstream snapshot. |

No new analysis was generated when the original snapshot was archived. The existing files in `docs/repo-maps/`, `docs/RepoMix/` and `docs/code-graph/` are retained for existing references; their generated outputs also belong to the original reference set and must not be refreshed in place. Those directories' guides and maintained tooling may evolve without changing archived snapshot bytes.

After a major verified application step, add a new uniquely named snapshot and a catalogue row describing the change and source state. Do not rename an old snapshot to `current`, silently replace a row's target, or mark a historical snapshot as fresh just because its commit is an ancestor of HEAD. See the [refresh and comparison workflow](workflow.md), which supplements the [Legacy Skill](../../.agents/skills/legacy-codebase-workflows/SKILL.md).

Prefer one bounded snapshot per meaningful completed step rather than per file save. No refresh is required for documentation-only work that leaves all analysed inputs unchanged; explicitly record reuse and source-match evidence in the task summary. The existing graph helper's exact-HEAD guard can still reject unchanged source after a documentation commit; that rejection must not be bypassed by rewriting historical provenance.
