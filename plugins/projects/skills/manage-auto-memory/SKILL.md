---
name: manage-auto-memory
description: "Understand, review, trim, or toggle AGENTS's main-session automatic memory stored per project under the global projects directory. Use for project memory and /memory; use manage-agent-memory for persistent subagent notes."
---

# Auto memory

## Purpose

Help distinguish and manage AGENTS's main-session automatic memory, which is stored globally and separately for each project.

## When to Use

- Reviewing or trimming the main session's remembered notes for a project.
- Finding the per-project `MEMORY.md` index and its topic files.
- Toggling automatic memory with `/memory` or the supported setting.

## When Not to Use

- Managing persistent memory for a subagent; use `manage-agent-memory`.
- Editing shared project instructions or configuration; use the corresponding authoring skill.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Project | Yes | The project whose automatic memory is being reviewed or changed. |
| Requested action | Yes | Review, trim, edit, delete, or toggle automatic memory. |

## Workflow

1. Locate the project's memory under the global AGENTS projects directory (`~/.claude/projects/<project>/memory/`).
2. Treat `MEMORY.md` as the index and topic files as detailed notes. Only the documented first 200 lines or 25 KB of each file load per session.
3. Make the requested review or edit without treating this global memory as committed project configuration. The agent may continue updating it.
4. Use `/memory` or the `autoMemoryEnabled` setting when the request is to toggle automatic memory.
5. Confirm the requested files or setting changed at the intended project-specific location.

## Validation

- [ ] The memory belongs to the intended project and is in the global projects directory.
- [ ] `MEMORY.md` remains a useful index and topic details are placed in topic files.
- [ ] Any change to automatic-memory behavior uses the documented toggle.
- [ ] No global memory files were added to shared project configuration.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Confusing automatic memory with subagent memory | Use `manage-agent-memory` for subagents. |
| Assuming automatic memory is project-shared | It is global and kept separately for each project. |
| Putting all notes in the index | Keep the index concise and use topic files for details. |
| Forgetting the loading limit | Keep high-value notes near the top and within the documented limit. |

## References

See [the plugin README](../../README.md) for the directory overview.

- [Debugging memory example](./references/debugging.md)
- [Memory file](./references/MEMORY.md)
- [Project memory](./references/project-memory.md)
