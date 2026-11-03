---
name: author-workflows
description: Understand and save dynamic workflow scripts in the workflows directory. Use when a multi-agent run should become a reusable slash command.
---

# Workflows

See ../../README.md for the directory overview.

## Where it lives

Project: .claude/workflows/*.js. Global: C:\Users\pmcro\.claude\workflows\.

## How to author it

1. Workflows are .js scripts written by the agent; save a run from /workflows rather than hand-writing one.
2. Each file becomes a /<name> command at startup.
3. A project workflow takes precedence over a global one with the same name.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/global.md
