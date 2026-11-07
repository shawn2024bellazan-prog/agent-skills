---
name: pmcro-invocation
description: "Construct structured PMCR-O messages with task context, capability calls, lifecycle-agent handoffs, plugin-agent routes, constraints and expected evidence. Use for every PMCR-O request, delegation or result."
---

# PMCR-O structured invocation protocol

## Purpose and profile

Primary profile: Schema/Contract + Procedural. Define the common message envelope and invocation decision rules. A message is not an agent identity, tool binding, permission grant or execution receipt.

## Canonical agent-plugin handoff

Use this compact form when an addressed agent must receive a seed through a plugin-scoped agent entrypoint:

~~~text
@<AGENT>
/agent-<PLUGIN>
"<NEXT_SEED_INTENT>"
~~~

- @<AGENT> identifies the accountable agent.
- /agent-<PLUGIN> addresses the plugin's agent entrypoint or a shared agent service such as /agent-orchestrator.
- The quoted text is the SeedIntent payload; preserve it verbatim and retain its provenance.
- /agent-orchestrator is the shared pre-invocation selection route. It discovers plugin ownership, inspects skill descriptions, selects the smallest relevant skill set, and coordinates dispatch.
- A route is executable only when the active host has registered it to a real agent entrypoint. Until verified, treat it as a logical protocol address.

Example:

~~~text
@PLUGIN-CREATOR
/agent-orchestrator
"Inspect the agent-skills repository. Determine which plugin owns the requested functionality, select the correct skill, and coordinate the required plugin update."
~~~

The selected skill is a separate object. Invoke the exact skill identifier through the target host's supported mechanism; do not assume /agent-<PLUGIN> itself loads a skill.

## Required PMCR-O lifecycle envelope

~~~yaml
@ORCHESTRATOR
/pmcro:<domain>:<action>

TASK:
  "<What needs to happen>"

CONTEXT:
  "<Relevant project, repository, or lifecycle context>"

INPUT:
  "<Source material, references, or artifacts>"

CAPABILITY_DISPATCH:
  - capability: "pmcro:<capability>"
    task: "<Specific capability task>"
    expect: "<Expected output>"

AGENT_DISPATCH:
  - agent: "@PLANNER"
    task: "<Planning responsibility>"
    expect: "PLAN_FRAME"

  - agent: "@MAKER"
    task: "<Authorized implementation responsibility>"
    expect: "IMPLEMENTATION_ARTIFACTS"

  - agent: "@CHECKER"
    task: "<Independent verification responsibility>"
    access: READ_ONLY
    expect: "VERIFICATION_RESULT"

  - agent: "@REFLECTOR"
    task: "<Evidence-based reflection>"
    expect: "REFLECTION_RESULT"

CONSTRAINTS:
  - preserve_role_boundaries
  - enforce_authorization
  - record_actual_execution
  - preserve_evidence_integrity
  - never_claim_unverified_execution

EXPECT:
  result: "<EXPECTED_RESULT_TYPE>"
  readiness: READY | PARTIAL | BLOCKED
  evidence: REQUIRED
~~~

## Address namespaces

- Agent identity: @AGENT identifies the accountable agent.
- Plugin-agent route: /agent-<PLUGIN> identifies a host-facing agent entrypoint; /agent-orchestrator is the shared pre-invocation selection route when registered.
- Subagent route: /pmcro:subagent:<agent-id> is a logical PMCR-O subagent address only where the host maps it to a real isolated context.
- Capability/skill route: invoke the exact registered plugin/skill identifier, for example pmcro-skill-creator/skill-creator. A skill is not an agent identity.
- Logical lifecycle action: /pmcro:<domain>:<action> is callable only when the active host has registered an exact mapping. Do not invent commands such as /pmcro:cycle:resume.

## Invocation resolution

1. Preserve the raw SeedIntent and determine whether the request addresses an agent, plugin, skill, command, or lifecycle operation.
2. Resolve the exact agent and plugin route from the active host registry. A textual route is not proof of registration.
3. For plugin-agent work, use the PMCR-O Agent Orchestrator capability to inspect the target plugin manifest and skill descriptions before loading any full skill.
4. Select the owning plugin's smallest relevant skill set; prefer native plugin ownership over adapter duplication.
5. Load only the selected SKILL.md and supporting resources actually needed.
6. Invoke the exact skill using the active host's registered mechanism. Do not assume a tool named load_skill exists unless the host registers it.
7. Record route, loading, authorization, dispatch and execution as separate states.
8. If no host route exists, keep the logical address in message metadata and report it unavailable. If no skill exists, report CAPABILITY_MISSING.

## Construction rules

1. Preserve the top-level order: addressed agent/invocation, TASK, CONTEXT, INPUT, CAPABILITY_DISPATCH, AGENT_DISPATCH, CONSTRAINTS, EXPECT.
2. Keep capability/skill dispatch separate from @AGENT dispatch. A skill is not an agent.
3. Give every dispatch a bounded task, necessary inputs, allowed scope and expected typed result.
4. Include only relevant agents/capabilities, but include all required lifecycle roles when the requested cycle requires them.
5. Checker must be read-only and structurally independent. A label change is not independence.
6. A plan/bootstrap does not grant project mutation. Maker needs a current host-issued grant scoped to a validated PlanFrame.
7. If a runtime cannot create isolated agent contexts, mark the handoff unavailable or unverified; do not claim that a textual @mention dispatched it.
8. Preserve evidence references in result messages.

## Result vocabulary

- SUCCEEDED: actual configured integration returned success.
- REJECTED: actual target rejected the operation.
- FORBIDDEN: actual permission boundary denied it.
- UNSUPPORTED: target does not provide the capability.
- CAPABILITY_MISSING: no configured implementation or entrypoint exists.
- AUTHORIZATION_REQUIRED: policy requires an authorization decision before dispatch.
- UNVERIFIED: evidence is insufficient to establish outcome.
- NOT_EVALUATED: Checker could not evaluate because required evidence or independent context was absent.

## Validation

- [ ] Exact marketplace skill/command exists or adapter mapping is evidenced.
- [ ] Task, context and inputs are explicit.
- [ ] Capability and agent dispatch are distinct.
- [ ] Each handoff has a bounded task and expected result.
- [ ] Authorization and read/write boundaries are visible.
- [ ] No execution claim is made without host evidence.
