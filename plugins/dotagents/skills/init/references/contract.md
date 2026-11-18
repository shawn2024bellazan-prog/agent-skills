# init contract

Delegate to the [canonical provider contract](../../dotagents/references/contract.md). Mutating; require explicit authorization before invocation.

Inputs: Existing project root and explicit host list. Do not replace existing agents.toml.

Execute only `init` using the fixed-verb entrypoint. Return BLOCKED when the installed provider or its preconditions are unavailable. Verify actual results against the request.
