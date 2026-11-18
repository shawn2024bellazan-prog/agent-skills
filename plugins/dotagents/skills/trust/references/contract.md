# trust contract

Delegate to the [canonical provider contract](../../dotagents/references/contract.md). List is read-only; mutations require explicit --apply. Never grant wildcard trust.

Inputs: Subcommand list/add/remove and exact org, repo or domain when mutating.

Execute only `trust` using the fixed-verb entrypoint. Return BLOCKED when the installed provider or its preconditions are unavailable. Verify actual results against the request.
