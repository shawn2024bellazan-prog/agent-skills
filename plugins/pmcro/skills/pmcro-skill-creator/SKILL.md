---
name: pmcro-skill-creator
description: "Coordinate PMCR-O skill design and validation through skill-creator, including evidence-based Reflector handoffs without granting creation authority."
---

# PMCR-O Skill creation adapter

## Purpose and profile

Primary profile: Procedural + Knowledge + Validation. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-skill-creator`.
- Logical capability ID: `pmcro:skill-creator:create`.
- Logical protocol address: `/pmcro:skill-creator:create`.
- Native capability owner: `skill-creator` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Approved skill intent; target repository and host; skill name/description; source material; capability contract; acceptance criteria.

## Procedure

1. Resolve the exact bounded skill intent and target host conventions. For a Reflector handoff, preserve the three-level SeedIntent hierarchy as proposed, unexecuted input.
2. Discover the native `skill-creator` capability and its current templates, creation procedure, and validators.
3. Create the smallest useful skill package: clear frontmatter, focused SKILL.md, and only the references/assets/scripts actually required.
4. Preserve ownership, safety, and capability boundaries. A skill describes a reusable capability; it does not create an agent identity, runtime integration, permission grant, or command route.
5. Validate naming, frontmatter, resource links, procedure, host compatibility, and repository-specific tests. Report any validator that did not run.

## Ownership and boundaries

The native `skill-creator` plugin owns skill-authoring mechanics. Reflector may propose a SeedIntent but cannot execute its own proposal, change creator governance, or claim the resulting skill was installed.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] The intent is bounded and authorized; the native creator was used; the package is minimal and valid; unsupported host behavior and unrun tests are reported.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
