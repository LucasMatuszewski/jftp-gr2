#!/usr/bin/env bash
# Codex passes one event as JSON on stdin. Never eval any part of that event.
set -uo pipefail

block() {
  printf 'POM security gate: %s\n' "$1" >&2
  # Native Windows hook shells can map an external exit 2 to shell exit 1.
  # Emit an explicit decision with exit 0 so the denial survives that wrapper.
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"POM security gate could not preview or audit this call. Use apply_patch for POM edits; see hook stderr for details."}}'
  exit 0
}

# Optional launch diagnostics contain no event payload or credentials.
if [[ -n "${JFTP_POM_TRACE_FILE:-}" ]]; then
  printf 'POM hook launched: pid=%s\n' "$$" >> "$JFTP_POM_TRACE_FILE" || block 'Cannot write requested launch trace.'
fi

hook_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || block 'Cannot locate hook scripts.'
if command -v python3 >/dev/null 2>&1; then
  python_cmd=python3
elif command -v python >/dev/null 2>&1; then
  python_cmd=python
else
  block 'Python 3 is required; the requested tool is blocked.'
fi

payload="$(cat)" || block 'Cannot read hook input.'
# launch.py has already filtered unrelated inputs before starting Bash.
# Preview once; the validator starts agents only for a semantic POM change.
if [[ -n "$payload" ]]; then
  printf '%s' "$payload" | "$python_cmd" -B "$hook_dir/pom_security.py" || block 'Audit process failed.'
else
  block 'Hook input is empty.'
fi
