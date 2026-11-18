# install contract

Delegate to the [canonical provider contract](../../dotagents/references/contract.md). Mutating; require explicit --apply.

Inputs: Existing project root, reviewed dependencies and trust policy.

Execute only `install` using the fixed-verb entrypoint. Return BLOCKED when the installed provider or its preconditions are unavailable. Verify actual results against the request.
