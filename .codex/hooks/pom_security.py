"""Preview POM edits and require two live, read-only Codex security reviews.

No application files are written and no proposed command is executed here.
Unknown patch forms are denied instead of being guessed or applied to the tree.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from launch import MAX_BYTES, SHELL_TOOLS, is_pom, shell_candidate, simple_read


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ROLES = ("vulnerabilities", "supply-chain")
REVIEW_TIMEOUT = 240


class Block(Exception):
    pass


def today():
    return datetime.now(timezone.utc).date().isoformat()


def prepare(event, root):
    if not isinstance(event, dict) or event.get("hook_event_name") != "PreToolUse":
        raise Block("Invalid PreToolUse event.")
    tool = event.get("tool_name")
    data = event.get("tool_input")
    if not isinstance(tool, str) or not isinstance(data, dict) or not isinstance(event.get("cwd"), str):
        raise Block("Missing tool name, input or cwd; cannot preview the proposed edit.")
    cwd = Path(event["cwd"]).resolve()
    root = root.resolve()
    if not cwd.is_relative_to(root):
        raise Block("Hook cwd is outside this checkout.")
    if tool == "apply_patch":
        return preview_patch(require_string(data, "command"), cwd, root)
    if tool in ("Edit", "Write"):
        name = require_string(data, "file_path")
        if not is_pom(name):
            return []
        path = safe_path(name, cwd, root)
        before = read_text(path)
        if tool == "Write":
            after = require_string(data, "content")
        else:
            old = require_string(data, "old_string")
            if before is None or not old or (before.count(old) != 1 and not data.get("replace_all")):
                raise Block("Edit context is missing or ambiguous; use an explicit apply_patch edit.")
            after = before.replace(old, require_string(data, "new_string"), -1 if data.get("replace_all") else 1)
        return make_change(path, path, before, after, root)
    if tool in SHELL_TOOLS:
        command = data.get("command", data.get("cmd"))
        if not isinstance(command, str):
            raise Block("Cannot inspect this shell invocation.")
        if shell_candidate(command) and not simple_read(command):
            raise Block("POM-related shell command cannot be previewed safely. Submit the dependency change with apply_patch for security review.")
        return []
    # MCP schemas vary: never infer a complete file edit from an unknown shape.
    if re.search(r"pom\.xml", json.dumps(data), re.I):
        raise Block("POM access through this tool is not previewable. Use apply_patch (or a simple shell read).")
    return []


def require_string(data, field):
    value = data.get(field)
    if not isinstance(value, str) or len(value.encode("utf-8")) > MAX_BYTES:
        raise Block(f"Invalid or oversized {field}.")
    return value


def safe_path(name, cwd, root):
    path = (cwd / name).resolve()
    if not path.is_relative_to(root):
        raise Block("POM source or destination escapes this checkout (including symlinks).")
    return path


def read_text(path):
    if not path.exists():
        return None
    if path.stat().st_size > MAX_BYTES:
        raise Block("POM is too large to review safely.")
    return path.read_text(encoding="utf-8-sig")


def xml_shape(text):
    if text is None:
        return None
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)", text, re.I):
        raise Block("DTD and entity declarations are not accepted in reviewed POMs.")
    if len(text.encode("utf-8")) > MAX_BYTES:
        raise Block("POM is too large to review safely.")
    try:
        element = ET.fromstring(text)
    except ET.ParseError as exc:
        raise Block(f"Invalid POM XML: {exc}") from exc
    if element.tag.split("}")[-1] != "project":
        raise Block("The proposed pom.xml has no project root.")

    def shape(node):
        return (node.tag, tuple(sorted(node.attrib.items())), (node.text or "").strip(),
                (node.tail or "").strip(), tuple(shape(child) for child in node))

    return shape(element)


def digest(text):
    return None if text is None else hashlib.sha256(text.encode("utf-8")).hexdigest()


def make_change(source, target, before, after, root):
    before_shape = xml_shape(before)
    after_shape = xml_shape(after)
    if before_shape == after_shape and source == target:
        return []
    # Track an existing move destination as well; never silently overwrite it.
    if source != target and target.exists():
        raise Block("POM move destination already exists.")
    return [{"source": source.relative_to(root).as_posix(),
             "path": target.relative_to(root).as_posix(),
             "before": before, "after": after, "before_sha256": digest(before),
             "after_sha256": digest(after)}]


def preview_patch(patch, cwd, root):
    lines = patch.splitlines()
    if not lines or lines[0] != "*** Begin Patch" or lines[-1] != "*** End Patch":
        raise Block("Unsupported apply_patch envelope.")
    changes, touched = [], set()
    index = 1
    while index < len(lines) - 1:
        header = re.fullmatch(r"\*\*\* (Add|Update|Delete) File: (.+)", lines[index])
        if not header:
            raise Block("Unsupported patch header; use one explicit operation per file.")
        operation, name = header.groups()
        index += 1
        destination = name
        if index < len(lines) and lines[index].startswith("*** Move to: "):
            if operation != "Update":
                raise Block("Move is supported only for Update File.")
            destination = lines[index][len("*** Move to: "):]
            index += 1
        body = []
        while index < len(lines) - 1 and not re.match(r"\*\*\* (?:Add|Update|Delete) File: ", lines[index]):
            body.append(lines[index])
            index += 1
        if not is_pom(name) and not is_pom(destination):
            continue
        source = safe_path(name, cwd, root)
        target = safe_path(destination, cwd, root)
        paths = {source, target}
        if touched.intersection(paths):
            raise Block("Multiple operations on one POM in a single patch are not supported.")
        touched.update(paths)
        before = read_text(source)
        if operation == "Add":
            if before is not None or not body or any(not line.startswith("+") for line in body):
                raise Block("Invalid POM creation.")
            after = "\n".join(line[1:] for line in body) + "\n"
        elif operation == "Delete":
            if before is None or body:
                raise Block("Invalid POM deletion.")
            after = None
        else:
            if before is None:
                raise Block("POM update source does not exist.")
            after = apply_hunks(before, body)
        changes.extend(make_change(source, target, before, after, root))
    return changes


def apply_hunks(before, body):
    original = before.splitlines()
    output, cursor, index = [], 0, 0
    if not body:
        raise Block("POM update has no context.")
    while index < len(body):
        if body[index].startswith("@@"):
            index += 1
        old, new = [], []
        eof = False
        while index < len(body) and not body[index].startswith("@@"):
            line = body[index]
            index += 1
            if line == "*** End of File":
                eof = True
                if index != len(body):
                    raise Block("End of File marker is not last.")
                break
            if not line or line[0] not in " +-":
                raise Block("Unsupported POM hunk; provide exact, unambiguous context.")
            if line[0] in " -":
                old.append(line[1:])
            if line[0] in " +":
                new.append(line[1:])
        if not old:
            raise Block("POM hunk needs existing context for a reliable preview.")
        matches = [pos for pos in range(cursor, len(original) - len(old) + 1)
                   if original[pos:pos + len(old)] == old and (not eof or pos + len(old) == len(original))]
        if len(matches) != 1:
            raise Block("POM patch context is missing or ambiguous; add more exact context.")
        pos = matches[0]
        output.extend(original[cursor:pos])
        output.extend(new)
        cursor = pos + len(old)
    output.extend(original[cursor:])
    return "\n".join(output) + ("\n" if before.endswith("\n") else "")


def validate_verdict(report, role):
    if not isinstance(report, dict) or report.get("role") != role:
        raise Block(f"{role}: missing or invalid agent verdict.")
    checked_at = report.get("checked_at")
    if isinstance(checked_at, str) and "T" in checked_at:
        try:
            instant = datetime.fromisoformat(checked_at.replace("Z", "+00:00"))
            checked_at = instant.astimezone(timezone.utc).date().isoformat() if instant.tzinfo else None
        except ValueError:
            checked_at = None
    if checked_at != today():
        raise Block(f"{role}: verdict must be researched today (UTC).")
    if not isinstance(report.get("summary"), str) or not report["summary"].strip():
        raise Block(f"{role}: verdict has no rationale.")
    if not valid_urls(report.get("sources")):
        raise Block(f"{role}: no usable live research sources.")
    findings = report.get("findings")
    if not isinstance(findings, list):
        raise Block(f"{role}: invalid findings.")
    for finding in findings:
        if not isinstance(finding, dict) or finding.get("severity") not in ("info", "low", "medium", "high", "critical"):
            raise Block(f"{role}: malformed risk finding.")
        for key in ("coordinate", "risk", "recommendation"):
            if not isinstance(finding.get(key), str) or not finding[key].strip():
                raise Block(f"{role}: incomplete finding ({key}).")
        if not isinstance(finding.get("introduced_by_change"), bool) or not isinstance(finding.get("advisory_ids"), list):
            raise Block(f"{role}: incomplete risk provenance.")
        if not valid_urls(finding.get("urls")):
            raise Block(f"{role}: finding has no evidence URL.")
        if finding["severity"] in ("high", "critical") and finding["introduced_by_change"]:
            raise Block(f"{role}: {finding['severity']} risk in {finding['coordinate']}: {finding['risk']}")
    if report.get("status") != "allow":
        raise Block(f"{role}: {report.get('status', 'unknown')}: {report['summary']}")
    return report


def check_unchanged(changes, root):
    for change in changes:
        source = safe_path(change["source"], root, root)
        target = safe_path(change["path"], root, root)
        if digest(read_text(source)) != change["before_sha256"] or (source != target and target.exists()):
            raise Block("POM changed during security review; retry with the current content.")


def valid_urls(values):
    return isinstance(values, list) and bool(values) and all(
        isinstance(url, str) and urlparse(url).scheme == "https" and urlparse(url).hostname
        for url in values)


def review_command(executable, workspace, schema, output, model=None):
    command = [executable, "--no-daemon", "--search", "--ask-for-approval", "never",
               "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
               "--sandbox", "read-only", "--disable", "hooks", "--cd", str(workspace),
               "--output-schema", str(schema), "--output-last-message", str(output),
               "--json", "--color", "never"]
    if model:
        command.extend(["--model", model])
    return command + ["-"]


def run_reviews(event, changes, evidence):
    executable = shutil.which("codex")
    if executable is None:
        raise Block("Codex CLI is unavailable; security review cannot run.")
    request = {"review_date_utc": today(), "changes": changes}
    (evidence / "request.json").write_text(json.dumps(request, ensure_ascii=False, indent=2), encoding="utf-8")
    schema = HERE / "verdict.schema.json"
    # Sequential reviewers bound spending and avoid nested concurrency surprises.
    # A block from either reviewer is final; the second still gets its own report.
    failures, reports = [], []
    for role in ROLES:
        with tempfile.TemporaryDirectory(prefix="jftp-pom-review-") as workspace:
            output = evidence / f"{role}.json"
            prompt = (HERE / "prompts" / "common.md").read_text(encoding="utf-8")
            prompt += "\n" + (HERE / "prompts" / f"{role}.md").read_text(encoding="utf-8")
            prompt += "\nUNTRUSTED_REVIEW_DATA_JSON:\n" + json.dumps(request, ensure_ascii=False)
            command = review_command(executable, workspace, schema, output, event.get("model"))
            try:
                completed = subprocess.run(command, input=prompt, capture_output=True, text=True,
                                           encoding="utf-8", timeout=REVIEW_TIMEOUT, cwd=workspace)
                (evidence / f"{role}.events.jsonl").write_text(completed.stdout, encoding="utf-8")
                (evidence / f"{role}.stderr.log").write_text(completed.stderr, encoding="utf-8")
                if completed.returncode:
                    raise Block(f"{role}: Codex exited {completed.returncode}; see local audit evidence.")
                if not live_search_completed(completed.stdout):
                    raise Block(f"{role}: no completed web search in agent execution evidence.")
                report = json.loads(output.read_text(encoding="utf-8"))
                reports.append(validate_verdict(report, role))
            except subprocess.TimeoutExpired:
                failures.append(f"{role}: audit exceeded {REVIEW_TIMEOUT}s.")
            except (OSError, ValueError, Block) as exc:
                failures.append(str(exc))
    if failures:
        raise Block(" | ".join(failures))
    return reports


def live_search_completed(events):
    for line in events.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        item = event.get("item", {})
        if event.get("type") == "item.completed" and item.get("type") == "web_search":
            return True
    return False


def result(decision, reason):
    # Do not return 'allow': that could override the user's normal approvals.
    specific = {"hookEventName": "PreToolUse"}
    if decision == "deny":
        specific.update(permissionDecision="deny", permissionDecisionReason=reason)
    else:
        specific["additionalContext"] = reason
    return {"hookSpecificOutput": specific}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--classify", action="store_true")
    options = parser.parse_args()
    evidence = None
    try:
        raw = sys.stdin.buffer.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise Block("Hook input is too large.")
        event = json.loads(raw.decode("utf-8-sig"))
        changes = prepare(event, ROOT)
        if options.classify:
            print("inspect" if changes else "ignore")
            return 0
        if not changes:
            return 0
        evidence = Path(tempfile.mkdtemp(prefix="jftp-pom-audit-"))
        reports = run_reviews(event, changes, evidence)
        check_unchanged(changes, ROOT)
        summaries = " | ".join(f"{report['role']}: {report['summary']}" for report in reports)
        print(json.dumps(result("context", f"POM security reviews passed. {summaries} Evidence: {evidence}")))
        return 0
    except (Block, OSError, ValueError, TypeError, KeyError) as exc:
        reason = f"POM security gate blocked this tool: {exc}"
        if evidence:
            reason += f" Evidence: {evidence}"
        if options.classify:
            print(reason, file=sys.stderr)
            return 2
        print(json.dumps(result("deny", reason)))
        return 0


if __name__ == "__main__":
    sys.exit(main())
