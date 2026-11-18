# mcp contract

Delegate to the [canonical provider contract](../../dotagents/references/contract.md). List is read-only; add/remove require --apply. MCP connectivity is not tested by declarations.

Inputs: Subcommand list/add/remove, exact server name and transport for add; environment variable names only.

Execute only `mcp` using the fixed-verb entrypoint. Return BLOCKED when the installed provider or its preconditions are unavailable. Verify actual results against the request.
