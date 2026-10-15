# Codex permissions for group two

The project [.codex/config.toml](../.codex/config.toml) selects workspace editing,
public network access and automatic approval review (`on-request` plus
`auto_review`). Logs remain readable for shell searches. Secret environment files
and `secrets/` are denied; the inherited workspace policy protects `.git`,
`.agents`, `.codex` and `.aws` from ordinary sandboxed writes.

The active network proxy allows public hosts through `"*" = "allow"` and retains
its default local/private-network guard. Network access does not mean every
request is judged. Matching `curl`/`wget` operations explicitly request review
through [network.rules](../.codex/rules/network.rules); other permitted operations
only invoke automatic review if another applicable control requires approval.

For log analysis, use bounded output rather than denying the file path:

```bash
rg -n -m 20 --max-columns 200 --max-columns-preview 'ERROR|WARN' logs | head -n 80
tail -n 80 logs/application.log
```

On PowerShell, replace `head` with `Select-Object -First 80`. Inspect small
relevant excerpts and avoid dumping whole logs. `tool_output_token_limit = 4000`
bounds each result stored in history; it is not a strict Read-tool prohibition.
Codex filesystem `deny` would also prevent sandboxed `rg`/`grep` access.

Project config/rules require a trusted checkout and a new/reloaded session.
Remove conflicting legacy `sandbox_mode` / `sandbox_workspace_write` settings
from other loaded layers. This change does not alter the current session's
sandbox or user-home configuration. Native sandbox enforcement remains unverified
on this PC because of the known sandbox launch failure.

Official references: [permissions](https://learn.chatgpt.com/docs/permissions),
[automatic review](https://learn.chatgpt.com/docs/sandboxing/auto-review),
[output budget](https://learn.chatgpt.com/docs/config-file/config-reference).
