---
name: manage-agent-memory
description: "Understand and manage persistent memory for AGENTS subagents configured with memory frontmatter. Use when choosing project, local, or user subagent memory; use manage-auto-memory for the main session's per-project automatic memory."
---

# Agent memory

## Purpose

Explain where persistent AGENTS subagent memory belongs and how its configured scope affects sharing and loading.

## When to Use

- Configuring or reviewing memory for a subagent that declares a memory scope.
- Deciding whether a subagent's notes should be project-shared, local, or user-wide.
- Understanding which part of a subagent's memory is loaded into its prompt.

## When Not to Use

- Managing the main session's automatic project memory; use `manage-auto-memory`.
- Creating or changing the subagent definition itself; use `author-agents`.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Subagent name or definition | Yes | Identify the agent whose memory is in question. |
| Desired sharing scope | If known | Project, local, or user-wide; determine from the request or existing definition. |

## Workflow

1. Inspect the subagent definition and confirm it declares a memory scope. Do not create a memory directory for an agent that has none.
2. Choose the scope deliberately: project memory is shared, local memory stays with the checkout, and user memory persists across projects.
3. Locate the corresponding `agent-memory` directory for that scope. The subagent maintains its own `MEMORY.md`; do not hand-write or silently replace its notes.
4. When reviewing loaded content, account for the first-200-lines/25-KB limit and keep durable, useful notes concise.

## Validation

- [ ] The target subagent has the intended memory scope in its definition.
- [ ] Memory is stored in the matching project, local, or user location.
- [ ] Project-shared notes contain no personal or machine-specific data.
- [ ] Any size-related conclusion reflects the documented loading limit.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Confusing subagent memory with main-session automatic memory | Use `manage-auto-memory` for main-session memory. |
| Adding memory files for an agent without a memory scope | Configure the subagent first, or leave memory unconfigured. |
| Treating local or user memory as team-shared | Use project scope only when notes are intended to be shared. |
| Editing the subagent's notes as if they were authored configuration | Let the subagent maintain its memory; make scope and lifecycle decisions here. |

## References

See [the plugin README](../../README.md) for the directory overview.

- [Agent memory example](./references/agent-name.md)
- [Global memory](./references/global.md)
- [Memory file](./references/MEMORY.md)
