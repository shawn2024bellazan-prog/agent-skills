---
name: pmcro-output-styles
description: "Coordinate PMCR-O response and artifact presentation through output-styles while keeping formatting separate from governance and execution."
---

# PMCR-O Output styles adapter

## Purpose and profile

Primary profile: Conversational + Procedural. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-output-styles`.
- Logical capability ID: `pmcro:output-styles:format`.
- Logical protocol address: `/pmcro:output-styles:format`.
- Native capability owner: `output-styles` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Audience; output purpose; required structure; target host style identifier; content and evidence that must be preserved.

## Procedure

1. Identify the presentation need and the exact output-style identifier available in the target host.
2. Discover the native `output-styles` plugin and inspect the selected style's scope and effect.
3. Apply the style only to presentation. Preserve required PMCR-O message fields, exact outcome vocabulary, source citations, and evidence references.
4. Do not let style instructions change role boundaries, authorization, tool permissions, or evidence requirements.
5. Return the artifact in the requested format and identify the style used when relevant.

## Ownership and boundaries

The native `output-styles` plugin owns style definitions and loading. Output formatting is not a policy engine, validator, identity boundary, or authorization mechanism.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] The style exists and is supported; required content and evidence are preserved; no governance rule was inferred from formatting.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
