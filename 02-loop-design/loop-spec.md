# Loop Spec: Cortex PM Chief-of-Staff Agent

> Module 2 · Loop Engineering, ★ Deliverable 2
>
> Your one-page blueprint for how the work you handed to the agent (M1) actually *runs*.
> An agent is just a prompt that fires itself, this spec says when it fires, what "done" means, and what it needs to do the job. Living document; refine as the course progresses.

## 1. Trigger & loop type

**Loop type:** Hook + Cron

Cortex needs to react when the PM needs support or when new material evidence arrives, but it should also run a regular sweep to catch anything that was missed — especially when a PM is OOO or something slips through because of human error.

**Why not heartbeat:** Cortex does not need to poll continuously; that would create unnecessary work and cost.

**Why not goal:** Each run has a bounded job rather than operating continuously toward an open-ended objective.

**Idempotency:** Cortex should deduplicate repeated triggers using a unique evidence/event ID where available, with source + timestamp + content hash as a fallback. Before processing, it should check state to confirm the evidence has not already been handled.

## 2. Goal / definition of done

**Goal:** For each valid PM request or evidence sweep, Cortex should retrieve the authorised project context, identify what matters, and prepare an evidence-grounded leadership update plus any relevant backlog story proposals for human review.

**Done:** A run is complete when Cortex has:

- used authorised sources and shown the evidence it relied on;
- drafted a concise status update with evidence-backed risks and status;
- queued no more than the permitted number of proposed stories, when relevant;
- passed independent validation; and
- stopped at the human-review checkpoint without posting, publishing, creating, merging, dating, or committing anything.

If Cortex cannot meet these conditions safely, the run is not done; it must stop and escalate to the PM with the reason.

## 3. Stop conditions

| Condition | What it looks like | What Cortex does |
|---|---|---|
| **Success** | The update is backed by trusted evidence, any proposed stories stay within the queue cap, and the independent check passes. | Stops and sends the work to the PM for review. Nothing is posted or committed. |
| **Cannot complete** | Important evidence is missing or conflicting, a tool rejects an action, or Cortex reaches a cost, iteration, or revision limit. | Stops, explains what it tried and what prevented it from finishing, and asks the PM for help. |
| **Needs a human decision** | The task involves confidential information, an unconfirmed date, an open Sev-1, a prompt-injection attempt, or a roadmap, pricing, investment, packaging, or GTM decision. | Stops and gives the PM the relevant evidence, any safe draft work, and a clear reason for escalating. |

## 4. State

Cortex keeps only the information that helps it avoid duplicate work and improve future drafts.

**Across runs, it keeps:**

- processed evidence or event IDs, using a content hash when no ID exists;
- approved summaries and their source links;
- the PM’s corrections and decisions; and
- whether work is awaiting review, approved, rejected, or needs follow-up.

**During a run, it tracks:** the evidence retrieved, tool results, draft status, and cost and iteration limits.

State stays within the relevant project. Confidential information must not carry into another project or audience. Cortex retrieves current facts again rather than treating saved information as up to date.

## 5. The five things every loop needs

| Component | For Cortex |
|---|---|
| **Work tree** | Each run works in its own isolated space using authorised, read-only project information. It cannot change the source project or publish work. |
| **Skills** | Retrieve evidence, decide what is relevant, draft a leadership update, flag risks, and prepare backlog story proposals. |
| **Plugins / connectors** | Read-only access to project status, activity, roadmap, past updates, and team norms, plus a capped queue for story proposals. There is no publishing or backlog-creation access. |
| **Subagents** | An independent validator checks the draft before the PM sees it. The full setup will be defined in M3. |
| **State tracking** | Track processed evidence, source links, review status, PM corrections, and run limits without sharing confidential information across projects. |

## 6. Context plan

_What context is written / selected / compressed / isolated each iteration? (Full depth in M4.)_

## 7. Hand-off to bounds & evals

_Placeholder → M5 `bounds-and-evals.md`: max iterations, timeout, budget, queue cap, kill switch._

## Link to live loop

[`../00-build/agent.py`](../00-build/agent.py)
