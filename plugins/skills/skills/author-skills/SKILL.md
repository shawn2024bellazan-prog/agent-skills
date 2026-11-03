---
name: author-skills
description: Author skills for skills/: a folder with SKILL.md plus supporting files. Use when creating or editing a reusable prompt invoked by name.
---

# Skills

See ../../README.md for the directory overview.

## Where it lives

Project: .agents/skills/<name>/. Global: C:\Users\pmcro\.agents\skills\<name>\.

## How to author it

1. Create skills/<name>/SKILL.md with a description frontmatter that says when to use it.
2. Use disable-model-invocation: true for user-only workflows; user-invocable: false to hide from the / menu.
3. Use $ARGUMENTS (or $0, $1) for parameters and !`cmd` to inject command output.
4. Bundle checklists, templates and scripts next to SKILL.md and mention them by name. Note: this repo gitignores .agents/skills/* so add a negation to .gitignore for each new project skill.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/checklist.md
- references/global.md
- references/security-review.md
- references/skill-entrypoint.md
