# Agent Line Map: Cortex PM Chief-of-Staff

> Module 1 · The Agent Line

## Agent purpose

Cortex takes a PM task brief, pulls authorised project context and recent activity, and prepares a grounded leadership status update plus a capped batch of proposed backlog stories. It stops at a human-in-the-loop checkpoint: nothing is posted, created, merged, dated, or committed without a human.

## The agentic slice

Retrieving project information is a deterministic, read-only tool step. Cortex's agentic slice is deciding which context is relevant, drafting the update, proposing commitment-safe language, interpreting risk, deciding when to escalate, and preparing a capped story proposal. A human validates the judgment calls and owns approval and publication.

## The workflow, decision by decision

| Decision / action | Reversibility (H/M/L) | Blast radius (H/M/L) | Measurability (H/M/L) | Above / Below | HITL? |
|---|---|---|---|---|---|
| Pull project state and recent activity through authorised read-only tools | H | L | H | Below | No |
| Decide which retrieved context is relevant to the leadership update | H | M | M | Below | Yes; human validates the selected context in the draft |
| Draft the evidence-grounded leadership update | H | L | H | Below | Yes; human reviews the completed update before publication |
| Decide tone and commitment-safe language | H | M | L | Below | Yes; human approves tone and implied commitments |
| Flag evidence-backed risks and propose green, yellow, or red status | H | M | M | Below | Yes; human validates the status and supporting evidence |
| Choose when to stop and escalate under the explicit safety rules | H | M | H | Below | Escalation is the HITL handoff |
| Propose and queue a capped story batch grounded in the PRD | H | M | M | Below | Yes; PM approves, changes, or rejects the proposal |
| Approve and publish the leadership update | L | H | H | Above | Human owned; Cortex has no publishing tool |

## The golden rule, applied

- **Pull project state and activity** sits below the line because it is highly reversible, has a low blast radius, and is highly measurable; deciding factor: all three axes are green.
- **Deciding which context is relevant** sits below the line with HITL because it is highly reversible, has a medium blast radius, and is only moderately measurable; deciding factor: measurability, because relevance requires human judgment.
- **Drafting the leadership update** sits below the line because it is highly reversible, has a low blast radius while private, and is highly measurable against the source evidence; deciding factor: all three axes are green, with HITL applied before the completed update is published.
- **Deciding tone and commitment level** sits below the line with HITL because wording is highly reversible, has a medium blast radius, and is difficult to measure objectively; deciding factor: low measurability, because appropriate tone and implied commitment require human judgment.
- **Flagging risks and assigning status** sits below the line with HITL because the proposed status is highly reversible, has a medium blast radius, and is only moderately measurable; deciding factor: measurability, because interpreting what the evidence means is not fully objective.
- **Choosing when to escalate** sits below the line because stopping is highly reversible, a missed trigger has a medium blast radius, and the explicit escalation rules are highly measurable; deciding factor: measurability, with escalation itself acting as the HITL handoff.
- **Proposing a capped story batch** sits below the line with HITL because the proposal is highly reversible, has a medium blast radius on sprint planning, and is only moderately measurable; deciding factor: measurability, because prioritisation requires PM judgment.
- **Approving and publishing the update** sits above the line because it has low reversibility, a high blast radius, and high measurability only after the impact; deciding factor: blast radius, because an incorrect or confidential update could affect leadership decisions and trust.

## Agent anatomy (sketch)

- **Model:** Use a fast model by default for routine relevance assessment, grounded drafting, and straightforward story proposals. Escalate to a frontier model only when evidence conflicts, context is ambiguous, or the decision involves sensitive commitment or prioritisation judgment. Deterministic retrieval remains a tool step.
- **Tools:** Use read-only project, activity, roadmap, past-update, and team-norm tools plus a capped proposal queue. The queue creates only a draft for human review, not backlog items or commitments. Cortex has no post, send, create, close, merge, commit-date, or launch-gate tools.
- **Memory:** Retain approved summaries, source provenance, and human corrections so Cortex can use useful context and past decisions, while always retrieving current project facts fresh.
- **HITL:** Use the checkpoints defined in this Agent Line Map. Cortex prepares and proposes; a human validates judgment calls and owns publication.
- **Loop:** Placeholder; defined in M2 `loop-spec.md`.
- **Bounds:** Placeholder; defined in M5 `bounds-and-evals.md`.
- **Evals:** Placeholder; defined in M5 `bounds-and-evals.md`.

## Hardest call

**My hardest call was deciding which context is relevant.** I initially questioned whether this should remain human-owned because selecting the wrong evidence—or missing something important—could distort the whole update. But if a human has to select all the context, Cortex loses the core judgment task that makes it useful as an agent. **Measurability settled it:** relevance does not always have one objectively correct answer, so Cortex should make the initial selection and explain its reasoning, with a human validating it at the HITL checkpoint.
