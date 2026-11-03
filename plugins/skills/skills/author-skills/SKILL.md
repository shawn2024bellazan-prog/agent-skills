---
name: author-skills
description: "Author reusable AGENTS skills: a SKILL.md entrypoint with actionable on-demand instructions and optional supporting files. Use when creating or editing a skill invoked by name; use author-commands for a focused single-file prompt."
---

# Skills

## Purpose

Create a focused, on-demand AGENTS skill whose description routes it to the right requests and whose body adds useful, verifiable guidance beyond the unassisted model.

## When to Use

- Creating a skill directory with a `SKILL.md` entrypoint.
- Improving an existing skill's routing description, workflow, references, or supporting assets.
- Deciding whether reusable task guidance belongs in a skill or a single-file command.

## When Not to Use

- Creating a single focused slash command without supporting files; use `author-commands`.
- Creating a custom subagent definition; use `author-agents`.
- Importing skill conventions from an unrelated marketplace or validator without confirming compatibility with this repository.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Skill name | Yes | Lowercase letters, numbers, and hyphens; match the directory name. |
| Purpose and triggers | Yes | The outcome, concrete user requests, and nearby tasks the skill should not claim. |
| Workflow | Recommended | Ordered steps with observable checkpoints and stop conditions. |
| Supporting files | No | References, scripts, or assets needed to complete the workflow. |

## Workflow

1. Confirm the work is a reusable, on-demand workflow. Discover the plugin's existing layout and follow this repository's `plugins/<plugin>/skills/<name>/SKILL.md` convention.
2. Write a concise description that names concrete triggers and separates the skill from its nearest sibling by the actual decision point. Keep it within the host's supported metadata limits and avoid XML-like text.
3. Design the body to add specific decisions, checks, stop conditions, and output expectations that improve on a baseline response. Do not pad it with generic advice.
4. Use relevant sections such as purpose, when to use/not use, inputs, workflow, validation, and common pitfalls. Include only sections that give this skill useful, actionable guidance.
5. Keep `SKILL.md` focused. Move detailed examples and supporting material into `references/`, `scripts/`, or `assets/`, and link to them with paths relative to `SKILL.md`.
6. Preserve project/global distinctions in the documented AGENTS subject. In this repository, `.agents/` is reserved for Codex marketplace metadata and repository-maintenance assets; do not move AGENTS skill content there.
7. Check plugin conventions before adding evaluation files or ownership entries. Use this repository's supported validation and test conventions; do not assume the unrelated .NET `eval.yaml` or validator workflow applies.
8. Remember that this repository ignores `.claude/skills/*`; if the task creates a project skill there, add the necessary `.gitignore` negation for that skill.

## Validation

- [ ] The skill name matches its folder and follows the repository's naming convention.
- [ ] Frontmatter parses, and the description is concrete, relevant, and within supported limits.
- [ ] The body is focused, actionable, and includes explicit validation and stop conditions where needed.
- [ ] Bundled-file references are relative to the skill directory and point to existing files.
- [ ] The entrypoint follows the current plugin layout and preserves AGENTS project/global scope.
- [ ] Any evaluation or ownership additions follow existing repository conventions rather than being copied from another project.

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| A vague description fails to route matching requests | Include concrete triggers and distinguish the nearest sibling skill. |
| Restating generic advice the model already knows | Encode the specific decision, verification, or stop condition this workflow needs. |
| Treating every recommended section as mandatory boilerplate | Keep only sections that improve the skill's decisions or outcomes. |
| Using absolute installation paths for bundled resources | Reference `./references/...`, `./scripts/...`, or `./assets/...` relative to the skill. |
| Assuming an upstream validator or eval format exists here | Check the plugin and repository's actual validation conventions first. |
| Placing AGENTS content under `.agents/` | Preserve this repository's Codex metadata boundary and existing plugin paths. |
| Adding a project skill without accounting for ignore rules | Add a targeted `.gitignore` negation for the new `.claude/skills/<name>/` path. |

## References

See [the plugin README](../../README.md) for the directory overview.

- [Checklist](./references/checklist.md)
- [Global skills](./references/global.md)
- [Security review example](./references/security-review.md)
- [Skill entrypoint](./references/skill-entrypoint.md)
