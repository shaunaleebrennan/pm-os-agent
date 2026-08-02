# Memory & Context: Cortex PM Chief-of-Staff Agent

> Module 4 · Memory & Context

## 1. Context budget

_What does each loop iteration actually receive, and why? (You can't fit everything, what's the priority order?)_

## 2. Retrieve vs. long-context: per source

For each data source, decide: **retrieve** (narrow a large/changing corpus to the relevant slice) or **long-context** (just include a bounded set you can reason over).

| Source | Size / volatility | Decision | Why |
|---|---|---|---|
| _Roadmap_ | _large, slow-changing_ | _Retrieve_ | _too big to include; need the relevant slice (and respect confidential flags)_ |
| _GitHub/Jira activity_ | _large, changing_ | _Retrieve_ | _… + audit/citation needs_ |
| _This week's task brief_ | _bounded_ | _Long-context_ | _reason over the whole thing_ |
| _Team norms / playbook_ | _bounded_ | _Long-context_ | _… _ |

## 3. Retrieval quality plan

_Which of these apply, and how? (This is what separates modern agentic retrieval from naive "embed → top-k → stuff".)_

- **Routing**: _which source to query?_
- **Document grading**: _is what I retrieved actually relevant?_
- **Reranking**: _…_
- **Self-verification**: _did the update use the retrieved evidence?_
- **Caching**: _…_

## 4. Memory map (your PM brain)

| Memory type | What Cortex stores | Scope / TTL |
|---|---|---|
| **Working** (in-loop) | _…_ | _this run_ |
| **Episodic** (past runs) | _past status updates, decisions_ | _…_ |
| **Semantic** (durable facts/prefs) | _team norms, roadmap facts_ | _…_ |
| **Shared** (across agents) | _…_ | _…_ |

## 5. Memory risks & mitigations

| Risk | Mitigation |
|---|---|
| _Drift_ | _…_ |
| _Poisoning_ | _…_ |
| _Staleness_ | _…_ |
| _Confidential / retention_ | _scoping + flags (Cortex touches embargoed roadmap)_ |
