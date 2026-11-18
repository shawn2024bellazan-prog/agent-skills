---
name: project-lifecycle
description: Register and initialize an authorized local Project Agent workspace, connect the verified DotAgents configuration adapter, resolve its private PMCR-O runtime scope, and manage registry lifecycle transitions. Use for /projects:project-lifecycle; delegate AI host project creation to the existing project skill.
---

# Project lifecycle

## Purpose
Manage one registered project and its private state without creating a second project system.

## When to Use
Register an existing workspace, initialize its portable configuration, check readiness, or perform a bounded registry lifecycle transition.

## When Not to Use
Do not create a Claude or ChatGPT project, start a model/runtime, delete a project, migrate legacy memory, or publish private state. Route host project creation through `/project:project:project`.

## Inputs
Use the exact authorized project ID, absolute existing workspace root, and action. State defaults to `~/.pmcro/projects/`; an explicit absolute `--pmcro-root` override is for authorized isolation/testing only. Mutations require `--apply`.

## Deliverables
Return the actual JSON receipt, state, and evidence. Registering a project does not install or activate any plugin or host.

## Workflow
1. Resolve `@project-agent → projects → project-lifecycle → /projects:project-lifecycle`, then emit the action and inputs.
2. Read [the registry contract](references/contract.md). Inspect existing project instructions.
3. Invoke `python3 scripts/project_lifecycle.py ACTION --project-id ID --project-root ABSOLUTE_PATH [--apply]`. Use Python 3 on the selected host. Do not infer authorization from an emitted command.
4. For initialization, reuse the bundled PMCR-O scaffold. When DotAgents is explicitly authorized, resolve the installed `agent-config/configure-agent/scripts/dotagents.py` adapter from a trusted release; pass `--dotagents-adapter ABSOLUTE_PATH --dotagents-sha256 SHA256` and, for a new `agents.toml`, `--agents claude,codex` (or the authorized host list). Invoke the adapter; do not reproduce its functionality. Require successful doctor before committing the state transition.
5. Verify a read-back using `status`, then resolve private runtime scope with the read-only `runtime` action. It verifies the registered path, initialization, private resource directories and any bound provider, returning relative resource handles without reading private memory. Return BLOCKED if any required operation is unavailable.

## Validation
Run `python3 scripts/test_project_lifecycle.py` against disposable directories. Verify the real project root and record, portable layout, private memory index and event history separately. For a real DotAgents smoke test, provide the verified adapter and installed CLI in a disposable project; test `runtime` after initialization.

## Pitfalls
Project IDs are not display names. Do not overwrite existing settings or memory, move existing .pmcro data, clear a lock automatically, or claim registry activation starts a running agent. Treat Windows ACLs as inherited and unverified.

## Resources
- [Registry contract](references/contract.md)
- [Request examples](assets/request.json)
- [Local-only scaffold](assets/directory-template.json)
