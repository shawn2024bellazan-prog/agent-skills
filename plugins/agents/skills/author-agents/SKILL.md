---
name: author-agents
description: Author subagents for agents/. Use when adding a specialized agent with its own system prompt, tools and context window.
---

# Agents

See ../../README.md for the directory overview.

## Where it lives

Project: .agents/agents/*.md. Global: C:\Users\pmcro\.agents\agents\.

## How to author it

1. Create agents/<name>.md with name, description and tools frontmatter; the body is the system prompt.
2. Make the description say when to delegate; restrict tools to what the agent needs (read-only reviewers get Read, Grep, Glob).
3. Add memory: project|local|user in frontmatter only if the agent should keep persistent notes.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/code-reviewer.md
- references/global.md
