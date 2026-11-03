# workflows/

> Dynamic workflow scripts that orchestrate many subagents

**Scope:** project  (.agents/workflows/)

**When it loads:** Loaded at startup; each file becomes a /<name> command.

Each .js file is a dynamic workflow: a script the runtime executes to spawn and coordinate many subagents. Workflows are written by the agent and saved here from /workflows rather than authored from scratch.

## Tips

- Save a run from /workflows with s to create one of these
- A project workflow takes precedence over a personal one in the global workflows/ directory with the same name

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
