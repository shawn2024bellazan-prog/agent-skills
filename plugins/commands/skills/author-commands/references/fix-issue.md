# fix-issue.md

> Invoked as `/fix-issue <number>`

**Scope:** project  (.claude/commands/fix-issue.md)

An example command for fixing a GitHub issue. Type /fix-issue 123 and the !`...` line runs gh issue view 123 in your shell, injecting the output into the prompt before the agent sees it. $ARGUMENTS substitutes whatever you typed after the command name. For positional access, use $0, $1 and so on.

## Example

```markdown
---
argument-hint: <issue-number>
---

!`gh issue view $ARGUMENTS`

Investigate and fix the issue above.

1. Trace the bug to its root cause
2. Implement the fix
3. Write or update tests
4. Summarize what you changed and why
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
