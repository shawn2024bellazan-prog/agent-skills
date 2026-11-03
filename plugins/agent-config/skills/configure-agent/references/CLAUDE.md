# CLAUDE.md / AGENTS.md (project)

> Project instructions the agent reads every session

**Scope:** project  (CLAUDE.md at the repo root; AGENTS.md can be used as an alternative)

**When it loads:** Loaded into context at the start of every session.

Project-specific instructions shape how AGENTS works in a repository. Put conventions, common commands, and architectural context here so it operates with the same assumptions as the team. AGENTS can read an existing AGENTS.md instead of CLAUDE.md when a repository uses that filename for shared agent instructions. The screenshot example is for a TypeScript and React project; the capture was cut off after the Rules heading.

## Tips

- Target under 200 lines. Longer files still load in full but may reduce adherence
- It loads into every session. If something only matters for specific tasks, move it to a skill or a path-scoped rule so it loads only when needed
- List the commands you run most, like build, test, and format, so the agent knows them without you spelling them out each time
- Run /memory to open and edit the file from within a session
- Also works inside the config directory if you prefer to keep the project root clean
- If your repo already has an AGENTS.md for other coding agents, AGENTS can read that in place of a CLAUDE.md

## Example

```markdown
# Project conventions

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Stack
- TypeScript with strict mode
- React 19, functional components only

## Rules
- Named exports, never default exports
- Tests live next to source: `foo.ts` -> `foo.test.ts`
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
