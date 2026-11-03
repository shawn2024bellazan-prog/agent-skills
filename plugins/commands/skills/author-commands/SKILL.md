---
name: author-commands
description: "Author single-file AGENTS slash commands in project or global commands directories. Use for a focused prompt invoked by name; use author-skills when the workflow needs a skill directory or supporting files."
---

# Commands

## Purpose

Create a focused, single-file AGENTS slash command and place it at the intended project or global scope.

## When to Use

- Adding a named prompt invoked as `/<name>`.
- Updating an existing single-file command.
- Choosing whether a command is shared by a project or personal.

## When Not to Use

- Building a multi-step workflow that needs supporting files; use `author-skills`.
- Creating or managing dynamic workflow scripts; use `author-workflows`.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Command behavior | Yes | The focused task the slash command should perform. |
| Name and scope | If known | Command name and project or global location; discover existing conventions if unspecified. |
| Arguments | No | Inputs the command should accept from the user. |

## Workflow

1. Confirm this is a single-file prompt rather than a reusable workflow with supporting assets.
2. Choose project scope (`.claude/commands/`) for shared commands or global scope (`~/.claude/commands/`) for personal commands.
3. Create or edit `<name>.md` with clear instructions. Use `argument-hint` and `$ARGUMENTS` when the command accepts parameters.
4. Check for a same-named skill: the skill takes precedence, so avoid creating a confusing duplicate.
5. Confirm the command is in the chosen scope and can be invoked with its intended slash name.

## Validation

- [ ] The Markdown file is in the correct project or global commands directory.
- [ ] The instructions are focused and any argument placeholders match the prompt.
- [ ] A same-named skill does not unexpectedly shadow the command.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Using a command for a workflow with supporting assets | Create a skill instead. |
| Omitting argument guidance | Add `argument-hint` and reference `$ARGUMENTS` where useful. |
| Creating a command with the same name as a skill | Rename one; skills take precedence. |
| Assuming a global command is shared with the team | Use project scope when teammates should receive it. |

## References

See the plugin README for the directory overview.

- [Fix issue command](./references/fix-issue.md)
- [Global commands](./references/global.md)
