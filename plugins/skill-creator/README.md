# skill-creator/

> Author new agent skills

**Scope:** project or global, depending on where the skill folder is created

**When it loads:** a skill's name and description load at session start; its SKILL.md body loads when the skill is invoked; references, assets, and scripts load on demand.

This plugin helps create a new skill: a folder containing a `SKILL.md` entrypoint plus optional `references/`, `assets/`, and `scripts/`. It scaffolds the structure, drafts focused instructions, and runs a validation checklist before the skill is committed.

## Skills

| Skill | Purpose |
|-------|---------|
| `create-skill` | Scaffold and validate a new skill folder from a stated purpose. |

## Tips

- Write the `description` for triggering: say what the skill does and when to use it.
- Keep `SKILL.md` focused; move detailed examples into `references/` and link to them.
- Use `scripts/` only for steps that must be deterministic, and `assets/` for templates or fixtures.

_Source: AGENTS docs on skills; see the `skills` plugin in this marketplace for the directory reference._
