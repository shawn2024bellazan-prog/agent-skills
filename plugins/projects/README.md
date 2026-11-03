# projects/

> Auto memory: the agent notes to itself, per project

**Scope:** global  (C:\Users\pmcro\.agents\projects\)

**When it loads:** MEMORY.md is loaded at session start; topic files are read on demand.

Auto memory lets the agent accumulate knowledge across sessions without you writing anything. It saves notes as it works: build commands, debugging insights, architecture notes. Each project gets its own memory directory keyed by the repository path. The agent writes this directory.

## Tips

- On by default. Toggle with /memory or autoMemoryEnabled in settings
- MEMORY.md is the index loaded each session. The first 200 lines, or 25KB, whichever comes first, are read
- Topic files like debugging.md are read on demand, not at startup
- These are plain markdown. Edit or delete them anytime

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
