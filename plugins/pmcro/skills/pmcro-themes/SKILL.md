---
name: pmcro-themes
description: "Coordinate PMCR-O visual theme discovery and authorized selection through themes without allowing presentation settings to alter operational policy."
---

# PMCR-O Themes and presentation preferences adapter

## Purpose and profile

Primary profile: Knowledge + Procedural. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-themes`.
- Logical capability ID: `pmcro:themes:apply`.
- Logical protocol address: `/pmcro:themes:apply`.
- Native capability owner: `themes` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Target host; requested theme name or visual preference; theme file location; scope (user/global/project); desired presentation change.

## Procedure

1. Resolve whether the request concerns a theme (color tokens and visual appearance) rather than an output style or governance policy.
2. Discover the native `themes` plugin and inspect the available theme definitions and supported host behavior.
3. Select an existing theme or prepare a focused theme definition using the host's supported schema.
4. Apply or write the theme only through a real host integration and within the requested scope; preserve current settings outside the authorized delta.
5. Verify the actual selected theme or resulting theme file and report unsupported hosts or failed changes.

## Ownership and boundaries

The native `themes` plugin owns theme formats and selection behavior. Themes change presentation only; they do not change model behavior, authorization, role identity, or security controls.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] The requested feature is genuinely a theme; schema and host support are confirmed; scope is respected; result is verified.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
