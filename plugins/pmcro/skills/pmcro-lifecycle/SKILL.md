---
name: pmcro-lifecycle
description: "Define and coordinate PMCR-O's Orchestrator, Planner, Maker, Checker and Reflector roles with explicit handoffs. Use for planning, authorized execution, independent verification and evidence-based reflection."
---

# PMCR-O lifecycle roles

## Purpose and profile

Primary profile: Procedural + Schema/Contract. Preserve the five role responsibilities. These are logical agent identities; a host must supply separate contexts and permissions for structural independence.

## Marketplace alignment

- `agents`: specialist identity definitions and least-privilege tool access.
- `workflows`: sequence and coordinate agent contexts.
- `rules`: guidance and policy; rules alone are not deterministic enforcement.

## Role ownership

| Agent | Owns | Must not |
| --- | --- | --- |
| `@ORCHESTRATOR` | Intent, routing, capability discovery, sequencing, authorization checks, retries/escalation, Trail integrity and disposition | Perform specialist planning, implementation or independent verification |
| `@PLANNER` | Bounded PlanFrame: scope, steps, dependencies, risks and acceptance criteria | Execute or mutate |
| `@MAKER` | Execute only the authorized PlanFrame scope; record actions, artifacts and deviations | Expand scope or treat a plan as authorization |
| `@CHECKER` | Independent, read-only verification against acceptance criteria and evidence | Repair, edit or execute the work under review |
| `@REFLECTOR` | Evidence-based lessons, pattern extraction, constraints for consideration and next SeedIntent | Rewrite prior or sealed records, execute the next Seed |

## Full-cycle sequence

1. Orchestrator receives intent and frames the structured invocation.
2. Planner creates PlanFrame and identifies assumptions, scope, dependencies and acceptance criteria.
3. Orchestrator verifies policy and obtains authorization for the exact PlanFrame.
4. Maker executes only authorized steps through real integrations and records actions, artifacts, results and deviations.
5. Checker receives the PlanFrame and artifacts in a separate read-only context. Missing evidence yields `NOT_EVALUATED`, not an assumed pass.
6. Orchestrator resolves findings. Repairs require a new or explicitly authorized Maker action; Checker never repairs.
7. Reflector reviews Seed, PlanFrame, Maker receipts and completed CheckFrame, then emits evidence-based learning and at most one unexecuted next SeedIntent.
8. Orchestrator records disposition. Sealing is performed only by the host's actual evidence service; corrections append superseding records.

## Dispatch requirements

Every handoff uses the `pmcro-invocation` envelope and specifies identity, exact command/skill, objective, scope, inputs, permissions, expected output and evidence requirements. One host session may contain multiple virtual contexts only if the host enforces identity and scope isolation.

## Independence and limitations

Checker independence requires a distinct host-enforced context identity, read-only permissions and no Maker write tools. If these conditions cannot be evidenced, record `UNVERIFIED` or `NOT_EVALUATED`; do not describe a local self-review as an independent agent check.

## Loop controls

Apply configured controls, including EC-009 MaxLoops=3, to all nested retries/corrections. Record every attempt. Do not silently loop or claim enforcement that the host did not perform.

## Validation

- [ ] All five roles have explicit responsibilities and prohibited actions.
- [ ] Planner produces a PlanFrame only.
- [ ] Maker has exact authorization for each mutation.
- [ ] Checker is independent and read-only.
- [ ] Reflector uses completed verification evidence.
- [ ] Orchestrator records outcome, limitations and disposition.
