---
name: pmcro-invocation
description: "Construct structured PMCR-O messages with task context, capability calls, lifecycle-agent handoffs, constraints and expected evidence. Use for every PMCR-O request, delegation or result."
---

# PMCR-O structured invocation protocol

## Purpose and profile

Primary profile: Schema/Contract + Procedural. Define the common message envelope and invocation decision rules. A message is not an agent identity, tool binding, permission grant or execution receipt.

## Required envelope

```yaml
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
```

## Address namespaces

- **Subagent route:** `@ORCHESTRATOR` addresses a subagent with `/pmcro:subagent:<agent-id>`, for example `/pmcro:subagent:agent-memory`. The host must resolve that agent identity and its implementation.
- **Capability/skill route:** invoke the exact registered plugin/skill identifier, for example `pmcro-skill-creator/skill-creator`. A skill is not an agent identity.
- **Logical lifecycle action:** `/pmcro:<domain>:<action>` is callable only when the active host has registered an exact mapping. Do not invent commands such as `/pmcro:cycle:resume`.

## Invocation resolution

The colon-form `/pmcro:<domain>:<action>` is a logical PMCR-O protocol address. It is callable only when the active host has a registered mapping for that exact address. Do not invent commands such as `/pmcro:cycle:resume` merely because they fit the naming pattern.

When no such mapping exists:
1. Resolve an installed/discoverable marketplace skill by its actual name (for example, `pmcro-marketplace`).
2. Identify the exact skill owner and expected output.
3. Keep the logical domain/action in the message metadata, not as a false claim that the slash command exists.
4. If no matching skill/adapter exists, report `CAPABILITY_MISSING`.

## Construction rules

1. Preserve the top-level order: addressed agent/invocation, TASK, CONTEXT, INPUT, CAPABILITY_DISPATCH, AGENT_DISPATCH, CONSTRAINTS, EXPECT.
2. Keep `pmcro:*` capability dispatch separate from `@AGENT` dispatch. A skill is not an agent.
3. Give every dispatch a bounded task, necessary inputs, allowed scope and expected typed result.
4. Include only relevant agents/capabilities, but include all required lifecycle roles when the requested cycle requires them.
5. Checker must be read-only and structurally independent. A label change is not independence.
6. A plan/bootstrap does not grant project mutation. Maker needs a current host-issued grant scoped to a validated PlanFrame.
7. If a runtime cannot create isolated agent contexts, mark the handoff unavailable or unverified; do not claim that a textual @mention dispatched it.
8. Preserve evidence references in result messages.

## Result vocabulary

- `SUCCEEDED`: actual configured integration returned success.
- `REJECTED`: actual target rejected the operation.
- `FORBIDDEN`: actual permission boundary denied it.
- `UNSUPPORTED`: target does not provide the capability.
- `CAPABILITY_MISSING`: no configured implementation or entrypoint exists.
- `AUTHORIZATION_REQUIRED`: policy requires an authorization decision before dispatch.
- `UNVERIFIED`: evidence is insufficient to establish outcome.
- `NOT_EVALUATED`: Checker could not evaluate because required evidence or independent context was absent.

## Validation

- [ ] Exact marketplace skill/command exists or adapter mapping is evidenced.
- [ ] Task, context and inputs are explicit.
- [ ] Capability and agent dispatch are distinct.
- [ ] Each handoff has a bounded task and expected result.
- [ ] Authorization and read/write boundaries are visible.
- [ ] No execution claim is made without host evidence.
