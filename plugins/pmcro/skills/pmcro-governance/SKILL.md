---
name: pmcro-governance
description: "Apply PMCR-O authorization, role boundaries, execution outcome vocabulary, verify-before-mutation controls and evidence integrity. Use before actions that alter files, services, permissions or external state."
---

# PMCR-O governance and evidence

## Purpose and profile

Primary profile: Procedural + Validation + Schema/Contract. Governance instructions describe required controls; host enforcement remains the actual security boundary.

## Marketplace alignment

- `rules`: policy and constraints.
- `agents`: least-privilege roles and tool declarations.
- `workflows`: ordered action and verification gates.

## Before acting

1. Log intended action before dispatch (EC-SYS-003 Log Before Act, when configured).
2. Verify target/current state before mutation (EC-VERIFY-FIRST-001 Verify Before Mutation, when configured).
3. Resolve exact identity, tool, resource, permission, side-effect and authorization scope.
4. Require a validated PlanFrame and current host-issued grant for Maker project execution.
5. Stop if authorization is absent, expired, ambiguous, or broader than requested.

## Outcome vocabulary

- `SUCCEEDED`: actual integration returned success.
- `REJECTED`: actual target rejected the operation.
- `FORBIDDEN`: actual permission boundary denied access.
- `UNSUPPORTED`: target lacks the capability.
- `CAPABILITY_MISSING`: no configured implementation.
- `AUTHORIZATION_REQUIRED`: policy requires an authorization decision.
- `UNVERIFIED`: evidence is insufficient.
- `NOT_EVALUATED`: Checker could not evaluate due to missing evidence/context.

A missing connector is not simulated success. Simulation models a candidate operation at actual capability boundaries; a denial, rejection, missing integration or absence of proof remains visible.

## Evidence integrity

Record actual invocation identity, inputs, target, result, artifacts and deviations. Never fabricate cycle IDs, receipts, hashes, grants, timestamps, CI results, verdicts or seals. Sealed Trails are immutable; corrections append superseding records. Checker is read-only and structurally independent. Apply configured retry/loop bounds, including EC-009 MaxLoops=3.

## Stop conditions

Stop when target, scope, policy or authorization is ambiguous; role separation cannot be enforced; Maker would exceed PlanFrame; or required evidence writer is unavailable.

## Validation

- [ ] Intent logged before action where required.
- [ ] Target verified before mutation.
- [ ] Authorization is exact and host-enforced.
- [ ] Maker remains within PlanFrame.
- [ ] Checker is independent and read-only.
- [ ] Outcomes are evidence-backed.
- [ ] Sealed records are never overwritten.
