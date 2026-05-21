# Changelog

## 0.1.1 - 2026-05-21

### Fixed

- CI now validates editable package installation with `pip install -e .` instead of relying only on `PYTHONPATH`.
- Release metadata now reflects the package-installable standalone plugin state.

## 0.1.0 - 2026-05-21

Initial standalone Hermes plugin release for Memory Evidence Repair governance.

### Added

- 30 Memory Evidence Repair tools under the dedicated `memory_evidence_repair` toolset.
- Preview-first governance flow covering planning, approval tokens, commit gates, receipts, rollback, recovery, closure ledgers, governance seals, and finalization readiness.
- Standalone plugin entry point: `hermes_memory_evidence_repair:register`.
- Plugin metadata in `plugin.yaml`.
- Local compatibility layer so the plugin can run and test outside Hermes core.
- GitHub Actions CI for Python 3.11 and 3.12.
- 403 tests covering core logic, tool wrappers, and plugin registration.
