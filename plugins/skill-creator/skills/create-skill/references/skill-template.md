# Skill template

Copy this into `<skill-name>/SKILL.md` and fill it in.

````markdown
---
name: <skill-name>
description: "<What the skill does>. Use when <trigger cues>."
---

# <Title>

## Purpose

<One or two sentences.>

## When to Use

- <Situation>

## When Not to Use

- <Situation, and which skill to use instead>

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| <Input> | Yes | <Description> |

## Workflow

1. <Step>

## Validation

- [ ] <Check>

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| <Pitfall> | <Solution> |

## References

- [<Reference>](./references/<file>.md)
````

## Folder layout

```text
<skill-name>/
├── SKILL.md
├── references/   optional: detailed docs and examples
├── assets/       optional: templates and fixtures
└── scripts/      optional: deterministic helpers
```
