---
name: pmcro-commands
description: "Coordinate PMCR-O entrypoint discovery, command validation, and host route mapping through the commands plugin without inventing executable slash commands."
---

# PMCR-O Command and route integration adapter

## Purpose and profile

Primary profile: Schema/Contract + Procedural + Validation. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-commands`.
- Logical capability ID: `pmcro:commands:route`.
- Logical protocol address: `/pmcro:commands:route`.
- Native capability owner: `commands` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Requested logical address; target host; native command or skill identifier; arguments; expected behavior; supported command format.

## Procedure

1. Classify the requested entrypoint as a marketplace skill, native command, subagent route, or PMCR-O logical capability address.
2. Discover the native `commands` plugin and inspect the host's supported command/skill loading rules.
3. Prefer the installed skill identifier when the host already exposes skills as invocable commands. Add a separate command adapter only when the host requires one.
4. Register or edit a route only through a real host/repository integration and only within authorized scope. Validate collisions, argument handling, and dispatch target.
5. Test the entrypoint through the target host and report whether it is registered, merely documented, or unavailable.

## Ownership and boundaries

The native `commands` plugin owns command file conventions. `/pmcro:<domain>:<action>` is a logical protocol address until an active host adapter registers the exact mapping; slash-shaped text alone creates no route.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] Entrypoint type is identified; exact target exists; the host mapping is verified; name collisions and arguments are checked; no unregistered route is described as callable.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
