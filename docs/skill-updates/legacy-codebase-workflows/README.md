# Architecture workflow update bundle

This review bundle records the reusable workflow prepared with the jFTP
architecture documentation. It belongs to the `legacy-codebase-workflows`
skill, rather than application code or runtime configuration.

- `SKILL.md.patch` adds the architecture workflow to the skill's routing table.
- `references/architecture-diagrams.md` is placed under the target skill's
  `references/` directory. Its relative links resolve in that installed skill,
  rather than this partial review bundle.

The project installations for [Codex](../../../.agents/skills/legacy-codebase-workflows/SKILL.md)
and [Claude](../../../.claude/skills/legacy-codebase-workflows/SKILL.md) include
this workflow. Both installed references match the exported reference after
newline normalization, including the reviewed installation flags and their
authorization explanation. The bundle does not install tools or activate hooks.
