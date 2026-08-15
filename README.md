# Cortex: PM Chief-of-Staff Agent

> My final project for Product School's **Run Your AI Agent Team** certification. Cortex turns a PM task brief and verified project context into a grounded leadership status update and a capped batch of proposed backlog stories, then stops at a human-in-the-loop checkpoint before anything is posted or committed.

This repository follows the supplied Cortex course scaffold. The project keeps the course's PM chief-of-staff workflow and develops it module by module: draw the agent line, shape the loop, add orchestration and an independent critic, design memory and context, enforce bounds and evals, and demonstrate the result through real runs.

The required Cortex anatomy remains visible throughout: a loop with a definition of done, read-only tools, an independent critic, iteration and cost/commitment bounds, an explicit human-in-the-loop (HITL) checkpoint, and jailbreak refusal. The runnable starter in `00-build/` is the implementation that these module decisions progressively refine.

---

## Deliverables at a glance

| # | Deliverable | Module | Status | File |
|---|---|---|---|---|
| 1 | **Working agent demo** (real run screenshots; link optional) | Built across labs | ☐ | `06-autonomy/prototype.md` |
| 2 | **Loop Spec** | M2 | ☑ | `02-loop-design/loop-spec.md` |
| 3 | **Orchestration Map** | M3 | ☐ | `03-orchestration/orchestration-map.md` |
| 4 | **Insights: build process** | M6 | ☐ | `06-autonomy/build-insights.md` |
| 5 | **Insights: bounds, trust & autonomy strategy** | M6 | ☐ | `06-autonomy/governance-and-strategy.md` |

## The agent in one sentence

Cortex helps a human PM prepare an evidence-grounded leadership update and a capped set of proposed backlog stories by deciding which authorised project context matters, drafting from that evidence, flagging risks, and escalating when required; the human approves all publication, commitments, dates, launch gates, and backlog changes.

## Agent line and blast radius

- **Below the line:** read the brief; retrieve authorised project, activity, roadmap, past-update, and team-norm data; select relevant context; draft the update; flag risks; decide when to escalate; and queue a capped story proposal for review.
- **Above the line:** post or send an update; create, close, or merge work; commit a ship date; mark a launch gate; approve scope; or bypass confidentiality and queue limits.
- **Explicit HITL:** a human reviews the grounded update and any proposed stories. Nothing is posted, created, merged, dated, or committed by Cortex.
- **Real blast radius:** Cortex handles live project evidence and prepares leadership-facing work, so an unsupported claim or implied commitment could misdirect decisions. Missing, conflicting, confidential, or out-of-bounds cases must stop and escalate.

## Build & demo

- **How it is built:** Direct a coding agent to refine the supplied transparent Cortex implementation in `00-build/`, one course module at a time.
- **Demo link:** _[optional shareable URL]_
- **Run screenshots:** _required, collected M2 to M6 in `06-autonomy/prototype.md`_

## Where it sits on the Trust Ladder

**Supervised.** Cortex retrieves, reasons, drafts, checks, and proposes; a human approves the output and owns every consequential action. Evals and bounded run evidence must justify any later increase in autonomy.

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
