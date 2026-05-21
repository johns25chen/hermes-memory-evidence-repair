"""Smoke tests for the standalone Hermes plugin registration surface."""

from __future__ import annotations

import tomllib
from pathlib import Path

import hermes_memory_evidence_repair


class RecordingPluginContext:
    def __init__(self) -> None:
        self.tools = []

    def register_tool(
        self,
        *,
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
        self.tools.append(
            {
                "name": name,
                "toolset": toolset,
                "schema": schema,
                "handler": handler,
                "check_fn": check_fn,
                "requires_env": requires_env,
                "is_async": is_async,
                "description": description,
                "emoji": emoji,
                "override": override,
            }
        )


def test_register_exposes_memory_evidence_repair_toolset() -> None:
    ctx = RecordingPluginContext()

    hermes_memory_evidence_repair.register(ctx)

    assert len(ctx.tools) == 30
    assert {tool["toolset"] for tool in ctx.tools} == {"memory_evidence_repair"}
    assert "memory_evidence_repair_planner" in {tool["name"] for tool in ctx.tools}
    assert "memory_evidence_repair_recovery_closure_governance_seal_preview" in {
        tool["name"] for tool in ctx.tools
    }


def test_distribution_entry_point_is_declared() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text())

    entry_points = pyproject["project"]["entry-points"]["hermes_agent.plugins"]

    assert entry_points["memory-evidence-repair"] == "hermes_memory_evidence_repair:register"
