---
name: mcp
description: "Manage project MCP declarations with DotAgents. Use for the DotAgents mcp operation in an explicitly scoped project."
---

# DotAgents mcp

## Purpose
Manage project MCP declarations with DotAgents.

## When to Use
Invoke the existing provider for this exact operation.

## When Not to Use
Do not change global state, private PMCR-O state, or use this skill for another verb.

## Inputs
Subcommand list/add/remove, exact server name and transport for add; environment variable names only.

## Deliverables
Return the real provider outcome and exit status or BLOCKED.

## Workflow
Resolve the project root and authorization. List is read-only; add/remove require --apply. MCP connectivity is not tested by declarations. Read [the contract](references/contract.md), then run `python scripts/run.py --project /absolute/project list`. Do not manually reproduce the provider action.

## Validation
Verify provider exit status and relevant project declaration or projection; use doctor after mutations.

## Pitfalls
Do not assume CLI availability, reuse stale authorization, expose secrets or imply a running runtime.

## Resources
- [Operation contract](references/contract.md)
- [Example](assets/request.json)
