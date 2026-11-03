# teaching.md

> Example style that adds explanations and leaves small changes for you

**Scope:** global  (C:\Users\pmcro\.claude\output-styles\teaching.md)

**When it loads:** Active when outputStyle in settings is set to teaching.

With this style, the agent adds a "Why this approach" note after each task and leaves TODO(human) markers for changes under 10 lines instead of writing them itself. Select it by setting outputStyle to the filename without .md, or to the name field if you set one in frontmatter. Local only (not committed).

## Example

```markdown
---
description: Explains reasoning and asks you to implement small pieces
keep-coding-instructions: true
---

After completing each task, add a brief "Why this approach" note
explaining the key design decision.

When a change is under 10 lines, ask the user to implement it
themselves by leaving a TODO(human) marker instead of writing it.
```

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
