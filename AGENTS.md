# Repository instructions

This repository is a directory-reference and authoring marketplace. It contains ten independent plugins under plugins/, each documenting one part of the Claude Code project or global directory layout.

## Product scope

The marketplace documents Claude Code root files and the project/global .claude/ layouts: settings, rules, skills, commands, output styles, agents, workflows, subagent persistent memory, global themes, and per-project automatic memory. The repository's own .agents/ directory is reserved for Codex marketplace metadata and repository-maintenance assets.

Do not reintroduce the upstream .NET skill catalog as part of this product. The upstream repository is recorded in PROVENANCE because its plugin packaging convention was reused; its domain content was removed.

## Plugin structure

Each plugins/<name>/ directory is an independently installable plugin and should retain:

- plugin.json at the plugin root
- version.json declaring the plugin's major.minor release base and canonical path filters
- .claude-plugin/plugin.json for Claude compatibility
- .codex-plugin/plugin.json for Codex compatibility
- skills/<skill-name>/SKILL.md as the skill entrypoint
- Optional references/, assets/, and scripts/ for supporting resources

Keep each skill's entrypoint focused. Put detailed examples and supporting documentation in its references/ directory and link to those files from SKILL.md.

## Marketplace consistency

The four marketplace catalogs are .claude-plugin/marketplace.json, .cursor-plugin/marketplace.json, .agents/plugins/marketplace.json, and .github/plugin/marketplace.json.

There is no generator today. When changing the plugin set, update all four catalogs and verify that their plugin names and source paths agree with the actual directories. Do not advertise a missing plugin.

## Documentation quality

- Preserve the distinction between project-scoped and global configuration.
- Distinguish subagent memory from main-session project auto memory.
- Ground host behavior in relevant official documentation and flag version-sensitive behavior instead of presenting it as universal.
- Keep root and per-plugin READMEs aligned with the marketplace catalogs.
- Avoid machine-specific paths except where a path is explicitly part of source evidence or an example clearly labeled as such.

## Validation

Before committing marketplace changes:

1. Parse all marketplace and plugin JSON files.
2. Check all manifest source directories and skill entrypoints.
3. Check that the four marketplace catalogs expose the same plugin names and source paths.
4. Check every plugin's version.json and synchronized root/Claude/Codex manifest versions.
5. Run git diff --check.
6. Review git status and stage only files related to the requested change.

Do not modify unrelated generated test fixtures or other pre-existing working-tree changes.
