"""Cortex, a minimal, explicit agent loop you (and your coding agent) can read end
to end. This is the agent you ship: your PM chief-of-staff. You build it by
directing your coding agent (Claude Code / Cursor / Codex) to shape this file. You
never have to hand-write it.

Every bound the course talks about is visible right here in code, not buried in a
framework: the max-iteration counter, the cost cap, the revision cap, the
stop/escalate conditions, the auto-queue cap, and the absence of any publish tool.

Usage (ask your coding agent to run these for you, or run them yourself):
    python agent.py                # runs the happy-path task (weekly status update)
    python agent.py missing-data   # the stuck/escalate case
    python agent.py jailbreak       # the prompt-injection refusal case

Requires OPENAI_API_KEY in your environment (see .env.example). Model and bounds
are read from env so you can tune them, that tuning is your M5 deliverable.

The loop is deliberately transparent (hand-written tool-calling on the openai
client) so a grader can see the machinery. Keep the bounds explicit if you rework it.
"""

from __future__ import annotations

import json
import os
import sys

from openai import OpenAI

import tools
from critic import review
from prompts import CORTEX_SYSTEM

try:  # load .env if python-dotenv is installed; harmless if it isn't
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# --- Bounds (your M5 deliverable: tune these and justify them) ----------------
MODEL = os.environ.get("CORTEX_MODEL", "gpt-4o-mini")
CRITIC_MODEL = os.environ.get("CORTEX_CRITIC_MODEL", "gpt-4o")
MAX_ITERATIONS = int(os.environ.get("CORTEX_MAX_ITERATIONS", "8"))
MAX_REVISIONS = min(max(int(os.environ.get("CORTEX_MAX_REVISIONS", "1")), 0), 1)
COST_CAP_USD = float(os.environ.get("CORTEX_COST_CAP_USD", "0.50"))
MAX_QUEUE_ITEMS = int(os.environ.get("CORTEX_MAX_QUEUE_ITEMS", "10"))
# Rough $ per 1M tokens for your chosen model, set to match its pricing.
PRICE_IN = float(os.environ.get("CORTEX_PRICE_IN_PER_M", "0.15"))
PRICE_OUT = float(os.environ.get("CORTEX_PRICE_OUT_PER_M", "0.60"))

TOOL_SCHEMAS = [
    {"type": "function", "function": {
        "name": "get_project", "description": "Look up a project by its ID (status, flags, linked PRD).",
        "parameters": {"type": "object", "properties": {
            "project_id": {"type": "string"}}, "required": ["project_id"]}}},
    {"type": "function", "function": {
        "name": "get_activity",
        "description": "Pull recent engineering activity for a project (merged PRs, open issues, Sev-1s).",
        "parameters": {"type": "object", "properties": {
            "project_id": {"type": "string"}}, "required": ["project_id"]}}},
    {"type": "function", "function": {
        "name": "search_past_updates",
        "description": "Search previous status updates and decisions for tone and precedent.",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string"}}, "required": []}}},
    {"type": "function", "function": {
        "name": "get_roadmap",
        "description": "Return the roadmap. Some items are flagged confidential/embargoed.",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string"}}, "required": []}}},
    {"type": "function", "function": {
        "name": "get_norms", "description": "Retrieve current team-norm sections. Query every task topic, e.g. 'status update backlog stories'.",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string"}}, "required": []}}},
    {"type": "function", "function": {
        "name": "propose_stories",
        "description": "Queue backlog stories for human approval (creates nothing; rejects oversized batches and work matching merged PRs).",
        "parameters": {"type": "object", "properties": {
            "project_id": {"type": "string"},
            "stories": {"type": "array", "items": {"type": "string"}},
            "reason": {"type": "string"}}, "required": ["project_id", "stories"]}}},
]


class Bounds:
    """Tracks spend and trips the cost cap. This is enforced OUTSIDE the model."""

    def __init__(self):
        self.cost = 0.0

    def add(self, usage) -> None:
        self.cost += (usage.prompt_tokens * PRICE_IN
                      + usage.completion_tokens * PRICE_OUT) / 1_000_000

    def over_cap(self) -> bool:
        return self.cost >= COST_CAP_USD


def banner(text: str) -> None:
    print(f"\n{'=' * 64}\n{text}\n{'=' * 64}")


def run(which: str = "happy") -> None:
    client = OpenAI()
    bounds = Bounds()
    task = tools.get_task(which)
    if "error" in task:
        print(task)
        return

    project_scope = tools.project_id_from_task(task["body"])
    banner(f"CORTEX RUN, fixture: task-{which}  (auto-queue cap {MAX_QUEUE_ITEMS} items)")
    print(task["body"])

    messages = [
        {"role": "system", "content": CORTEX_SYSTEM},
        {"role": "user", "content": f"PM task brief:\n\n{task['body']}"},
    ]
    evidence_log: list[dict] = []
    latest_proposal_source = None
    revisions = 0
    requires_story_proposal = ("propose" in task["body"].lower()
                               and "stories" in task["body"].lower())

    for step in range(1, MAX_ITERATIONS + 1):
        if bounds.over_cap():
            banner(f"BOUND TRIPPED, cost cap ${COST_CAP_USD} hit at "
                   f"${bounds.cost:.4f}. Halting and escalating to a human.")
            return

        resp = client.chat.completions.create(
            model=MODEL, messages=messages, tools=TOOL_SCHEMAS)
        bounds.add(resp.usage)
        msg = resp.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for call in msg.tool_calls:
                fn = call.function.name
                args = json.loads(call.function.arguments or "{}")
                scoped_args, scope_error = tools.enforce_project_scope(fn, args, project_scope)
                result = scope_error or tools.TOOLS[fn](**scoped_args)
                source_entry = {"tool": fn, "arguments": scoped_args, "result": result}
                if fn == "propose_stories" and latest_proposal_source is not None:
                    # A revised draft replaces the earlier mock queue proposal. Keep
                    # only the current version in the evidence sent to the critic.
                    evidence_log[latest_proposal_source] = source_entry
                else:
                    evidence_log.append(source_entry)
                    if fn == "propose_stories":
                        latest_proposal_source = len(evidence_log) - 1
                print(f"\n[step {step}] TOOL {fn}({args})")
                print(f"          -> {json.dumps(result)[:300]}")
                messages.append({"role": "tool", "tool_call_id": call.id,
                                 "content": json.dumps(result)})
                if (fn == "get_project"
                        and result.get("error") == "project_not_found"):
                    banner("MISSING REQUIRED SOURCE, escalating to a human. "
                           "No project evidence was found, no substitute project "
                           "was used, and no GA date or status update was invented.")
                    return
            continue

        # No tool calls => Cortex produced a proposed output. Validate it.
        proposed = msg.content or ""
        print(f"\n[step {step}] PROPOSED OUTPUT:\n{proposed}")

        proposal_succeeded = any(
            entry.get("tool") == "propose_stories"
            and entry.get("result", {}).get("status") == "queued_for_approval"
            for entry in evidence_log
        )
        if requires_story_proposal and not proposal_succeeded:
            banner("INFRASTRUCTURE GUARD, required story proposal was not queued."
                   " Blocking unsupported completion claim.")
            if revisions >= MAX_REVISIONS:
                banner(f"REVISION CAP hit ({MAX_REVISIONS}). Escalating to a human "
                       f"instead of accepting an incomplete handoff. "
                       f"Run cost ≈ ${bounds.cost:.4f}")
                return
            revisions += 1
            messages.append(msg)
            messages.append({"role": "user", "content":
                             "Infrastructure rejected that completion claim: this task "
                             "requires proposed stories to be queued through "
                             "propose_stories before you say they are queued or done. "
                             "Use the tool with evidence-grounded stories, or escalate."})
            continue

        banner("CRITIC, independent validation")
        validator_handoff = {
            "task_goal": task["body"],
            "source_evidence": evidence_log,
            "agent_line_rules": {
                "allowed_outcome": "prepare work and queue it for human review",
                "prohibited_actions": [
                    "post, publish, or send",
                    "create, close, or merge a ticket or PR",
                    "commit a ship date or mark a launch gate",
                    "make roadmap, pricing, investment, packaging, or GTM decisions",
                    "share confidential or embargoed material",
                ],
                "max_revisions": MAX_REVISIONS,
                "max_validator_calls": MAX_REVISIONS + 1,
                "max_queue_items": MAX_QUEUE_ITEMS,
            },
            "proposed_output": proposed,
        }
        verdict = review(client, CRITIC_MODEL, validator_handoff)
        # Estimate critic spend too.
        bounds.cost += (verdict["_usage"]["prompt"] * PRICE_IN
                        + verdict["_usage"]["completion"] * PRICE_OUT) / 1_000_000
        print(json.dumps({k: v for k, v in verdict.items() if k != "_usage"}, indent=2))

        if verdict["verdict"] == "pass":
            banner(f"HITL CHECKPOINT, status update + any proposed stories queued for "
                   f"your review. Nothing posted, no commitments made. "
                   f"Run cost ≈ ${bounds.cost:.4f}")
            return

        if revisions >= MAX_REVISIONS:
            banner(f"REVISION CAP hit ({MAX_REVISIONS}). Escalating to a human "
                   f"instead of looping. Run cost ≈ ${bounds.cost:.4f}")
            return

        revisions += 1
        print(f"\n-> critic rejected; revision {revisions}/{MAX_REVISIONS}")
        messages.append(msg)
        messages.append({"role": "user", "content":
                         "A validator rejected that for these reasons: "
                         f"{verdict['reasons']}. Fix it or escalate."})

    banner(f"MAX ITERATIONS ({MAX_ITERATIONS}) reached without finishing. "
           f"Escalating. Run cost ≈ ${bounds.cost:.4f}")


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "happy")
