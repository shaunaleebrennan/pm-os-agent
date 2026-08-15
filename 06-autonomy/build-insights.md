# Build Insights: Cortex PM Chief-of-Staff Agent

> Module 6 · ★ Deliverable 4, what you learned building it

## Module 2 reflection: from instinct to working loop

My first instinct was that Cortex should react when the PM needs support and also run a regular sweep for anything missed through absence or human error.

The lecture gave that instinct a clearer structure. I defined Cortex as a Hook + Cron loop, added idempotency, set a clear definition of done, documented three exits, and mapped the five components the loop needs.

Running the updated loop exposed issues the written spec alone did not: repeated proposals and inconsistent interpretation of completed work, normal open issues, and escalation. Tightening those rules and rerunning the happy path showed me that a good loop design must work in practice, not just read well on paper.

## Friction

_Where did the build fight you? (Loop stop conditions? Context budget? The validator? Bounds?)_

## Learning

_The two or three things you now understand about shipping agents that you didn't before the course._

## Aha moment

_The single insight that changed how you'd design your next agent._

## What you'd do differently

_If you rebuilt Cortex from scratch, what changes?_
