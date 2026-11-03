---
name: author-rules
description: "Author topic-scoped rule files. Use when adding project or global rules, or splitting long instructions into focused rule files."
---

# Rules

See ../../README.md for the directory overview.

## Where it lives

Project: .claude/rules/*.md. Global: C:\Users\pmcro\.claude\rules\.

## How to author it

1. One topic per file; name it for the topic (testing.md, api-design.md).
2. Add paths: frontmatter globs to load the rule only when matching files are touched; omit paths: to load at session start.
3. Write short, checkable bullets. Rules are guidance, not enforcement; use hooks or permissions for guarantees.
4. Split the main instructions file into rules when it nears 200 lines.

## References

These pages hold the content data (when it loads, tips, and a worked example) taken from the Claude directory screenshots:

- references/api-design.md
- references/global.md
- references/testing.md
