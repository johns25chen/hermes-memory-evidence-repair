"""Test registration for standalone plugin tools."""

from __future__ import annotations

import hermes_memory_evidence_repair
from tools.registry import registry


class _TestPluginContext:
    def register_tool(
        self,
        name,
        toolset,
        schema,
        handler,
        check_fn=None,
        requires_env=None,
        is_async=False,
        description="",
        emoji="",
        override=True,
    ):
        registry.register(
            name=name,
            toolset=toolset,
            schema=schema,
            handler=handler,
            check_fn=check_fn,
            requires_env=requires_env,
            is_async=is_async,
            description=description,
            emoji=emoji,
            override=True,
        )


hermes_memory_evidence_repair.register(_TestPluginContext())
