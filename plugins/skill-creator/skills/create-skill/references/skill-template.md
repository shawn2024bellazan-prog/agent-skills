# Skill scaffold profiles and progressive disclosure

Use templates under [assets/templates/](../assets/templates/) as needed. A generated skill does not need every support folder.

## Choose the package size

### Focused

Create a single SKILL.md with a specific description, the common workflow, important boundaries, and an observable result. This is the default for a narrow task or a small/local model.

### Extended

Add only the resources that solve a real problem:

- references for detailed examples, schemas, or rare paths that would overload the entrypoint;
- assets for reusable prompts, forms, fixtures, or other task materials;
- scripts for deterministic work that genuinely benefits from automation;
- a README or folder index when maintainers need a resource map or the target repository requires one;
- a host-specific command or adapter only when that host requires it.

Do not create empty support folders, placeholder files, or repeated instructions. If no extra file is needed, stop at SKILL.md.

### Complete modular product

When a skill must produce a complete repository or application, use the [modular product blueprint](../assets/templates/references/modular-product-blueprint.md.template) as a source when drafting a focused reference. The ProjectName example was inspected read-only as a pattern with distinct BuildingBlocks, Governance, Hosting/AppHost, Protocols, Runtime, Services, clients, MCP, SDK, templates, tests, documentation, and engineering scripts. These are examples, not required modules for unrelated products.

Enumerate deliverables, module owners and public contracts, allowed dependency direction, and wiring through the declared composition host. Include integrations, configuration, automation, documentation, validation, and evidence in scope. Do not stop at an empty directory tree or placeholder projects. Add only the supporting package files required to make that generation reproducible.

## Progressive disclosure

1. **Discovery:** Keep name and description concise and specific so the runtime can decide whether to load the skill.
2. **Runtime entrypoint:** Put the common procedure, task-specific decisions, boundaries, and observable output in SKILL.md.
3. **Supporting detail:** Put longer examples and infrequent paths in linked references; load them only when the workflow reaches that detail.
4. **Reusable materials:** Add assets only when a task uses them. They are task inputs or output templates, not hidden instructions.
5. **Deterministic helpers:** Add scripts only when they improve reliability or reduce repetitive work. Document their runner, inputs, effects, and outputs when needed.
6. **Repository metadata:** Keep evals, CODEOWNERS entries, manifests, and other repository policy files in the target repository's established locations; they are not automatically part of a portable skill package.

## Portable source and host projections

DotAgents-style setups can keep portable skill or plugin sources separate from generated harness-specific outputs. Treat the portable source as canonical. Add or regenerate only the projections required by selected hosts; do not author redundant copies or assume every host supports the same commands, permissions, or model settings. Preserve generated ownership markers and source provenance where the target tool requires them.

A skill may already be callable by slash name. A separate command file is optional and host-specific; keep it short and delegate to the skill rather than duplicating its instructions.

## Runtime and authority

When a workflow uses tools, models, hosted actions, or side effects, document the relevant execution boundary in the smallest useful place:

- execution host or runner;
- invoked workflow, action, or existing skill;
- model/provider/runtime and configuration source;
- required permissions, network access, and secret names (never values);
- observable outputs/evidence and the authorized decision-maker.

A hosted action may invoke an existing Aspire setup skill if the workflow declares that integration. Ollama is used only when its endpoint/model is configured. Do not treat model availability as worker readiness, approval, or authority. Do not run an action or its helper locally as an automatic part of authoring.

## Repository-level evaluations

Some skill repositories use evals to compare skill-assisted output against a baseline model. Keep those scenarios in the repository's own test/evaluation tree rather than adding them to every skill bundle. The dotnet/skills convention places evals in a tests directory organized by plugin and skill, with repository-specific validation and ownership rules. Create eval scaffolding only when the target repository requires it and the test has meaningful, distinct scenarios.

## Template map

Copy only the templates needed for the selected profile:

- [SKILL.md template](../assets/templates/SKILL.md.template) — focused entrypoint.
- [Package README template](../assets/templates/README.md.template) — optional maintainer overview.
- [References index template](../assets/templates/references/README.md.template) — optional, when reference files exist.
- [Detailed reference template](../assets/templates/references/reference-document.md.template) — optional, for real supporting detail.
- [Modular product blueprint](../assets/templates/references/modular-product-blueprint.md.template) — for complete modular-product generation.
- [Assets index template](../assets/templates/assets/README.md.template) — optional, when asset files exist.
- [Reusable prompt template](../assets/templates/assets/prompt-template.md.template) — optional, for a repeated fill-in prompt.
- [Scripts index template](../assets/templates/scripts/README.md.template) — optional, when scripts exist.
- [Command adapter](../assets/templates/commands/command.md.template) — optional and host-specific.

The creator's [draft prompt](../assets/skill-draft-prompt.md) is itself an optional authoring aid and does not need to be copied into generated skills.
