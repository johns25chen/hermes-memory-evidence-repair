"""Minimal test registry compatible with Hermes tool registry assertions."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ToolEntry:
    name: str
    toolset: str
    schema: dict[str, Any]
    handler: Callable[..., Any]
    check_fn: Callable[..., Any] | None = None
    requires_env: list[str] | None = None
    is_async: bool = False
    description: str = ""
    emoji: str = ""


class TestRegistry:
    def __init__(self) -> None:
        self._entries: dict[str, ToolEntry] = {}

    def register(
        self,
        *,
        name: str,
        toolset: str,
        schema: dict[str, Any],
        handler: Callable[..., Any],
        check_fn: Callable[..., Any] | None = None,
        requires_env: list[str] | None = None,
        is_async: bool = False,
        description: str = "",
        emoji: str = "",
        override: bool = True,
    ) -> ToolEntry:
        if name in self._entries and not override:
            raise ValueError(f"tool already registered: {name}")
        entry = ToolEntry(
            name=name,
            toolset=toolset,
            schema=schema,
            handler=handler,
            check_fn=check_fn,
            requires_env=requires_env,
            is_async=is_async,
            description=description,
            emoji=emoji,
        )
        self._entries[name] = entry
        return entry

    def get_entry(self, name: str) -> ToolEntry | None:
        return self._entries.get(name)


registry = TestRegistry()


def tool_error(message: str, *, code: str = "error", **details: Any) -> str:
    """Return a Hermes-style JSON error payload."""
    payload: dict[str, Any] = {"success": False, "error": message, "code": code}
    if details:
        payload.update(details)
    return json.dumps(payload, sort_keys=True)
