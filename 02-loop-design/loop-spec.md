# Loop Spec: Cortex PM Chief-of-Staff Agent

> Module 2 · Loop Engineering, ★ Deliverable 2
>
> Your one-page blueprint for how the work you handed to the agent (M1) actually *runs*.
> An agent is just a prompt that fires itself, this spec says when it fires, what "done" means, and what it needs to do the job. Living document; refine as the course progresses.

## 1. Trigger & loop type

**Chosen type:** _heartbeat · cron · hook · goal_

_Why this type? (e.g. a Monday-morning cron that assembles the weekly update, plus a hook on a new PRD to propose stories.)_

## 2. Goal / definition of done

_What outcome is this loop responsible for? For a goal loop, what validation says "done"? (e.g. a status update grounded in real activity, queued for review, nothing posted.)_

## 3. Stop conditions

| Condition | What it looks like | What happens |
|---|---|---|
| **Success** | _…_ | _…_ |
| **Stuck / give up** | _…_ | _escalate / log / halt_ |
| **Escalate to human** | _…_ | _HITL checkpoint (from agent-line-map)_ |

## 4. State

_What persists across iterations, and what's the scope? (e.g. per-project context and last week's update; no cross-project confidential leakage.)_

## 5. The five things every loop needs

| Component | For Cortex |
|---|---|
| **Work tree** (isolated workspace per run) | _…_ |
| **Skills** (reusable capabilities) | _…_ |
| **Plugins / connectors** (tools & access) | _…_ |
| **Subagents** (delegated / validation) | _placeholder → M3 orchestration-map.md_ |
| **State tracking** | _…_ |

## 6. Context plan

_What context is written / selected / compressed / isolated each iteration? (Full depth in M4.)_

## 7. Hand-off to bounds & evals

_Placeholder → M5 `bounds-and-evals.md`: max iterations, timeout, budget, queue cap, kill switch._

## Link to live loop

_[path to your agent in `00-build/`]_
