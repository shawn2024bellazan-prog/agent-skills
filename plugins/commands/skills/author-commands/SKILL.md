---
name: author-commands
description: "Author single-file slash commands. Use when adding a named prompt; prefer a skill for new workflows that need supporting files."
---

# Commands

See ../../README.md for the directory overview.

## Where it lives

Project: .claude/commands/*.md. Global: C:\Users\pmcro\.claude\commands\.

## How to author it

1. Create commands/<name>.md; it is invoked as /<name>.
2. Use argument-hint frontmatter and $ARGUMENTS for parameters.
3. If a skill and a command share a name, the skill wins; new workflows should usually be skills.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/fix-issue.md
- references/global.md
