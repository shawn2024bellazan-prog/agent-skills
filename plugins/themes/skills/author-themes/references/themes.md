# themes/

> Custom color themes

**Scope:** global  (C:\Users\pmcro\.claude\themes\)

**When it loads:** Read at session start and hot-reloaded when files change. Listed in /theme.

Each .json file defines a custom color theme: a built-in base preset plus an overrides map of color tokens. Create one interactively with /theme or write the JSON by hand. Selecting a custom theme stores custom:<slug> as your theme preference.

## Example

```json
{
  "name": "Dracula",
  "base": "dark",
  "overrides": {
    "claude": "#bd93f9",
    "error": "#ff5555",
    "success": "#50fa7b"
  }
}
```

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
