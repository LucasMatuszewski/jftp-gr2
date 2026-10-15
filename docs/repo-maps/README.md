# JFTP repository maps

Snapshot of `cdc95025ac74098f129bfd9cdcd613fa6348c8d0`, refreshed on 2026-10-15 from the working tree. These reports navigate original source; they do not prove runtime behavior.

| Report | Captured definitions included | Raw map estimate | Annotated report estimate | Generation |
| --- | --- | --- | --- | --- |
| [Overview](jftp.overview.python.md) | 1,018 / 1,629 (611 omitted) | 16,384 tokens | 16,785 tokens | 5.144 s |
| [Complete captured-definition index](jftp.definitions.python.md) | 1,629 / 1,629 (none omitted) | 24,917 tokens | 25,328 tokens | 4.461 s |

Token estimates use `ceil(Unicode characters / 4)`, not a model tokenizer. Overview budget: 16,384; complete-index budget: 65,536. Both use compact declarations with original paths and line numbers. No snippets were clipped; all 189 Java files parsed without parser failures. Definitions occur in 186 files.

This working-copy refresh includes 182 production Java files and seven new test/helper sources; the Maven descriptor differs from HEAD. Application source bodies are unchanged.

## Scope and limits

Scope is `src/` plus `pom.xml`: 572 candidates, 433 eligible UTF-8 files, 189 parsed Java files. The mapper skipped 98 binary files and 41 non-UTF-8 German properties files. The source pack preserves those properties after explicit decoding; see [Repomix guide](../RepoMix/README.md).

The complete index covers every definition captured by the configured Java queries, not every possible construct, dependency or runtime relationship. The overview is deliberately selective. External `ftpapi` and JavaHelp implementations are outside this checkout. Reflection, XML/resources and application lifecycle still require original-source inspection.

For architecture, system design or module ownership, start with the overview. For a missing declaration, search the complete index. For application workflows or broad implementation context, use [the full-code pack](../RepoMix/jftp.full-no-comments.xml), then inspect original bodies and callers before edits. These outputs are snapshots; refresh after relevant source changes.

## Implementation and provenance

The installed skill pins native release `legacy-tools-v0.3.0`. Native setup stalled and the GitHub CLI release check returned HTTP 401, so these reports use the documented Python fallback, version 1.2.0, with `tree-sitter==0.25.2` and `tree-sitter-language-pack==0.13.0`. No older native binary was substituted and no Rust compilation was attempted.

The Windows sandbox's repository trust is provided through Git environment configuration. The mapper sanitizes that configuration; a small process-local adapter reapplies `safe.directory` only to Git commands targeting this exact repository. Git configuration and installed skill files are unchanged. Both exported reports contain the independently verified HEAD; their working-copy fingerprints match their inventory sidecars.

[Shared provenance](../RepoMix/provenance.json) records the configuration, source encodings, original byte hashes, output hashes and measured generation times. Local raw maps, inventories, metadata, logs and regeneration helpers are under `artifacts/`. Only `artifacts/` is ignored; primary reports and this guide remain Git-visible. Scoped attributes preserve LF report bytes.

## Refresh

Try the skill's `setup_native.py status` and pinned installation first. Use the returned verified native program when ready and label newly generated native reports accordingly. If native execution remains unavailable, use the isolated Python fallback. Do not install tooling into the application environment or stage generation inside this checkout.

The local helper regenerates both maps and the selected pack, including verification. From the repository root in PowerShell, with a working Python 3.12–3.14 interpreter and an external Repomix runtime:

```powershell
$pythonExe = 'C:\Users\BiuroEdukey\AppData\Local\Python\pythoncore-3.14-64\python.exe'
$skillPath = Join-Path $env:USERPROFILE '.agents\skills\legacy-codebase-workflows'
$toolRoot = Join-Path $env:TEMP 'jftp-gr2-context'
$env:PYTHONPATH = Join-Path $toolRoot 'python-deps'
uv --no-cache pip install --python $pythonExe --target $env:PYTHONPATH --only-binary :all: -r (Join-Path $skillPath 'requirements-map.txt')
pnpm --dir (Join-Path $toolRoot 'repomix-runtime') --store-dir (Join-Path $toolRoot 'pnpm-store') add --save-exact --ignore-scripts repomix@1.18.1
$contextStage = Join-Path $toolRoot ('generation-' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
& $pythonExe docs/repo-maps/artifacts/build_context.py --skill $skillPath --runtime (Join-Path $toolRoot 'repomix-runtime') --staging $contextStage --refresh
```

Helpers are local ignored artifacts. For another checkout, the primary provenance provides the selected paths, processing policy and exact dependency pins; the skill's mapper and exporter provide the standard generation path. Do not reuse `--pack-only` after changing source: regenerate maps too. No application build, tests or GUI launch are part of this refresh.
