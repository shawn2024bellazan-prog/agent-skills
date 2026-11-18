# doctor contract

Delegate to the [canonical provider contract](../../dotagents/references/contract.md). Read-only unless both --fix and --apply are supplied.

Inputs: Existing project root; optional --fix --apply for repair.

Execute only `doctor` using the fixed-verb entrypoint. Return BLOCKED when the installed provider or its preconditions are unavailable. Verify actual results against the request.
