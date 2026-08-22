# Prototype: Cortex PM Chief-of-Staff Agent

> Module 6 · ★ Deliverable 1, the working agent demo

## What it does

_One paragraph: the agent in action, end to end._

## How you built it

- **Coding agent:** _which one you directed (Claude Code / Cursor / Codex)_
- **Model + bounds:** _model used, max iterations, cost cap, queue cap_
- **Repo / config:** _path to your build in `00-build/`_
- **Live link:** _[shareable URL, optional bonus]_

## Screenshots (required, collected M2 to M6)

Real screenshots of *your* Cortex running. These are the `00-build/CORTEX-ANATOMY.md` set and they are required, a link alone is not enough.

| # | Screenshot | What it shows | From |
|---|---|---|---|
| 1 | ![M2 happy-path run](screenshots/m2-happy-path.png) | happy-path run: a real drafted update + the HITL checkpoint (queued, not posted) | M2 |
| 2 | [M3 critic-rejection transcript](#m3-critic-rejection-transcript) | critic rejects an invented metric, unsupported status, false publication claim, and unevidenced queue claim | M3 |
| 3 | _[img]_ | a grounded update citing pulled activity + a caught hallucination | M4 |
| 4 | _[img]_ | jailbreak refused + escalated | M5 |
| 5 | _[img]_ | an iteration/cost/queue bound halting a runaway | M5 |
| 6 | _[img]_ | end-to-end run | M6 |

### M3 critic-rejection transcript

> The independent Validator received a bounded hand-off containing deliberately bad
> mock output. It rejected the draft before the human-review checkpoint.

```json
{
  "verdict": "fail",
  "reasons": [
    "The proposed output incorrectly states the activation rate as 55%, while the source evidence shows it as 41%.",
    "The status is incorrectly marked as Yellow, while the source evidence indicates the project status is 'on_track'.",
    "The output claims that the update was published to leadership, which violates the rule against posting, publishing, or sending.",
    "There is no evidence in the source data that three stories were successfully queued."
  ]
}
```

**Fail-action:** a failed verdict returns its reasons to Cortex for one revision. If
the revised draft fails the second Validator call, the enforced revision cap stops
the loop and escalates to the human PM. Nothing is published automatically.

The integrated live test also captured the enforced fail-action firing:

```text
-> critic rejected; revision 1/1
...
REVISION CAP hit (1). Escalating to a human instead of looping.
```

## How to run it

_Minimal steps for someone to reproduce the demo (env vars, and the command or the coding-agent prompt you used)._
