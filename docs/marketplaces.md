# Marketplace manifests

This repository publishes the same twelve marketplace plugins through multiple host marketplace catalogs: ten directory-reference plugins and the separate `skill-creator` authoring plugin. The catalogs are maintained as synchronized copies; there is currently no manifest generator, so update and validate all copies together.

## Catalog locations

- .claude-plugin/marketplace.json — AGENTS marketplace.
- .cursor-plugin/marketplace.json — Cursor marketplace.
- .agents/plugins/marketplace.json — Codex marketplace.
- .github/plugin/marketplace.json — GitHub-hosted plugin catalog.

Each catalog must contain the same plugin names and relative source paths. Host-specific metadata may differ where a host requires a different schema, but a plugin must never be advertised by a catalog unless its source directory exists.

## Current plugin set

The marketplace contains ten directory-reference plugins: agent-config, agent-memory, agents, commands, output-styles, projects, rules, skills, themes, and workflows. It also contains the separate `skill-creator` authoring plugin and the cross-cutting `pmcro` architecture integration plugin.

Each plugin lives under plugins/<name>/ and includes a root plugin.json, version.json, Claude and Codex compatibility metadata, and a skills/ directory. The skill entrypoint is skills/<skill-name>/SKILL.md; supporting material belongs in that skill's references/, assets/, or scripts/ directories as appropriate.

## Updating catalogs

When adding, renaming, or removing a plugin:

1. Update all four marketplace catalogs.
2. Verify every catalog's plugin names and source values match.
3. Verify each referenced directory exists and contains its expected plugin metadata and skill entrypoint.
4. Update the root README and relevant plugin documentation.
5. Run JSON parsing and marketplace consistency checks before committing.

The upstream .NET skills repository supplied the original packaging convention only. Its .NET plugin collection is not part of this marketplace. See PROVENANCE for the exact source commit and retrieval details.

## PMCR-O integration note

The `pmcro` plugin provides portable invocation, lifecycle, host/genome, memory, marketplace-alignment and governance contracts. It does not ship a runtime implementation. Its deployment `.agents/` and `.pmcro/` paths refer to the target host/project; this repository's root `.agents/` remains reserved for Codex marketplace metadata and maintenance assets. The colon-form `/pmcro:<domain>:<action>` is only callable when an active host explicitly maps it; otherwise use an existing marketplace skill name or report `CAPABILITY_MISSING`.
