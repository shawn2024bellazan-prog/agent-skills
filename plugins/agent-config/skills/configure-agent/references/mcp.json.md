# .mcp.json

> Project-scoped MCP servers, shared with your team

**Scope:** project  (.mcp.json at the repo root)

**When it loads:** Servers connect when the session begins. Tool schemas are deferred by default and load on demand via tool search.

Configures Model Context Protocol servers that give the agent access to external tools: databases, APIs, browsers, and more. This file holds the project-scoped servers your whole team uses. Personal servers go in the global app-state file instead. The example configures the Notion MCP server; the ${NOTION_TOKEN} reference is read from your shell environment when the server starts, so the token never lands in the file.

## Tips

- Use environment variable references for secrets: ${NOTION_TOKEN}
- Lives at the project root, not inside the config directory
- For servers only you need, add them at user scope; that writes to the global app-state file instead of .mcp.json

## Example

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_TOKEN": "${NOTION_TOKEN}"
      }
    }
  }
}
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
