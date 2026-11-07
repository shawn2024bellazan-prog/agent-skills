---
name: pmcro-agents
description: "Coordinate lifecycle-agent discovery and real subagent dispatch through the agents plugin while preserving role identity, isolation, and least privilege."
---

# PMCR-O Agent identity and dispatch adapter

## Purpose and profile

Primary profile: Orchestration + Schema/Contract + Validation. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-agents`.
- Logical capability ID: `pmcro:agents:dispatch`.
- Logical protocol address: `/pmcro:agents:dispatch`.
- Native capability owner: `agents` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Agent ID and role; task and context; allowed tools; model/host constraints; expected result; read/write boundary.

## Procedure

1. Resolve the intended agent definition and its role, instructions, tool allowlist, and context boundary.
2. Discover the native `agents` plugin capability and confirm that the host can create or address the required isolated context.
3. For lifecycle work, enforce the PMCR-O role boundaries: Planner plans, Maker executes only authorized PlanFrame scope, Checker is independent and read-only, Reflector reasons from recorded evidence.
4. Dispatch through the actual host subagent mechanism. A textual `@AGENT` label or `/pmcro:subagent:<agent-id>` address is not proof that a context was created or invoked.
5. Capture host-issued invocation identity, scope, returned result, artifacts, and any failure or unsupported boundary.

## Ownership and boundaries

The native `agents` plugin owns agent definitions and host-facing subagent behavior. This adapter cannot fabricate isolated contexts, tool permissions, or agent receipts; Checker must not receive Maker write tools.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] Agent identity is resolvable; the host enforces context and tool boundaries; the correct role is used; dispatch and result are evidenced.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
