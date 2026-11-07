---
name: pmcro-init
description: "Bootstrap PMCR-O foundational capabilities and evaluate host readiness using explicit capability and agent handoffs. Use when initializing a PMCR-O deployment or checking bootstrap dependencies; initialization does not authorize project execution."
---

# PMCR-O initialization

## Purpose and profile

Primary profile: Procedural. Secondary facets: Schema/Contract + Validation.

Coordinate bootstrap of PMCR-O itself. `pmcro:init` is the root initialization workflow, not a sixth lifecycle agent and not a replacement for the host runtime.

## Invocation identity

- Marketplace skill identifier: `pmcro-init`.
- Logical bootstrap operation: `pmcro:init`.
- Use `/pmcro:init` only if the active host has registered that exact mapping. Otherwise invoke the installed `pmcro-init` skill by its actual marketplace name.

## Marketplace alignment

- `commands`: user- or agent-invocable bootstrap entrypoint.
- `workflows`: multi-step orchestration across capabilities and agents.
- `agent-config`: target-host configuration and compatibility discovery.

## Inputs

- Target deployment and host identity.
- Canonical genome location (normally `.agents/` in the target deployment).
- Runtime/evidence location (normally `.pmcro/`).
- Capability registry and concrete implementation references.
- Authorization available for bootstrap scope only.

## Workflow

1. Start with the structured envelope in `pmcro-invocation`.
2. Resolve the host adapter and discover the target deployment's authored genome.
3. Resolve foundational capabilities: memory, marketplace, identity, governance, protocol, runtime, Trails, and lifecycle contracts. Record unsupported or missing integrations explicitly.
4. Establish runtime services only through the host's real implementation. Keep authored definitions in `.agents/` and mutable state/evidence in `.pmcro/`.
5. Initialize Orchestrator, Planner, Maker, Checker, and Reflector contexts only after their role definitions, identity boundaries, and host dispatch requirements are resolved.
6. Verify readiness against actual host responses. Do not infer success from files merely existing or instructions being loaded.
7. Return `READY`, `PARTIAL`, or `BLOCKED`, with unresolved dependencies and evidence references.

## Capability dispatch

Bootstrap may call foundational `pmcro:*` capabilities. Each invocation has its own task, inputs, implementation boundary, and expected result. Capability initialization does not itself make every capability executable.

## Agent dispatch

Use `@ORCHESTRATOR` to coordinate bootstrap. Delegate specialist planning or verification only when a real host can create the required role-isolated contexts. Planner plans; Maker does not perform project work without a separately authorized PlanFrame; Checker is independent and read-only; Reflector works from recorded evidence.

## Authorization boundary

Initialization authorization is limited to bootstrap operations explicitly in scope. It does not grant Maker authority to mutate a project, call external services, or deploy anything. Require a separately approved PlanFrame for phase execution.

## Validation

- [ ] Genome discovery resolves to a target deployment source, not this repository's reserved `.agents/` marketplace directory.
- [ ] Host implementation resolution is based on callable integrations, not documentation alone.
- [ ] Foundational capability outcomes are individually recorded.
- [ ] Agent role identities and isolation are confirmed by the host.
- [ ] Runtime and evidence services are available and tested.
- [ ] No phase execution is implicitly authorized.
- [ ] Readiness and missing dependencies are explicit.

## Expected result

Return `PMCRО_INIT_RESULT` with readiness, resolved capabilities, agent-context status, unresolved requirements, and evidence references. Use `CAPABILITY_MISSING`, `UNSUPPORTED`, `FORBIDDEN`, `AUTHORIZATION_REQUIRED`, or `UNVERIFIED` where applicable instead of reporting success.
