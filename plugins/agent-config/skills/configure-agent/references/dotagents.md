# DotAgents legacy compatibility contract

**New calls:** resolve the dedicated `dotagents` plugin and its canonical adapter at `skills/dotagents/scripts/dotagents.py`. The original adapter below remains at its existing path, frozen for existing Project Agent registry pins (SHA-256 `2d9d01eab9f932a0fbd11c2491d71fd2fd662e2643b75607c9e1ef3603fd4711`). Do not silently rebind private records or maintain the legacy adapter as a second implementation.

DotAgents is the existing configuration provider; AgentSkills routes calls to it. PMCR-O owns private project runtime state and accountability, not host-specific file formats.

## Boundaries

- `agents.toml` declares installed skills, plugins, MCP servers, hooks and subagents.
- Project `.agents/` contains portable configuration and managed skills; the native CLI creates host-specific projections (links or generated files depending on host).
- Do not replace complete `.claude/`, `.codex/`, or other host directories with symbolic links. Preserve native files and let the CLI synchronize its supported entries.
- Keep `~/.pmcro/projects/<project-id>/` private. Resolve it with an authorized PMCR-O project/runtime provider; do not link it to project `.agents/`, copy its memory or trails, or publish its contents.
- DotAgents project scope rejects paths escaping the repository. Global scope is separate (`~/.agents/`); this adapter intentionally does not perform global changes.

## Invoke the installed provider

Prerequisites: Python 3.10+, trusted `dotagents` CLI already installed on PATH, explicit project root. Use the official [CLI documentation](https://dotagents.sentry.dev/cli/) to provision and review the provider separately. No implicit downloads, trust grants, forced initialization, shell command strings or global fallback are permitted by the adapter.

From the `configure-agent/` skill directory:

```bash
python scripts/dotagents.py --project /path/to/project init --agents claude,cursor,codex,vscode,copilot
python scripts/dotagents.py --project /path/to/project sync
python scripts/dotagents.py --project /path/to/project doctor
```

For an existing `agents.toml`, skip `init`; review the declared sources/trust policy before an authorized sync. Init can install declared dependencies; sync reconciles locally and can prune stale managed entries. Review the expected scope before approving either mutation. Doctor is read-only (no `--fix`). The selected directory must be the Git root when inside a repository. The adapter rejects configuration symlinks targeting private PMCR-O state or locations outside the project.

## Evidence

The adapter prints the command, selected project, provider result and exit code. `0` means provider success; `1` provider failure or a blocked precondition; `2` invalid arguments. A provider success is not proof that every host is operational. Run `doctor` and inspect relevant host projections before reporting a successful integration. Preserve only non-sensitive evidence through the authorized PMCR-O trail provider; never commit runtime memory or trails.

References: [DotAgents repository](https://github.com/getsentry/dotagents), [CLI](https://dotagents.sentry.dev/cli/), [security](https://dotagents.sentry.dev/security/).
