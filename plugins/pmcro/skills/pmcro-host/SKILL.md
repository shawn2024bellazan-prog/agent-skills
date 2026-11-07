---
name: pmcro-host
description: "Resolve PMCR-O host compatibility and distinguish the portable deployment .agents/ genome contract from host adapters and .pmcro/ runtime evidence. Use during bootstrap or host integration."
---

# PMCR-O host and genome contract

## Purpose and profile

Primary profile: Knowledge + Procedural + Schema/Contract. Separate authored source, host implementation and runtime state.

## Layers

| Layer | Responsibility | Contents |
| --- | --- | --- |
| `.agents/` in a PMCR-O deployment | Portable authored genome/source of truth | Agent definitions, skills, capabilities, policies, workflows, host initialization contract |
| `pmcro:host:init` | Bootstrap contract authored in that genome | Discover, load, resolve, invoke and validate the host |
| Host adapter/runtime | Executes and enforces contracts | Native tools, MCP services, scripts, sessions, identity, authorization and persistence |
| `.pmcro/` | Runtime/evidence plane | Sessions, queues, handoffs, auth records, Trails, artifacts and receipts |

A manifest or skill describes a capability; only an installed adapter can execute it.

## Repository-specific boundary

This repository reserves its own root `.agents/` for Codex marketplace metadata and maintenance assets. The PMCR-O deployment genome contract refers to a target deployment's `.agents/`, not this repository's directory. The PMCR-O plugin belongs under `plugins/pmcro/`.

## Host resolution

For each required capability, resolve the contract/version, concrete implementation, host compatibility, permissions, secret names (never values), network/side effects, invocation method, observable evidence, failure results and fallbacks. A platform listed in metadata is not proof of compatibility.

Distinguish discoverable, loaded, registered, authorized, invoked, executed, verified and sealed as separate states.

## Outcomes

Use `CAPABILITY_MISSING`, `UNSUPPORTED`, `FORBIDDEN`, `AUTHORIZATION_REQUIRED` and `UNVERIFIED` exactly where applicable.

## Validation

- [ ] Deployment genome path is unambiguous.
- [ ] Actual host adapter is callable and identified.
- [ ] Compatibility is evidenced by real host validation or an explicit unsupported result.
- [ ] Identity, scope and permissions are host-enforced.
- [ ] Runtime evidence is separate from authored genome.
- [ ] Repository-reserved paths remain untouched.
