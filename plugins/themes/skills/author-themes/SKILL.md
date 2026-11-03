---
name: author-themes
description: "Author or edit AGENTS custom color themes as JSON. Use when defining a theme's built-in base preset and color-token overrides; use output styles for response formatting rather than terminal colors."
---

# Themes

## Purpose

Create a global AGENTS color theme using a supported base preset and explicit token overrides.

## When to Use

- Creating or editing a theme JSON file.
- Choosing a built-in base preset and specifying color-token overrides.
- Selecting an existing custom theme.

## When Not to Use

- Changing response tone or formatting; use `author-output-styles`.
- Changing project-shared instructions or runtime settings.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Theme appearance | Yes | The desired colors or tokens to customize. |
| Base preset | Yes | A supported built-in preset, such as `dark`. |
| Theme slug | If creating | The filename/identifier used to select the custom theme. |

## Workflow

1. Locate or create the theme JSON in the global themes directory. Themes are global, not project-scoped.
2. Set the theme name, a built-in base preset, and an overrides map containing only the intended color tokens.
3. Validate that the JSON is well-formed and token names and values follow the host's supported theme format.
4. Select the theme as `custom:<slug>` and verify the intended appearance. Theme files are hot-reloaded when changed.

## Validation

- [ ] The file is in the global themes directory and parses as JSON.
- [ ] It uses a built-in base preset and a valid overrides map.
- [ ] The selected `custom:<slug>` matches the theme identifier.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Treating themes as project-scoped | Keep themes in the global themes directory. |
| Using a response style to change colors | Use a theme for color tokens and an output style for response behavior. |
| Replacing the whole palette unnecessarily | Start from a built-in preset and override only the desired tokens. |
| Selecting the wrong custom theme | Match the selector slug to the theme file/name. |

## References

See [the plugin README](../../README.md) for the directory overview.

- [Themes reference](./references/themes.md)
