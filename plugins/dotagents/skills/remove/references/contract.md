# remove contract

Delegate to the [canonical provider contract](../../dotagents/references/contract.md). Mutating; require explicit --apply; do not remove unrelated dependencies.

Inputs: Exact name or source and reviewed removal impact.

Execute only `remove` using the fixed-verb entrypoint. Return BLOCKED when the installed provider or its preconditions are unavailable. Verify actual results against the request.
