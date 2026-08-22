"""Cortex mock tools, the tools your PM chief-of-staff agent is allowed to call.

These are plain Python functions over the files in `fixtures/`. They are imported
directly by `agent.py`, so this file is the single place that defines what Cortex
can and cannot do. Ask your coding agent to add, remove, or tighten a tool here.

Design note that matters for the course: there is deliberately NO publish tool.
Cortex can read and DRAFT a status update, and it can PROPOSE backlog stories (which
are capped and queued for a human), but it can never post to a channel, create or
merge a ticket/PR, commit a ship date, or mark a launch gate. The agent line is
enforced here, in infrastructure, not by a prompt.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Optional

FIXTURES = Path(__file__).parent / "fixtures"

# Commitment bound (M5). A run that tries to queue more than this many backlog
# stories is rejected by infrastructure and must be escalated, even if the PRD
# would justify more. Auto-committing a flood of "real" work is the money analog.
MAX_QUEUE_ITEMS = int(os.environ.get("CORTEX_MAX_QUEUE_ITEMS", "10"))


def _load_json(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


def project_id_from_task(task_body: str) -> Optional[str]:
    """Return the single project ID named by the task, if present."""
    match = re.search(r"\bP-[A-Z0-9-]+\b", task_body or "", flags=re.IGNORECASE)
    return match.group(0).upper() if match else None


def _project_id_from_query(query: str) -> Optional[str]:
    """Resolve a known project ID or name in a query to its project ID."""
    query_lower = (query or "").lower()
    for project_id, record in _load_json("projects.json").items():
        short_name = record.get("name", "").split(" (")[0]
        if project_id.lower() in query_lower or short_name.lower() in query_lower:
            return project_id
    return None


def _project_name_from_query(query: str) -> Optional[str]:
    """Resolve a known project ID or name in a query to its short name."""
    project_id = _project_id_from_query(query)
    if not project_id:
        return None
    return _load_json("projects.json")[project_id].get("name", "").split(" (")[0]


def enforce_project_scope(fn: str, args: dict, project_scope: Optional[str]):
    """Bind every project-aware retrieval/action to the task's project."""
    args = dict(args)
    if not project_scope:
        return args, None
    if fn in {"get_project", "get_activity", "propose_stories"}:
        requested = str(args.get("project_id", "")).strip().upper()
        if requested and requested != project_scope:
            return args, {"error": "cross_project_request_rejected",
                          "task_project_id": project_scope,
                          "requested_project_id": requested,
                          "action": "use only the project named in the task"}
        args["project_id"] = project_scope
    elif fn in {"search_past_updates", "get_roadmap"}:
        query = str(args.get("query", ""))
        query_project = project_id_from_task(query) or _project_id_from_query(query)
        if query_project and query_project != project_scope:
            return args, {"error": "cross_project_request_rejected",
                          "task_project_id": project_scope,
                          "requested_project_id": query_project,
                          "action": "use only the project named in the task"}
        args["query"] = f"{project_scope} {query}".strip()
    return args, None


def _markdown_sections(text: str) -> list[tuple[str, str]]:
    """Split a Markdown document into H2 sections, preserving each heading."""
    matches = list(re.finditer(r"^## .+$", text, flags=re.MULTILINE))
    sections = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(0)[3:].strip(), text[match.start():end].strip()))
    return sections


def get_task(which: str = "happy") -> dict:
    """Read the inbound PM task brief to work on.

    Args:
        which: one of "happy", "missing-data", "jailbreak".
    Returns the raw task text plus its source label.
    """
    path = FIXTURES / f"task-{which}.md"
    if not path.exists():
        return {"error": f"no task fixture named '{which}'",
                "available": ["happy", "missing-data", "jailbreak"]}
    return {"which": which, "body": path.read_text()}


def get_project(project_id: str) -> dict:
    """Look up a single project by its ID. Returns {"error": ...} if not found."""
    project_id = str(project_id).strip()
    projects = _load_json("projects.json")
    record = projects.get(project_id)
    if record is None:
        return {"error": "project_not_found", "project_id": project_id,
                "hint": "no source data exists for the project named in the task; do not substitute another project"}
    # Return the project WITHOUT its activity blob; activity is a separate tool call
    # so the agent has to deliberately pull it (a teachable retrieval step).
    return {k: v for k, v in record.items() if k != "activity"}


def get_activity(project_id: str) -> dict:
    """Pull recent engineering activity (merged PRs, open issues, Sev-1s) for a project."""
    project_id = str(project_id).strip()
    projects = _load_json("projects.json")
    record = projects.get(project_id)
    if record is None:
        return {"error": "project_not_found", "project_id": project_id}
    return {"project_id": project_id, "activity": record.get("activity", [])}


def search_past_updates(query: str = "") -> dict:
    """Search previous status updates and decisions for tone and precedent (the
    memory/retrieval surface).

    Naive keyword overlap over a small fixture so M4's retrieve-vs-reason lesson is
    concrete: relevant precedent is returned, irrelevant precedent is not."""
    query = (query or "").lower()
    corpus = _load_json("past-updates.json") + _load_json("decision-log.json")
    project_name = _project_name_from_query(query)
    requested_project_id = project_id_from_task(query)
    if requested_project_id and not project_name:
        return {"query": query, "matches": [],
                "note": "no history found for the project named in the task; no fallback used."}
    terms = {t for t in re.findall(r"[a-z0-9-]+", query) if len(t) > 2}
    ranked_hits = []
    for u in corpus:
        haystack = f"{u.get('project','')} {u.get('summary','')} {u.get('theme','')}".lower()
        if project_name and u.get("project", "").lower() != project_name.lower():
            continue
        score = sum(term in haystack for term in terms)
        if project_name or score:
            ranked_hits.append((score, u.get("week", u.get("date", "")), u))
    ranked_hits.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return {"query": query, "matches": [item[2] for item in ranked_hits],
            "note": "relevant prior updates + decisions, newest relevant evidence first."}


def get_roadmap(query: str = "") -> dict:
    """Return the roadmap. Some items are flagged confidential/embargoed, those must
    never appear in an external or company-wide update. `query` is a hint; the file
    is small enough to return whole so the agent can cite what it relied on."""
    text = (FIXTURES / "roadmap.md").read_text()
    project_name = _project_name_from_query(query)
    query_lower = (query or "").lower()
    for heading, section in _markdown_sections(text):
        if ((project_name and project_name.lower() in heading.lower())
                or (not project_name and query_lower and query_lower in heading.lower())):
            visibility = heading.rsplit(".", 1)[-1].strip() if "." in heading else "unspecified"
            result = {"query": query, "project": project_name or heading,
                      "visibility": visibility, "roadmap_section": section}
            if "confidential" in heading.lower() or "embargoed" in heading.lower():
                result["warning"] = "CONFIDENTIAL: do not share outside the core team."
            return result
    return {"error": "roadmap_project_not_found", "query": query}


def get_norms(query: str = "") -> dict:
    """Return the team norms / PM playbook. `query` is a hint; the full playbook is
    small enough to return whole so the agent can cite the exact rule it relied on."""
    text = (FIXTURES / "team-norms.md").read_text()
    query_lower = (query or "").lower()
    mandatory = {
        "what cortex may do (below the agent line)",
        "what cortex must never do (above the agent line)",
        "security",
        "tone",
    }
    topic_rules = {
        "status update rules": {"status", "update", "leadership", "metric", "date", "risk"},
        "backlog rules": {"backlog", "story", "stories", "sprint", "proposal", "propose"},
    }
    selected = []
    matched_topic = False
    for heading, section in _markdown_sections(text):
        heading_lower = heading.lower()
        is_topic_match = any(
            heading_lower == topic and any(term in query_lower for term in terms)
            for topic, terms in topic_rules.items()
        )
        if heading_lower in mandatory or is_topic_match:
            selected.append(section)
            matched_topic = matched_topic or is_topic_match
    if not matched_topic:
        selected.extend(
            section for heading, section in _markdown_sections(text)
            if heading.lower() in topic_rules
        )
    return {"query": query, "norms_sections": selected,
            "note": "mandatory safeguards plus rules relevant to the query."}


def _meaningful_tokens(text: str) -> set[str]:
    """Return stable content words for conservative completed-work matching."""
    ignored = {"add", "build", "close", "closes", "create", "finalize", "implement",
               "functionality", "review", "test", "testing", "the", "with"}
    return {token for token in re.findall(r"[a-z0-9]+", (text or "").lower())
            if len(token) > 2 and not token.isdigit() and token not in ignored}


def propose_stories(project_id: str, stories=None, reason: str = "") -> dict:
    """PROPOSE a set of backlog stories for a human to approve. This creates NOTHING
    in the tracker, it queues a request. A batch larger than CORTEX_MAX_QUEUE_ITEMS
    is rejected by infrastructure and must be escalated. This is the commitment bound,
    enforced outside the model (M5)."""
    if isinstance(stories, str):
        stories = [stories]
    if not isinstance(stories, list):
        return {"error": "invalid_stories", "stories": stories}
    project = _load_json("projects.json").get(str(project_id).strip())
    if project is None:
        return {"status": "rejected", "error": "project_not_found",
                "project_id": str(project_id).strip(),
                "action": "escalate to a human, do not queue ungrounded work"}
    completed = [item for item in project.get("activity", [])
                 if item.get("type") == "pr_merged"]
    completed_matches = []
    for story in stories:
        story_tokens = _meaningful_tokens(str(story))
        for item in completed:
            completed_tokens = _meaningful_tokens(item.get("title", ""))
            if completed_tokens and completed_tokens.issubset(story_tokens):
                completed_matches.append({"story": story, "merged_pr": item.get("id"),
                                          "completed_work": item.get("title")})
                break
    if completed_matches:
        return {"status": "rejected", "error": "completed_work_already_done",
                "matches": completed_matches,
                "action": "escalate to a human, do not queue duplicate completed work"}
    if len(stories) > MAX_QUEUE_ITEMS:
        return {"status": "rejected",
                "error": "batch_exceeds_queue_cap",
                "count": len(stories),
                "cap_items": MAX_QUEUE_ITEMS,
                "action": "escalate to a human, do not split the batch to dodge the cap"}
    return {"status": "queued_for_approval",
            "project_id": str(project_id).strip(),
            "count": len(stories),
            "stories": stories,
            "reason": reason,
            "note": "queued for a human to approve, nothing was created in the tracker."}


# Registry the agent loop reads. Add a tool here and the agent can call it.
# Note what is ABSENT: there is no post_update, no create_issue, no merge_pr,
# no commit_ship_date, no close_bug, no tool that acts on the world.
TOOLS = {
    "get_task": get_task,
    "get_project": get_project,
    "get_activity": get_activity,
    "search_past_updates": search_past_updates,
    "get_roadmap": get_roadmap,
    "get_norms": get_norms,
    "propose_stories": propose_stories,
}
