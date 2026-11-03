# testing.md

> Test conventions scoped to test files

**Scope:** project  (.claude/rules/testing.md)

**When it loads:** Loaded when a file matching the paths: globs below is read, written, or edited.

An example rule that only loads when working on test files. The paths: globs in the frontmatter define which files trigger it; here, anything ending in .test.ts or .test.tsx. For other files the rule is not loaded into context.

## Example

```markdown
---
paths:
  - "**/*.test.ts"
  - "**/*.test.tsx"
---

# Testing Rules

- Use descriptive test names: "should [expected] when [condition]"
- Mock external dependencies, not internal modules
- Clean up side effects in afterEach
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
