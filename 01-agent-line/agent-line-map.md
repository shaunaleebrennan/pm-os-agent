# Agent Line Map: Cortex PM Chief-of-Staff

> Module 1 · The Agent Line

## Agent purpose

Cortex takes a PM task brief, pulls authorised project context and recent activity, and prepares a grounded leadership status update plus a capped batch of proposed backlog stories. It stops at a human-in-the-loop checkpoint: nothing is posted, created, merged, dated, or committed without a human.

## The agentic slice

Cortex uses judgment to decide which retrieved context is relevant, how to synthesise it into an accurate update, whether the evidence supports a risk status, and when uncertainty or policy requires escalation. Retrieval, permission checks, provenance, queue-cap enforcement, and the final review handoff are deterministic tools or workflow steps. The agent may prepare and propose work; the human owns approval and action.

## The workflow, decision by decision

The course's Cortex working set is kept intact. Each of its eight atomic decisions is scored on **reversibility**, **blast radius**, and **measurability**. **Below** means Cortex may perform the work within its enforced bounds; **Above** means a human owns it.

| Decision / action | Reversibility (H/M/L) | Blast radius (H/M/L) | Measurability (H/M/L) | Above / Below | HITL? |
|---|---|---|---|---|---|
| Pull the task's project state, recent activity, roadmap context, past updates, and team norms through authorised read-only tools | H | L | H | Below | No; deterministic read-only step |
| Decide which retrieved context is relevant to the requested leadership update and exclude unrelated or confidential material | H | M | M | Below | Targeted review for ambiguity or confidentiality |
| Draft a concise leadership status update whose claims, metrics, and dates are traceable to the retrieved evidence | H | M | H | Below | Required approval before use or publication |
| Choose tone and commitment-safe language using past updates and team norms, without implying an unconfirmed date or launch decision | H | M | M | Below | Required approval before use or publication |
| Flag evidence-backed risks and blockers and assign green, yellow, or red only when the sources support it | H | M | M | Below | Required review of risk status |
| Decide whether to stop and escalate because evidence is missing or conflicting, a Sev-1 or unconfirmed date is involved, the request is outside norms, or content is confidential | H | M | H | Below | Escalation is the HITL outcome |
| Propose and queue only the capped batch of backlog stories justified by the brief and PRD, clearly labelled for human review | H | M | H | Below | Required approval; proposal creates nothing |
| Approve or post the update, create or merge backlog work, commit a ship date, or mark a launch gate | L | H | H | Above | Human owned; Cortex has no execution tools |

## One-sentence justifications

- **Pull project context:** Below the line because authorised read-only retrieval is easy to reverse, has low blast radius, and can be checked exactly against the source records.
- **Decide relevant context:** Below the line with targeted review because selections can be corrected, but omitting a key fact or including confidential material could distort the update and relevance is only partly measurable.
- **Draft the update:** Below the line with required approval because a draft is reversible and its factual grounding is highly testable, but leadership-facing language can still influence decisions.
- **Choose tone and commitment-safe language:** Below the line with required approval because wording can be revised, but implied promises can carry a medium blast radius and tone is only moderately measurable.
- **Flag risks and blockers:** Below the line with required review because the classification is reversible and evidence can be inspected, but an incorrect status could misdirect attention or conceal risk.
- **Decide when to escalate:** Below the line because stopping is highly reversible and measurable against explicit conditions, while escalation prevents uncertain or prohibited work from gaining blast radius.
- **Propose a capped story batch:** Below the line with required approval because the queue is reversible, the tool-enforced cap is measurable, and the proposal creates no backlog items or commitments.
- **Approve, publish, or commit:** Above the line because externalised decisions and commitments have high blast radius, are difficult to reverse once acted upon, and require accountable human authority.

## Agent anatomy (Module 1 view)

- **Model:** Decide relevant context, synthesise the evidence, draft the update, flag supported risks, and recognise when to escalate.
- **Tools:** Read-only project, activity, roadmap, past-update, and team-norm tools · a bounded `propose_stories` queue that creates nothing · no post, send, create, close, merge, commit-date, or launch-gate tools.
- **Memory/context:** Use retrieved past updates and decisions for tone and precedent while grounding every current-state claim in fresh project evidence.
- **HITL:** End with either `DONE`—the update and any story proposals queued for review—or `ESCALATE`; in both cases a human takes over before any consequential action.
- **Loop:** Defined in M2 `loop-spec.md`.
- **Bounds and evals:** Defined and demonstrated in M5 `bounds-and-evals.md`.

## Hardest call

**Whether Cortex should propose backlog stories as well as draft the update.** A proposal makes the agent useful across the full supplied workflow, but backlog changes can create hidden commitments. The deciding factor is blast radius: Cortex may queue a small, tool-capped proposal backed by the PRD, but it cannot create, prioritise, size, or approve the stories, and a human must review the batch.
