"""Standalone Hermes plugin for Memory Evidence Repair governance tools."""
from __future__ import annotations

from hermes_memory_evidence_repair.tools.memory_evidence_repair_apply_preview_tool import MEMORY_EVIDENCE_REPAIR_APPLY_PREVIEW_SCHEMA, memory_evidence_repair_apply_preview_tool, check_memory_evidence_repair_apply_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_approval_candidates_tool import MEMORY_EVIDENCE_REPAIR_APPROVAL_CANDIDATES_SCHEMA, memory_evidence_repair_approval_candidates_tool, check_memory_evidence_repair_approval_candidates_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_approval_token_gate_tool import MEMORY_EVIDENCE_REPAIR_APPROVAL_TOKEN_GATE_SCHEMA, memory_evidence_repair_approval_token_gate_tool, check_memory_evidence_repair_approval_token_gate_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_commit_gate_tool import MEMORY_EVIDENCE_REPAIR_COMMIT_GATE_SCHEMA, memory_evidence_repair_commit_gate_tool, check_memory_evidence_repair_commit_gate_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_commit_ledger_tool import MEMORY_EVIDENCE_REPAIR_COMMIT_LEDGER_SCHEMA, memory_evidence_repair_commit_ledger_tool, check_memory_evidence_repair_commit_ledger_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_commit_receipt_tool import MEMORY_EVIDENCE_REPAIR_COMMIT_RECEIPT_SCHEMA, memory_evidence_repair_commit_receipt_tool, check_memory_evidence_repair_commit_receipt_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_executor_preview_tool import MEMORY_EVIDENCE_REPAIR_EXECUTOR_PREVIEW_SCHEMA, memory_evidence_repair_executor_preview_tool, check_memory_evidence_repair_executor_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_human_approval_token_tool import MEMORY_EVIDENCE_REPAIR_HUMAN_APPROVAL_TOKEN_SCHEMA, memory_evidence_repair_human_approval_token_tool, check_memory_evidence_repair_human_approval_token_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_manual_commit_dry_run_tool import MEMORY_EVIDENCE_REPAIR_MANUAL_COMMIT_DRY_RUN_SCHEMA, memory_evidence_repair_manual_commit_dry_run_tool, check_memory_evidence_repair_manual_commit_dry_run_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_planner_tool import MEMORY_EVIDENCE_REPAIR_PLANNER_SCHEMA, memory_evidence_repair_planner_tool, check_memory_evidence_repair_planner_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_post_commit_audit_preview_tool import MEMORY_EVIDENCE_REPAIR_POST_COMMIT_AUDIT_PREVIEW_SCHEMA, memory_evidence_repair_post_commit_audit_preview_tool, check_memory_evidence_repair_post_commit_audit_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_approval_token_gate_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_APPROVAL_TOKEN_GATE_SCHEMA, memory_evidence_repair_recovery_approval_token_gate_tool, check_memory_evidence_repair_recovery_approval_token_gate_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_closure_finalization_readiness_audit_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_FINALIZATION_READINESS_AUDIT_PREVIEW_SCHEMA, memory_evidence_repair_recovery_closure_finalization_readiness_audit_preview_tool, check_memory_evidence_repair_recovery_closure_finalization_readiness_audit_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_closure_finalization_readiness_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_FINALIZATION_READINESS_PREVIEW_SCHEMA, memory_evidence_repair_recovery_closure_finalization_readiness_preview_tool, check_memory_evidence_repair_recovery_closure_finalization_readiness_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_closure_gate_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_GATE_SCHEMA, memory_evidence_repair_recovery_closure_gate_tool, check_memory_evidence_repair_recovery_closure_gate_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_closure_governance_seal_audit_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_GOVERNANCE_SEAL_AUDIT_PREVIEW_SCHEMA, memory_evidence_repair_recovery_closure_governance_seal_audit_preview_tool, check_memory_evidence_repair_recovery_closure_governance_seal_audit_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_closure_governance_seal_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_GOVERNANCE_SEAL_PREVIEW_SCHEMA, memory_evidence_repair_recovery_closure_governance_seal_preview_tool, check_memory_evidence_repair_recovery_closure_governance_seal_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_closure_ledger_audit_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_LEDGER_AUDIT_PREVIEW_SCHEMA, memory_evidence_repair_recovery_closure_ledger_audit_preview_tool, check_memory_evidence_repair_recovery_closure_ledger_audit_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_closure_ledger_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_LEDGER_PREVIEW_SCHEMA, memory_evidence_repair_recovery_closure_ledger_preview_tool, check_memory_evidence_repair_recovery_closure_ledger_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_completion_audit_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_COMPLETION_AUDIT_PREVIEW_SCHEMA, memory_evidence_repair_recovery_completion_audit_preview_tool, check_memory_evidence_repair_recovery_completion_audit_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_completion_receipt_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_COMPLETION_RECEIPT_SCHEMA, memory_evidence_repair_recovery_completion_receipt_tool, check_memory_evidence_repair_recovery_completion_receipt_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_decision_gate_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_DECISION_GATE_SCHEMA, memory_evidence_repair_recovery_decision_gate_tool, check_memory_evidence_repair_recovery_decision_gate_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_execution_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_EXECUTION_PREVIEW_SCHEMA, memory_evidence_repair_recovery_execution_preview_tool, check_memory_evidence_repair_recovery_execution_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_executor_preview_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_EXECUTOR_PREVIEW_SCHEMA, memory_evidence_repair_recovery_executor_preview_tool, check_memory_evidence_repair_recovery_executor_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_human_approval_token_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_HUMAN_APPROVAL_TOKEN_SCHEMA, memory_evidence_repair_recovery_human_approval_token_tool, check_memory_evidence_repair_recovery_human_approval_token_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_recovery_write_lock_gate_tool import MEMORY_EVIDENCE_REPAIR_RECOVERY_WRITE_LOCK_GATE_SCHEMA, memory_evidence_repair_recovery_write_lock_gate_tool, check_memory_evidence_repair_recovery_write_lock_gate_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_rollback_drill_preview_tool import MEMORY_EVIDENCE_REPAIR_ROLLBACK_DRILL_PREVIEW_SCHEMA, memory_evidence_repair_rollback_drill_preview_tool, check_memory_evidence_repair_rollback_drill_preview_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_rollback_plan_tool import MEMORY_EVIDENCE_REPAIR_ROLLBACK_PLAN_SCHEMA, memory_evidence_repair_rollback_plan_tool, check_memory_evidence_repair_rollback_plan_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_snapshot_planner_tool import MEMORY_EVIDENCE_REPAIR_SNAPSHOT_PLANNER_SCHEMA, memory_evidence_repair_snapshot_planner_tool, check_memory_evidence_repair_snapshot_planner_requirements
from hermes_memory_evidence_repair.tools.memory_evidence_repair_write_lock_gate_tool import MEMORY_EVIDENCE_REPAIR_WRITE_LOCK_GATE_SCHEMA, memory_evidence_repair_write_lock_gate_tool, check_memory_evidence_repair_write_lock_gate_requirements


def register(ctx):
    """Register Memory Evidence Repair tools with Hermes."""
    ctx.register_tool(
        name="memory_evidence_repair_apply_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_APPLY_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_apply_preview_tool,
        check_fn=check_memory_evidence_repair_apply_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_approval_candidates",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_APPROVAL_CANDIDATES_SCHEMA,
        handler=memory_evidence_repair_approval_candidates_tool,
        check_fn=check_memory_evidence_repair_approval_candidates_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_approval_token_gate",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_APPROVAL_TOKEN_GATE_SCHEMA,
        handler=memory_evidence_repair_approval_token_gate_tool,
        check_fn=check_memory_evidence_repair_approval_token_gate_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_commit_gate",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_COMMIT_GATE_SCHEMA,
        handler=memory_evidence_repair_commit_gate_tool,
        check_fn=check_memory_evidence_repair_commit_gate_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_commit_ledger",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_COMMIT_LEDGER_SCHEMA,
        handler=memory_evidence_repair_commit_ledger_tool,
        check_fn=check_memory_evidence_repair_commit_ledger_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_commit_receipt",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_COMMIT_RECEIPT_SCHEMA,
        handler=memory_evidence_repair_commit_receipt_tool,
        check_fn=check_memory_evidence_repair_commit_receipt_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_executor_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_EXECUTOR_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_executor_preview_tool,
        check_fn=check_memory_evidence_repair_executor_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_human_approval_token",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_HUMAN_APPROVAL_TOKEN_SCHEMA,
        handler=memory_evidence_repair_human_approval_token_tool,
        check_fn=check_memory_evidence_repair_human_approval_token_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_manual_commit_dry_run",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_MANUAL_COMMIT_DRY_RUN_SCHEMA,
        handler=memory_evidence_repair_manual_commit_dry_run_tool,
        check_fn=check_memory_evidence_repair_manual_commit_dry_run_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_planner",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_PLANNER_SCHEMA,
        handler=memory_evidence_repair_planner_tool,
        check_fn=check_memory_evidence_repair_planner_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_post_commit_audit_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_POST_COMMIT_AUDIT_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_post_commit_audit_preview_tool,
        check_fn=check_memory_evidence_repair_post_commit_audit_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_approval_token_gate",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_APPROVAL_TOKEN_GATE_SCHEMA,
        handler=memory_evidence_repair_recovery_approval_token_gate_tool,
        check_fn=check_memory_evidence_repair_recovery_approval_token_gate_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_closure_finalization_readiness_audit_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_FINALIZATION_READINESS_AUDIT_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_closure_finalization_readiness_audit_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_closure_finalization_readiness_audit_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_closure_finalization_readiness_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_FINALIZATION_READINESS_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_closure_finalization_readiness_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_closure_finalization_readiness_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_closure_gate",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_GATE_SCHEMA,
        handler=memory_evidence_repair_recovery_closure_gate_tool,
        check_fn=check_memory_evidence_repair_recovery_closure_gate_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_closure_governance_seal_audit_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_GOVERNANCE_SEAL_AUDIT_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_closure_governance_seal_audit_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_closure_governance_seal_audit_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_closure_governance_seal_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_GOVERNANCE_SEAL_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_closure_governance_seal_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_closure_governance_seal_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_closure_ledger_audit_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_LEDGER_AUDIT_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_closure_ledger_audit_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_closure_ledger_audit_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_closure_ledger_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_CLOSURE_LEDGER_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_closure_ledger_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_closure_ledger_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_completion_audit_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_COMPLETION_AUDIT_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_completion_audit_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_completion_audit_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_completion_receipt",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_COMPLETION_RECEIPT_SCHEMA,
        handler=memory_evidence_repair_recovery_completion_receipt_tool,
        check_fn=check_memory_evidence_repair_recovery_completion_receipt_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_decision_gate",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_DECISION_GATE_SCHEMA,
        handler=memory_evidence_repair_recovery_decision_gate_tool,
        check_fn=check_memory_evidence_repair_recovery_decision_gate_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_execution_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_EXECUTION_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_execution_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_execution_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_executor_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_EXECUTOR_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_recovery_executor_preview_tool,
        check_fn=check_memory_evidence_repair_recovery_executor_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_human_approval_token",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_HUMAN_APPROVAL_TOKEN_SCHEMA,
        handler=memory_evidence_repair_recovery_human_approval_token_tool,
        check_fn=check_memory_evidence_repair_recovery_human_approval_token_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_recovery_write_lock_gate",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_RECOVERY_WRITE_LOCK_GATE_SCHEMA,
        handler=memory_evidence_repair_recovery_write_lock_gate_tool,
        check_fn=check_memory_evidence_repair_recovery_write_lock_gate_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_rollback_drill_preview",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_ROLLBACK_DRILL_PREVIEW_SCHEMA,
        handler=memory_evidence_repair_rollback_drill_preview_tool,
        check_fn=check_memory_evidence_repair_rollback_drill_preview_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_rollback_plan",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_ROLLBACK_PLAN_SCHEMA,
        handler=memory_evidence_repair_rollback_plan_tool,
        check_fn=check_memory_evidence_repair_rollback_plan_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_snapshot_planner",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_SNAPSHOT_PLANNER_SCHEMA,
        handler=memory_evidence_repair_snapshot_planner_tool,
        check_fn=check_memory_evidence_repair_snapshot_planner_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
    ctx.register_tool(
        name="memory_evidence_repair_write_lock_gate",
        toolset="memory_evidence_repair",
        schema=MEMORY_EVIDENCE_REPAIR_WRITE_LOCK_GATE_SCHEMA,
        handler=memory_evidence_repair_write_lock_gate_tool,
        check_fn=check_memory_evidence_repair_write_lock_gate_requirements,
        emoji="🧠",
        description="Memory Evidence Repair governance workflow tool.",
    )
