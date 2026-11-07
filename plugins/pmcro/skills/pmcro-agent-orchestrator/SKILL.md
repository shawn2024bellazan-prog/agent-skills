---
name: pmcro-agent-orchestrator
description: "Resolve the owning plugin and select the minimum relevant skill before dispatching an addressed agent task. Use for cross-plugin routing, pre-invocation skill selection, Plugin Creator coordination, or when an agent must choose which capability to load."
---

# PMCR-O Agent Orchestrator

## Purpose and profile

Primary profile: Orchestration + Retrieval + Schema/Contract + Validation.

Resolve the correct agent, plugin owner, and skill for a seed before work is dispatched. This is the shared pre-invocation selection capability. It is not a replacement for a domain agent, native plugin skill, host runtime, or the PMCR-O lifecycle Orchestrator.

## Invocation envelope

The canonical agent-plugin handoff is:

~~~text
@<AGENT>
/agent-<PLUGIN>
"<NEXT_SEED_INTENT>"
~~~

Interpret the fields as follows:

- The agent address identifies the accountable agent.
- The agent-plugin route identifies the requested plugin-scoped agent entrypoint.
- The quoted text is the next SeedIntent; preserve its wording and provenance.
- A route such as /agent-orchestrator is a logical address until the active host registers it to a real agent entrypoint.
- The host may use different native mention, command, workflow, or subagent syntax. Resolve the exact registered mechanism; never infer that slash-shaped text is executable.

Example:

~~~text
@PLUGIN-CREATOR
/agent-orchestrator
"Inspect the agent-skills repository. Determine which plugin owns the requested functionality, select the correct skill, and coordinate the required plugin update."
~~~

The shared Agent Orchestrator uses this skill to decide which native plugin capability should receive the task. The addressed Plugin Creator remains accountable for package composition and release work; it does not replace a native skill owner.

## Required inputs

- Raw SeedIntent and its provenance.
- Addressed agent identity, if supplied.
- Requested plugin route, if supplied.
- Target repository or project and exact source references.
- Available plugin inventory, manifests, skill entrypoints, and host registration state.
- Requested outcome, scope, constraints, and expected evidence.
- Authorization reference when a later operation may cause side effects.

## Identity and ownership model

Keep these objects separate:

| Object | Responsibility |
| --- | --- |
| Agent | Accountable actor with a bounded role and context. |
| Plugin | Distribution and capability-ownership package. |
| Skill | Reusable instructions and resources for one capability. |
| Command or route | Host-facing entrypoint that must be registered by the host. |
| Tool or integration | Actual callable operation supplied by the host. |
| PMCR-O lifecycle | Governance, authorization, evidence and disposition. |

A skill does not create an agent, a plugin does not prove runtime registration, and a route string does not prove dispatch.

## Procedure

### 1. Admit and classify the seed

1. Preserve the raw SeedIntent unchanged.
2. Identify the desired result, target artifact/repository, constraints, and whether the request is advisory, authoring, configuration, packaging, or execution.
3. Resolve the addressed agent and plugin route independently. If either is unknown, record the gap rather than guessing.
4. Determine whether the task belongs to one plugin or requires a bounded handoff across multiple owners.

### 2. Discover plugin ownership

1. Inspect the active marketplace catalog and the selected plugin's manifest.
2. Use the plugin's README and capability crosswalk when ownership is not obvious.
3. Enumerate that plugin's skill entrypoints and read their frontmatter names and descriptions first.
4. Confirm each candidate skill belongs to the intended plugin and exists at the referenced path.
5. Prefer the native plugin owner. A PMCR-O adapter may coordinate discovery and governance, but must not copy or supersede the native implementation.
6. Do not assume the current repository contains every runtime plugin or connector visible in another host. Distinguish repository packages from externally installed services.

### 3. Select the minimum relevant skill set

Evaluate candidates against:

- Outcome match: does the skill own the requested deliverable?
- Trigger match: do its description and activation criteria cover this request?
- Scope match: does it include the requested artifact, domain, and operation?
- Boundary match: is the requested work permitted by its role?
- Input readiness: are required inputs and references available?
- Host readiness: can the active host load and invoke this exact skill?

Select one primary skill for the work. Add another skill only when it owns a distinct required step or dependency. Do not load every skill in a plugin, and do not load a PMCR-O adapter and the native skill as duplicate executors.

If multiple candidates remain materially equivalent, return an AMBIGUOUS selection with the candidates and decision point. If no candidate exists, return CAPABILITY_MISSING. Do not invent a skill name or route.

### 4. Load progressively

1. Load only the selected skill's SKILL.md through the active host's supported mechanism.
2. Read a reference only when the entrypoint links to it or the task requires its detail.
3. Read assets only when they are actual inputs or templates for the work.
4. Execute scripts only when the host has a supported runner, required permissions, and applicable authorization.
5. Record whether each item is discovered, available, loaded, registered, authorized, invoked, or executed. These are distinct states.
6. Do not assume a tool called load_skill exists. Use it only if the active provider registers that exact tool; otherwise use the host's documented skill-loading mechanism.

### 5. Dispatch to the native owner

1. Build a bounded handoff with objective, inputs, scope, exclusions, expected output, and evidence requirements.
2. Invoke the selected native skill or agent using its exact registered host identifier.
3. If the route is logical but unregistered, report the host mapping as unavailable. Do not translate it into an invented command.
4. For plugin-package changes, coordinate the relevant content owner first and the Plugin Creator for manifests, package composition, versioning, and release.
5. For skill-content changes, use the native skill authoring owner; for agent-definition changes, use the agents owner; for command changes, use the commands owner; for workflow changes, use the workflows owner.
6. A selection or planning result is not authorization to mutate files, publish, deploy, or merge.

### 6. Apply PMCR-O governance

- Preserve parent/child SeedIntent lineage and correlation.
- Apply Log Before Act and Verify Before Mutation where configured.
- Planner creates PlanFrame; it does not execute.
- Maker performs only the exact authorized PlanFrame scope with a current host-issued grant.
- Checker is structurally independent and read-only; it never repairs.
- Reflector learns from completed CheckFrame evidence and emits at most one unexecuted next SeedIntent.
- A missing grant, host route, independent Checker context, or evidence writer must stop or constrain the operation appropriately.
- Never fabricate IDs, grants, receipts, hashes, tests, verdicts, approvals, or seals.

## Repository plugin ownership quick reference

Use this as a starting crosswalk only; verify the current manifest and skill entrypoint before every dispatch.

| Requested work | Native plugin | Primary skill |
| --- | --- | --- |
| Project/global AGENTS configuration | agent-config | configure-agent |
| Persistent subagent memory | agent-memory | manage-agent-memory |
| Subagent definition and tool scope | agents | author-agents |
| Single-file slash command | commands | author-commands |
| Reusable skill authoring | skills | author-skills |
| Skill creation workflow and package validation | skill-creator | create-skill |
| Dynamic multi-agent workflow | workflows | author-workflows |
| Topic-scoped instructions | rules | author-rules |
| Response presentation mode | output-styles | author-output-styles |
| Main-session per-project automatic memory | projects | manage-auto-memory |
| Global terminal color theme | themes | author-themes |

The repository's Plugin Creator connector is a separate host capability, not one of these eleven repository plugins. Use it only when the active host actually exposes it. Do not claim it is installed in this repository's marketplace.

## Output contract: AgentSelectionFrame

Return a structured selection record containing:

- raw_seed_ref or the preserved raw SeedIntent;
- addressed_agent and requested_route;
- target_repository_or_project;
- owning_plugin and manifest/source reference;
- selected_skill_ids and exact skill paths;
- selection_rationale and relevant alternatives considered;
- required_supporting_resources;
- host_route_state: REGISTERED | LOGICAL_ONLY | UNAVAILABLE;
- skill_load_state: NOT_LOADED | LOADED | PARTIAL | UNAVAILABLE;
- dispatch_state: NOT_DISPATCHED | DISPATCHED | FAILED;
- authorization_state: NOT_REQUIRED | REQUIRED | GRANTED | DENIED | UNKNOWN;
- expected_result_type, returned_artifact_refs, evidence_refs, assumptions, and blockers.

Do not fabricate host-generated references. Omit identifiers that the host did not issue.

## Stop conditions

Stop or return a bounded partial result when:

- the owning plugin or skill cannot be verified;
- required input artifacts are unavailable;
- the host cannot load or invoke the selected skill;
- the requested route is not registered;
- authority or authorization is missing;
- two skill owners have unresolved overlapping responsibility;
- the requested mutation exceeds the addressed agent's scope.

## Validation

- [ ] Raw SeedIntent and provenance are preserved.
- [ ] Agent, plugin, skill, route, tool and lifecycle authority are not conflated.
- [ ] The owning plugin is confirmed from the active inventory.
- [ ] Candidate descriptions were inspected before full skill loading.
- [ ] The smallest relevant skill set was selected with a recorded rationale.
- [ ] Only selected skills and needed resources were loaded.
- [ ] Host registration and actual dispatch are reported truthfully.
- [ ] Native plugin ownership is preserved.
- [ ] Any side effect has a validated PlanFrame and current host-issued authorization.
- [ ] Evidence and unresolved gaps are returned to the caller.
