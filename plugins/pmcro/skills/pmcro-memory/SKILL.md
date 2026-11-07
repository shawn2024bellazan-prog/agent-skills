---
name: pmcro-memory
description: "Design or initialize PMCR-O memory with explicit agent, project, cycle and runtime scopes. Use when assigning ownership or storage for durable context and evidence."
---

# PMCR-O memory

## Purpose and profile

Primary profile: Knowledge + Procedural. Prevent unrelated memory and evidence from collapsing into a single writable store.

## Marketplace alignment

- `agent-memory`: durable notes owned by an individual agent identity.
- `projects`: project-scoped automatic context, distinct from subagent memory.
- `agents`: identity and role configuration controlling permitted memory access.

## Scopes

| Scope | Purpose | Mutability |
| --- | --- | --- |
| Agent memory | Durable notes for one agent identity | Agent or authorized memory service |
| Project memory | Reusable context within project boundary | Project memory policy |
| Cycle context | Working context for one cycle | Cycle scope; archive by policy |
| Runtime/evidence | Invocations, handoffs, results, Trails, receipts and artifacts | Runtime/evidence services; append/supersede |
| Authored genome | Definitions of agents, skills, policies, workflows and schemas | Version-controlled canonical source |

## Subagent route and marketplace capability

- PMCR-O logical subagent address: `@ORCHESTRATOR /pmcro:subagent:agent-memory`.
- Existing marketplace skill: `agent-memory/manage-agent-memory`.
- The route identifies the PMCR-O subagent identity; the skill supplies memory-management guidance. A host must register and resolve the subagent route before it can be executed. Do not treat the skill's presence as proof that an independent subagent is running.
- Keep main-session project memory routed to `projects/manage-auto-memory`, not the agent-memory subagent.

## Workflow

1. Identify owner and sharing scope.
2. Distinguish agent memory from project auto memory.
3. Keep credentials and unnecessary sensitive data out of shared memory.
4. Store cycle evidence in the runtime/evidence plane, not informal memory narratives.
5. Record provenance and freshness for changing facts.
6. Require an authorized memory operation for mutation; preserve sealed evidence.

## Validation

- [ ] Scope and owner are explicit.
- [ ] Agent and project memory are distinct.
- [ ] Trails and receipts are not treated as ordinary mutable memory.
- [ ] Shared memory contains no credentials.
- [ ] Provenance and history are preserved.
