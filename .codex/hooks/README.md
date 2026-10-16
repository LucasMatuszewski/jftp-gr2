# Maven dependency security gate for Codex

This repository's `.codex/hooks.json` registers a synchronous `PreToolUse` command
hook. It previews proposed POM changes before the write and runs two independent
Codex CLI review sessions. It does not change the application's dependencies.

## Activation

Requirements: Codex CLI with the documented hooks and `exec` flags (verified
locally with **0.162.1**), an existing working Codex login, Python 3.10+
(`python3` on PATH), Bash, and access to live web search. `launch.py` selects Git
for Windows Bash at `%ProgramFiles%/Git/bin/bash.exe`; `C:/Windows/System32/bash.exe`
starts WSL and is not this native Windows launcher. Adjust `launch.py` if Git is elsewhere.
The local `.gitattributes` keeps hook files in LF format, including Windows
checkouts with `core.autocrlf` enabled, so Bash scripts remain executable.
Linux/WSL uses Bash and its own installed/authenticated Codex CLI.

1. Open a new Codex session in this trusted checkout, or reload its configuration.
2. Open `/hooks`, inspect `.codex/hooks.json` and the scripts/prompts in this
   directory, then trust this hook. New or changed hook definitions need review.
3. Confirm the hook is enabled. A global or managed `features.hooks = false`
   prevents dispatch. Installing files alone does not establish activation.

No global settings, stored trust decisions, application PRD/ADR, agent instructions
or existing project permission settings are changed by this implementation.

## Dispatch and review

Codex's matcher filters **tool names**, not POM paths or XML. `apply_patch` has
`Edit` and `Write` matcher aliases, but the JSON event still names `apply_patch`
and carries the patch in `tool_input.command`. Shell/unified-exec events are named
`Bash` and also use `tool_input.command`. This differs from Claude's
`old_string`/`new_string` edit shape. Codex currently skips `prompt`/`agent` hook
handlers; the Claude example cannot be copied as an executable Codex agent hook.
The documented configuration does not provide Claude's example `if` selector.

The matcher covers tools broadly so that MCP POM writes are not silently omitted.
`pom-security.sh` reads the JSON, invokes the Python preview classifier, and uses
an `if` to start reviewers only for a semantic POM change. Paths resolve from the
session working directory and must remain inside this checkout, including symlinks.
The configured Python bootstrap resolves from the Git root, including sessions
in subfolders. `launch.py` forwards stdin to Bash without shell interpolation.

The preview supports explicit `apply_patch` add/update/delete/move operations,
multiple POMs, exact unambiguous hunks, and direct `Edit`/`Write` JSON shapes.
It reads the current working-tree content, never a stale HEAD-only diff. POMs
are compared as XML; comments and formatting alone do not start model calls.
Other semantic changes are reviewed conservatively, including parent/BOM/profile,
properties, repository, plugin, scope and exclusion changes. No Maven command or
proposed shell command runs during preview. Unsupported/ambiguous hunks, invalid
XML, DTD/entities, oversized inputs and concurrent POM changes are denied.

| Reviewer | Prompt | Main responsibility |
| --- | --- | --- |
| `vulnerabilities` | `prompts/vulnerabilities.md` | Exact versions, CVE/GHSA/OSV/vendor reports, affected/fixed ranges, security release notes and transitive risks |
| `supply-chain` | `prompts/supply-chain.md` | Publisher/repository trust, malicious releases, typosquatting, maintenance, build execution and compatibility changes |

Both use `prompts/common.md` and `verdict.schema.json`. Each receives only the
proposed before/after POM data and uses live web search. The supplied event's model
is preserved when present; otherwise the CLI default applies. They run sequentially,
each with a 240-second deadline, in a temporary working directory outside the
checkout, with read-only sandboxing, no approval prompts, ephemeral sessions and
user config loading disabled. Hooks are disabled **only in those child processes**
to prevent recursive review. No trust or sandbox bypass is used by the reviewers.
They do not inherit this repository's unrelated MCP configuration or agent task.

The gate requires valid verdicts from both roles, research dated today in UTC,
HTTPS sources and an actual completed web-search event in each CLI execution log.
An introduced/increased high or critical finding blocks even if the agent says
`allow`. A `block`/`unknown` verdict, missing evidence, malformed JSON, failed CLI,
unavailable login/network or timeout also blocks. Existing unrelated legacy risks
are reported separately. Lower risks require rationale and mitigation.

Denial uses explicit JSON `permissionDecision: deny` with exit **0**, including
launcher/classifier failures. This is deliberate: native validation found that
the Windows hook shell mapped a child exit **2** to **1**, which Codex treated as
a hook failure and allowed the tool to continue. Exit-code-only blocking did not
work in this environment. Diagnostic details are also written to stderr.
Success adds review context without emitting `permissionDecision: allow`, so the
normal tool approval policy still applies. Both reviewers run even if one blocks.
There is no approval cache: every proposed semantic change is researched again.

Audit evidence is kept outside Git in the printed system-temp directory
`jftp-pom-audit-*`: request, individual JSON verdicts, CLI JSONL events and stderr.
Treat it as local project data; the operating system may clean it up. The prompts
prohibit uploading whole POMs to search engines and treat XML/web content as data.
Optional `JFTP_POM_TRACE_FILE` launch diagnostics contain only a process marker;
the native smoke test uses this to prove the actual Bash handler was reached.

## Coverage limits

POM-related shell commands and Maven `versions:`/`release:` mutation commands are
denied when their result cannot be previewed; submit an `apply_patch` instead.
A small allowlist permits simple `cat`, `Get-Content`, `type` and `git diff --`
reads without pipes, redirection or command substitution. Unknown MCP schemas
mentioning `pom.xml` are denied; even MCP reads may need a simple shell read.

This hook is a review guard, not filesystem isolation or a complete dependency
scanner. An arbitrary script that hides a POM write without mentioning the file,
a Git checkout/reset, an external editor or a continued interactive shell can
escape this filter. Codex does not emit another `PreToolUse` for `write_stdin`.
Full inherited/transitive resolution is not established by parsing one POM; the
reviewers must report material uncertainty. They do not execute untrusted Maven
plugins to obtain an effective POM or dependency tree. This can block proposals
that need additional local resolution evidence.

Codex skips untrusted/disabled hooks. A hook engine launch failure, hard timeout
or malformed hook response may fail open in Codex. The script converts its own
known failures to denials and uses a 540-second outer deadline, longer than both
review deadlines, but cannot change Codex's engine behavior. Research and model
judgment can miss vulnerabilities. An `allow` is a scoped review result, not a
guarantee that a dependency is secure. Repeated edits incur model usage and latency.

## Verification

Deterministic behavior and actual launcher wiring (no model calls):

```powershell
python -B -m unittest discover -s .codex/hooks/tests -p 'test_*.py' -v
& 'C:\Program Files\Git\bin\bash.exe' -n .codex/hooks/pom-security.sh
```

Opt-in real-model checks with an existing Codex login and live web search:

```powershell
python -B .codex/hooks/tests/live_smoke.py risky
python -B .codex/hooks/tests/live_smoke.py removal
python -B .codex/hooks/tests/inspect_hooks.py
python -B .codex/hooks/tests/native_smoke.py
python -B .codex/hooks/tests/native_smoke.py --case risky
```

These create synthetic POMs in a temporary test subdirectory and remove them.
`risky` proposes Log4j Core 2.14.1 and requires a concrete high/critical risk denial;
`removal` removes that dependency and requires both reviews to pass. A CLI failure
is not counted as proof of CVE detection. Neither test writes the application's
POM. Direct launcher checks do not prove native Codex dispatch or persistent trust.
The native smoke uses the installed app-server protocol and checks real
`hook/completed` notifications, actual file state, and a successful unrelated
command. The `risky` case exercises native `apply_patch` plus both real model
reviews. It uses existing repository permissions: it does not attempt to repair
or replace this PC's Windows Sandbox configuration.

For automation that has already inspected this sole hook definition, the native
test accepts `--reviewed-hook`. It bypasses trust for that test thread only,
refuses to run if another hook is discovered, and does not persist a trust
decision. Normal activation still uses `/hooks`; changing the definition requires
reviewing its new hash. Reviewers themselves never bypass trust or sandboxing.
See [verification.md](verification.md) for observed results and limitations.

## Documentation consulted

Verified on 2026-10-16 against the installed CLI help, Context7 `/openai/codex`, and
the [official Hooks documentation](https://learn.chatgpt.com/docs/hooks) and
[non-interactive mode documentation](https://learn.chatgpt.com/docs/non-interactive-mode).
The generated schemas/source indexed by Context7 were supplementary; current
release behavior and local execution take precedence over the `main` branch.
