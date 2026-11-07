# PMCR-O integration

> Portable PMCR-O capability and lifecycle contracts aligned with the Agent Skills marketplace.

This plugin packages PMCR-O's invocation conventions, bootstrap sequence, lifecycle role boundaries, marketplace mapping, host/genome contract, memory distinctions, agent/skill selection, and evidence governance as discoverable Agent Skills. It also provides one PMCR-O coordination adapter skill for each of the eleven existing marketplace plugins; the native plugin remains the owner of its implementation.

It is an **architecture and instruction package**, not a PMCR-O execution daemon. A host must provide real dispatch, identity isolation, authorization, tools, persistence, and evidence services before any skill can claim those operations occurred.

## Skills

| Skill | Purpose | Marketplace alignment |
| --- | --- | --- |
| [pmcro-init](skills/pmcro-init/SKILL.md) | Bootstrap foundational capabilities and evaluate readiness | commands, workflows, agent-config |
| [pmcro-invocation](skills/pmcro-invocation/SKILL.md) | Structured invocation and result messages, including agent-plugin handoffs | commands, skills, output-styles |
| [pmcro-lifecycle](skills/pmcro-lifecycle/SKILL.md) | Five lifecycle roles and handoff boundaries | agents, workflows, rules |
| [pmcro-marketplace](skills/pmcro-marketplace/SKILL.md) | Align capabilities with all eleven existing marketplace categories (ten directory-reference categories plus skill-creator) | All eleven existing plugin categories |
| [pmcro-host](skills/pmcro-host/SKILL.md) | Separate portable genome, host adapter, and runtime state | agent-config, skills, workflows |
| [pmcro-memory](skills/pmcro-memory/SKILL.md) | Separate agent, project, cycle, and runtime memory | agent-memory, projects, agents |
| [pmcro-governance](skills/pmcro-governance/SKILL.md) | Authorization, outcomes, verification, and evidence integrity | rules, agents, workflows |
| [pmcro-reflector-seed-handoff](skills/pmcro-reflector-seed-handoff/SKILL.md) | Layered Reflector seed handoff to Skill Creator | workflows, skill-creator, skills |
| [pmcro-agent-config](skills/pmcro-agent-config/SKILL.md) | Coordinate target-host configuration discovery and authorized updates | agent-config, pmcro-host |
| [pmcro-agent-memory](skills/pmcro-agent-memory/SKILL.md) | Resolve and manage scoped subagent memory without mixing evidence planes | agent-memory, pmcro-memory |
| [pmcro-agents](skills/pmcro-agents/SKILL.md) | Resolve lifecycle agent identity, isolation, and subagent dispatch | agents, pmcro-lifecycle |
| [pmcro-agent-orchestrator](skills/pmcro-agent-orchestrator/SKILL.md) | Resolve plugin ownership, cognitively select the minimum relevant skills, and coordinate pre-invocation dispatch | agents, skills, commands, pmcro-invocation |
| [pmcro-commands](skills/pmcro-commands/SKILL.md) | Discover and validate command/route registrations without inventing routes | commands, pmcro-invocation |
| [pmcro-output-styles](skills/pmcro-output-styles/SKILL.md) | Apply presentation styles without changing policy or role boundaries | output-styles, pmcro-invocation |
| [pmcro-projects](skills/pmcro-projects/SKILL.md) | Retrieve project context while preserving memory-scope distinctions | projects, pmcro-memory |
| [pmcro-rules](skills/pmcro-rules/SKILL.md) | Evaluate applicable rules and distinguish guidance from host enforcement | rules, pmcro-governance |
| [pmcro-skill-creator](skills/pmcro-skill-creator/SKILL.md) | Create and validate bounded skills using the existing creator capability | skill-creator, pmcro-reflector-seed-handoff |
| [pmcro-skills](skills/pmcro-skills/SKILL.md) | Discover and invoke exact installed skills through supported host mechanisms | skills, pmcro-invocation |
| [pmcro-themes](skills/pmcro-themes/SKILL.md) | Discover and apply visual themes without changing operational policy | themes |
| [pmcro-workflows](skills/pmcro-workflows/SKILL.md) | Validate and coordinate multi-step workflow execution and evidence | workflows, pmcro-lifecycle |

## Core architecture

- The deployment's .agents/ directory is the portable authored genome: agent definitions, skills, capabilities, policies, workflows, and host initialization contracts.
- pmcro:host:init is the bootstrap contract defined by that genome; a real host adapter executes it.
- The deployment's .pmcro/ directory is the runtime and evidence plane: sessions, queues, authorization decisions, invocation records, trails, artifacts, and receipts.
- pmcro:init is the root bootstrap workflow. It initializes foundational capabilities; it does not authorize arbitrary project execution.
- The compact handoff is @<AGENT> → /agent-<PLUGIN> → quoted NEXT_SEED_INTENT. /agent-orchestrator is the shared pre-invocation selector when a host registers it. The selector resolves plugin ownership and skill descriptions before loading the minimum needed capability.
- Capability dispatch (pmcro:*) and lifecycle-agent dispatch (@AGENT) remain distinct operations. Address a PMCR-O subagent with /pmcro:subagent:<agent-id> only where the host maps it; invoke a skill by its exact registered skill identifier.
- The colon-form /pmcro:<domain>:<action> is a protocol address only when a host maps it; marketplace skill invocation uses the actual installed skill name. Never invent a command such as /pmcro:cycle:resume.
- The five lifecycle roles are structurally isolated. Checker is read-only and cannot repair the work it evaluates.

## Repository boundary

This repository's own root .agents/ directory is reserved for Codex marketplace metadata and repository-maintenance assets. The PMCR-O deployment genome described by this plugin is a target-host contract, not a claim that this repository already contains a live PMCR-O runtime or genome. Do not repurpose this repository's marketplace directory as deployment runtime state.

## Reflector-to-Skill-Creator loop

Reflector can emit a single bounded hierarchy of META_SEED_INTENT, META_META_SEED_INTENT, and META_META_META_SEED_INTENT. The structured handoff targets the existing PMCR-O Skill Creator capability. The three levels refine (1) the concrete skill, (2) the reusable skill-authoring method, and (3) the broader skill-creation system. They remain unexecuted intent until separately planned and authorized. The Skill Creator does not inherit Reflector authority or mutate creator governance.

## Host and execution truth

A skill may describe an invocation, but a prompt is not an execution primitive or permission grant. Only a configured host adapter can dispatch an implementation and return host-issued evidence. Report missing integrations, forbidden operations, unsupported capabilities, and authorization requirements explicitly. Never fabricate agent runs, cycle IDs, receipts, hashes, grants, timestamps, test results, or sealed Trails.

## Versioning and compatibility

The root, Claude, and Codex plugin manifests are synchronized. Host-specific execution support must be established by an actual implementation and validation in that host; listing a host in documentation is not proof of compatibility.
