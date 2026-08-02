# Cortex: PM Chief-of-Staff Agent

> My final project for Product School's **Run Your AI Agent Team** certification. A chief-of-staff agent that turns raw inputs (project state, GitHub/Jira activity, roadmap, past updates) into finished PM work, a leadership status update and a proposed backlog for a human to clear, built loop-first, bounded, grown into a fleet, and shipped up the Trust Ladder.

This is a **template repo**. Click **Use this template → Create a new repository**, name it `pm-os-agent` (or your own agent's name), and fill in one folder per module as you go.

---

## Deliverables at a glance

| # | Deliverable | Module | Status | File |
|---|---|---|---|---|
| 1 | **Working agent demo** (real run screenshots; link optional) | Built across labs | ☐ | `06-autonomy/prototype.md` |
| 2 | **Loop Spec** | M2 | ☐ | `02-loop-design/loop-spec.md` |
| 3 | **Orchestration Map** | M3 | ☐ | `03-orchestration/orchestration-map.md` |
| 4 | **Insights: build process** | M6 | ☐ | `06-autonomy/build-insights.md` |
| 5 | **Insights: bounds, trust & autonomy strategy** | M6 | ☐ | `06-autonomy/governance-and-strategy.md` |

## The agent in one sentence

_What does your agent do, for whom, and where is the agent line, what does it decide vs. what stays human?_

## Build & demo

- **How you built it:** _which coding agent (Claude Code / Cursor / Codex) you directed, start in `00-build/`_
- **Demo link:** _[optional shareable URL]_
- **Run screenshots:** _required, collected M2 to M6 in `06-autonomy/prototype.md`_

## Where it sits on the Trust Ladder

_shadow · assisted · supervised · bounded-autonomous · autonomous, which rung today, and what eval evidence would let it climb the next one?_

---

## How to submit

- Turn the five deliverable files into your final deck (use the **Final Project Deliverables Builder** that ships with the course, it generates `pitch.html` + a clean `README.md` for you, or a tool like Gamma).
- Submit your own copy to the LMS within 7 days of your cohort ending.

## Repo structure

```
pm-os-agent/
├── README.md                          ← this dashboard
├── 00-build/                          ← runnable starter: the transparent Cortex agent,
│   │                                    fixtures, RUNBOOK, PROMPTS, CORTEX-ANATOMY
│   ├── RUNBOOK.md                     ← open in your coding agent, add a key, run a fixture, screenshot
│   ├── PROMPTS.md                     ← the prompt pack: what to say to your coding agent
│   ├── CORTEX-ANATOMY.md              ← the 7 things every submission must show
│   ├── agent.py · critic.py · tools.py · prompts.py
│   └── fixtures/                      ← mock PM tasks + project/roadmap/updates/norms data
├── 01-agent-line/
│   └── agent-line-map.md              ← M1: what to hand to the agent (above vs below the line)
├── 02-loop-design/
│   └── loop-spec.md                   ← M2: the Loop Spec                 ★ Deliverable 2
├── 03-orchestration/
│   └── orchestration-map.md           ← M3: your fleet + the validator     ★ Deliverable 3
├── 04-memory-context/
│   └── memory-and-context.md          ← M4: retrieve-vs-long-context + your PM brain
├── 05-bounds-evals/
│   └── bounds-and-evals.md            ← M5: hard bounds + trajectory evals
└── 06-autonomy/
    ├── prototype.md                   ← demo + screenshots                ★ Deliverable 1
    ├── build-insights.md              ← friction · learning · aha         ★ Deliverable 4
    └── governance-and-strategy.md     ← Trust Ladder + autonomy strategy  ★ Deliverable 5
```
