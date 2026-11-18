# Project registry contract v1

The Project Agent owns one real local workspace per stable lowercase kebab-case
ID (1–64 characters). The canonical absolute path is bound to the ID. A different
ID cannot register the same path. No implicit migration or deletion.

The default private registry is `~/.pmcro/projects/<id>/`. Register creates
`project.json`; initialize adds `memory/MEMORY.md`, `tasks/`, and `trails/`.
The record's event list is the lifecycle accountability journal, committed in
the same atomic replacement as its state. It contains observed transitions
only, not approvals or model reasoning. The project root contains portable
`.agents/`, root AGENTS.md and ignore rules. The existing local initializer
engine is copied unchanged (SHA-256
6e587bc0fd0746c9d35c409817b88996c02fbefd4abe9bc3630ede8c946f08e2)
and uses a derived local-only manifest; existing files remain unchanged.
The source project must be outside the global private tree and vice versa.

| Action | Allowed prior state | Result |
| --- | --- | --- |
| register | absent | registered |
| initialize | registered | initialized |
| activate | initialized | active |
| deactivate | active | initialized |
| archive | registered or initialized | archived |
| status | any existing state | read only |
| runtime | initialized or active | verified scoped resource handles, read only |

## DotAgents provider binding

An explicitly authorized initialization can delegate to the already installed
`dotagents` plugin's canonical `skills/dotagents/scripts/dotagents.py` adapter. Existing legacy `agent-config` bindings remain valid at their original path and digest. Supply its absolute `--dotagents-adapter`
path, independently verified `--dotagents-sha256` pin, and `--agents` only if
`agents.toml` does not exist. Resolve the adapter from a trusted release before
the call. The lifecycle runs the existing adapter's `init` or `sync`, then
`doctor`. It stores the verified binding only in the private project record.
No absolute runtime paths or memory are written into portable project files.

After a failed provider operation, newly generated configuration may remain but
the registry state is not advanced. Review partial output; if `agents.toml`
exists on retry, omit `--agents` and authorize sync. Existing initialized
local-only projects can bind DotAgents once; active projects must deactivate
first. Existing bindings cannot be replaced implicitly. `activate` and `runtime`
recheck the binding digest, doctor, scaffold and private resource permissions.

Runtime resolution returns relative handles under the explicitly scoped private
root for `memory/MEMORY.md`, `tasks/`, and `trails/`. It does not read memory,
execute tasks, start a model, or grant authority to subsequent operations.
Every downstream provider must separately validate its scope and authorization.

Repeats of already-satisfied operations are idempotent when prerequisites still
hold. Archived is terminal. Activation is registry metadata only; it checks
the scaffold and private index, and grants no runtime authority.

Mutations require explicit `--apply`. Registration and initialization may
leave newly created paths after IO errors; no existing content is rolled back
or removed. Initialization can be retried from registered state. A lock
prevents concurrent registry mutation; stale locks require operator inspection.
No symlinks, reparse points, malformed records, or unsafe POSIX permissions are
accepted. Windows inherits ACLs, which require host-specific verification.

Exit codes: 0 PASS, 1 BLOCKED, 2 CLI usage error. A JSON receipt never certifies
an AI host provider, deployed runtime, or separate independent Checker verdict.
