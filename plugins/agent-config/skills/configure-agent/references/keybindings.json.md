# keybindings.json

> Custom keyboard shortcuts

**Scope:** global  (C:\Users\pmcro\.claude\keybindings.json)

**When it loads:** Read at session start and hot-reloaded when you edit the file.

Rebind keyboard shortcuts in the interactive CLI. Run /keybindings to create or open this file with a schema reference. Ctrl+C, Ctrl+D, Ctrl+M, and Caps Lock are reserved and cannot be rebound. The example binds Ctrl+E to open your external editor and unbinds Ctrl+S by setting it to null. The context field scopes bindings to a specific part of the CLI, here the main chat input. Local only.

## Example

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "$docs": "https://code.claude.com/docs/en/keybindings",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+s": null
      }
    }
  ]
}
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
