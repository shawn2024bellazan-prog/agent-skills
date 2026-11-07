---
name: pmcro-marketplace
description: "Map PMCR-O capabilities and plugins to the existing Agent Skills marketplace without duplicating or redefining its categories. Use when packaging or reviewing PMCR-O marketplace integration."
---

# PMCR-O marketplace alignment

## Purpose and profile

Primary profile: Knowledge + Schema/Contract + Validation. Extend the existing marketplace taxonomy without replacing each category's documented role.

## Category crosswalk

| Existing category | PMCR-O alignment and adapter skill | Boundary |
| --- | --- | --- |
| `agent-config` | `pmcro:host`, [`pmcro-agent-config`](../pmcro-agent-config/SKILL.md) | Configuration is not runtime execution |
| `agent-memory` | `pmcro:memory`, [`pmcro-agent-memory`](../pmcro-agent-memory/SKILL.md) | Keep separate from project auto memory |
| `agents` | Five lifecycle role definitions, [`pmcro-agents`](../pmcro-agents/SKILL.md) | Agent identity differs from skill capability |
| `commands` | `pmcro:init`, [`pmcro-commands`](../pmcro-commands/SKILL.md) | Entry command is not orchestration runtime |
| `output-styles` | Structured invocation/result presentation, [`pmcro-output-styles`](../pmcro-output-styles/SKILL.md) | Format does not enforce authorization |
| `projects` | Project context and memory, [`pmcro-projects`](../pmcro-projects/SKILL.md) | Separate from agent memory and cycle evidence |
| `rules` | Governance and policy guidance, [`pmcro-rules`](../pmcro-rules/SKILL.md) | Guidance alone is not deterministic enforcement |
| `skill-creator` | PMCR-O capability/skill authoring, [`pmcro-skill-creator`](../pmcro-skill-creator/SKILL.md) | Reuse creator conventions; don't duplicate them |
| `skills` | Portable PMCR-O capability contracts, [`pmcro-skills`](../pmcro-skills/SKILL.md) | A skill is not necessarily executable integration |
| `themes` | Optional presentation preferences, [`pmcro-themes`](../pmcro-themes/SKILL.md) | Does not change lifecycle or governance |
| `workflows` | Bootstrap and lifecycle orchestration, [`pmcro-workflows`](../pmcro-workflows/SKILL.md) | Actual host dispatch must exist |

## Alignment requirements

Each PMCR-O capability declares a stable ID, primary/secondary category, responsibility and exclusions, exact invocation name, input/output contract, implementation requirements, supported hosts, authorization/evidence needs and validation criteria.

Mapping is many-to-many. Preserve category ownership. Each of the eleven existing plugin categories has a dedicated PMCR-O adapter skill named `pmcro-<plugin>`. These adapters discover and coordinate the native plugin; they do not copy, fork, or supersede its implementation. Skills package reusable capabilities; agents own accountability; plugins package capabilities for distribution; the marketplace catalogs packages; host adapters execute and enforce; PMCR-O governs lifecycle and evidence.

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
- [ ] Each of the eleven existing plugin categories has one linked PMCR-O adapter skill.
- [ ] Adapter skills preserve native plugin ownership and do not invent host routes.
- [ ] No category responsibility is silently replaced.
- [ ] All manifests, versions and four catalogs agree.
- [ ] Each source path and skill entrypoint exists.
