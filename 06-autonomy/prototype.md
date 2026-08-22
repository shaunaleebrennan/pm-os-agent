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
| 2 | ![M3 critic-rejection run](screenshots/m3-critic-rejection.png) | critic rejects an invented metric, unsupported status, false publication claim, and unevidenced queue claim | M3 |
| 3 | ![M4 grounded run](screenshots/m4-grounded.png) | grounded update citing scoped activity; duplicate completed work is caught before the corrected proposal reaches HITL | M4 |
| 4 | ![M4 missing-source run](screenshots/m4-missing-source.png) | required project evidence is unavailable, so Cortex refuses to invent a status or GA date and escalates | M4 |
| 5 | _[img]_ | jailbreak refused + escalated | M5 |
| 6 | _[img]_ | an iteration/cost/queue bound halting a runaway | M5 |
| 7 | _[img]_ | end-to-end run | M6 |

## How to run it

_Minimal steps for someone to reproduce the demo (env vars, and the command or the coding-agent prompt you used)._
