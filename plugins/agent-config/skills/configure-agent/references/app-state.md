# .claude.json (global app state)

> App state and UI preferences

**Scope:** global  (C:\Users\pmcro\.claude.json)

**When it loads:** Read at session start for your preferences and MCP servers. Written back when you change settings in /config or approve trust prompts.

Holds state that does not belong in settings.json: account details, per-project trust decisions, your personal MCP servers, and UI toggles. Mostly managed through /config rather than editing directly. Local only.

## Tips

- IDE toggles like autoConnectIde and externalEditorContext live here, not in settings.json
- The projects key tracks per-project state like trust-dialog acceptance and last-session metrics. Permission rules you approve in-session go to settings.local.json instead
- MCP servers here are yours only: user scope applies across all projects, local scope is per-project but not committed. Team-shared servers go in .mcp.json at the project root instead

## Example

```json
{
  "autoConnectIde": true,
  "externalEditorContext": true,
  "mcpServers": {
    "my-tools": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"]
    }
  }
}
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
