# Naming Convention Guide

**Status:** naming proposal for this repository. The guide does not rename the repository, plugins, skills, or workflow packages.

## What this repository names

This repository is a cross-host reference and authoring marketplace for agent workspace configuration. It documents project-level and global configuration layouts and offers an authoring tool. It also contains separately packaged GitHub Agentic Workflows.

Related research on MAF, CodeAct, Hyperlight, AGT, Aspire, MCP, and A2A provides useful ecosystem context. Those topics do not establish that this repository ships orchestration, sandbox execution, governance, or protocol hosting. Keep product names and descriptions tied to the reference and authoring content that is actually in this repository.

The current repository title, **Agent Skills — Claude Directory Reference**, describes only part of that scope. The current Git slug, **agent-skills**, is useful for continuity and discoverability, but the product title should explain the broader cross-host purpose.

### Recommended product name

**Agent Workspace Atlas**

**Descriptor:** Cross-host references and authoring tools for agent workspace configuration.

“Atlas” signals a navigable reference collection; “workspace” covers both project and global configuration. The descriptor makes clear that the repository includes reference material and authoring support.

Keep **agent-skills** as the repository slug unless a separate decision is made to rename it. Keep “Agent Skills” in the repository description or metadata where it helps people find the project. A title change and a GitHub repository rename are separate choices.

## Naming principles

1. **Name the repository by its full scope.** Prefer “agent workspace” or “agent configuration” over a single host name.
2. **Use lowercase kebab-case for stable identifiers.** Apply it to repository slugs, plugin IDs, skill directories, workflow packages, and filenames.
3. **Use readable title case for display names.** Keep the display name and stable identifier clearly associated.
4. **Make names specific and concise.** Name the configuration area, authoring task, or workflow purpose; avoid broad claims like “complete” or “universal.”
5. **Keep host names only where the artifact is host-specific.** Do not imply that cross-host content belongs to one host.
6. **Keep each name aligned across its directory, manifest, marketplace catalogs, and documentation.**
7. **Prefer durable names.** Avoid versions, dates, personal names, and temporary implementation details in product or plugin names.
8. **Distinguish the repository’s Codex maintenance metadata under `.agents/` from the AGENTS.md project/global layouts documented as product content.**
## Naming conventions by artifact

| Artifact | Convention | Guidance |
| --- | --- | --- |
| Repository display name | Short, host-neutral product name | Recommended: **Agent Workspace Atlas** |
| Repository slug | Lowercase kebab-case | Keep `agent-skills` unless a separate repository rename is approved |
| Repository tagline | One plain sentence | Say it covers cross-host references and authoring tools for agent workspace configuration |
| Plugin ID | Lowercase kebab-case | Keep it aligned with the plugin directory and all catalog entries |
| Plugin display name | Clear title case | Describe one configuration area or authoring capability |
| Skill name and directory | Lowercase kebab-case; verb + object for actions | Use a short task name such as `create-skill` for a skill that creates skills |
| Workflow package | Lowercase kebab-case; action or problem + subject | Name the task the workflow handles, not its implementation |
| Documentation file | Lowercase kebab-case | Use a direct subject name, such as `naming-convention-guide.md` |

### Plugin and skill rules

- Use a plural name when the artifact represents a collection of directory types, and a singular name for one tool or capability.
- Keep plugin IDs stable once published. A display-name improvement does not require changing an ID.
- Skill names should start with an action when the user invokes a task; reference plugins can use the name of the directory area they explain.
- Keep host-specific instructions, metadata, and cross-host references distinct in the text and names.
- Avoid abbreviations unless they are standard in the repository’s audience and already used consistently.
- Before reusing a name, check for collisions with another plugin, skill, workflow package, directory, or command in this repository.
## Changing a name safely

A name change can affect installs and links, so treat it as a coordinated documentation and metadata update:

1. Decide whether the change is to a display name, stable identifier, or repository slug. Do not bundle these decisions by default.
2. Search the entire repository for the old name, including hidden files and workflow installation instructions.
3. If a plugin ID changes, update its directory and metadata and keep all four marketplace catalogs synchronized: Claude, Cursor, Codex, and GitHub.
4. Update the README, marketplace documentation, links, examples, and any GitHub Agentic Workflow instructions that refer to the name.
5. Check that manifest paths and catalog source paths still resolve. Review the full diff and preserve unrelated worktree changes.
6. State whether the change is a proposal, local update, committed change, or published change. Do not imply a repository rename or release until it has happened.

For a product display-name change, update the README title and description only after the owner chooses a name. Keep the Git slug and plugin IDs stable unless their own changes are explicitly intended.

## Product name candidates

These are display-name ideas for the repository’s current scope. **Agent Workspace Atlas** is the recommended starting point.

1. Agent Workspace Atlas
2. Agent Workspace Reference
3. Agent Configuration Atlas
4. Agent Directory Atlas
5. Agent Workspace Guide
6. Agent Configuration Handbook
7. Agent Workspace Reference Hub
8. Agent Configuration Commons
9. Agent Workspace Toolkit
10. Agent Configuration Marketplace
11. Agent Setup Field Guide
12. Agent Project Layouts
13. Agent Context Workbench
14. Agent Workspace Patterns
15. Agent Structure Library
16. Agent Config Navigator
17. Agent Workspace Studio
18. Agent Configuration Library
19. Agent Environment Handbook
20. Agent Workspace Almanac

These candidates have not been checked for trademark, domain, or marketplace-name availability. The existing repository title and identifiers remain unchanged until a choice is made.
