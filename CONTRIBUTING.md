# Contributing

Thanks for helping improve the Agent Skills directory-reference marketplace.

This repository documents and packages reusable skills for understanding and authoring the AGENTS project and global directory layout. Contributions should improve the accuracy, clarity, or practical usefulness of that reference material.

The user-facing reference plugins document AGENTS's project `.claude/` directory and global `~/.claude/` directory, plus root files such as `CLAUDE.md`, `.mcp.json`, and `.worktreeinclude`. The repository's own `.agents/` folder is separate and contains Codex marketplace metadata and repository-maintenance assets.

## Repository layout

    .agents/
      rules/                       Repository authoring guidance
      skills/                      Skills used to maintain this repository
    .claude-plugin/
      marketplace.json             AGENTS marketplace
    .cursor-plugin/
      marketplace.json             Cursor marketplace
    .agents/plugins/
      marketplace.json             Codex marketplace
    .github/plugin/
      marketplace.json             GitHub-hosted plugin catalog
    plugins/
      <plugin-name>/
        plugin.json
        version.json
        .claude-plugin/plugin.json
        .codex-plugin/plugin.json
        README.md
        skills/
          <skill-name>/
            SKILL.md
            references/
            assets/
            scripts/

## Adding or changing a plugin

Each top-level directory in plugins/ is one independently installable reference plugin. A plugin should document one coherent part of the directory layout.

When adding a plugin:

1. Create plugins/<plugin-name>/ with root and host-specific plugin metadata.
2. Add at least one skill under skills/<skill-name>/SKILL.md.
3. Put detailed examples and supporting material in references/; use assets/ and scripts/ only when they materially support the skill.
4. Add a concise plugin README explaining its scope and the skill it contains.
5. Add the plugin to all four marketplace catalogs: .claude-plugin/marketplace.json, .cursor-plugin/marketplace.json, .agents/plugins/marketplace.json, and .github/plugin/marketplace.json.
6. Update the root README and docs/marketplaces.md.
7. Verify every catalog entry points to an existing plugin and that all four catalogs have matching plugin names and source paths.

When removing or renaming a plugin, update all four catalogs and every documentation link in the same change. Do not leave stale entries pointing to deleted directories.

## Writing skills

A skill should state what outcome it produces and when it should be used; explain relevant directory or file conventions; distinguish project-scoped and global-scoped behavior; identify version- or host-specific behavior where it matters; and provide concrete examples and verification steps.

Keep SKILL.md focused; move lengthy details into linked reference files. Do not invent product behavior. Prefer official documentation and the repository's documented source material. If a behavior is uncertain or version-dependent, say so.

## Plugin versioning

Every plugin has a version.json file declaring its major.minor release base and the canonical
path filters used by the repository's versioning tool. Keep the root, Claude, and Codex
plugin.json version fields synchronized.

Do not hand-edit the version field in plugin.json or either host manifest. For same-repository
pull requests, maintainers can comment /version-bump to calculate and stamp the post-merge
version. The weekly version-sync workflow is the backstop for changes that were not stamped
during review. When deliberately starting a new release line, update only the version base in
version.json and follow the versioning workflow.

## Validation checklist

Before opening or merging a change:

- Parse all changed JSON files.
- Confirm all four marketplace manifests contain the same plugin names and source paths.
- Confirm each manifest source exists and each plugin has its metadata and skill entrypoint.
- Check internal Markdown links where practical.
- Run git diff --check.
- Review the final diff and ensure unrelated user changes are not staged.

## Provenance

The upstream dotnet/skills repository supplied the plugin packaging convention used here. Its .NET plugin content is not part of this marketplace. The exact upstream commit, license, and retrieval method are recorded in PROVENANCE.
