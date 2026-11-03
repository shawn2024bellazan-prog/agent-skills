# skills/

> Reusable prompts you or the agent invoke by name

**Scope:** project  (.agents/skills/)

**When it loads:** Invoked with /skill-name, or when the agent matches the task to a skill.

Each skill is a folder with a SKILL.md file plus any supporting files it needs. By default both you and the agent can invoke a skill. Frontmatter controls that: disable-model-invocation: true makes it user-only (for workflows like /deploy), and user-invocable: false hides it from the / menu while the agent can still invoke it.

## Tips

- Skills accept arguments: /deploy staging passes "staging" as $ARGUMENTS. Use $0, $1, and so on for positional access
- The description frontmatter determines when the agent auto-invokes the skill
- Bundle reference docs alongside SKILL.md. The agent knows the skill directory path and can read supporting files when you mention them

_Source: Claude Code docs, Explore the .claude directory (captures in G:\ProjectName\docs\claude-directory-screenshots)._
