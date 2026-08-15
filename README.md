# Cortex: Product Investment & Commercial Strategy Agent

> My final project for Product School's **Run Your AI Agent Team** certification. Cortex connects product, market, customer, competitive, analyst, pipeline, win/loss, adoption, roadmap, cost, and ROI evidence to support product investment and commercial strategy decisions—while humans retain ownership of consequential commitments.

This project follows the Final Project Brief's approved **bring-your-own agent/domain** path. It adapts the supplied Cortex PM chief-of-staff scenario to a product investment and commercial strategy domain; it does not replace the course's learning architecture. The same Cortex scaffold and required anatomy remain in place: an agent line, loop, tools, critic, explicit human-in-the-loop (HITL) checkpoint, memory, bounds, evals, a real run, and a real blast radius. Each module will evolve that architecture in sequence.

For now, only this dashboard and the Module 1 Agent Line Map have been adapted. The runnable starter in `00-build/` and Modules 2–6 remain unchanged until their corresponding course work begins.

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

Cortex helps product and commercial leaders decide where deeper investigation or action may be warranted by selecting relevant cross-functional evidence, judging whether it is sufficient, applying approved scoring rules, and drafting evidence-linked interpretations and recommendations; humans approve publication and own roadmap, investment, pricing, packaging, and GTM commitments.

## Agent line and blast radius

- **Real access:** read-only access to approved product, market, customer, competitive, analyst, pipeline, win/loss, adoption, roadmap, cost, and ROI evidence sources.
- **Agentic work:** decide which evidence is relevant to the decision, identify conflicts or gaps, judge whether the evidence is sufficient, and draft a recommendation with confidence and caveats.
- **Deterministic workflow:** retrieve authorised records, preserve provenance, remove exact duplicates, apply approved calculations, and route drafts to review.
- **Explicit HITL:** a named human must review evidence, confidence, caveats, and the draft before anything is published or used as a commitment.
- **Human-owned decisions:** roadmap, product investment, pricing, packaging, and GTM commitments are never made or executed by the agent.
- **Real blast radius:** a weak interpretation could influence executive prioritisation or commercial direction, so the system stops before publication or commitment and provides no write tools for those actions.

## Build & demo

- **How you built it:** Adapt the supplied transparent Cortex build with a coding agent, module by module, starting in `00-build/` when the course reaches implementation.
- **Demo link:** _[optional shareable URL]_
- **Run screenshots:** _required, collected M2 to M6 in `06-autonomy/prototype.md`_

## Where it sits on the Trust Ladder

**Design stage.** The intended starting rung is supervised: Cortex may retrieve, assess, score, and draft, but a human reviews the output before publication and owns every consequential strategic decision. Later eval evidence will determine whether any bounded tasks can climb the ladder.

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
