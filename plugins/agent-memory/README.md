# agent-memory/

> Subagent persistent memory, separate from your main session auto memory

**Scope:** project  (.agents/agent-memory/)

**When it loads:** The first 200 lines (capped at 25KB) of MEMORY.md are loaded into the subagent system prompt when it runs.

Subagents with memory: project in their frontmatter get a dedicated memory directory here. This is distinct from the main session auto memory under projects/: each subagent reads and writes its own MEMORY.md, not yours. The agent writes this directory; it can be committed.

## Tips

- Only created for subagents that set the memory: frontmatter field
- This directory holds project-scoped subagent memory, meant to be shared with your team. To keep memory out of version control use memory: local, which writes to agent-memory-local/ instead. For cross-project memory use memory: user, which writes to the global agent-memory/
- The main session auto memory is a different feature; see projects/ in the global scope

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
