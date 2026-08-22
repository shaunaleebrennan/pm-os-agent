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

## 2. Topology

**Pattern:** _single+subagents · sequential · parallel+aggregate · hierarchical_

```
[ simple text diagram of the flow ]
e.g.  task → [Research] + [GitHub/Jira reader] → [Writer] → [Critic ✓] → human checkpoint → queued
```

## 3. Roster

| Agent / subagent | Responsibility | Runs which Loop Spec |
|---|---|---|
| _Chief-of-staff (Cortex)_ | _orchestrates + assembles the update_ | _M2 loop_ |
| _Research subagent_ | _pulls competitive / market context_ | _research loop_ |
| _GitHub/Jira reader_ | _summarizes recent activity_ | _read loop_ |
| _Critic / Validator_ | _checks the draft before it advances_ | _validation loop_ |
| _…_ | | |

## 4. Communication & hand-offs

_What passes between the parts? Any protocol (MCP / A2A, optional, note if used)._

## 5. The validator

- **What the critic checks:** _grounded claims · norms compliance · no confidential leak · nothing posted/committed_
- **Fail action:** _what happens when it fails (retry · revise · escalate to human)_

## 6. State: shared vs isolated

_What's shared across the fleet vs kept isolated per subagent (carry from M2)._

## 7. Cost & latency budget

_Coordination has a price. Rough token/latency cost of the fleet vs a single agent. (Forward-link to M5 bounds.)_
