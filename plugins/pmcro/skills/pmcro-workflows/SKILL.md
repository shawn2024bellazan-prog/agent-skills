---
name: pmcro-workflows
description: "Coordinate PMCR-O multi-step workflow discovery and execution through workflows while preserving authorized sequencing, bounded loops, and evidence."
---

# PMCR-O Workflow orchestration adapter

## Purpose and profile

Primary profile: Orchestration + Procedural + Validation. This is the PMCR-O coordination adapter for the existing marketplace plugin, not a replacement implementation.

## Capability identity

- PMCR-O marketplace skill: `pmcro-workflows`.
- Logical capability ID: `pmcro:workflows:execute`.
- Logical protocol address: `/pmcro:workflows:execute`.
- Native capability owner: `workflows` plugin.

Invoke this skill by its exact installed marketplace identifier. The colon-form address is callable only if the active host has registered that exact mapping. Do not describe the logical address as an installed command without host evidence.

## Inputs

Workflow goal; workflow identifier/script; task dependencies; lifecycle roles; authorization; retry/loop policy; required evidence outputs.

## Procedure

1. Resolve the exact workflow and inspect its steps, side effects, dependencies, and subagent/tool calls before execution.
2. Discover the native `workflows` plugin and confirm the host provides a real workflow runtime.
3. Build or validate a PlanFrame for the requested work. Confirm each mutation is within scope and Maker has a current host-issued grant.
4. Execute only through the host runtime. Dispatch lifecycle agents through real isolated contexts; keep Checker read-only and independent.
5. Apply configured bounds such as EC-009 MaxLoops=3, log actions before acting when configured, and stop on missing capability, authorization, or evidence writer.
6. Verify the workflow's actual outputs and preserve invocation, action, result, artifact, and deviation evidence.

## Ownership and boundaries

The native `workflows` plugin owns workflow files and execution conventions. A workflow script on disk is not proof that a runtime exists or that its subagents/tools were actually invoked.

For side-effecting operations, apply PMCR-O governance: log before acting where configured, verify the target before mutation, require a validated PlanFrame and current host-issued authorization for Maker project execution, and record actual outcomes. Report missing integrations or insufficient evidence explicitly.

## Validation

- [ ] Workflow implementation and runtime are available; plan and grant are valid; role and retry boundaries hold; each result is evidenced; Checker is independent.
- [ ] Exact native owner and capability identifier are resolved.
- [ ] Host dispatch is real and supported, or the capability is reported as unavailable.
- [ ] No permission, route, agent context, or execution result is inferred from this skill's presence.
