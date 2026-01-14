# Ralph-Loop Best Practices

Comprehensive guide for creating effective prompts for the ralph-loop plugin.

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [Anatomy of an Effective Prompt](#anatomy-of-an-effective-prompt)
3. [The Promise Tag](#the-promise-tag)
4. [Max Iterations Strategy](#max-iterations-strategy)
5. [Patterns That Work](#patterns-that-work)
6. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
7. [Multi-Project Optimization](#multi-project-optimization)
8. [Debugging Failed Loops](#debugging-failed-loops)

## Core Concepts

Ralph-loop implements the "Ralph Wiggum technique" - running the same prompt repeatedly in a loop where Claude sees its previous work and can refine it.

**Key principle:** The loop continues until either:
1. Claude outputs the completion promise
2. Max iterations is reached
3. User cancels with `/cancel-ralph`

**Critical rule:** Claude cannot output false promises. The promise must be "completely and unequivocally true" when stated.

## Anatomy of an Effective Prompt

A well-structured ralph-loop prompt has these components:

### 1. Clear Task Description
```
Build a REST API for todo management with CRUD operations.
```

### 2. Detailed Workflow/Requirements
```
Requirements:
- GET /todos - list all todos
- POST /todos - create new todo
- PUT /todos/:id - update todo
- DELETE /todos/:id - delete todo
- Input validation for all endpoints
- Error handling with appropriate status codes
```

### 3. Measurable Completion Criteria
```
Completion Criteria:
- All 4 endpoints implemented and working
- Input validation in place (reject empty titles, invalid IDs)
- Tests written for each endpoint
- Test coverage >= 80%
- No linting errors
```

### 4. Explicit Completion Signal
```
When all criteria above are met, output <promise>API_COMPLETE</promise>
```

### Complete Example
```
Build a REST API for todo management with CRUD operations.

Requirements:
- GET /todos - list all todos
- POST /todos - create new todo
- PUT /todos/:id - update todo
- DELETE /todos/:id - delete todo
- Input validation for all endpoints
- Error handling with appropriate status codes

Completion Criteria:
- All 4 endpoints implemented and working
- Input validation in place (reject empty titles, invalid IDs)
- Tests written for each endpoint
- Test coverage >= 80%
- No linting errors

When all criteria above are met, output <promise>API_COMPLETE</promise>
```

## The Promise Tag

### Correct Format

```xml
<promise>YOUR_EXACT_PHRASE</promise>
```

**Rules:**
- Must be wrapped in XML tags: `<promise>...</promise>`
- Must match exactly what was set in `--completion-promise` (case-sensitive)
- Cannot be output until the statement is completely true
- Only output once, when actually complete

### Common Promise Phrases

- `COMPLETE` - Generic completion
- `DONE` - Alternative generic
- `ALL_TESTS_PASS` - For TDD workflows
- `BUILD_SUCCESS` - For build-focused tasks
- `BUG_FIXED` - For bug fixing
- `FEATURE_COMPLETE` - For feature development
- `REFACTOR_DONE` - For refactoring tasks

**Tip:** Use descriptive promise phrases that reflect the task type.

### Promise Placement in Prompt

Always include the promise instruction at the end of your prompt:

```
[Task description]
[Requirements]
[Completion criteria]

When all criteria are met, output <promise>PHRASE</promise>
```

## Max Iterations Strategy

### Recommended Values

| Task Type | Iterations | Rationale |
|-----------|-----------|-----------|
| Simple bug fix | 10-20 | Quick iteration, focused scope |
| TDD feature | 30-50 | Multiple test-code-refactor cycles |
| Medium feature | 50-75 | More complex requirements |
| Greenfield project | 100-150 | Full project setup + implementation |
| Complex refactor | 75-100 | Careful iterative changes |

### Always Set Max Iterations

**Never use unlimited iterations** unless:
- You have a very specific reason
- You're actively monitoring the loop
- The task has clear automatic stopping criteria

**Why:** Prevents runaway costs and infinite loops.

### Setting Max Iterations

```bash
/ralph-loop "prompt" --completion-promise "DONE" --max-iterations 50
```

## Patterns That Work

### Pattern 1: TDD Workflow

```
Implement [feature] following TDD:

1. Write failing test for [specific behavior]
2. Run tests and confirm failure
3. Implement minimal code to pass the test
4. Run tests again
5. If any tests fail:
   - Debug and identify the issue
   - Fix the implementation
   - Re-run tests
6. If all tests pass, refactor if needed
7. Repeat steps 1-6 for next behavior
8. When all behaviors implemented and all tests pass, output <promise>ALL_TESTS_PASS</promise>

Behaviors to implement:
- [Behavior 1]
- [Behavior 2]
- [Behavior 3]

Completion: All tests pass, coverage >= 80%
```

**Why it works:** Built-in feedback loop with automatic verification.

### Pattern 2: Phased Implementation

```
Implement user authentication in 3 phases:

Phase 1: JWT Token Generation
- Create token generation function
- Add expiration logic
- Write tests for token creation
- Verify: All Phase 1 tests pass

Phase 2: Token Validation Middleware
- Implement middleware to validate tokens
- Handle expired tokens
- Write tests for validation
- Verify: All Phase 2 tests pass

Phase 3: Protected Routes
- Apply middleware to protected endpoints
- Test unauthorized access (should fail)
- Test authorized access (should succeed)
- Verify: All Phase 3 tests pass

When all 3 phases complete and all tests pass, output <promise>AUTH_COMPLETE</promise>
```

**Why it works:** Clear milestones, incremental progress, measurable checkpoints.

### Pattern 3: Iterative Refinement

```
Optimize database query performance:

1. Identify slow queries (execution time > 100ms)
2. For each slow query:
   - Add appropriate indexes
   - Rewrite query if needed
   - Run performance tests
   - Measure new execution time
   - If still > 100ms, try alternative optimization
3. Repeat until all queries < 100ms
4. Run full test suite to ensure correctness
5. When all queries optimized and tests pass, output <promise>OPTIMIZED</promise>

Target: All queries execute in < 100ms with tests passing
```

**Why it works:** Specific numeric target, iterative improvement, automatic verification.

### Pattern 4: Build-Verify Loop

```
Add ESLint to the project and fix all issues:

1. Install ESLint and configure rules
2. Run ESLint on codebase
3. Fix all errors reported
4. Re-run ESLint
5. If errors remain, fix and repeat
6. When ESLint reports 0 errors, run tests
7. If tests fail, fix and re-test
8. When ESLint clean and tests pass, output <promise>LINTING_COMPLETE</promise>

Success criteria: 0 ESLint errors, all tests passing
```

**Why it works:** Tool-driven feedback, clear pass/fail, automatic iteration.

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Vague Success Criteria

```
Build a todo app and make it good.

When done, output <promise>DONE</promise>
```

**Problems:**
- "make it good" is subjective
- No specific requirements
- No measurable completion
- Claude doesn't know when it's actually "done"

**Fix:** Define specific, measurable criteria.

### ❌ Anti-Pattern 2: Requires Human Judgment

```
Design a beautiful UI for the dashboard. Choose colors that look professional.

When the design looks good, output <promise>DESIGN_DONE</promise>
```

**Problems:**
- "beautiful" is subjective
- "looks professional" requires human aesthetic judgment
- No automatic verification possible

**Fix:** Define specific design requirements or provide design specs.

### ❌ Anti-Pattern 3: No Completion Promise

```
Build a REST API with user authentication and all CRUD operations.
```

**Problems:**
- No promise tag means loop runs until max iterations
- No clear signal when task is complete
- Wastes iterations after completion

**Fix:** Always include promise instruction.

### ❌ Anti-Pattern 4: No Max Iterations

```bash
/ralph-loop "Build entire e-commerce platform" --completion-promise "COMPLETE"
```

**Problems:**
- Could run indefinitely
- No safety limit on API costs
- Hard to estimate completion time

**Fix:** Always set max iterations.

### ❌ Anti-Pattern 5: Ambiguous Requirements

```
Fix the authentication bug. When fixed, output <promise>FIXED</promise>
```

**Problems:**
- Which authentication bug?
- How to verify it's fixed?
- What tests to run?

**Fix:** Specify the bug, reproduction steps, and verification method.

### ❌ Anti-Pattern 6: Too Broad Scope

```
Build a complete social media platform with posts, comments, likes, follows, messaging, and notifications. Output <promise>COMPLETE</promise> when done.
```

**Problems:**
- Too many features for single loop
- No incremental milestones
- Hard to debug if it fails

**Fix:** Break into smaller tasks or use phased approach.

## Multi-Project Optimization

When running multiple ralph-loop projects simultaneously, avoid redundant context.

### Problem: Context Duplication

If you have 3 projects all using the same tech stack, don't repeat setup info in each prompt.

### Solution 1: Reference Existing Context

**First project prompt:**
```
Project: User Service API
Tech stack: Node.js, Express, PostgreSQL
[Full details...]
```

**Subsequent project prompts:**
```
Project: Product Service API
Use same tech stack as User Service API (Node.js, Express, PostgreSQL).
[Only project-specific details...]
```

### Solution 2: Shared Context Section

Add a "Context" section that references shared state:

```
Context:
- Repository structure: microservices/[service-name]
- Shared configs in: microservices/shared-config
- Testing framework: Jest (see User Service for examples)

Task: Build Product Service following the same patterns...
```

### Solution 3: Focus on Differences

```
Build Payment Service API.

Differences from existing services:
- Add Stripe integration (new dependency)
- Requires webhook handling (new pattern)
- PCI compliance considerations (new security requirement)

Everything else follows User Service patterns.
```

## Debugging Failed Loops

### Loop Doesn't Complete

**Symptoms:** Reaches max iterations without outputting promise.

**Diagnoses:**
1. Completion criteria too strict or impossible
2. Tests keep failing for subtle reason
3. Task requires human judgment
4. Missing dependencies or environment issues

**Fixes:**
- Review criteria - are they achievable?
- Check logs for recurring errors
- Simplify the task
- Increase max iterations if close to completion

### Loop Completes Too Early

**Symptoms:** Outputs promise but work is incomplete.

**Diagnoses:**
1. Completion criteria too loose
2. Missing verification steps
3. Tests don't cover all requirements

**Fixes:**
- Add more specific criteria
- Require automated verification
- Add comprehensive tests to criteria

### Loop Gets Stuck Repeating

**Symptoms:** Same actions repeated across many iterations.

**Diagnoses:**
1. No feedback from failures
2. Criteria never measurably improve
3. Missing escape condition

**Fixes:**
- Ensure errors/failures produce informative output
- Add debug logging to track progress
- Include "escape hatch" for stuck scenarios:
  ```
  After 15 iterations without progress:
  - Document what's blocking
  - List attempted solutions
  - Suggest alternative approaches
  - Output <promise>NEEDS_HUMAN_INPUT</promise>
  ```

### Infinite Retry Loop

**Symptoms:** Retrying same failing operation endlessly.

**Diagnoses:**
1. Error condition never changes
2. No alternative strategies
3. External dependency always fails

**Fixes:**
- Add retry limit to prompt
- Require strategy change after N failures
- Check for external dependencies first
- Always set max iterations

## Summary Checklist

Before running `/ralph-loop`, verify your prompt has:

- [ ] Clear, specific task description
- [ ] Detailed requirements or workflow steps
- [ ] Measurable completion criteria (no subjective terms)
- [ ] Explicit `<promise>PHRASE</promise>` instruction
- [ ] `--completion-promise` matches promise phrase exactly
- [ ] `--max-iterations` is set (not unlimited)
- [ ] Task can be verified automatically (tests, builds, tools)
- [ ] No requirements for human judgment or design decisions
- [ ] Appropriate max iterations for task complexity
- [ ] If multi-project: references shared context efficiently
