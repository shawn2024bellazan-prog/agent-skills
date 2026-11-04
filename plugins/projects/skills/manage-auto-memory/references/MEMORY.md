# MEMORY.md

> The agent writes and maintains this file automatically

**Scope:** global  (`<project>/memory/MEMORY.md`)

**When it loads:** The first 200 lines (capped at 25KB) are loaded at session start.

The agent creates and updates this file as it works; you do not write it. It acts as an index read at the start of every session, pointing to topic files for detail. You can edit or delete it, but the agent will keep updating it. Local only.

## Example

```markdown
# Memory Index

## Project
- [build-and-test.md](build-and-test.md): npm run build (~45s), Vitest, dev server on 3001
- [architecture.md](architecture.md): API client singleton, refresh-token auth

## Reference
- [debugging.md](debugging.md): auth token rotation and DB connection troubleshooting
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
