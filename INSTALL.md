# Installation smoke test

The v0.1.2 release artifact has been validated in a clean virtual environment.

Validated flow:

```bash
python3 -m venv /tmp/hermes-memory-evidence-repair-smoke
/tmp/hermes-memory-evidence-repair-smoke/bin/python -m pip install --upgrade pip
/tmp/hermes-memory-evidence-repair-smoke/bin/python -m pip install hermes_memory_evidence_repair-0.1.2-py3-none-any.whl
/tmp/hermes-memory-evidence-repair-smoke/bin/python - <<'PY'
from importlib.metadata import entry_points, version
import hermes_memory_evidence_repair
assert version('hermes-memory-evidence-repair') == '0.1.2'
ep = [ep for ep in entry_points(group='hermes_agent.plugins') if ep.name == 'memory-evidence-repair'][0]
assert ep.load() is hermes_memory_evidence_repair.register
PY
```

Expected result:

- package imports successfully
- `hermes_agent.plugins` entry point is present
- entry point loads `hermes_memory_evidence_repair:register`
- `register(ctx)` registers 30 tools
- every registered tool uses the dedicated `memory_evidence_repair` toolset
