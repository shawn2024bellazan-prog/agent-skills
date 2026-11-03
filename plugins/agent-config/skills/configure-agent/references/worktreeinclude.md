# .worktreeinclude

> Gitignored files to copy into new worktrees

**Scope:** project  (.worktreeinclude at the repo root)

**When it loads:** Read when the agent creates a git worktree via --worktree, the EnterWorktree tool, or subagent isolation: worktree.

Lists gitignored files to copy from your main repository into each new worktree. Worktrees are fresh checkouts, so untracked files like .env are missing by default. Patterns use .gitignore syntax. Only files that match a pattern and are also gitignored get copied, so tracked files are never duplicated. Comments start with # and blank lines are ignored.

## Tips

- Lives at the project root, not inside the config directory
- Git-only: if you configure a WorktreeCreate hook for a different VCS, this file is not read. Copy files inside your hook script instead
- Also applies to parallel sessions in the desktop app

## Example

```text
# Local environment
.env
.env.local

# API credentials
config/secrets.json
```

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
