# projects — Project Agent

Version 0.2.0 adds the `project-lifecycle` skill while retaining the original
`manage-auto-memory` reference. Register, initialize, activate, deactivate,
archive, inspect and resolve the runtime scope of a local project through the private registry at
`~/.pmcro/projects/<project-id>/`. The portable `.agents/` scaffold remains in
the project; no private memory or trail is distributed. The existing scaffold
engine is reused with a local-only manifest. See
`skills/project-lifecycle/references/contract.md`.

The lifecycle can invoke the existing DotAgents adapter in `agent-config` v0.2.0.
Provide its trusted absolute path and independently verified SHA-256 pin when
initializing; include an explicit host list for a new configuration. The private registry
stores that binding and verifies it before runtime resolution or activation. No
runtime path or memory data is copied into host configuration.

Example, from the plugin directory (replace the absolute path with an
authorized existing workspace):

```bash
python3 skills/project-lifecycle/scripts/project_lifecycle.py register --project-id everything-as-agent --project-root /absolute/EverythingAsAgent --apply
python3 skills/project-lifecycle/scripts/project_lifecycle.py initialize --project-id everything-as-agent --project-root /absolute/EverythingAsAgent --apply
python3 skills/project-lifecycle/scripts/project_lifecycle.py status --project-id everything-as-agent --project-root /absolute/EverythingAsAgent
python3 skills/project-lifecycle/scripts/project_lifecycle.py runtime --project-id everything-as-agent --project-root /absolute/EverythingAsAgent
```

For DotAgents-backed initialization, add `--dotagents-adapter /absolute/configure-agent/scripts/dotagents.py --dotagents-sha256 VERIFIED_SHA256 --agents claude,codex` to the initialize command. Omit `--agents` when `agents.toml` already exists, and review the configuration before authorizing sync.

These are local registry operations, not AI host project creation or runtime
startup. Resolve the existing Project Agent host provider for those requests.

## Original Claude memory reference

> Auto memory: the agent notes to itself, per project

**Scope:** global  (C:\Users\pmcro\.claude\projects\)

**When it loads:** MEMORY.md is loaded at session start; topic files are read on demand.

Auto memory lets the agent accumulate knowledge across sessions without you writing anything. It saves notes as it works: build commands, debugging insights, architecture notes. Each project gets its own memory directory keyed by the repository path. The agent writes this directory.

## Tips

- On by default. Toggle with /memory or autoMemoryEnabled in settings
- MEMORY.md is the index loaded each session. The first 200 lines, or 25KB, whichever comes first, are read
- Topic files like debugging.md are read on demand, not at startup
- These are plain markdown. Edit or delete them anytime

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
