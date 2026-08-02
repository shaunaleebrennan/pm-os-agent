# Cortex RUNBOOK, build it, run it, screenshot it

You will actually run an agent in this course. You build **one** thing: the
transparent Cortex agent in this `00-build/` folder (`agent.py`, `critic.py`,
`tools.py`, `prompts.py`), your PM chief-of-staff. You build it by **directing your
coding agent** (Claude Code, Cursor, or Codex), you do not have to hand-write
Python. Your coding agent edits these files and runs them for you; you read the
results and capture screenshots. A full run costs roughly a few cents on a cheap fast
model.

> New here? You never type code. You paste plain-English prompts. The exact ones
> to use, module by module, are in [`PROMPTS.md`](PROMPTS.md), keep it open.

## 0. One-time setup

1. On GitHub, click **Use this template -> Create a new repository** and name it
   `pm-os-agent` (or your own agent's name).
2. Open your new repo in your coding agent (Claude Code, Cursor, or Codex).
3. Get set up. Paste the **Setup** prompt from [`PROMPTS.md`](PROMPTS.md), or do it
   yourself in a terminal:

```bash
cd 00-build
pip install -r requirements.txt
cp .env.example .env        # add your OPENAI_API_KEY and set the caps
```

> The `.env` file is gitignored. Never commit your key. Also set a hard spend limit
> in your provider's dashboard, that limit is part of your M5 bounds story.
>
> On macOS, use `python3`/`pip3` if `python`/`pip` isn't found (that's the default on
> recent Macs). Every `python`/`pip` command below works the same way.

## 1. Build and run it with your coding agent

Work module by module using the prompts in [`PROMPTS.md`](PROMPTS.md): shape the
loop (M2), add the fleet + critic (M3), wire context and your PM brain (M4), and set
the bounds (M5). After each change, have your coding agent run a fixture and show you
the trace.

If you'd rather drive the terminal yourself, the same runs are:

```bash
python agent.py              # happy path, assemble the weekly status update
python agent.py missing-data # stuck/escalate
python agent.py jailbreak    # injection refusal
```

> Each run prints the full trace to your terminal, it does not write an output file.
> To save a trace, redirect it: `python agent.py | tee happy-run.txt`. (Your module
> deliverables, like `agent-line-map.md`, are files you edit and commit, separate from
> these runs.)

Then prove the bound trips (ask your coding agent to run these, or run them yourself):

```bash
CORTEX_MAX_ITERATIONS=2 python agent.py happy      # hits the iteration cap
CORTEX_COST_CAP_USD=0.001 python agent.py happy     # hits the cost cap
CORTEX_MAX_QUEUE_ITEMS=2 python agent.py happy       # the story batch is rejected + escalated
```

> Note: the `=2` override is deliberately set *below* the number of stories the PRD
> justifies, so the runtime bound (the tool) forces a stop. That is the point, the
> tool's rejection is authoritative and the run escalates rather than quietly
> committing a flood of work to the tracker.

## What to capture (and when)

| Module | Run | Screenshot |
|---|---|---|
| M2 | happy path | a real drafted update + the HITL stop (update + stories queued, nothing posted) |
| M3 | any | the critic rejecting an output (revise/block) |
| M4 | happy path | a grounded update that cites pulled activity; a caught hallucination when a source is withheld |
| M5 | jailbreak + bound trip | Cortex refusing & escalating; the iteration/cost/queue cap halting a run |
| M6 | end to end | the full run for `prototype.md` |

Drop these into `../06-autonomy/prototype.md` as you go.

## Make it yours

These files are **starters**. As you move through the modules you (via your coding
agent) will edit the agent-line behaviour (M1), the loop + stop conditions (M2), the
fleet + critic checks (M3), the retrieval/context (M4), and the bounds (M5) to match
your own specs. That editing is the assignment, don't just run the defaults and submit.
