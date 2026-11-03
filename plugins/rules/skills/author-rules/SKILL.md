---
name: author-rules
description: "Author topic-scoped AGENTS rules for project or global use. Use when creating or splitting rules in .claude/rules; use settings, hooks, or permissions when behavior must be enforced rather than guided."
---

# Rules

## Purpose

Write focused, maintainable AGENTS rules and choose when they load, without presenting guidance as deterministic enforcement.

## When to Use

- Adding project or global topic-specific rules.
- Splitting long instructions into focused rule files.
- Scoping a rule to matching file paths with frontmatter globs.

## When Not to Use

- Enforcing behavior that must be deterministic; use the relevant hooks or permissions.
- Writing a single focused slash command or multi-step skill.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Rule topic | Yes | The single concern the rule should address. |
| Scope | If known | Project-shared or global/personal; discover current conventions if unspecified. |
| Applicable paths | No | File patterns that should cause a scoped rule to load. |

## Workflow

1. Choose project `.claude/rules/` or global `~/.claude/rules/` based on whether the guidance is shared.
2. Keep one topic per file and use a descriptive filename.
3. Add `paths:` globs when the rule should load only for matching files; omit them when it should load at session start.
4. Write concise, checkable guidance. If the main instructions file approaches 200 lines, consider splitting topic-specific guidance into rules.
5. Use hooks or permissions instead when a requirement needs enforcement rather than model guidance.

## Validation

- [ ] The rule is in the intended scope and addresses one topic.
- [ ] Any `paths:` patterns match the intended files.
- [ ] Requirements that need deterministic enforcement are not represented as a rule alone.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Treating a rule as guaranteed enforcement | Use hooks or permissions for guarantees. |
| Adding an overly broad path pattern | Scope the rule to the smallest relevant set of files. |
| Combining unrelated topics in one file | Split the content into focused rule files. |
| Using global rules for team requirements | Put shared rules in the project configuration. |

## References

See the plugin README for the directory overview.

- [API design rule](./references/api-design.md)
- [Global rules](./references/global.md)
- [Testing rule](./references/testing.md)
