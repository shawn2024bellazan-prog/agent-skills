# settings.local.json

> Your personal settings overrides for this project

**Scope:** project  (.claude/settings.local.json, gitignored)

**When it loads:** Highest of the user-editable settings files; CLI flags and managed settings still take precedence.

Personal settings that take precedence over the project defaults. Same JSON format as settings.json, gitignored. Use it when you need different permissions or defaults than the team config. The example adds Docker permissions on top of whatever the team settings.json allows.

## Tips

- Same schema as settings.json. Array settings like permissions.allow combine across scopes; scalar settings like model use the local value
- To share the ignore rule with your team, also add it to the project .gitignore (this repo does)

## Example

```json
{
  "permissions": {
    "allow": [
      "Bash(docker *)"
    ]
  }
}
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
