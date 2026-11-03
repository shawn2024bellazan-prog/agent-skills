---
name: configure-agent
description: "Configure project and global agent instructions, MCP settings, keybindings, and application state. Use when creating or changing those configuration files."
---

# Agent configuration files

See ../../README.md for the directory overview.

## Where it lives

Project: CLAUDE.md (or AGENTS.md as an alternative), .mcp.json, and .worktreeinclude at the repository root; .claude/settings.json and .claude/settings.local.json for project configuration. Global: C:\Users\pmcro\.claude\ (CLAUDE.md, settings.json, keybindings.json) and C:\Users\pmcro\.claude.json for application state.

## How to author it

1. Decide scope first: project (shared, committed) or global (personal, never committed).
2. Put project guidance in CLAUDE.md (Claude Code can use AGENTS.md instead); put enforced behavior in .claude/settings.json (permissions, hooks).
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
