# Hermes Memory Evidence Repair Plugin

Standalone Hermes plugin for the Hermes Memory Fabric evidence-repair governance workflow.

This plugin is read-only / preview-first by default. It provides planning,
approval-token, commit-gate, rollback, recovery, closure-ledger,
governance-seal, and finalization-readiness tools for Memory Evidence Repair
without writing real Memory Graph data.

## Why this is a standalone plugin

Hermes core now expects specialized memory workflows to live outside the core
repository. This package exposes Memory Evidence Repair through the general
Hermes plugin surface instead of expanding the default core `memory` toolset.

## Install and enable

Install the plugin into the same Python environment as Hermes:

```bash
pip install -e /path/to/hermes-memory-evidence-repair
```

The package declares this Hermes plugin entry point:

```toml
[project.entry-points."hermes_agent.plugins"]
memory-evidence-repair = "hermes_memory_evidence_repair:register"
```

When loaded, the plugin registers 30 tools under the dedicated toolset
`memory_evidence_repair`.

## Toolset

Toolset: `memory_evidence_repair`

Tools registered by this plugin:

- `memory_evidence_repair_apply_preview`
- `memory_evidence_repair_approval_candidates`
- `memory_evidence_repair_approval_token_gate`
- `memory_evidence_repair_commit_gate`
- `memory_evidence_repair_commit_ledger`
- `memory_evidence_repair_commit_receipt`
- `memory_evidence_repair_executor_preview`
- `memory_evidence_repair_human_approval_token`
- `memory_evidence_repair_manual_commit_dry_run`
- `memory_evidence_repair_planner`
- `memory_evidence_repair_post_commit_audit_preview`
- `memory_evidence_repair_recovery_approval_token_gate`
- `memory_evidence_repair_recovery_closure_finalization_readiness_audit_preview`
- `memory_evidence_repair_recovery_closure_finalization_readiness_preview`
- `memory_evidence_repair_recovery_closure_gate`
- `memory_evidence_repair_recovery_closure_governance_seal_audit_preview`
- `memory_evidence_repair_recovery_closure_governance_seal_preview`
- `memory_evidence_repair_recovery_closure_ledger_audit_preview`
- `memory_evidence_repair_recovery_closure_ledger_preview`
- `memory_evidence_repair_recovery_completion_audit_preview`
- `memory_evidence_repair_recovery_completion_receipt`
- `memory_evidence_repair_recovery_decision_gate`
- `memory_evidence_repair_recovery_execution_preview`
- `memory_evidence_repair_recovery_executor_preview`
- `memory_evidence_repair_recovery_human_approval_token`
- `memory_evidence_repair_recovery_write_lock_gate`
- `memory_evidence_repair_rollback_drill_preview`
- `memory_evidence_repair_rollback_plan`
- `memory_evidence_repair_snapshot_planner`
- `memory_evidence_repair_write_lock_gate`

## Governance boundary

All current tools are designed for governed evidence-repair workflows:
planning, preview, dry-run, approval-token generation/checking, ledger/receipt
preview, rollback planning, recovery preview, closure checks, and finalization
readiness. They do not directly write the real Memory Graph by default.

Any future tool that performs durable Memory writes must keep these gates:

1. explicit human approval token,
2. write-lock validation,
3. rollback plan or recovery path,
4. receipt/audit output,
5. tests proving preview-only behavior remains preview-only.


## Release status

Current version: `0.1.1`

Validation status:

- Local syntax check: passing
- Local tests: 403 passing
- GitHub Actions CI: passing on Python 3.11 and 3.12

Repository:

- https://github.com/johns25chen/hermes-memory-evidence-repair

## Local validation

Smoke test:

```bash
PYTHONPATH=src pytest tests/test_plugin_registration.py -q
```

Full test suite:

```bash
PYTHONPATH=src pytest tests -q
```

Syntax check:

```bash
python -m py_compile $(find src tests -name '*.py' -print)
```
