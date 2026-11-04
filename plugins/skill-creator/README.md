# skill-creator/

> Author new agent skills

**Scope:** project or global, depending on where the skill folder is created

**When it loads:** a skill's name and description help route it; the runtime instructions load when invoked; linked resources load only when needed.

The creator defaults to a concise, model-efficient skill containing only SKILL.md. It adds references, assets, scripts, maintainer docs, evaluations, or host projections only when the task and target conventions need them. The creator itself includes reusable templates for those optional layers.

## Skills

| Skill | Purpose |
|-------|---------|
| create-skill | Create and validate a focused skill, scaling its package to the task and target runtime. |

## Choose the smallest useful package

| Profile | Files |
|---------|-------|
| Focused skill | SKILL.md only |
| Extended skill | SKILL.md plus the references, assets, or scripts actually used |
| Modular product skill | Focused SKILL.md plus a product architecture reference and only the supporting resources required to generate and validate the complete product |

Do not create empty directories, placeholder indexes, or boilerplate sections just to fill out a package. Keep repository-level evaluations separate from portable skill resources. For small or local models, keep the common path concise and add detail only when it improves the result.

## Progressive disclosure

- Write a specific description so the runtime can select the skill without loading its full body.
- Keep the common procedure and important boundaries in SKILL.md.
- Move detailed examples, schemas, and rare paths into a reference only when needed.
- Put reusable prompts, forms, or fixtures in assets only when the workflow uses them.
- Add deterministic scripts only when they provide a real benefit; document runner, inputs, effects, and outputs when scripts exist.
- Avoid repeating the same instructions in SKILL.md, README, prompt, command, and host projections.

## Templates

The create-skill skill contains copyable templates for the entrypoint and optional resources.

| Template | Creates |
|----------|---------|
| [SKILL.md](skills/create-skill/assets/templates/SKILL.md.template) | Concise, portable skill entrypoint |
| [README.md](skills/create-skill/assets/templates/README.md.template) | Optional maintainer overview for a package with multiple resources |
| [References index](skills/create-skill/assets/templates/references/README.md.template) | Optional index when reference files exist |
| [Detailed reference](skills/create-skill/assets/templates/references/reference-document.md.template) | Optional long-form guidance |
| [Modular product blueprint](skills/create-skill/assets/templates/references/modular-product-blueprint.md.template) | Full module inventory, contracts, integration, automation, and acceptance plan |
| [Assets index](skills/create-skill/assets/templates/assets/README.md.template) | Optional index when asset files exist |
| [Prompt template](skills/create-skill/assets/templates/assets/prompt-template.md.template) | Optional fill-in prompt for a repeated task |
| [Scripts index](skills/create-skill/assets/templates/scripts/README.md.template) | Optional runtime contract and helper index when scripts exist |
| [Command adapter](skills/create-skill/assets/templates/commands/command.md.template) | Optional host-specific command entrypoint |

The optional [draft prompt](skills/create-skill/assets/skill-draft-prompt.md) produces the smallest useful package by default. Skills may already be slash-invokable; add a separate command only when a target host requires it. Approval and denial actions require a real policy and authorized reviewer.

For repositories that require skill evaluations, place eval files in that repository's test layout rather than in the portable skill package. Keep hosted workflow execution on its declared runner unless a supported local mode is explicitly requested.
