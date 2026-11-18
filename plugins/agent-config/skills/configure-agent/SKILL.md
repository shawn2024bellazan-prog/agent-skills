---
name: configure-agent
description: "Configure AGENTS project or global instructions and runtime settings, including DotAgents project initialization, synchronization and health checks across AI hosts. Use when choosing configuration scope or editing host settings; use specialized skills for agents, skills, rules, commands, memory, or workflows."
---

# Agent configuration files

## Purpose

Place AGENTS instructions and settings at the correct project or global scope, preserving the distinction between shared configuration and personal preferences.

## When to Use

- Adding or changing `CLAUDE.md` or project `AGENTS.md` instructions.
- Editing project `.claude/settings.json`, `.claude/settings.local.json`, `.mcp.json`, or `.worktreeinclude`.
- Editing global AGENTS instructions, settings, keybindings, or application state.
- Deciding whether a configuration should be shared with a project or remain personal.
- Connecting a project’s portable `.agents/` configuration to supported AI hosts using DotAgents.

## When Not to Use

- Authoring agents, skills, rules, commands, output styles, workflows, or memory; use the corresponding skill.
- Managing credentials or granting access to external services.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Configuration change | Yes | The setting or behavior to add, change, or explain. |
| Scope | If known | Project-shared or global/personal; discover the existing layout if unspecified. |
| Existing configuration | No | Relevant files and repository ignore rules, when available. |
| DotAgents project root | For DotAgents | Explicit project directory; select `init`, `sync`, or `doctor`. |

## Deliverables

Return the changed configuration and verification evidence, or a blocked outcome if the required provider is unavailable.

## Workflow

1. Decide whether the change belongs to the project or the user's global AGENTS configuration. Keep personal overrides out of shared project files.
2. Select the corresponding file and preserve its existing structure. Use `CLAUDE.md` for project instructions (`AGENTS.md` may be used instead); use settings for supported runtime configuration.
3. Keep secrets out of configuration files. Reference environment variables for secret values and do not write tokens directly.
4. Make the smallest change that expresses the requested behavior. Keep local-only settings ignored by version control.
5. Check syntax for edited structured files and confirm that project/global scope and ignore behavior are correct.

For DotAgents requests, use [the integration contract](./references/dotagents.md) and run `scripts/dotagents.py` from this skill's directory. Invoke the installed CLI, not a reimplementation. The adapter requires an explicit project root, never selects global scope, and does not install or download a CLI automatically. Native host directories are projections; private PMCR-O state under `~/.pmcro/` is accessed through a separately authorized provider, never symlinked into `.agents/`.

## Validation

- [ ] Instructions and settings are in the intended project or global location.
- [ ] JSON files parse, and no secret values were added.
- [ ] Personal overrides remain untracked and shared configuration contains no machine-specific assumptions.
- [ ] For DotAgents, confirm the CLI exit status and run `doctor` after an authorized initialization or sync; do not claim PASS if the provider is unavailable.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Putting personal preferences in a project file | Use global configuration or an ignored local override. |
| Committing `settings.local.json` | Confirm the repository ignores local settings before finishing. |
| Writing a credential into `.mcp.json` | Use an environment-variable reference instead. |
| Using configuration files to author another customization type | Use the skill for that type so its format and scope rules are followed. |

## References

See the plugin README for the directory overview.

- [Application state](./references/app-state.md)
- [Project instructions](./references/CLAUDE.md)
- [Global configuration](./references/global.md)
- [Global instructions](./references/global-CLAUDE.md.md)
- [Keybindings](./references/keybindings.json.md)
- [MCP configuration](./references/mcp.json.md)
- [Settings](./references/settings.json.md)
- [Local settings](./references/settings.local.json.md)
- [Worktree include](./references/worktreeinclude.md)
- [DotAgents and PMCR-O integration](./references/dotagents.md)
