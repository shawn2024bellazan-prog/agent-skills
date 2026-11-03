# Agent Skills — Claude Directory Reference

A plugin marketplace that documents and helps author the files and directories used to
configure Claude Code at the project and global levels.

Each plugin focuses on one part of the directory layout. Its bundled Agent Skill explains
the purpose, scope, loading behavior, conventions, and practical use of that part of the
configuration. Supporting reference material lives beside the skill so it can be consulted
when needed.

This repository is a **directory-layout reference and authoring toolkit**. It is not the
upstream .NET skills collection, and it does not ship the .NET development skills that were
present in the source repository used as a packaging reference.

## What's included

| Plugin | Directory or area | What it covers |
| --- | --- | --- |
| [agent-config](plugins/agent-config/) | Root files and `.agents/` | Project instructions, settings, MCP configuration, keybindings, app state, and the project-level configuration layout. |
| [rules](plugins/rules/) | `rules/` | Topic-scoped instructions, including optional path-based loading with frontmatter globs. |
| [skills](plugins/skills/) | `skills/` | Reusable, invocable skill folders with a `SKILL.md` entrypoint and supporting files. |
| [commands](plugins/commands/) | `commands/` | Single-file prompts invoked by name, including argument conventions and the relationship to skills. |
| [output-styles](plugins/output-styles/) | `output-styles/` | Custom instruction sets that change the assistant's response style. |
| [agents](plugins/agents/) | `agents/` | Specialized subagents with their own context, tool access, and optional model configuration. |
| [workflows](plugins/workflows/) | `workflows/` | Dynamic workflow scripts that coordinate subagents. |
| [agent-memory](plugins/agent-memory/) | `agent-memory/` | Persistent, project-scoped memory belonging to individual subagents. |
| [themes](plugins/themes/) | Global `themes/` | Custom color themes and their configuration. |
| [projects](plugins/projects/) | Global `projects/` | Automatic memory organized by project, distinct from subagent memory. |

The marketplace manifest is [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json).
Each plugin has its own `plugin.json`, host metadata where applicable, and a `skills/`
directory containing its `SKILL.md` entrypoint and any supporting `references/`.

## Repository layout

```text
.
├── .agents/
│   ├── rules/                 # Repository-wide authoring guidance
│   └── skills/                # Skills used to maintain this repository
├── .claude-plugin/
│   └── marketplace.json       # Claude Code marketplace catalog
├── .cursor-plugin/            # Cursor marketplace metadata
├── plugins/
│   ├── agent-config/
│   ├── agent-memory/
│   ├── agents/
│   ├── commands/
│   ├── output-styles/
│   ├── projects/
│   ├── rules/
│   ├── skills/
│   ├── themes/
│   └── workflows/
│       ├── plugin.json
│       └── skills/
│           └── <skill-name>/
│               ├── SKILL.md
│               └── references/
├── AGENTS.md
└── README.md
```

The exact files vary by plugin. Consult the plugin's own README and skill references for
its specific directory conventions and examples.

## Scope and terminology

The reference material distinguishes areas that can look similar but serve different roles:

- **Project configuration** lives with a project and can be shared with its contributors.
- **Global configuration** belongs to the user's environment and can apply across projects.
- **Skills** package reusable instructions and supporting resources behind a `SKILL.md`.
- **Commands** are single-file prompts; the reference explains their conventions and how they
  relate to skills.
- **Subagent memory** is separate from the main session's **project auto memory**.
- **Plugins** package and distribute skills; they are not themselves the Claude configuration
  directories being documented.

Some details are host- and version-specific. Treat the skill references as documentation of
the conventions they describe, and check the linked official documentation when validating
behavior for a particular Claude Code release.

## Installation and use

This repository is organized as a Claude Code plugin marketplace. To use it, make the
repository available to Claude Code (for example, by cloning it locally), then add that
marketplace from the local checkout using Claude Code's marketplace command:

```text
/plugin marketplace add <path-to-local-checkout>
```

Browse the marketplace and install the reference plugins you want:

```text
/plugin
```

After installation, invoke a plugin's skill by its skill name, or let Claude Code select it
when the task matches its description. The skill's `SKILL.md` is the entrypoint; consult
its bundled `references/` for deeper details and examples.

> **Access note:** If you use a remote GitHub marketplace instead of a local checkout, the
> repository must be accessible to the account and environment performing the installation.
> This repository has previously been configured as a private GitHub repository, so a local
> checkout is the predictable option unless its visibility or access has changed.

## Source material and provenance

The directory descriptions and examples were prepared from the Claude Code directory
documentation and the project/global directory screenshots referenced by the plugin READMEs.
The repository records the upstream source used for plugin packaging conventions in
[`PROVENANCE`](PROVENANCE). That upstream repository supplied the **plugin layout convention**;
its .NET plugin content was removed and is not part of this marketplace.

For behavior that may change between releases, consult the
[Claude Code documentation](https://docs.claude.com/en/docs/claude-code/overview).

## Contributing

When adding or changing a reference area:

1. Keep each top-level `plugins/<name>/` directory independently understandable.
2. Preserve the plugin packaging convention: plugin metadata, host metadata as required,
   and a `skills/` directory.
3. Give each skill a clear `SKILL.md` entrypoint.
4. Put substantial supporting material in that skill's `references/` directory rather than
   overloading the entrypoint.
5. Keep the root marketplace manifest synchronized with the plugin directories.
6. Ground behavioral claims in the relevant official documentation and identify version-specific
   behavior where appropriate.

See [`AGENTS.md`](AGENTS.md) for repository-specific authoring guidance.

## License

See [`LICENSE`](LICENSE) for license terms.
