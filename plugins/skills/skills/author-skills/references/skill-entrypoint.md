# SKILL.md

> Entrypoint: trigger, invocability, instructions

**Scope:** project  (.agents/skills/security-review/SKILL.md)

**When it loads:** The user types /security-review <target>; the agent cannot auto-invoke this skill.

This skill uses disable-model-invocation: true so only you can trigger it. The !`...` line runs a shell command and injects its output into the prompt. $ARGUMENTS substitutes whatever you typed after the skill name. The agent sees the skill directory path, so mentioning a bundled file like checklist.md lets it read it.

## Example

```markdown
---
description: Reviews code changes for security vulnerabilities, authentication gaps, and injection risks
disable-model-invocation: true
argument-hint: <branch-or-path>
---

## Diff to review

!`git diff $ARGUMENTS`

Audit the changes above for:

1. Injection vulnerabilities (SQL, XSS, command)
2. Authentication and authorization gaps
3. Hardcoded secrets or credentials

Use checklist.md in this skill directory for the full review checklist.

Report findings with severity ratings and remediation steps.
```

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
