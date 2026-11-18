# DotAgents plugin

This dedicated micro-marketplace exposes the real installed Sentry DotAgents CLI. Each bare-verb skill delegates to one canonical adapter; the `dotagents` router discovers the operation. The Project Agent binds the adapter from this release using an explicit absolute path and SHA-256 pin.

| Skill | Provider operation |
| --- | --- |
| init | Initialize explicitly selected project hosts |
| sync | Reconcile generated state offline |
| doctor | Check health; repairs require explicit approval |
| install | Install declared dependencies |
| add | Add an explicitly selected dependency or all from one source |
| remove | Remove an explicitly selected dependency/source |
| list | Inspect declared skills and plugins |
| mcp | List/add/remove MCP declarations |
| trust | List/add/remove exact trusted sources |

See [the provider contract](skills/dotagents/references/contract.md). The legacy agent-config adapter remains frozen for existing integrity-pinned project bindings. No global changes, native `config` command, or `--create`/ `--new` flags are advertised: they are either out of scope or unsupported by the tested CLI. This repository package does not install DotAgents or start a server.
