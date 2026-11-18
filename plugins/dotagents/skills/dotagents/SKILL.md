---
name: dotagents
description: Route explicitly scoped DotAgents commands to the corresponding micro-skill and installed CLI. Use for initialization, synchronization, dependency and MCP declarations, trust management, and health checks.
---

# DotAgents

## Purpose
Resolve one real DotAgents capability for a specific project.

## When to Use
Manage portable agent dependencies, projections, MCP declarations or trust in an authorized project.

## When Not to Use
Do not create projects, write PMCR-O memory, install the CLI, change global configuration or invent unsupported commands.

## Inputs
Explicit project root, exact operation, operation arguments, and mutation authorization.

## Deliverables
Actual provider output and exit status or BLOCKED.

## Workflow
1. Discover the installed CLI and read [the contract](references/contract.md).
2. Resolve the bare-verb micro-skill and follow its instructions. Use the shared scripts/dotagents.py adapter, never an arbitrary shell command.
3. Confirm the exact result and avoid disclosing private runtime state.

## Validation
Run scripts/test_dotagents.py; verify the provider's real exit status. Do not report installation or activation without evidence.

## Pitfalls
DotAgents scope defaults to global without an explicit flag; the adapter always selects project scope. New project bindings use this canonical script; existing pins remain unchanged.

## Resources
- [Provider contract](references/contract.md)
- [Request example](assets/request.json)
