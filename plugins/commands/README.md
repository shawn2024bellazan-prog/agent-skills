# commands/

> Single-file prompts invoked with /name

**Scope:** project  (.claude/commands/)

**When it loads:** The user types /command-name.

Commands and skills are now the same mechanism. For new workflows, use skills/ instead: same /name invocation, plus you can bundle supporting files. A file at commands/deploy.md creates /deploy the same way a skill at skills/deploy/SKILL.md does, and both can be auto-invoked by the agent.

## Tips

- Use $ARGUMENTS in the file to accept parameters: /fix-issue 123
- If a skill and command share a name, the skill takes precedence
- New commands should usually be skills instead; command files still work

_Source: AGENTS docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
