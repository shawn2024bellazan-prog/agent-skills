---
name: author-output-styles
description: "Author AGENTS custom output styles for response modes such as teaching or review. Use when defining or selecting an output style; use instructions or skills for task-specific behavior and workflows."
---

# Output styles

## Purpose

Define a reusable AGENTS response mode while keeping it distinct from always-on instructions and task-specific skills.

## When to Use

- Creating or editing a custom response style, such as teaching or review.
- Deciding whether a style should be project-shared or personal.
- Preserving default coding instructions while applying a custom style.

## When Not to Use

- Adding always-on project guidance; use agent instructions or rules.
- Defining a task workflow or tool procedure; use a skill.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Response mode | Yes | The response behavior or presentation style to define. |
| Scope | If known | Global is usually personal; use project scope only when the team shares the style. |
| Coding-instruction behavior | No | Whether the style should preserve default coding instructions. |

## Workflow

1. Prefer the global output-styles directory for a personal style; use project configuration only for a style the team shares.
2. Create a Markdown style file with a clear description in its frontmatter.
3. Set `keep-coding-instructions: true` when the custom style should retain the default coding instructions.
4. Select the style through `/output-style`, `/config`, or the `outputStyle` setting using the supported filename or name.
5. Verify the selected style name and confirm it does not replace instructions the user intends to keep.

## Validation

- [ ] The style file is in the intended global or project location.
- [ ] Frontmatter describes the style and preserves coding instructions when required.
- [ ] The selected style name matches the file or declared name.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Making a personal style project-wide | Keep it global unless the team explicitly shares it. |
| Using a style for task-specific procedures | Put repeatable task workflows in a skill. |
| Accidentally replacing default coding instructions | Set `keep-coding-instructions: true` when they must remain active. |

## References

See [the plugin README](../../README.md) for the directory overview.

- [Global output styles](./references/global.md)
- [Teaching style](./references/teaching.md)
