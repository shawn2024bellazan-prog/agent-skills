---
name: manage-auto-memory
description: Understand and manage global automatic memory stored separately for each project. Use when reviewing, trimming, or toggling the notes the agent keeps.
---

# Auto memory

See ../../README.md for the directory overview.

## Where it lives

Global only: C:\Users\pmcro\.claude\projects\<project>\memory\ (MEMORY.md index plus topic files).

## How to author it

1. The agent writes these files; you can edit or delete them but it will keep updating them.
2. MEMORY.md is an index (first 200 lines or 25KB load each session); topic files such as debugging.md load on demand.
3. Toggle with /memory or autoMemoryEnabled in settings.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/debugging.md
- references/MEMORY.md
- references/project-memory.md
