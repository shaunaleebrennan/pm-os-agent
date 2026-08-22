# Memory & Context: Cortex PM Chief-of-Staff Agent

> Module 4 · Memory & Context

**In plain English:** Context is the information Cortex needs access to in order to
run the current task effectively. Memory is what Cortex deliberately saves from
previous and current tasks to use in future tasks.

## 1. Context budget

Each iteration receives the smallest set of context needed to complete the current
PM task safely and accurately. Current evidence and safety rules take priority over
historical context.

**Priority order:**

1. The current task brief and Agent Line rules.
2. Current project status and recent engineering activity.
3. The relevant project and roadmap slice.
4. The current team-norm sections governing the task.
5. A relevant past update or decision, when needed for precedent or tone.
6. The current draft and Validator feedback, only during the single revision pass.

Cortex excludes unrelated projects, full histories, duplicate tool results, and
confidential material that is not required for the task. Large or changing sources
are narrowed before inclusion; bounded sources are included only when they are
relevant to the current run.

## 2. Retrieve vs. long-context: per source

For each data source, decide: **retrieve** (narrow a large/changing corpus to the relevant slice) or **long-context** (just include a bounded set you can reason over).

| Source | Size / volatility | Decision | Deciding factor and why |
|---|---|---|---|
| `get_activity` | Large, growing, and fast-changing | Retrieve | **Volatility:** pull only the latest records for the requested project. |
| `search_past_updates` | Growing historical corpus with no fixed limit | Retrieve | **Corpus size:** search for relevant project precedent instead of loading the complete history. |
| `get_roadmap` | Medium, changing, and access-sensitive | Retrieve | **Citation / audit:** pull only the relevant project section so claims remain traceable and unrelated confidential projects do not enter the task context. |
| `get_norms` | Medium and updated over time | Retrieve | **Size and volatility:** pull the current sections governing the task instead of loading the entire playbook. |
| `get_task` | One small, static document | Long-context | **Bounded corpus size:** include the complete brief without retrieval overhead or loss of instructions. |

## 3. Retrieval quality plan

| Retrieved source | Routing | Document grading | Reranking | Self-verification | Caching |
|---|---:|---:|---:|---:|---:|
| `get_activity` | Yes | Yes | No | Yes | No |
| `search_past_updates` | Yes | Yes | Yes | Yes | No |
| `get_roadmap` | Yes | Yes | No | Yes | No |
| `get_norms` | Yes | Yes | No | Yes | No |

- **`get_activity`:** route by project ID, reject activity from another project,
  and verify that every progress or metric claim matches the returned records.
- **`search_past_updates`:** route by project and task, discard irrelevant history,
  rank the newest relevant decision first, and verify any precedent used in the draft.
- **`get_roadmap`:** route to the requested project section, reject unrelated or
  confidential sections, and verify every roadmap claim against that selected slice.
- **`get_norms`:** route to the rules governing the current task, reject unrelated
  sections, and verify the draft against the retrieved safeguards.

Caching is deferred because these sources can change. Reusing stale activity,
roadmap, or norms currently creates more risk than the small cost or latency saving.

## 4. Memory map (your PM brain)

| Memory type | What Cortex stores | Scope / TTL |
|---|---|---|
| **Working** (in-loop) | Current task, retrieved evidence, tool results, draft, Validator feedback, and run counters | One run; discard at completion |
| **Episodic** (past runs) | Approved updates, PM corrections and decisions, escalation outcomes, and review status | Per project; retain for 90 days, then archive or delete |
| **Semantic** (durable facts/prefs) | Team norms, Agent Line rules, project identifiers, stable PM preferences, and enforced bounds | Long-lived; versioned and reviewed when the authoritative source changes |
| **Shared** (across agents) | The four-field Cortex-to-Validator hand-off and the Validator's failure reasons | Current collaboration and run only; discard at completion |

Cortex does not write raw confidential roadmap content, unapproved drafts, or
speculative model conclusions into durable memory.

## 5. Memory risks & mitigations

| Risk | Where it affects Cortex | Mitigation |
|---|---|---|
| Drift | A stored project fact gradually diverges from the authoritative source. | Revalidate stored facts against the authoritative source before using them. |
| Poisoning | Bad task content or an untrusted correction is written once and trusted in future runs. | Write memory only from approved sources or explicit PM corrections, and retain source provenance. |
| Staleness | Cortex reuses a status, metric, decision, or norm that was once correct but has changed. | Apply the 90-day episodic TTL and re-fetch volatile project facts on every run. |
| PII / retention | Confidential roadmap or personal data is stored for too long or becomes reachable by the wrong audience. | Store the minimum, scope by project and audience, preserve confidentiality labels, and never persist raw embargoed content. |
| Cross-project leakage | Evidence or decisions from one project enter another project's update. | Partition memory by project ID and never retrieve one project's memory into another project. |
| Unapproved inference becoming fact | A model interpretation is recalled later as if it were verified evidence. | Persist model interpretations only after PM approval, with their approval status and source clearly labelled. |

Memory read and write permissions follow the M1 Agent Line. TTL, retention, and
project scope become infrastructure-enforced bounds in M5, not prompt preferences.
