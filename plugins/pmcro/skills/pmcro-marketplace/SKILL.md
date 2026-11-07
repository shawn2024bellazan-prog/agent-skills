---
name: pmcro-marketplace
description: "Map PMCR-O capabilities and plugins to the existing Agent Skills marketplace without duplicating or redefining its categories. Use when packaging or reviewing PMCR-O marketplace integration."
---

# PMCR-O marketplace alignment

## Purpose and profile

Primary profile: Knowledge + Schema/Contract + Validation. Extend the existing marketplace taxonomy without replacing each category's documented role.

## Category crosswalk

| Existing category | PMCR-O alignment | Boundary |
| --- | --- | --- |
| `agent-config` | `pmcro:host` configuration and adapter discovery | Configuration is not runtime execution |
| `agent-memory` | `pmcro:memory` agent-scoped memory | Keep separate from project auto memory |
| `agents` | Five lifecycle role definitions and identity contracts | Agent identity differs from skill capability |
| `commands` | `pmcro:init` and invocation entrypoints | Entry command is not orchestration runtime |
| `output-styles` | Structured invocation/result presentation | Format does not enforce authorization |
| `projects` | Project context and memory | Separate from agent memory and cycle evidence |
| `rules` | Governance and policy guidance | Guidance alone is not deterministic enforcement |
| `skill-creator` | PMCR-O capability/skill authoring | Reuse creator conventions; don't duplicate them |
| `skills` | Portable PMCR-O capability contracts | A skill is not necessarily executable integration |
| `themes` | Optional presentation preferences | Does not change lifecycle or governance |
| `workflows` | Bootstrap and lifecycle orchestration | Actual host dispatch must exist |

## Alignment requirements

Each PMCR-O capability declares a stable ID, primary/secondary category, responsibility and exclusions, exact invocation name, input/output contract, implementation requirements, supported hosts, authorization/evidence needs and validation criteria.

Mapping is many-to-many. Preserve category ownership. Skills package reusable capabilities; agents own accountability; plugins package capabilities for distribution; the marketplace catalogs packages; host adapters execute and enforce; PMCR-O governs lifecycle and evidence.

## Repository packaging

Follow `plugins/<name>/` with root `plugin.json`, `version.json`, synchronized Claude/Codex metadata, focused `skills/<skill-name>/SKILL.md`, README and links. Sync all four catalogs:
- `.claude-plugin/marketplace.json`
- `.cursor-plugin/marketplace.json`
- `.agents/plugins/marketplace.json`
- `.github/plugin/marketplace.json`

The repository root `.agents/` is reserved for Codex catalog/maintenance content. Do not put the PMCR-O deployment genome or runtime state there.

## Validation

- [ ] All eleven existing categories have a documented relationship.
- [ ] Each PMCR-O capability declares primary/secondary alignment.
- [ ] No category responsibility is silently replaced.
- [ ] All manifests, versions and four catalogs agree.
- [ ] Each source path and skill entrypoint exists.
