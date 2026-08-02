# Agent Line Map: Workvivo Product Investment and Commercial Strategy Radar

> Module 1 · The Agent Line

## Agent purpose

Cortex connects competitive, analyst, customer, prospect, win/loss, pipeline, roadmap, and cost evidence to Workvivo's product capabilities so leaders can decide where to invest, monetise, enable, defend, investigate, monitor, or stop.

## The workflow, decision by decision

Each action is scored on reversibility, blast radius, and measurability before deciding whether a human or the agent should own it.

| Decision / action | Reversibility (H/M/L) | Blast radius (H/M/L) | Measurability (H/M/L) | Above / Below | HITL? |
|---|---|---|---|---|---|
| Pull new evidence from Steve, analyst research, customer insights, manual team submissions, win/loss information, pipeline data, roadmap plans, and cost-to-serve information, preserving its source and verification status | H | L | H | Below | No |
| Tag and assess each signal's source, date, reliability, segment, competitor, commercial relevance, and confidence | H | M | M | Below | Targeted review |
| Map each signal to the relevant Workvivo pillar and product capability | H | M | M | Below | Targeted review |
| Remove duplicates and connect related evidence into isolated signals, emerging themes, or strongly supported patterns | H | M | M | Below | Targeted review |
| Calculate capability scores across product strength, competitive position, demand, pipeline, win/loss, adoption, cost, ROI, and evidence confidence | H | M | M | Below | Targeted review |
| Draft a decision interpretation and recommend whether to invest, monetise, enable, differentiate, defend, investigate, monitor, or stop | H | M | L | Below | Required approval |
| Publish an approved finding, its evidence, scores, confidence, and recommendation to the executive decision dashboard | M | H | M | Above | Required approval |
| Commit a strategic change to the roadmap, investment level, pricing, packaging, or GTM strategy | L | H | L | Above | Human owned |

## Agent anatomy (sketch)

- **Model:** Use a fast, lower-cost model for collecting, tagging, mapping, deduplicating, and applying the approved scoring method. Escalate to a more capable model for cross-source interpretation and drafting strategic recommendations, while keeping publication and business decisions under human control.
- **Tools:** Read-only Steve connector · approved document and upload reader for analyst research, ZooMate summaries, customer research, and manual team submissions · win/loss and pipeline evidence reader that connects capabilities, competitors, segments, deal outcomes, and commercial value · roadmap and cost-to-serve readers · Workvivo capability map · approved scoring rules · draft dashboard writer. There are deliberately no tools that can publish to executives or change the roadmap, investment, pricing, packaging, or GTM strategy.
- **Memory:** Persist the Workvivo capability map, approved scoring definitions and weightings, source and verification records, historical scores and trends, accepted or rejected mappings, past recommendations, and human decisions and outcomes. Retain redacted evidence summaries and protected source references rather than unnecessary raw customer, prospect, or deal information.
- **Loop:** placeholder, defined in M2 `loop-spec.md`
- **Bounds:** placeholder, defined in M5 `bounds-and-evals.md`
- **Evals:** placeholder, defined in M5 `bounds-and-evals.md`

## The golden rule, applied

- **Pull new evidence:** Below the line because a read-only pull is highly reversible, has a low blast radius, and is highly measurable against the original source — deciding factor: all three axes are favourable.
- **Tag and assess each signal:** Below the line with targeted review because tags are highly reversible, but reliability and confidence have a medium blast radius and are only moderately measurable — deciding factor: measurability.
- **Map each signal to Workvivo:** Below the line with targeted review because mappings are highly reversible, but an ambiguous mapping can affect several capability scores and is only moderately measurable — deciding factor: measurability.
- **Connect related evidence:** Below the line with targeted review because groupings are highly reversible, but incorrectly combining signals can create a misleading pattern with a medium blast radius — deciding factor: blast radius.
- **Calculate capability scores:** Below the line with targeted review because scores are highly reversible and the arithmetic is checkable, but the approved weightings contain judgment and create medium downstream impact — deciding factor: measurability.
- **Draft an interpretation and recommendation:** Below the line with required approval because the draft is highly reversible and has a medium blast radius, but the correct strategic treatment is not objectively measurable — deciding factor: measurability.
- **Publish to the executive dashboard:** Above the line because publication is only moderately reversible, has a high blast radius across executive decisions, and is only moderately measurable — deciding factor: blast radius.
- **Commit a strategic business change:** Above the line because the decision has low reversibility, a high blast radius across product and commercial strategy, and low measurability over a long outcome period — deciding factor: blast radius.

## Hardest call

**How far the agent should go beyond identifying gaps, risks, and opportunities.** The most valuable part is giving us one bird's-eye view of the entire state of play so I can support the product team and relay evidence to executives. But it should not make the strategic call for us. Blast radius settled it: a mistaken strategic decision could redirect product investment, pricing, or GTM activity, so those decisions remain human-owned.
