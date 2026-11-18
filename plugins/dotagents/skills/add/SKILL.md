---
name: add
description: "Add a named dependency or explicitly all dependencies from a source. Use for the DotAgents add operation in an explicitly scoped project."
---

# DotAgents add

## Purpose
Add a named dependency or explicitly all dependencies from a source.

## When to Use
Invoke the existing provider for this exact operation.

## When Not to Use
Do not change global state, private PMCR-O state, or use this skill for another verb.

## Inputs
Source, one or more names or --all, optional Git ref. Local paths must stay inside project.

## Deliverables
Return the real provider outcome and exit status or BLOCKED.

## Workflow
Resolve the project root and authorization. Mutating; require explicit --apply; never grant trust implicitly. Read [the contract](references/contract.md), then run `python scripts/run.py --project /absolute/project owner/repo skill-name --ref v1 --apply`. Do not manually reproduce the provider action.

## Validation
Verify provider exit status and relevant project declaration or projection; use doctor after mutations.

## Pitfalls
Do not assume CLI availability, reuse stale authorization, expose secrets or imply a running runtime.

## Resources
- [Operation contract](references/contract.md)
- [Example](assets/request.json)
