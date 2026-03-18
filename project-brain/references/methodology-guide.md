# Methodology Guide

This reference explains each supported development methodology and when to use them.

---

## BMAD (Backlog, Milestones, Architecture, Decisions)

### Overview
A lightweight methodology focused on four core documentation pillars that keep projects organized without heavy process overhead.

### When to Use
- MVPs and Micro-SaaS projects
- Solo developers or small teams
- When you want minimal process but maximum clarity
- Projects with clear scope and timeline

### Core Documents
| Document | Purpose | Update Frequency |
|----------|---------|-----------------|
| BACKLOG.md | All work items prioritized | Every session |
| MILESTONES.md | Version-based goals | Weekly |
| ARCHITECTURE.md | System design docs | On architecture changes |
| DECISIONS.md | ADRs for every decision | When decisions are made |

### Workflow
1. Define milestones (v1.0, v1.1, etc.)
2. Fill backlog with work items tagged to milestones
3. Pick items from top of backlog each session
4. Document architecture as it evolves
5. Record every significant decision as ADR

---

## OpenSpec

### Overview
Specification-first development where you write the complete product spec before implementation, then track implementation against the spec.

### When to Use
- Products with clear requirements upfront
- When you need to validate ideas before building
- Client projects with defined scope
- When multiple people/agents need to implement

### Core Documents
| Document | Purpose | Update Frequency |
|----------|---------|-----------------|
| SPEC.md | Complete product specification | Before each phase |
| DECISION-LOG.md | Chronological decisions | When decisions occur |
| IMPLEMENTATION-STATUS.md | Spec vs reality tracking | Every session |

### Workflow
1. Write complete SPEC.md with all features, user stories, acceptance criteria
2. Break spec into implementable phases
3. Implement phase by phase
4. Track what's implemented vs what's specified
5. Log deviations and decisions

---

## GSD (Get Shit Done)

### Overview
A spec-driven development system designed to prevent "context rot" — quality degradation as AI fills its context window. Uses phased approach with documentation that stays under quality thresholds.

### When to Use
- AI-assisted development (Claude Code, Codex, etc.)
- Complex projects needing structured execution
- When context management is critical
- Multi-phase projects with parallel work

### Core Documents
| Document | Purpose | Update Frequency |
|----------|---------|-----------------|
| PROJECT.md | Vision statement | Once |
| REQUIREMENTS.md | Scoped features per version | Per milestone |
| ROADMAP.md | Phase breakdown with status | Per phase |
| STATE.md | Cross-session memory | Every session |
| {phase}-CONTEXT.md | Implementation decisions | Per phase |
| {phase}-RESEARCH.md | Investigated patterns | Per phase |
| VERIFICATION.md | Test results | After verification |

### Workflow Phases
1. **new-project**: Clarify vision, research, create roadmap
2. **discuss-phase**: Capture preferences, identify gray areas, output CONTEXT.md
3. **plan-phase**: Research + create atomic task plans (XML structured)
4. **execute-phase**: Parallel execution with atomic commits
5. **verify-work**: Test deliverables, debug failures

### Key Concepts
- **Context Engineering**: Documentation deliberately sized under quality thresholds
- **Wave-Based Parallelization**: Group tasks by dependencies, parallelize within waves
- **Atomic Commits**: Each task = one commit (bisectable history)
- **Fresh Context Windows**: Each execution task gets clean context

---

## SpecKit

### Overview
A specification-centered approach where detailed specs drive implementation. Specs are organized by domain (features, API, data) with implementation tracking.

### When to Use
- API-first development
- Projects with complex data models
- When you need detailed technical specifications
- Team environments needing clear contracts

### Core Documents
| Document | Purpose | Update Frequency |
|----------|---------|-----------------|
| SPEC/overview.md | Product overview and goals | Per milestone |
| SPEC/features/*.md | Individual feature specs | Per feature |
| SPEC/api/*.md | API endpoint specifications | Per API change |
| SPEC/data/*.md | Data model specifications | Per schema change |
| IMPLEMENTATION/status.md | Implementation vs spec | Every session |
| IMPLEMENTATION/deviations.md | Where reality differs from spec | When deviations occur |

### Workflow
1. Write specifications first (overview, features, API, data)
2. Review and validate specs
3. Implement against specs
4. Track status and deviations
5. Update specs when requirements change (never silently deviate)

---

## Hybrid Approach (Recommended for MVPs)

For most MVP and SaaS projects, combine the best of each:

```
From BMAD: Backlog + ADR discipline
From GSD: STATE.md cross-session memory + phased execution
From OpenSpec: Spec before complex features
From SpecKit: API and data model specs

Result: Lightweight but complete documentation
```

### Minimum Viable Documentation
1. **STATE.md** (GSD): What's happening now, cross-session memory
2. **BACKLOG.md** (BMAD): Prioritized work items
3. **DECISIONS.md** (BMAD): ADRs for every decision
4. **CODEBASE-MAP.json**: Structural truth of the codebase
5. **architecture.canvas**: Visual system overview
