---
name: pmcro-reflector-seed-handoff
description: "Turn verified Reflector learning into a structured, layered SeedIntent for Agent Skill Creator. Use when meta-level learning should refine a skill or the skill-creation system itself."
---

# Reflector-to-Skill-Creator seed handoff

## Purpose and profile

Primary profile: Procedural + Schema/Contract + Template/Asset. Preserve the handoff from evidence-based reflection into reusable skill authoring.

This skill does not impersonate Reflector or Skill Creator. Reflector owns interpretation of completed evidence and next-seed intent. Skill Creator owns skill authoring. Plugin Creator owns plugin manifests and packaging. Marketplace Creator owns catalogs and distribution.

## Preconditions

- Reflector has a completed CheckFrame and evidence lineage.
- Facts are separated from interpretations and hypotheses.
- Any proposed seed is explicitly unexecuted.
- Target skill/plugin ownership and destination are known.
- A seed is intent, not authorization.

If completed independent verification evidence is missing, label the output provisional and `NOT_EVALUATED`; do not claim a completed-cycle reflection.

## Three-level seed model

1. **META_SEED_INTENT — improve the concrete skill.** Identify the exact skill outcome, user trigger, inputs, outputs, workflow, boundaries and acceptance evidence.
2. **META_META_SEED_INTENT — improve the skill-creation method.** Identify reusable authoring decisions, capability profile, source representation, progressive disclosure, validation and host portability that Skill Creator should apply.
3. **META_META_META_SEED_INTENT — improve the skill system.** Identify any evidence-supported improvement to creator contracts, discovery/routing, cross-skill composition, governance, evaluation or marketplace alignment. Do not turn an isolated preference into a global law.

The three levels form one bounded hierarchy. They are not three independent execution grants and do not authorize self-modification of creator governance.

## Structured handoff

```yaml
@ORCHESTRATOR
/pmcro-invocation

TASK:
  "Route the Reflector's layered seed intent to the registered Skill Creator capability."

CONTEXT:
  source_agent: "@REFLECTOR"
  recipient_type: CAPABILITY_NOT_AGENT
  reflection_status: "VERIFIED | PROVISIONAL | NOT_EVALUATED"
  evidence_lineage: "<exact references or none>"
  target_plugin: "<plugin identity>"
  target_skill: "<skill identity>"

INPUT:
  META_SEED_INTENT:
    "<specific skill-level change>"
  META_META_SEED_INTENT:
    "<reusable skill-authoring-method improvement>"
  META_META_META_SEED_INTENT:
    "<skill-system or creator-ecosystem improvement>"
  constraints:
    - preserve_skill_identity_and_ownership
    - use_repository_packaging_conventions
    - keep_seed_unexecuted
    - do_not_widen_authority

CAPABILITY_DISPATCH:
  - capability: "pmcro-skill-creator/skill-creator"
    task: "Resolve capability profile, author skill source, and validate package-local references."
    expect: "SKILL_PACKAGE_DRAFT"
  - capability: "pmcro-skill-creator/skill-reviewer"
    task: "Review skill specification compliance, portability, safety and governance."
    expect: "SKILL_REVIEW_RESULT"
  - capability: "pmcro-skill-creator/skill-validator"
    task: "Run deterministic structural and package checks."
    expect: "SKILL_VALIDATION_RESULT"

AGENT_DISPATCH:
  - agent: "@CHECKER"
    task: "Independently review the resulting package when a separate read-only agent context is available."
    access: READ_ONLY
    expect: "SKILL_CHECK_RESULT"

CONSTRAINTS:
  - no_invented_host_execution
  - no_creator_self_authorization
  - preserve_evidence_provenance
  - require_explicit_approval_for_mutation

EXPECT:
  result: "SKILL_CREATION_HANDOFF"
  readiness: READY | PARTIAL | BLOCKED
  evidence: REQUIRED
```

## Creator routing

Use the installed PMCR-O Skill Creator for skill content, Skill Reviewer for static quality review, Skill Validator for deterministic package checks, Plugin Creator for plugin metadata/package integration, and Marketplace Creator for catalog/distribution work. Do not route a skill-only change to Marketplace Creator or edit plugin manifests as if they were skill content.

## Validation

- [ ] Reflector input derives from completed verification evidence or is labelled provisional.
- [ ] All three seed levels are distinct and traceable.
- [ ] The handoff targets a real skill and creator capability.
- [ ] Skill Creator receives bounded intent, constraints, and expected outputs.
- [ ] The seed remains unexecuted until separately planned and authorized.
- [ ] Reviewer/validator results are reported separately from host loading or execution.
