---
name: trust
description: "Manage exact authorized project trusted sources. Use for the DotAgents trust operation in an explicitly scoped project."
---

# DotAgents trust

## Purpose
Manage exact authorized project trusted sources.

## When to Use
Invoke the existing provider for this exact operation.

## When Not to Use
Do not change global state, private PMCR-O state, or use this skill for another verb.

## Inputs
Subcommand list/add/remove and exact org, repo or domain when mutating.

## Deliverables
Return the real provider outcome and exit status or BLOCKED.

## Workflow
Resolve the project root and authorization. List is read-only; mutations require explicit --apply. Never grant wildcard trust. Read [the contract](references/contract.md), then run `python scripts/run.py --project /absolute/project list --json`. Do not manually reproduce the provider action.

## Validation
Verify provider exit status and relevant project declaration or projection; use doctor after mutations.

## Pitfalls
Do not assume CLI availability, reuse stale authorization, expose secrets or imply a running runtime.

## Resources
- [Operation contract](references/contract.md)
- [Example](assets/request.json)
