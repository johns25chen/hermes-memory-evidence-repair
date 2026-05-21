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
