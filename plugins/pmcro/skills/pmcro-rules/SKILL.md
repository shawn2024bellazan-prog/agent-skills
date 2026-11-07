---
name: pmcro-rules
description: "Coordinate PMCR-O rule discovery and policy evaluation through rules, distinguishing model-readable guidance from host-enforced controls."
---

# PMCR-O Rules and policy evaluation adapter

## Purpose and profile

Primary profile: Knowledge + Validation + Schema/Contract. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-rules`.
- Logical capability ID: `pmcro:rules:evaluate`.
- Logical protocol address: `/pmcro:rules:evaluate`.
- Native capability owner: `rules` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Action or decision under review; target paths/resources; applicable rule scope; host permissions/hooks; expected decision and evidence.

## Procedure

1. Identify the proposed action, affected resources, and any path-scoped or topic-scoped rules that apply.
2. Discover the native `rules` plugin and load only the relevant rule instructions.
3. Evaluate the action against PMCR-O constraints, the validated PlanFrame, and the current authorization scope.
4. Determine whether the control is merely model-readable guidance or is enforced by host permissions, hooks, sandboxing, or policy services. Do not equate the two.
5. Return the applicable constraints, conflicts, required approval, and evidence. Stop when a required host-enforced control is missing.

## Ownership and boundaries

The native `rules` plugin owns reusable rule files. Rules read by a model guide behavior but do not guarantee enforcement; only actual host controls can enforce permissions and prevent operations.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] Relevant rules are identified; guidance/enforcement distinction is explicit; authorization and host policy are checked; unresolved conflicts are surfaced.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
