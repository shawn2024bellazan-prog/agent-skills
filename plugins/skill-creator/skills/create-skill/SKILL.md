---
name: create-skill
description: "Create a new agent skill: scaffold the folder with SKILL.md, references, assets, and scripts, draft focused instructions, and validate the result. Use when asked to make, add, or start a new skill."
---

# Create a skill

## Purpose

Turn a stated purpose into a well-formed skill folder that an agent can discover, trigger, and follow.

## When to Use

- Creating a new skill from a description of a repeatable task.
- Turning an ad hoc workflow into a reusable skill.

## When Not to Use

- Editing a single existing skill's wording only; edit its `SKILL.md` directly.
- Documenting the `skills/` directory itself; see the `skills` plugin.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Skill name | Yes | Lowercase kebab-case, matching the folder name. |
| Purpose | Yes | What the skill does and the task it repeats. |
| Trigger cues | No | Phrases or situations that should invoke it. |
| Destination | No | Parent `skills/` directory; defaults to the current plugin or project. |

## Workflow

1. Confirm the name is kebab-case and does not already exist at the destination.
2. Create `<destination>/<name>/SKILL.md` with frontmatter (`name`, `description`) and the sections used in [the template](./references/skill-template.md).
3. Write the `description` to say what the skill does and when to use it.
4. Keep the body short. Move long examples or background into `references/` and link them from `SKILL.md`.
5. Add `scripts/` only for deterministic steps and `assets/` only for templates or fixtures the skill uses.
6. Run the validation checklist below and fix anything that fails.

## Validation

- [ ] Folder name equals the frontmatter `name`.
- [ ] `description` states both what the skill does and when to use it.
- [ ] `SKILL.md` has Purpose, When to Use, When Not to Use, Inputs, Workflow, Validation, and Common Pitfalls.
- [ ] Every linked file under `references/`, `assets/`, or `scripts/` exists.
- [ ] No machine-specific paths unless labeled as examples.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Vague description that never triggers | Name the task and the cues that should invoke the skill. |
| Oversized `SKILL.md` | Move detail into `references/` and link to it. |
| Broken links after moving files | Re-run the validation checklist. |

## References

- [Skill template](./references/skill-template.md)
