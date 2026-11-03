# code-reviewer.md

> Subagent for isolated code review

**Scope:** project  (.claude/agents/code-reviewer.md)

**When it loads:** The agent spawns it for review tasks, or you @-mention it from the autocomplete.

An example subagent restricted to read-only tools. The description frontmatter tells the agent when to delegate to it automatically; tools: limits it to Read, Grep, and Glob so it can inspect code but never edit. The body becomes the subagent system prompt.

## Example

```markdown
---
name: code-reviewer
description: Reviews code for correctness, security, and maintainability
tools: Read, Grep, Glob
---

You are a senior code reviewer. Review for:

1. Correctness: logic errors, edge cases, null handling
2. Security: injection, auth bypass, data exposure
3. Maintainability: naming, complexity, duplication

Every finding must include a concrete fix.
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
