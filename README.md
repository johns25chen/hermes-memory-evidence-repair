# Hermes Memory Evidence Repair Plugin

Standalone Hermes plugin for the Memory Fabric evidence-repair governance workflow.

This plugin is read-only / preview-first by default. It provides planning, approval-token, commit-gate, rollback, recovery, closure-ledger, governance-seal, and finalization-readiness tools for Memory Evidence Repair without writing real Memory Graph data.

## Install for local development

```bash
pip install -e .
```

Hermes can discover this package through the `hermes.plugins` entry point, or the directory can be copied into `~/.hermes/plugins/memory-evidence-repair`.

## Safety model

- No direct Memory Graph writes.
- No config mutations.
- Durable write paths are represented as previews, gates, receipts, and approval-token checks.

## Install and Enable

This repository is packaged as a standalone Hermes plugin. Install it into the
same Python environment as Hermes, then enable the plugin through Hermes plugin
configuration/UI.

```bash
pip install -e /path/to/hermes-memory-evidence-repair
```

The Python package declares this entry point:

```toml
[project.entry-points."hermes_agent.plugins"]
memory-evidence-repair = "hermes_memory_evidence_repair:register"
```

When loaded, the plugin registers 30 tools under the dedicated toolset
`memory_evidence_repair`. It intentionally does not register tools into the core
`memory` toolset, so the default Memory surface is not expanded accidentally.

## Governance Boundary

All current tools are designed for governed evidence-repair workflows:
planning, preview, dry-run, approval-token generation/checking, ledger/receipt
preview, rollback planning, recovery preview, closure checks, and finalization
readiness. They do not directly write the real Memory Graph by default.

Any future tool that performs durable Memory writes should keep these gates:

1. explicit human approval token,
2. write-lock validation,
3. rollback plan or recovery path,
4. receipt/audit output,
5. tests proving preview-only behavior remains preview-only.

## Smoke Test

```bash
PYTHONPATH=src pytest tests/test_plugin_registration.py -q
```

Full test suite:

```bash
PYTHONPATH=src pytest tests -q
```

