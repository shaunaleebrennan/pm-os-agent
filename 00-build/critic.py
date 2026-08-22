"""Independent validator (M3). A separate model call that never saw the drafting
context, so it can't inherit the draft's blind spots. Returns a pass/fail verdict.
The revision cap that stops a critic<->drafter loop lives in `agent.py`.
"""

from __future__ import annotations

import json

from prompts import CRITIC_SYSTEM


def review(client, model: str, validator_handoff: dict) -> dict:
    """Return {"verdict": "pass"|"fail", "reasons": [...]} for a proposed output."""
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": CRITIC_SYSTEM},
            {"role": "user", "content": json.dumps(
                validator_handoff, indent=2, sort_keys=True)},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "critic_verdict",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "verdict": {"type": "string", "enum": ["pass", "fail"]},
                        "reasons": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["verdict", "reasons"],
                    "additionalProperties": False,
                },
            },
        },
        temperature=0,
    )
    usage = resp.usage
    try:
        verdict = json.loads(resp.choices[0].message.content)
    except (json.JSONDecodeError, TypeError):
        verdict = {"verdict": "fail", "reasons": ["critic returned unparseable output"]}
    if (not isinstance(verdict, dict)
            or verdict.get("verdict") not in {"pass", "fail"}
            or not isinstance(verdict.get("reasons"), list)
            or not all(isinstance(reason, str) for reason in verdict.get("reasons", []))):
        verdict = {"verdict": "fail", "reasons": ["critic returned an invalid verdict"]}
    verdict["_usage"] = {"prompt": usage.prompt_tokens, "completion": usage.completion_tokens}
    return verdict
