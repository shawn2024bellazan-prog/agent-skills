# settings.json (project)

> Permissions, hooks, and configuration

**Scope:** project  (.claude/settings.json)

**When it loads:** Overrides the global settings.json. Local settings, CLI flags, and managed settings override this.

Settings the tool applies directly. Permissions control which commands and tools the agent can use; hooks run your scripts at specific points in a session. Unlike the instructions file, which is read as guidance, these are enforced whether the agent follows them or not. The example allows npm test and npm run without prompting, blocks rm -rf, and runs Prettier on files after edits. The hooks block is completed from the description because the capture was cut off.

## Tips

- Bash permission patterns support wildcards: Bash(npm test *) matches any command starting with npm test
- Array settings like permissions.allow combine across all scopes; scalar settings like model use the most specific value

## Example

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test *)",
      "Bash(npm run *)"
    ],
    "deny": [
      "Bash(rm -rf *)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "npx prettier --write \"$CLAUDE_FILE_PATH\"" }
        ]
      }
    ]
  }
}
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
