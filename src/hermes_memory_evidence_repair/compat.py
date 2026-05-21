"""Small compatibility helpers used when running outside Hermes core."""
from __future__ import annotations

import json
from typing import Any


def tool_error(message: str, *, code: str = "error", **details: Any) -> str:
    """Return a Hermes-style JSON error payload."""
    payload: dict[str, Any] = {"success": False, "error": message, "code": code}
    if details:
        payload.update(details)
    return json.dumps(payload, sort_keys=True)
