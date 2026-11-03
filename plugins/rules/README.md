# rules/

> Topic-scoped instructions, optionally gated by file paths

**Scope:** project  (.claude/rules/)

**When it loads:** Rules without paths: load at session start. Rules with paths: load when the agent reads, writes, or edits a matching file.

Project instructions split into topic files that can load conditionally based on file paths. A rule without a paths: frontmatter loads at session start like the main instructions file; a rule with paths: loads only when a matching file is touched. Rules are guidance the agent reads, not configuration the tool enforces. For guaranteed behavior use hooks or permissions.

## Tips

- Use paths: frontmatter with globs to scope rules to directories or file types
- Subdirectories work: rules/frontend/react.md is discovered automatically
- When the main instructions file approaches 200 lines, start splitting it into rules

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
