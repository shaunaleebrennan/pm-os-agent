# Agent Line Map: Cortex: Product Investment & Commercial Strategy Agent

> Module 1 · The Agent Line

## Agent purpose

Cortex connects product, market, customer, competitive, analyst, pipeline, win/loss, adoption, roadmap, cost, and ROI evidence so product and commercial leaders can decide where to investigate, invest, monetise, enable, differentiate, defend, monitor, or stop. It adapts the course's supplied Cortex to a new domain while preserving the required agent anatomy, supervised loop, and real blast radius.

The agentic slice is deliberately narrow: Cortex decides which authorised evidence is relevant to the decision, identifies contradictions and gaps, and judges whether the available evidence is sufficient to support an interpretation. Retrieval, provenance, exact deduplication, calculations, and review routing are deterministic workflow or tool steps. Humans approve publication and own all roadmap, investment, pricing, packaging, and GTM commitments.

## The workflow, decision by decision

Each atomic decision is scored on reversibility, blast radius, and measurability. **Below** means Cortex may perform it within its bounds; **Above** means it remains human-owned. HITL is explicit wherever judgment could influence a consequential decision.

| Decision / action | Reversibility (H/M/L) | Blast radius (H/M/L) | Measurability (H/M/L) | Above / Below | HITL? |
|---|---|---|---|---|---|
| Retrieve authorised evidence and preserve source, date, permissions, and verification status | H | L | H | Below | No; deterministic tool step |
| Decide which evidence is relevant to the decision, product area, segment, market, or competitor in scope | H | M | M | Below | Targeted human review for low-confidence or ambiguous classifications |
| Remove exact duplicates, link related evidence, and keep source observations separate from interpretations | H | M | H | Below | Targeted review when links are inferred rather than exact |
| Judge whether the evidence is sufficient, current, representative, and consistent enough to proceed; otherwise stop and request specific missing evidence | H | M | M | Below | Required review when proceeding despite conflicts or material gaps |
| Apply approved scoring rules across product strength, demand, competitive position, pipeline, win/loss, adoption, cost, ROI, and evidence confidence | H | M | H | Below | Targeted review for missing inputs or rule exceptions |
| Draft an evidence-linked interpretation and recommendation, with alternatives, confidence, gaps, and no commitment language | H | M | M | Below | Required approval before use or publication |
| Approve and publish a finding, its evidence, scores, confidence, caveats, and recommendation to an executive decision surface | M | H | M | Above | Required; named human approves and publishes |
| Make or execute a roadmap, investment, pricing, packaging, or GTM commitment | L | H | L | Above | Human owned; agent has no execution tools |

## Agent anatomy (sketch)

- **Model:** Use a model for relevance, evidence-sufficiency, cross-source interpretation, and drafting. Do not use a model where deterministic retrieval, provenance checks, exact matching, calculations, or routing will do.
- **Tools:** Read-only connectors and approved document readers for product, market, customer, competitive, analyst, pipeline, win/loss, adoption, roadmap, cost, and ROI evidence · provenance and permission checks · exact-deduplication workflow · capability taxonomy · approved scoring rules · review-queue writer. There are deliberately no tools that can publish to executives or change roadmap, investment, pricing, packaging, or GTM commitments.
- **Memory:** Persist the approved taxonomy and scoring definitions, source and verification records, historical scores and trends, accepted or rejected mappings, past recommendations, human corrections, decisions, and outcomes. Retain redacted evidence summaries and protected source references rather than unnecessary raw customer, prospect, or deal information.
- **Loop:** placeholder, defined in M2 `loop-spec.md`
- **Bounds:** placeholder, defined in M5 `bounds-and-evals.md`
- **Evals:** placeholder, defined in M5 `bounds-and-evals.md`

## The golden rule, applied

- **Retrieve evidence:** Below the line because read-only retrieval is easy to reverse, affects only the working set, and can be checked exactly against its source.
- **Decide relevance:** Below the line with targeted review because classifications can be changed, but an incorrect inclusion or omission can distort the evidence base and relevance is only partly objectively measurable.
- **Deduplicate and link evidence:** Below the line with targeted review because exact matches are measurable and reversible, while inferred links need review to prevent separate observations being mistaken for corroboration.
- **Judge evidence sufficiency:** Below the line with escalation because the judgment is reversible but could determine whether a consequential recommendation proceeds, and representativeness is only moderately measurable.
- **Apply approved scoring rules:** Below the line with targeted review because calculations are reversible and testable, but missing inputs or exceptions can create a medium downstream impact.
- **Draft an interpretation and recommendation:** Below the line with required approval because a draft is reversible, but its strategic influence gives it a medium blast radius and its quality is not fully objectively measurable.
- **Approve and publish a finding:** Above the line because executive publication has a high organisational blast radius, is not fully reversible once read, and requires accountable human judgment.
- **Make or execute a strategic commitment:** Above the line because it is difficult to reverse, can redirect product and commercial activity, and may take a long time to measure reliably.

## Hardest call

**How far Cortex should go beyond identifying gaps, risks, and opportunities.** Its value comes from forming a cross-functional view and making the reasoning inspectable, but a persuasive draft could still shape executive action. Blast radius settled it: Cortex may judge relevance and sufficiency and draft an evidence-linked recommendation, but a named human must approve publication and humans alone own roadmap, investment, pricing, packaging, and GTM commitments.
