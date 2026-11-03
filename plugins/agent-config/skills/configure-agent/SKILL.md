---
name: configure-agent
description: Configure the agent: project and global instructions, .mcp.json, settings.json, settings.local.json, .worktreeinclude, keybindings and app state. Use when creating or changing any of those files.
---

# Agent configuration files

See ../../README.md for the directory overview.

## Where it lives

Project: AGENTS.md, .mcp.json, .worktreeinclude (repo root), .agents/settings.json, .agents/settings.local.json. Global: C:\Users\pmcro\.agents\ (AGENTS.md, settings.json, keybindings.json) and C:\Users\pmcro\.claude.json.

## How to author it

1. Decide scope first: project (shared, committed) or global (personal, never committed).
2. Put guidance the agent reads in AGENTS.md; put behavior that must be enforced in settings.json (permissions, hooks).
3. Keep personal overrides in settings.local.json and make sure it is gitignored.
4. Use ${ENV_VAR} references for secrets in .mcp.json; never write tokens into the file.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/app-state.md
- references/CLAUDE.md
- references/global.md
- references/global-CLAUDE.md.md
- references/keybindings.json.md
- references/mcp.json.md
- references/settings.json.md
- references/settings.local.json.md
- references/worktreeinclude.md
