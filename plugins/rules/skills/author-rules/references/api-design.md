# api-design.md

> API conventions scoped to backend code

**Scope:** project  (.claude/rules/api-design.md)

**When it loads:** Loaded when a file matching the paths: glob below is read, written, or edited.

A second example showing a rule scoped to backend code. The paths: glob matches files under src/api/, so these conventions load only when working on API routes.

## Example

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Design Rules

- All endpoints must validate input with Zod schemas
- Return shape: { data: T } | { error: string }
- Rate limit all public endpoints
```

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
