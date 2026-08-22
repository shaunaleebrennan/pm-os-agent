# Orchestration Map: Cortex PM Chief-of-Staff Agent

> Module 3 · Orchestration & Subagents, ★ Deliverable 3
>
> Builds on your M2 Loop Spec. Only split one agent into a team when there's a real reason, coordination has a cost.

## 1. Why split? (or why not)

**Decision: Split once — Cortex + one independent validator.**

| Reason | Applies? | Why / why not |
|---|---|---|
| Separation of concerns | No | The evidence and recommendation work is clear enough to stay together; quality control can be justified separately under the validator reason. |
| Parallelism | No | The work is better handled in one reasoning flow. The value is in the quality of the analysis, not trying to save time in retrieval. |
| Independent validator | Yes | Cortex is making recommendations that could significantly change what a PM chooses to focus on, so independent validation is crucial to ensure the recommendations are sound. |
| Context-window pressure | No | Cortex can keep the main analysis coherent using retrieval, selection and bounded context. Context management should be solved through product and engineering design, not by adding another agent. |

**Why this boundary:** There is no need to split further because additional agents would not add meaningful value.

The validator receives a bounded hand-off rather than Cortex's drafting conversation,
so it can check the draft without inheriting the same conversational context or being
asked to defend its own work.

## 2. Topology

**Pattern:** sequential Class 3 critic pattern

```
task → Cortex retrieves evidence → Cortex drafts / queues proposals
     → isolated Validator
          ├─ pass → human review checkpoint
          └─ fail → Cortex revises once → isolated Validator
                                          ├─ pass → human review checkpoint
                                          └─ fail → stop and escalate to human
```

Nothing is published, committed, created in the tracker, or approved automatically.

## 3. Roster

| Agent / subagent | Responsibility | Runs which Loop Spec |
|---|---|---|
| Cortex | Retrieves project evidence, drafts the update, and uses `propose_stories` to queue proposals for approval | M2 bounded agent loop |
| Validator | Independently checks the proposed output against evidence and rules; returns only pass/fail plus reasons | M3 validation loop |
| Human PM | Reviews the safe draft and queued proposals; owns approval and all consequential decisions | Human checkpoint |

## 4. Communication & hand-offs

Cortex sends the Validator one structured four-field payload:

1. `task_goal` — the original PM task.
2. `source_evidence` — labelled tool arguments and results used during the run.
3. `agent_line_rules` — permitted outcome, prohibited actions, and enforced bounds.
4. `proposed_output` — the draft being reviewed.

The Validator returns strict structured JSON:

```json
{"verdict": "pass" | "fail", "reasons": ["specific evidence-backed reason"]}
```

A malformed verdict fails safely. No MCP or A2A protocol is needed; both model calls
are coordinated explicitly in `agent.py`.

## 5. The validator

- **Evidence grounding:** project, activity, claims, dates, metrics, and status match
  the supplied evidence.
- **Fact vs inference:** interpretation and recommendations are not presented as
  established facts.
- **Agent Line:** nothing is posted, committed, created, merged, approved, or leaked.
- **Recommendation quality:** recommendations are specific, useful, supported, and
  do not duplicate completed work.
- **Queue evidence:** any claim that stories were queued must match a successful
  `propose_stories` result in the hand-off.
- **Fail action:** return specific reasons to Cortex for one revision. A second
  failure stops the loop and escalates to the human PM.

## 6. State: shared vs isolated

**Shared deliberately:** the task goal, selected source evidence, Agent Line rules,
the current proposal, and (after failure) the Validator's reasons.

**Kept isolated:** Cortex's system prompt, drafting conversation, intermediate
reasoning, and full message history. Each Validator call is a fresh model call.

Within a run, Cortex retains tool results and replaces an earlier `propose_stories`
result only when a revised proposal is actually queued.

## 7. Cost & latency budget

- Cortex defaults to `gpt-4o-mini`; the Validator defaults to `gpt-4o` because the
  cheaper model produced unreliable rule interpretation in testing.
- Maximum revisions: **1**, enforced in code even if the environment requests more.
- Maximum Validator calls: **2** (initial draft plus one revision).
- Whole-run cost cap: **$0.50**; queue cap: **10 stories**.
- The successful happy-path test reached the human checkpoint with one Validator
  call and reported an internal estimate of approximately **$0.0019**.

The reported cost is directional, not a verified mixed-model cost: the current
calculator applies one configured input/output price pair to both Cortex and the
Validator. Per-model accounting should be added in M5 before using it as a financial
control or reporting actual spend.
