# Open-source graph and navigation tools for JFTP

Assessed 2026-10-15 using the installed legacy workflow's graph reference, current upstream documentation through Context7, upstream license files, and a fresh local pilot. This is a suitability comparison, not a benchmark. Only Graphify successfully indexed JFTP in this Windows session. Earlier trials described in the installed skill were treated as regression prompts, not as current local results.

| Tool | License checked | Useful role | JFTP decision |
| --- | --- | --- | --- |
| [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp/tree/v0.11.0) | [MIT, v0.11.0](https://github.com/DeusData/codebase-memory-mcp/blob/v0.11.0/LICENSE) | Persistent structural graph; CLI and MCP caller/impact queries without a successful application build. | First candidate from the skill. Verified Windows binary runs, but graph/config commands refuse the existing profile ACL. No JFTP index was produced by it here. |
| [Graphify](https://github.com/Graphify-Labs/graphify/tree/v8), package `graphifyy==0.9.91` | [Apache-2.0 main license](https://github.com/Graphify-Labs/graphify/blob/v8/LICENSE); repository also carries component notices | Local AST extraction; portable graph JSON, CLI relationship traversal and visualization/export options. | Working pilot. Agent queries use the saved graph and a small standard-library wrapper. The local acceptance checks expose constructor omissions and an incorrect worker target. |
| [Serena with Eclipse JDT LS](https://github.com/oraios/serena/blob/main/docs/02-usage/050_configuration.md) | [Application GPL-3.0-or-later; SolidLSP MIT](https://github.com/oraios/serena/blob/main/LICENSE) | Agent symbol/reference navigation through a Java language server. Depends on correct project import and classpath. | Strong candidate for the later API-refactoring phase; not installed or validated against this checkout. Distinguish current component licensing from older MIT releases. |
| [SCIP Java](https://github.com/sourcegraph/scip-java/blob/main/docs/getting-started.md) | [Apache-2.0](https://github.com/sourcegraph/scip-java/blob/main/LICENSE) | Build-integrated Java/Kotlin indexing; a durable semantic index for a suitable code-intelligence consumer. | Consider when build/dependency import works and a consumer is selected. It is not an agent query service by itself; not installed here. |

[GitNexus](https://github.com/abhigyanpatwari/GitNexus) was excluded from the unrestricted open-source shortlist: its [current license](https://github.com/abhigyanpatwari/GitNexus/blob/main/LICENSE) is PolyForm Noncommercial 1.0.0. Do not assume it permits the same corporate use as the listed permissive tools. This comparison does not bundle third-party runtime code or redistribute their executables.

## Why this pilot uses Graphify

JFTP's Maven descriptor targets Java 1.5 and declares external `ftpapi` and JavaHelp dependencies. Those facts come from the current `pom.xml`; no build was attempted to infer dependency availability. AST extraction provides useful navigation without first repairing the build. A graph database service would add operational work without addressing the resolution errors found here. Portable JSON plus bounded local queries is sufficient for the measured repository size.

The selected graph has no embeddings, clustering or model-generated labels. Provisioning fetched packages, then extraction used the cached pinned package with offline package resolution. Graphify's visual exports remain an optional upstream facility; no visualization server or hosted account is required for this pilot. See [README.md](README.md) for actual commands, coverage, source checks and the distinction between offline dependency resolution and denied network access.

## Codebase Memory MCP trial boundary

The official [v0.11.0 release](https://github.com/DeusData/codebase-memory-mcp/releases/tag/v0.11.0) Windows x86-64 archive was downloaded with Python TLS verification. `codebase-memory-mcp-windows-amd64.zip` SHA-256 matched its exact entry in the release's `checksums.txt`:

```text
6eb6beaf261b19e419766e78baf93cbc3cf1c6338cff8fb7c0234859f96d1685
```

`--version` returned `codebase-memory-mcp 0.11.0`; help confirmed local `cli` support. With an isolated external cache, `config list` refused secure CLI coordination because the account profile DACL grants mutation rights to an identity it treats as untrusted. This is a local environment refusal, not a JFTP parsing failure or evidence about current CBM graph accuracy. No ACL was changed, no alternate account identity was fabricated, and no auto-configuration installer was used. No CBM process remained at the cleanup check.

The installed skill notes that CBM's Java `lsp` resolver label is not equivalent to running JDT LS or javac. Should CBM be tried in a suitable environment later, repeat the same caller/startup/constructor/worker/dependency checks rather than assuming a resolver label or confidence number guarantees correctness.

## Recommendation for agent-led modernization

Use the saved Graphify graph now for bounded navigation, together with RepoMap, original source and characterization tests. Evaluate Serena/JDT LS when project import is healthy, because signature changes and overload-sensitive questions benefit from resolved Java references. Retain the five pilot questions as regression checks when replacing a backend. A different backend should be adopted based on measured answers to JFTP questions and its operational cost, not graph size or advertised language count.
