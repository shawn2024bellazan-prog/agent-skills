# debugging.md

> Topic notes the agent writes when MEMORY.md gets long

**Scope:** global  (<project>/memory/debugging.md)

**When it loads:** The agent reads this when a related task comes up.

An example of a topic file the agent creates when MEMORY.md grows too long. The agent picks the filename based on what it splits out: debugging.md, architecture.md, build-commands.md, or similar. You never create these yourself. The agent reads a topic file back only when the current task relates to it. Local only.

## Example

```markdown
---
name: Debugging patterns
description: Auth token rotation and database connection troubleshooting for this project
type: reference
---

## Auth Token Issues
- Refresh token rotation: old token invalidated immediately
- If 401 after refresh: check clock skew between client and server

## Database Connection Drops
- Connection pool: max 10 in dev, 50 in prod
- Always check `docker compose ps` first
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
