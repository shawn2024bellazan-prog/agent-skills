---
name: pmcro-projects
description: "Coordinate PMCR-O project-context retrieval through projects while keeping project auto memory distinct from agent memory and cycle evidence."
---

# PMCR-O Project context and memory adapter

## Purpose and profile

Primary profile: Knowledge + Retrieval + Procedural. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-projects`.
- Logical capability ID: `pmcro:projects:context`.
- Logical protocol address: `/pmcro:projects:context`.
- Native capability owner: `projects` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Project/repository identity; project memory location; requested context; read/write intent; relevant privacy and retention boundaries.

## Procedure

1. Resolve the exact project identity and its memory namespace before accessing context.
2. Discover the native `projects` plugin capability and confirm the host's actual auto-memory location and read/write behavior.
3. Retrieve relevant project facts such as architecture, build commands, and prior debugging findings; treat memory as fallible context that may need current verification.
4. For updates, preserve project-specific knowledge and require authorization for the target memory mutation.
5. Keep user/global memory, subagent memory, cycle state, and immutable PMCR-O Trail evidence in their distinct stores.

## Ownership and boundaries

The native `projects` plugin owns project auto-memory behavior. Project memory is not the same as `agent-memory`, and neither replaces `.pmcro/` runtime/evidence records.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] Project identity and namespace are correct; relevant context is current enough for the task; any write is authorized; memory planes remain separate.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
