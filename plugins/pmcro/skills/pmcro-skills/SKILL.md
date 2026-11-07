---
name: pmcro-skills
description: "Coordinate PMCR-O discovery and invocation of installed skills through the skills plugin, preserving exact identifiers and capability boundaries."
---

# PMCR-O Skill discovery and invocation adapter

## Purpose and profile

Primary profile: Retrieval + Orchestration + Schema/Contract. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-skills`.
- Logical capability ID: `pmcro:skills:discover`.
- Logical protocol address: `/pmcro:skills:discover`.
- Native capability owner: `skills` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

User goal; relevant plugin/skill domain; target host; available marketplace inventory; expected capability and output.

## Procedure

1. Translate the goal into a capability need and search the installed marketplace inventory using names and descriptions.
2. Discover the native `skills` plugin and resolve the exact skill directory/identifier and its owner.
3. Read the skill entrypoint and only the supporting resources needed for the task. Check supported host and invocation constraints.
4. Invoke the exact installed skill through the host's supported mechanism. Do not substitute an imagined `/pmcro:<domain>:<action>` route for a missing mapping.
5. Return the skill identity, owner, actual dispatch outcome, and any missing implementation or authorization requirement.

## Ownership and boundaries

The native `skills` plugin owns reusable skill discovery and invocation conventions. A skill is not an agent, tool, MCP server, workflow runtime, or proof of execution.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] The exact skill is installed and resolvable; owner and supported host are known; only necessary resources are loaded; dispatch is evidenced.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
