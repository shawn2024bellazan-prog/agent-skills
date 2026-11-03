# agents/

> Specialized subagents with their own context window

**Scope:** project  (.claude/agents/)

**When it loads:** Runs in its own context window when you or the agent invoke it.

Each markdown file defines a subagent with its own system prompt, tool access, and optionally its own model. Subagents run in a fresh context window, keeping the main conversation clean. Useful for parallel work or isolated tasks.

## Tips

- Each agent gets a fresh context window, separate from your main session
- Restrict tool access per agent with the tools: frontmatter field
- Type @ and pick an agent from the autocomplete to delegate directly

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
