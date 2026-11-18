# add contract

Delegate to the [canonical provider contract](../../dotagents/references/contract.md). Mutating; require explicit --apply; never grant trust implicitly.

Inputs: Source, one or more names or --all, optional Git ref. Local paths must stay inside project.

Execute only `add` using the fixed-verb entrypoint. Return BLOCKED when the installed provider or its preconditions are unavailable. Verify actual results against the request.
