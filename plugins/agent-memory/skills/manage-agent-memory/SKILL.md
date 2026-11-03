---
name: manage-agent-memory
description: "Manage persistent subagent memory in agent-memory. Use when assigning subagent memory or choosing project, local, or user memory."
---

# Agent memory

See ../../README.md for the directory overview.

## Where it lives

Project: .claude/agent-memory/<agent-name>/MEMORY.md. Local: agent-memory-local/. Global: C:\Users\pmcro\.claude\agent-memory\.

## How to author it

1. Only subagents that set memory: in frontmatter get a directory here.
2. memory: project is shared with the team; memory: local stays out of version control; memory: user persists across projects.
3. The subagent writes MEMORY.md itself; the first 200 lines (25KB cap) load into its system prompt. Do not hand-write it.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/agent-name.md
- references/global.md
- references/MEMORY.md
