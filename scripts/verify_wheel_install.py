"""Validate the built wheel in a clean virtual environment.

This intentionally installs the wheel from dist/ into a fresh venv and verifies
the Hermes plugin entry point, registration count, and toolset boundary.
"""
from __future__ import annotations

import glob
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap

EXPECTED_VERSION = "0.1.3"
EXPECTED_ENTRY_POINT = "memory-evidence-repair"
EXPECTED_TOOLSET = "memory_evidence_repair"
EXPECTED_TOOL_COUNT = 30


def run(cmd: list[str], **kwargs) -> None:
    subprocess.run(cmd, check=True, **kwargs)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    wheels = sorted(glob.glob(str(root / "dist" / "hermes_memory_evidence_repair-*.whl")))
    if not wheels:
        raise SystemExit("No hermes_memory_evidence_repair wheel found under dist/. Run python -m build first.")
    if len(wheels) != 1:
        raise SystemExit(f"Expected exactly one wheel under dist/, found {len(wheels)}: {wheels}")
    wheel = wheels[0]

    venv_dir = Path(tempfile.mkdtemp(prefix="hermes-memory-evidence-repair-smoke-"))
    try:
        run([sys.executable, "-m", "venv", str(venv_dir)])
        python = venv_dir / ("Scripts" if os.name == "nt" else "bin") / "python"
        run([str(python), "-m", "pip", "install", "--upgrade", "pip"])
        run([str(python), "-m", "pip", "install", wheel])
        probe = textwrap.dedent(
            f'''
            from importlib.metadata import entry_points, version
            import hermes_memory_evidence_repair

            assert version("hermes-memory-evidence-repair") == "{EXPECTED_VERSION}"
            eps = entry_points(group="hermes_agent.plugins")
            matched = [ep for ep in eps if ep.name == "{EXPECTED_ENTRY_POINT}"]
            assert len(matched) == 1, matched
            assert matched[0].load() is hermes_memory_evidence_repair.register

            class Ctx:
                def __init__(self):
                    self.tools = []
                def register_tool(self, **kwargs):
                    self.tools.append(kwargs)

            ctx = Ctx()
            hermes_memory_evidence_repair.register(ctx)
            assert len(ctx.tools) == {EXPECTED_TOOL_COUNT}, len(ctx.tools)
            assert {{tool["toolset"] for tool in ctx.tools}} == {{"{EXPECTED_TOOLSET}"}}
            print("clean_wheel_smoke_ok")
            '''
        )
        run([str(python), "-c", probe])
    finally:
        shutil.rmtree(venv_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
