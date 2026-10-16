# POM hook verification - 2026-10-16

Scope: repository tooling, hook configuration, prompts, tests and README link.
Application Java sources, application `pom.xml`, dependencies and existing project
permissions were not changed. Pre-existing working-tree changes were preserved.

Environment: native Windows 365 PC, Python 3.14.3, Git for Windows Bash, Codex CLI
0.162.1. The native app-server selected `gpt-6.1-sol`. Native checks use the existing
project permission profile; no permanent sandbox or approval setting was changed.

## Deterministic verification

```powershell
python -B -m unittest discover -s .codex/hooks/tests -p 'test_*.py' -v
& 'C:\Program Files\Git\bin\bash.exe' -n .codex/hooks/pom-security.sh
```

35 tests passed, none skipped. They cover working-tree previews, property/parent/
BOM/profile/plugin/repository changes, nested/multiple/new/deleted/moved POMs,
ambiguous context, XML/entity/path checks, concurrent edits, provenance and date
validation, high-risk denials, missing research, CLI failure/timeout, real Bash
launches and configured command execution from a repository subdirectory.

Tests were written before the gate implementation. The initial fail-open scaffold
failed meaningful assertions, including property-change detection and required
denials. Missing-module discovery was not counted as a valid Red step. The UTC
timestamp regression was reproduced before its fix. The Windows denial regression
also had an observed Red: three launcher tests expected explicit JSON denial but
received exit 2; after the fix all passed.

## Real model and native checks

These checks used synthetic fixture POMs only, existing Codex access and real web
search. No advisory endpoint or reviewer was mocked. Fixtures were removed after
the checks; system-temp evidence was retained locally.

| Command | Observed result | Local evidence directory under `%TEMP%` |
| --- | --- | --- |
| `python -B .codex/hooks/tests/live_smoke.py risky` | PASS: both reviewers identified critical risks in proposed Log4j Core 2.14.1; source fixture unchanged | `jftp-pom-audit-4214d0z8` |
| `python -B .codex/hooks/tests/live_smoke.py removal` | PASS: both reviewers permitted complete removal in the standalone fixture; source fixture unchanged | `jftp-pom-audit-xmf_x6fr` |
| `python -B .codex/hooks/tests/native_smoke.py --reviewed-hook` | PASS: normal shell command executed; POM write denied before execution; native `hook/completed` status `blocked`; no destination POM created | `jftp-pom-native-g_2wu7ja` |
| `python -B .codex/hooks/tests/native_smoke.py --reviewed-hook --case risky` | PASS: native `apply_patch` triggered both real reviewers; critical risk denial blocked the patch and preserved the fixture content | `jftp-pom-native-bm3k80ru`, `jftp-pom-audit-bbo9qd6q` |
| `python -B .codex/hooks/tests/native_smoke.py` | PASS: normal activation with persisted user trust, without a trust bypass; ordinary command allowed and POM write blocked | `jftp-pom-native-lqmzslgp` |

The two direct review cases retain request data, separate verdict JSON files,
completed web-search JSONL events and stderr for both real reviewers. The removal
check exposed an overly broad uncertainty rule: inability to enumerate a removed
dependency's old transitive graph should not alone block an empty new graph. The
prompt was corrected and the actual check was repeated successfully.

The native check uses local app-server JSON-RPC, real tool calls, persisted
filesystem checks and native hook notifications. It does not infer successful
dispatch from the model's final statement. A process-only launch marker confirms
that Bash was actually reached.

The full native case waits for the actual completed hook, including code-mode
wait/poll calls. A model's early final message while the audit is still running
is not accepted as a completed security check.

## Windows regression and trust

Earlier native attempts failed despite successful direct script checks: the tool
executed and created the isolated fixture file. Native app-server evidence showed
`hook/completed` with `status: failed`, `hook exited with code 1`, and no blocking
decision. The Windows shell did not preserve exit-code-only denial as expected.
The final launcher and Bash error paths return explicit JSON denial with exit 0.
This was verified against both a successful ordinary command and a blocked POM
write, rather than counting a generic hook error as a successful denial.

A separate diagnostic attempt with an explicit read-only native thread stalled
in this machine's Windows sandbox setup. That test process was stopped. The final
native check uses the existing repository settings and does not claim a repaired
Windows sandbox.

The user trusted the original definition in `/hooks`; the launcher definition was
then corrected during native validation. Changing that definition changes its
trust hash. The `--reviewed-hook` check permits only this sole inspected hook for
one test thread and does not persist trust. The user subsequently trusted the final
definition, with hash
`sha256:b5e65c4d5dcbb284d0db7b1d337cef43c8ed950e74f1e37ea5145eb0d5f875c3`.
Native discovery reported `enabled: true` and `trustStatus: trusted`, without
warnings or errors. The ordinary native smoke then passed without a trust bypass.
`inspect_hooks.py` reports discovery and trust without modifying them.

## Scope limits

Maven compilation/build, application startup and Swing GUI QA were not run:
application behavior and packaging were not changed. No application context
snapshot refresh is required for this tooling-only change. Linux/WSL execution
has not been validated; the launcher includes its Bash selection path.

The guard is not a filesystem sandbox. Untrusted/disabled hooks, engine failures,
hard timeouts, hidden writes inside arbitrary scripts and tools outside native
hook coverage remain limitations described in [README.md](README.md). Research
may miss a vulnerability; an allowed proposal is not a universal security claim.
