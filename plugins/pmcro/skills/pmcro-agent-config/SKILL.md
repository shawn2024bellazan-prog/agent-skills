---
name: pmcro-agent-config
description: "Coordinate PMCR-O discovery and authorized configuration of target-host agent settings, instruction roots, and integrations through the agent-config plugin."
---

# PMCR-O Agent configuration adapter

## Purpose and profile

Primary profile: Knowledge + Procedural + Schema/Contract. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-agent-config`.
- Logical capability ID: `pmcro:agent-config:inspect`.
- Logical protocol address: `/pmcro:agent-config:inspect`.
- Native capability owner: `agent-config` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Target host and project; configuration paths; requested settings; allowed read/write scope; host compatibility requirements.

## Procedure

1. Resolve the target host and configuration scope before reading or changing anything. Distinguish project `.claude/` settings from the deployment genome boundary.
2. Discover the native `agent-config` plugin capability and confirm its installed version, supported host, and exact entrypoint.
3. Inspect current configuration first. Summarize the proposed delta and identify settings that affect tools, permissions, identity, or external integrations.
4. For any mutation, require the relevant validated PlanFrame and current host-issued authorization. Apply only the authorized delta through the native plugin.
5. Verify the resulting state from the host and record the actual paths, changed values, result, and evidence references.

## Ownership and boundaries

The native `agent-config` plugin owns configuration semantics and implementation. This adapter does not treat repository `.agents/` marketplace metadata as the PMCR-O deployment genome, and configuration instructions do not enforce runtime security by themselves.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] The target host and paths are explicit; the native capability is present; current state was inspected; any write is authorized; the post-change state is verified.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
