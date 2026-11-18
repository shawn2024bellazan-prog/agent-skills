# DotAgents provider contract

Tested provider: Sentry DotAgents 3.4.0, installed as `dotagents` on PATH. See [upstream CLI](https://dotagents.sentry.dev/cli/) and [security](https://dotagents.sentry.dev/security/). The adapter executes the installed binary with the explicit project flag and no shell. It does not install the CLI, grant implicit trust, or execute MCP servers.

## Scope and authorization

- Supply the exact existing project root (Git root when in a repository).
- Keep `~/.pmcro/projects/<id>/` private. Managed paths may not escape the project or point into private PMCR-O state. No global fallback.
- Init and sync retain the v0.2 agent-config invocation protocol for existing Project Agent orchestration: their call must already have explicit mutation authority. New mutating commands require `--apply`; remove forwards the provider's noninteractive confirmation only after this gate.
- `agents.toml` remains the declaration; the CLI owns native projections and managed state. Review sources, trust policy, and changes. Do not store credentials in commands, URLs or headers; only environment variable names are accepted for MCP. Name/transport/env-name inventory is returned for MCP list; targets are intentionally withheld.
- Local dependency paths must reside inside the project and contain neither symlinks nor private .pmcro directories; the adapter normalizes them to the provider's native `path:<relative>` source. Remote sources must be explicit owner/repo or credential-free HTTPS URLs (`git:https://...` for explicit Git URLs).

## CLI examples

Run from the canonical skill directory with a trusted CLI installed:

```bash
python scripts/dotagents.py --project /project init --agents claude,codex
python scripts/dotagents.py --project /project sync
python scripts/dotagents.py --project /project doctor
python scripts/dotagents.py --project /project install --apply
python scripts/dotagents.py --project /project add owner/repo skill-name --ref v1 --apply
python scripts/dotagents.py --project /project remove skill-name --apply
python scripts/dotagents.py --project /project list --json
python scripts/dotagents.py --project /project mcp list
python scripts/dotagents.py --project /project mcp add local --url http://127.0.0.1:8080/mcp --apply
python scripts/dotagents.py --project /project trust list --json
python scripts/dotagents.py --project /project trust add owner/repo --apply
```

Doctor is read-only unless both `--fix` and `--apply` are supplied. A successful add declares or installs a dependency; a successful MCP add declares a server, not its connectivity. Exit 0 means provider success, 1 blocked/provider failure, 2 invalid arguments. Run doctor after mutations. No unsupported `config` or `--create`/ `--new` flags.

## Project Agent compatibility

New initialization binds this shared script path and verified SHA-256 via `--dotagents-adapter` and `--dotagents-sha256`. The existing Project Agent expects the exact `Provider exit: 0` receipt and guards against pin mismatch. Its previous adapter remains frozen in agent-config at its original bytes; never switch an existing registry pin silently.
