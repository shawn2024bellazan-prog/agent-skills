---
name: author-agents
description: "Author AGENTS subagent definitions in project or global agents directories. Use when creating or editing an agent's role, delegation description, tool access, or memory scope; this is not for Codex agent metadata under .agents/."
---

# Agents

## Purpose

Create focused AGENTS subagents with a clear role, appropriate delegation triggers, and only the tools and persistent memory they need.

## When to Use

- Adding or revising a specialized subagent definition.
- Defining an agent's role, delegation description, tools, or memory scope.
- Choosing between a project subagent and a global subagent.

## When Not to Use

- Editing Codex marketplace agent metadata under `.agents/`.
- Creating a reusable multi-step skill, slash command, or project-wide instruction file.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Agent responsibility | Yes | The bounded role and outcome the subagent should own. |
| Delegation trigger | Yes | The tasks or conditions for which the agent should be used. |
| Tools and memory scope | If known | Required capabilities and whether memory should be project, local, or user-wide. |

## Workflow

1. Choose project scope (`.claude/agents/`) for team-shared agents or global scope (`~/.claude/agents/`) for personal agents.
2. Create a Markdown definition with the required name, description, and tools frontmatter; use the body for the agent's system prompt.
3. State when to delegate to the agent and keep its responsibility bounded.
4. Grant only the tools needed for the role. For read-only review work, use the repository's read-only tool pattern.
5. Add a memory scope only when persistent notes are needed; follow `manage-agent-memory` for its storage and sharing implications.

## Validation

- [ ] The definition is in the intended project or global agents directory.
- [ ] Frontmatter is valid and includes the required fields for the host.
- [ ] The description gives a useful delegation trigger and the tool list matches the role.
- [ ] Memory is absent unless intentionally configured.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Giving an agent broad tools by default | Grant the minimum capabilities needed for its defined task. |
| Writing a generic delegation description | Name concrete tasks and conditions that should route to this agent. |
| Adding persistent memory without a sharing decision | Choose a scope explicitly or omit memory. |
| Confusing AGENTS agents with `.agents/` metadata | Keep this skill's definitions in `.claude/agents/`; `.agents/` serves Codex marketplace metadata in this repository. |

## References

See [the plugin README](../../README.md) for the directory overview.

- [Code reviewer example](./references/code-reviewer.md)
- [Global agents](./references/global.md)
