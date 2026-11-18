---
name: init
description: "Initialize portable project configuration for explicitly selected AI hosts. Use for the DotAgents init operation in an explicitly scoped project."
---

# DotAgents init

## Purpose
Initialize portable project configuration for explicitly selected AI hosts.

## When to Use
Invoke the existing provider for this exact operation.

## When Not to Use
Do not change global state, private PMCR-O state, or use this skill for another verb.

## Inputs
Existing project root and explicit host list. Do not replace existing agents.toml.

## Deliverables
Return the real provider outcome and exit status or BLOCKED.

## Workflow
Resolve the project root and authorization. Mutating; require explicit authorization before invocation. Read [the contract](references/contract.md), then run `python scripts/run.py --project /absolute/project --agents claude,codex`. Do not manually reproduce the provider action.

## Validation
Verify provider exit status and relevant project declaration or projection; use doctor after mutations.

## Pitfalls
Do not assume CLI availability, reuse stale authorization, expose secrets or imply a running runtime.

## Resources
- [Operation contract](references/contract.md)
- [Example](assets/request.json)
