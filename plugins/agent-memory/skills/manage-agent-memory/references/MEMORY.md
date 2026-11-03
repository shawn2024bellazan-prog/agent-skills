# MEMORY.md

> The subagent writes and maintains this file automatically

**Scope:** project  (.agents/agent-memory/agent-name/MEMORY.md)

**When it loads:** Loaded into the subagent system prompt when the subagent starts.

Works the same as the main auto memory: the subagent creates and updates this file itself. You do not write it. The subagent reads it at the start of each task and writes back what it learns.

## Example

```markdown
# code-reviewer memory

## Patterns seen
- Project uses custom Result<T, E> type, not exceptions
- Auth middleware expects Bearer token in Authorization header
- Tests use factory functions in test/factories/

## Recurring issues
- Missing null checks on API responses (src/api/*)
- Unhandled promise rejections in background jobs
```

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
