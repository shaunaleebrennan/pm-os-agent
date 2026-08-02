# Bounds & Evals: Cortex PM Chief-of-Staff Agent

> Module 5 · Bounds, Trust & Evals
>
> Real access = real blast radius. This is where you design for "when it goes sideways," and where you spec the agent by writing its evals.

## 1. Bounds table

| Bound | Value / policy | Which Cortex risk it caps |
|---|---|---|
| **Max iterations** | _e.g. 8_ | _runaway reasoning loop_ |
| **Timeout** | _e.g. 90s/run_ | _hung tool call_ |
| **Token / cost budget** | _e.g. $X per run_ | _cost blow-up_ |
| **Auto-queue / commitment cap** | _e.g. max 10 stories per run_ | _flooding the backlog / over-committing scope_ |
| **Permissions (JIT / ephemeral)** | _read-only access; no standing post/merge rights_ | _confidential leak / unapproved post ("control starts at infrastructure")_ |
| **Kill switch** | _who/what halts it_ | _everything_ |
| **HITL checkpoints** | _above-the-line decisions from agent-line-map_ | _irreversible actions (post / commit date / merge)_ |

## 2. Failure-mode register

| Failure mode | How detected | PM lever |
|---|---|---|
| _Tool misuse_ | _…_ | _…_ |
| _Reasoning loop_ | _iteration count_ | _max-iterations bound_ |
| _Memory drift / poisoning_ | _…_ | _…_ |
| _Confidential leak / permission escalation_ | _…_ | _JIT permissions + confidential guard_ |
| _Coordination conflict_ | _…_ | _…_ |
| _Overconfidence (invented metric / date)_ | _…_ | _critic subagent / HITL_ |

## 3. Trajectory eval suite

Grade the *path*, not just the final answer.

| Dimension | What it checks | Pass threshold | Owner |
|---|---|---|---|
| **Tool-call accuracy** | _right tool, right args_ | _…_ | _…_ |
| **Path / trajectory quality** | _no redundant or unsafe steps_ | _…_ | _…_ |
| **Recovery** | _recovers from a failed step_ | _…_ | _…_ |
| **Task completion** | _outcome actually achieved (grounded update, no leak)_ | _…_ | _…_ |

## 4. Eval lifecycle

- **Offline (fixtures):** _…_
- **CI gate (every change):** _…_
- **Production traces (online):** _…_

> For judge calibration, family separation, and per-turn classifiers, see the sister certification **AI Evals**.

## 5. Replay set

_Which recorded runs become deterministic fixtures you replay on every change?_

## Runaway-loop check

_Describe one runaway scenario and the exact bound that stops it._
