---
name: lisa-prompt-engineering
description: This skill should be used when the user asks to "create a prompt for Lisa", "generate PROMPT.md", "write specs for Lisa loop", "prepare Lisa execution", mentions "Lisa plugin", "iterative loops", "spec-based verification", or discusses creating high-quality prompts with completion promises and verification steps for the Lisa Claude Code plugin.
version: 1.0.0
---

# Lisa Prompt Engineering Skill

This skill helps create high-quality prompts, specifications, and implementation plans for use with the **Lisa plugin** - an iterative loop system for Claude Code that executes tasks through repeated iterations until completion.

## Overview

Lisa is a Claude Code plugin that enables observable iterative loops using the Ralph Wiggum technique. It repeatedly feeds the same prompt to Claude until a completion promise is detected or max iterations is reached. This skill guides the creation of effective prompts and specs that maximize Lisa's potential.

**Lisa Repository:** https://github.com/Arakiss/lisa

## When This Skill Applies

This skill activates when the user's request involves:

- Creating prompts for Lisa iterative loops (`PROMPT.md`)
- Generating specification files (`specs/features.md`)
- Designing implementation plans (`IMPLEMENTATION_PLAN.md`)
- Setting up completion promises and verification criteria
- Applying spec-based verification methodology
- Planning complex multi-step projects with Lisa
- Converting requirements into Lisa-compatible structures

## Interactive Workflow (AUTOMATED)

When the user requests prompt generation, this skill follows an **automated, interactive process**:

### Phase 1: Discovery & Analysis (ASK QUESTIONS)
The skill will automatically:

1. **Ask about the project:**
   - What do you want to implement? (Brief description)
   - What are the main features/requirements?
   - What tech stack? (Node.js, React, Python, etc.)
   - Any specific constraints or requirements?

2. **Determine complexity:**
   - Simple (1-5 requirements, straightforward)
   - Medium (5-15 requirements, some dependencies)
   - Complex (15+ requirements, multi-phase, critical)

3. **Clarify verification:**
   - How will we know it's done? (tests pass, files exist, etc.)
   - Any quality gates? (coverage %, linting, etc.)

### Phase 2: Architecture Design (ANALYZE)
The skill will:

1. Break down the project into phases
2. Identify critical requirements
3. Determine if spec-based verification is needed
4. Estimate iteration count
5. Choose appropriate completion criteria

### Phase 3: File Generation (CREATE)
The skill will automatically create:

**For Simple Projects:**
- `PROMPT.md` - Basic prompt with clear completion promise
- `IMPLEMENTATION_PLAN.md` - Task list with checkboxes

**For Medium/Complex Projects:**
- `PROMPT.md` - Full prompt with spec-based verification
- `IMPLEMENTATION_PLAN.md` - Multi-phase plan with detailed tasks
- `specs/features.md` - Detailed requirements with checkboxes
- Directory structure (if needed)

### Phase 4: Execution Prep (DELIVER)
The skill will provide:

1. **Ready-to-use files** (all created and saved)
2. **Execution commands:**
   ```bash
   # Ready to run
   /lisa:loop PROMPT.md --max-iterations [calculated]
   ```
3. **Monitoring commands:**
   ```bash
   /lisa:status
   tail -f .claude/lisa-loop.log
   ```
4. **Estimated iterations** and timeline

### Example: User Request

**User says:**
```
"Crie um prompt para implementar um sistema de autenticação com JWT"
```

**Skill responds:**
```
Vou preparar tudo para o Lisa! Preciso de algumas informações:

1. Tecnologia backend: Node.js + Express ou outra?
2. Banco de dados: PostgreSQL, MongoDB, MySQL?
3. Requisitos além de login/registro:
   - Refresh token?
   - Password reset?
   - Email verification?
   - Role-based access?
4. Testes necessários? (Jest, Supertest, etc.)
5. Cobertura mínima esperada? (ex: >80%)

[User answers...]

Analisando... Complexidade: MÉDIA (8-10 requisitos)

Criando arquivos:
✅ PROMPT.md (com spec-based verification)
✅ IMPLEMENTATION_PLAN.md (4 fases)
✅ specs/features.md (8 features detalhadas)
✅ Estrutura de diretórios

Pronto para executar!
Comando: /lisa:loop PROMPT.md --max-iterations 40
Estimativa: 25-35 iterações, ~1-2 horas
```

### Benefits of This Approach

✅ **Zero Manual Work:** You just describe, skill creates everything
✅ **Smart Analysis:** Automatically determines complexity and approach
✅ **Complete Setup:** All files ready, no missing pieces
✅ **Ready to Delegate:** Just run the command, Lisa does the rest
✅ **Multiple Projects:** Repeat process for each project quickly

## Core Lisa Concepts

### 1. **Completion Promises**
Lisa stops iterating when it detects a specific completion promise in Claude's output:
```markdown
<promise>EXACT_TEXT</promise>
```

### 2. **Max Iterations Safety**
Always specify `--max-iterations` to prevent infinite loops:
```bash
/lisa:loop PROMPT.md --max-iterations 50
```

### 3. **Spec-Based Verification**
Critical approach to prevent premature completion:
- Create detailed `specs/features.md` FIRST (the contract)
- Embed verification rules in the prompt (the enforcement)
- Claude must verify against spec BEFORE promising (the check)

### 4. **Progress Tracking**
Lisa auto-detects progress from `IMPLEMENTATION_PLAN.md` with checkboxes:
```markdown
## Tasks
- [x] Completed task
- [ ] Pending task
```

### 5. **Dynamic Stop Conditions**
Use external commands to control loop termination:
```bash
/lisa:loop PROMPT.md --stop-command "npm test" --stop-when "pass"
```

## PROMPT.md Structure

### Essential Components
```markdown
# Mission
[Clear, single-sentence objective describing the end goal]

# Source of Truth (For Spec-Based Verification)
The ONLY definition of "done" is specs/features.md. Your subjective sense of completion is IRRELEVANT.

# Process Per Iteration
1. [Specific action to take each iteration]
2. [Next step in the process]
3. [Verification or checkpoint]
4. [Commit or save work]

# Mandatory Verification (NEVER SKIP)
Before outputting completion promise:
1. Re-read specs/features.md from disk (not memory)
2. For EACH requirement:
   - Verify code exists
   - Verify test exists and passes
   - Mark [x] in specs/features.md
3. Count: X checked, Y unchecked
4. IF Y > 0: Continue working
5. IF Y == 0 AND all tests pass: Output promise

# Completion Criteria
When [VERIFIABLE CONDITION with specific metrics]:
<promise>EXACT_TEXT_TO_OUTPUT</promise>

# Constraints
- [What to avoid]
- [Limits or boundaries]
- [Quality standards]
```

### Prompt Quality Guidelines

**✅ GOOD Completion Promises:**
```markdown
<promise>DONE</promise> when:
- `npm test` exits with code 0
- `tsc --noEmit` has no errors
- All 48 chapters exist in drafts/
- specs/features.md shows 24/24 checked
```

**❌ BAD Completion Promises:**
```markdown
<promise>DONE</promise> when finished.
<promise>COMPLETE</promise> when work looks good.
```

## specs/features.md Structure

For critical projects requiring systematic verification:
```markdown
## [FEATURE-ID]: Feature Name

### Requirements
- [ ] REQ-1: Specific, testable requirement
- [ ] REQ-2: Another specific requirement with acceptance criteria
- [ ] REQ-3: Technical implementation detail

### Acceptance Criteria
- [ ] All unit tests pass
- [ ] Integration test covers happy path
- [ ] Error handling implemented for edge cases

### Technical Details
- API endpoint: `POST /api/endpoint`
- Expected input: `{ field: "value" }`
- Expected output: `{ result: "success", data: {...} }`

---

## [FEATURE-ID-2]: Next Feature
...
```

## IMPLEMENTATION_PLAN.md Structure

For progress tracking:
```markdown
# Implementation Plan

## Phase 1: Setup
- [x] Initialize project structure
- [x] Configure dependencies
- [ ] Setup testing framework

## Phase 2: Core Features
- [ ] Implement feature A
- [ ] Implement feature B
- [ ] Add error handling

## Phase 3: Testing
- [ ] Write unit tests
- [ ] Write integration tests
- [ ] Achieve 80%+ coverage

## Phase 4: Documentation
- [ ] Write API documentation
- [ ] Create user guide
- [ ] Add code comments
```

## Template Generation Process

When creating prompts for Lisa, follow this process:

### Step 1: Requirements Gathering
Ask clarifying questions:
- What is the end goal?
- What are the specific deliverables?
- How will we verify completion?
- Are there intermediate checkpoints?
- What's the expected iteration count?

### Step 2: Determine Approach
Choose the appropriate methodology:

**Simple Approach:** For straightforward tasks
- Basic `PROMPT.md` with clear completion promise
- No specs needed
- Direct verification (e.g., tests pass, files exist)

**Spec-Based Approach:** For complex/critical tasks
- Full `specs/features.md` with checkboxes
- Verification-enforced `PROMPT.md`
- Systematic requirement checking

### Step 3: Create Supporting Files

**Always create:**
1. `PROMPT.md` - Main loop instruction
2. `IMPLEMENTATION_PLAN.md` - Progress tracking (if multi-phase)

**For spec-based verification:**
3. `specs/features.md` - Detailed requirements with checkboxes
4. Update `PROMPT.md` with verification enforcement

### Step 4: Set Loop Parameters

Determine and communicate:
- `--max-iterations`: Safety limit (10-100 typical)
- `--completion-promise`: Override if needed
- `--stop-command`: External condition (optional)
- `--stop-when`: Expected value (if using stop-command)

## Example: Creating a REST API

### User Request
"Create a REST API for todo management with CRUD operations, validation, and tests."

### Generated Files

**specs/features.md:**
```markdown
## API-1: Create Todo

- [ ] POST /api/todos accepts { title, description }
- [ ] Validates title is required, min 3 chars
- [ ] Returns 201 with created todo object
- [ ] Returns 400 for validation errors

## API-2: Read Todos

- [ ] GET /api/todos returns array of all todos
- [ ] GET /api/todos/:id returns single todo
- [ ] Returns 404 if todo not found

## API-3: Update Todo

- [ ] PUT /api/todos/:id updates title and/or description
- [ ] Returns 200 with updated todo
- [ ] Returns 404 if todo not found

## API-4: Delete Todo

- [ ] DELETE /api/todos/:id removes todo
- [ ] Returns 204 on success
- [ ] Returns 404 if todo not found

## API-5: Testing

- [ ] Unit tests for all endpoints
- [ ] Test coverage >80%
- [ ] All tests pass with `npm test`
```

**PROMPT.md:**
```markdown
# Mission
Build a complete REST API for todo management with full CRUD operations, validation, and comprehensive tests.

# Source of Truth
The ONLY definition of "done" is specs/features.md. Your subjective sense of completion is IRRELEVANT.

# Process Per Iteration
1. Read specs/features.md from disk (not memory)
2. Find FIRST unchecked requirement (- [ ])
3. Implement that specific requirement with tests
4. Verify implementation works (run tests)
5. Mark [x] in specs/features.md for completed requirement
6. Commit changes with message: "feat: implement [REQ-ID]"

# Mandatory Verification (NEVER SKIP)
Before outputting completion promise:
1. Re-read specs/features.md from disk
2. For EACH requirement in ALL sections (API-1 through API-5):
   - Verify implementation code exists
   - Verify test file exists
   - Verify test passes when run
3. Run `npm test` and verify ALL tests pass
4. Count: X requirements checked [x], Y unchecked [ ]
5. IF Y > 0: Continue working on next requirement
6. IF Y == 0 AND `npm test` shows all pass: Output promise

# Completion Criteria
When ALL requirements in specs/features.md are checked [x] AND `npm test` exits with code 0:
<promise>ALL API REQUIREMENTS VERIFIED AND TESTED</promise>

# Constraints
- One requirement per iteration (systematic progress)
- Always write test BEFORE or WITH implementation
- No skipping ahead - follow specs/features.md order
- Commit after each completed requirement
```

**IMPLEMENTATION_PLAN.md:**
```markdown
# TODO API Implementation Plan

## Phase 1: Project Setup
- [ ] Initialize Node.js project
- [ ] Install dependencies (express, jest, etc.)
- [ ] Setup project structure
- [ ] Configure test environment

## Phase 2: CRUD Operations
- [ ] Implement POST /api/todos (Create)
- [ ] Implement GET /api/todos (Read All)
- [ ] Implement GET /api/todos/:id (Read One)
- [ ] Implement PUT /api/todos/:id (Update)
- [ ] Implement DELETE /api/todos/:id (Delete)

## Phase 3: Validation & Error Handling
- [ ] Add input validation middleware
- [ ] Implement error responses (400, 404)
- [ ] Add request validation for all endpoints

## Phase 4: Testing
- [ ] Write unit tests for all endpoints
- [ ] Test validation logic
- [ ] Test error handling
- [ ] Achieve >80% coverage
- [ ] All tests passing

## Phase 5: Documentation
- [ ] Add API endpoint documentation
- [ ] Create usage examples
- [ ] Document error responses
```

**Usage:**
```bash
# Use /lisa:prep to create scaffolding (optional)
/lisa:prep

# Start the loop with specs-based verification
/lisa:loop PROMPT.md --max-iterations 50
```

## Anti-Patterns to Avoid

❌ **Vague completion criteria:**
```markdown
<promise>DONE</promise> when everything works
```

❌ **No verification steps:**
```markdown
# Just implement the feature
<promise>COMPLETE</promise>
```

❌ **Trusting Claude's memory across iterations:**
```markdown
Check if you already implemented X (memory fades!)
```

❌ **No external validation:**
```markdown
Promise when you think it's done (subjective!)
```

✅ **Always use concrete, verifiable conditions:**
```markdown
When specs/features.md shows 15/15 [x] AND `npm test` passes:
<promise>VERIFIED_COMPLETE</promise>
```

## Key Principles

1. **Spec is King:** For critical work, specs/features.md is the single source of truth
2. **Verify Don't Trust:** Always re-read specs from disk, never rely on memory
3. **One Thing Per Iteration:** Break work into atomic steps
4. **Commit Often:** Each iteration should produce a commit
5. **Test Everything:** Completion requires passing tests, not just code
6. **Be Specific:** Promises must be based on measurable criteria

## Advanced Features

### Dynamic Stop Conditions

Use external commands for stopping:
```markdown
# Stop Condition
<stop-command>npm test > /dev/null 2>&1 && echo pass || echo fail</stop-command>
<stop-when>pass</stop-when>
```

Or via command line:
```bash
/lisa:loop PROMPT.md --stop-command "tsc --noEmit 2>&1 | grep -c error || echo 0" --stop-when "0"
```

### Progress Detection

Lisa automatically shows progress when `IMPLEMENTATION_PLAN.md` exists:
```
🔄 Lisa iteration 15 | Progress: 12/24 items | To stop: <promise>DONE</promise>
```

## Troubleshooting

**Loop runs forever:**
- Add `--max-iterations` safety limit
- Verify `<promise>` tag exists in PROMPT.md

**Loop exits too early:**
- Make promise more specific
- Add verification steps that check actual conditions
- Use spec-based verification for multi-step work

**Claude loses track:**
- Add "Re-read from disk" reminders in verification steps
- Use specs/features.md as external memory
- Make each iteration atomic and self-contained

## Decision Matrix: Choosing the Right Approach

| Project Type | Complexity | Files Needed | Max Iterations | Approach |
|--------------|-----------|--------------|----------------|----------|
| Bug fix | Simple | PROMPT.md | 10-20 | Simple Loop |
| Small feature | Simple | PROMPT.md + IMPLEMENTATION_PLAN.md | 20-40 | Iterative Dev |
| API endpoint | Medium | All 3 files | 30-60 | Spec-Based |
| Full CRUD API | Medium | All 3 files | 50-100 | Spec-Based |
| Multi-feature app | Complex | All 3 files + dirs | 100-200 | Phased Spec-Based |
| E-commerce/SaaS | Complex | All 3 files + dirs | 150-300 | Phased Spec-Based |

## Question Templates (For Automated Discovery)

When the skill detects a prompt creation request, it uses these question templates:

### Basic Questions (Always Ask)
```
1. O que você quer implementar?
   [One-sentence description]

2. Quais são as principais funcionalidades?
   - Feature 1
   - Feature 2
   - ...

3. Stack tecnológico?
   - Backend: [Node.js, Python, Go, etc.]
   - Frontend: [React, Vue, Angular, etc.]
   - Database: [PostgreSQL, MongoDB, MySQL, etc.]
   - Testing: [Jest, Pytest, Vitest, etc.]

4. Critério de sucesso?
   - Testes passam?
   - Funcionalidade completa?
   - Cobertura mínima?
```

### Medium/Complex Projects (Additional Questions)
```
5. Requisitos de qualidade?
   - Cobertura de testes: [% esperado]
   - Linting: [ESLint, Prettier, etc.]
   - Type checking: [TypeScript, etc.]

6. Arquitetura específica?
   - Clean Architecture?
   - MVC?
   - Microservices?
   - Monolito?

7. Integração com sistemas externos?
   - APIs de terceiros?
   - Webhooks?
   - Serviços cloud?

8. Documentação necessária?
   - Swagger/OpenAPI?
   - README?
   - Exemplos de uso?
```

## Quick Start Guide

### For Users: How to Use This Skill

**Step 1: Request Prompt Creation**
```
"Crie um prompt Lisa para [seu projeto]"
"Prepare arquivos Lisa para implementar [feature]"
"Gerar PROMPT.md para [objetivo]"
```

**Step 2: Answer Questions**
The skill will ask 4-8 questions. Answer briefly and clearly.

**Step 3: Review & Execute**
The skill generates all files. Review them, then run:
```bash
/lisa:loop PROMPT.md --max-iterations [provided]
```

**Step 4: Monitor Progress**
```bash
/lisa:status  # Check current iteration
```

**Step 5: Done!**
Lisa will stop when completion promise is detected.

---

## Advanced: Customization After Generation

If you want to customize generated files:

1. **Edit PROMPT.md:**
   - Adjust completion promise
   - Add/remove constraints
   - Modify verification steps

2. **Edit IMPLEMENTATION_PLAN.md:**
   - Add/remove tasks
   - Reorder phases
   - Add checkpoints

3. **Edit specs/features.md:**
   - Add requirements
   - Adjust acceptance criteria
   - Add technical details

Then re-run: `/lisa:loop PROMPT.md --max-iterations [adjust if needed]`

---

## Best Practices Summary

1. **Let the skill ask questions** - Don't skip the discovery phase
2. **Be specific in answers** - Better input = better output
3. **Review generated files** - Quick sanity check before running
4. **Trust the complexity analysis** - Skill chooses right approach
5. **Use provided max-iterations** - Based on project analysis
6. **Monitor first few iterations** - Verify Lisa is on track
7. **Multiple projects?** - Repeat process for each (parallel safe)

## References

- Lisa Plugin Repository: https://github.com/Arakiss/lisa
- Ralph Wiggum Technique: https://ghuntley.com/ralph/
- Spec-Based Verification: Inspired by @trq212 (Thariq, Claude Code team)

---

**Remember:**
- This skill is your **Lisa preparation assistant**
- You describe → Skill generates → Lisa implements
- Perfect for managing multiple simultaneous projects
- Lisa excels at systematic, verifiable work with proper prompts