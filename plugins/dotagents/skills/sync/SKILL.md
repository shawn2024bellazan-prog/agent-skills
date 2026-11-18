---
name: sync
description: "Reconcile DotAgents-managed project projections offline. Use for the DotAgents sync operation in an explicitly scoped project."
---

# DotAgents sync

## Purpose
Reconcile DotAgents-managed project projections offline.

## When to Use
Invoke the existing provider for this exact operation.

## When Not to Use
Do not change global state, private PMCR-O state, or use this skill for another verb.

## Inputs
Existing project root and agents.toml. Review intended prune/reconcile changes.

## Deliverables
Return the real provider outcome and exit status or BLOCKED.

## Workflow
Resolve the project root and authorization. Mutating; require explicit authorization before invocation. Read [the contract](references/contract.md), then run `python scripts/run.py --project /absolute/project`. Do not manually reproduce the provider action.

## Validation
Verify provider exit status and relevant project declaration or projection; use doctor after mutations.

## Pitfalls
Do not assume CLI availability, reuse stale authorization, expose secrets or imply a running runtime.

## Resources
- [Operation contract](references/contract.md)
- [Example](assets/request.json)
