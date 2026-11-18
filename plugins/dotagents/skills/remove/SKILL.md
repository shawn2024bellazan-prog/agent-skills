---
name: remove
description: "Remove one explicitly selected DotAgents dependency or source. Use for the DotAgents remove operation in an explicitly scoped project."
---

# DotAgents remove

## Purpose
Remove one explicitly selected DotAgents dependency or source.

## When to Use
Invoke the existing provider for this exact operation.

## When Not to Use
Do not change global state, private PMCR-O state, or use this skill for another verb.

## Inputs
Exact name or source and reviewed removal impact.

## Deliverables
Return the real provider outcome and exit status or BLOCKED.

## Workflow
Resolve the project root and authorization. Mutating; require explicit --apply; do not remove unrelated dependencies. Read [the contract](references/contract.md), then run `python scripts/run.py --project /absolute/project skill-name --apply`. Do not manually reproduce the provider action.

## Validation
Verify provider exit status and relevant project declaration or projection; use doctor after mutations.

## Pitfalls
Do not assume CLI availability, reuse stale authorization, expose secrets or imply a running runtime.

## Resources
- [Operation contract](references/contract.md)
- [Example](assets/request.json)
