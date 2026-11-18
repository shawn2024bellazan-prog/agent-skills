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

1. Resolve the actual host and registered project. For PMCR-O, invoke the sibling `project-lifecycle` read-only `runtime` operation to confirm project identity, initialization and private resource scope, then use `~/.pmcro/projects/<project-id>/memory/` only for the authorized operation. For Claude, use its existing `~/.claude/projects/<project>/memory/` reference. Never guess a project ID, migrate memory, or read unrelated projects.
2. Treat `MEMORY.md` as the index and topic files as detailed notes. Only the documented first 200 lines or 25 KB of each file load per session.
3. Make the requested review or edit without treating this global memory as committed project configuration. The agent may continue updating it.
4. For Claude, use `/memory` or the `autoMemoryEnabled` setting when the request is to toggle automatic memory. Do not claim those controls exist in PMCR-O; return NOT_INVOKED if the applicable runtime provider is unavailable.
5. Confirm the requested files or setting changed at the intended project-specific location.

## Validation

- For PMCR-O, invoke `python3 -B scripts/check_index.py --project-id ID --project-root ABSOLUTE_PATH` to verify the index exists and its private registry is correctly scoped without reading memory content. See [example request](assets/request.json).
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

See the plugin README for the directory overview.

- [Debugging memory example](./references/debugging.md)
- [Memory file](./references/MEMORY.md)
- [Project memory](./references/project-memory.md)
