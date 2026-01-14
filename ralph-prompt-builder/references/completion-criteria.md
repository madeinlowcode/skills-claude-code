# Completion Criteria Guide

How to define clear, measurable, achievable completion criteria for ralph-loop prompts.

## Table of Contents

1. [SMART Criteria Framework](#smart-criteria-framework)
2. [Criteria by Task Type](#criteria-by-task-type)
3. [Measurable vs Subjective](#measurable-vs-subjective)
4. [Verification Methods](#verification-methods)
5. [Common Criteria Patterns](#common-criteria-patterns)
6. [Criteria Anti-Patterns](#criteria-anti-patterns)

## SMART Criteria Framework

Effective ralph-loop completion criteria should be **SMART**:

### S - Specific
Be precise about what constitutes completion.

❌ "Code works"
✅ "All 4 API endpoints (GET, POST, PUT, DELETE) respond with correct status codes and data formats"

### M - Measurable
Use quantifiable or verifiable conditions.

❌ "Good test coverage"
✅ "Test coverage >= 80% (measured by Jest coverage report)"

### A - Achievable
Ensure criteria can actually be met within the loop.

❌ "Deploy to production and monitor for a week"
✅ "Build passes, tests pass, ready for deployment"

### R - Relevant
Criteria should directly relate to task completion.

❌ "Update documentation website" (when task is building an API)
✅ "API endpoints documented in README"

### T - Time-Bounded (via max-iterations)
Use max-iterations to bound the task in time.

```bash
--max-iterations 50  # bounds the task
```

## Criteria by Task Type

### Development Tasks

**Good criteria:**
- All tests pass (npm test exits with code 0)
- Build succeeds (npm run build exits with code 0)
- Test coverage >= X% (measurable percentage)
- No TypeScript errors (tsc --noEmit exits with code 0)
- No linting errors (eslint . exits with code 0)
- All required features implemented (checklist of specific features)

**Example:**
```
Completion Criteria:
- User registration endpoint implemented
- Login endpoint implemented
- JWT token generation working
- All unit tests pass (npm test)
- Test coverage >= 80%
- No ESLint errors
```

### Bug Fixing Tasks

**Good criteria:**
- Bug no longer reproducible (specific steps fail to trigger bug)
- Regression test added and passing
- All existing tests still pass
- No new errors in console/logs
- Original error message no longer appears

**Example:**
```
Completion Criteria:
- Clicking "Submit" with empty form no longer crashes app
- New test added that verifies form validation
- All 47 existing tests still pass
- Console shows no errors during form submission
- Form displays validation error message correctly
```

### Feature Implementation Tasks

**Good criteria:**
- All requirements from spec implemented (specific checklist)
- Feature works as described in acceptance criteria
- Tests cover main use cases
- Feature integrated with existing code
- No breaking changes to existing features

**Example:**
```
Completion Criteria:
- Users can upload profile pictures (jpeg, png)
- Pictures are resized to 200x200px
- Pictures are stored in /uploads directory
- Profile page displays uploaded picture
- Tests verify upload, resize, and display
- Existing user features still work (tests pass)
```

### Refactoring Tasks

**Good criteria:**
- All tests still pass (no behavior changes)
- Target metrics improved (e.g., cyclomatic complexity reduced)
- No new linting warnings
- Code follows new pattern consistently
- Documentation updated if needed

**Example:**
```
Completion Criteria:
- All database queries moved to repository layer
- No direct SQL in controller files
- All 52 existing tests still pass
- New repository pattern used consistently (100% of queries)
- No ESLint warnings
```

### Greenfield Project Tasks

**Good criteria:**
- Project structure created (specific folders/files)
- Core features implemented (checklist)
- Tests written and passing
- Build process working
- README with setup instructions exists
- Basic usage documented

**Example:**
```
Completion Criteria:
- Project initialized with package.json
- Express server starts successfully
- Database schema created (users, posts tables)
- CRUD endpoints for users implemented
- CRUD endpoints for posts implemented
- 20+ tests written and passing
- Test coverage >= 75%
- README documents setup and API endpoints
- npm run build succeeds
```

## Measurable vs Subjective

### Measurable (Use These) ✅

**Quantitative:**
- Test coverage percentage: `>= 80%`
- Number of items: `All 15 unit tests pass`
- Exit codes: `npm test exits with 0`
- File existence: `README.md exists`
- Line counts: `No files exceed 300 lines`
- Timing: `All API calls respond in < 200ms`

**Binary (Yes/No):**
- Tests pass/fail
- Build succeeds/fails
- File exists/doesn't exist
- Error appears/doesn't appear
- Feature works/doesn't work

**Tool-Verified:**
- Linter reports 0 errors
- Type checker reports 0 errors
- Test runner shows all green
- Build completes successfully
- Git diff shows expected changes

### Subjective (Avoid These) ❌

**Quality judgments:**
- "Code is clean" → Instead: "No ESLint errors, no files > 300 lines"
- "Good performance" → Instead: "All endpoints respond in < 200ms"
- "Well-documented" → Instead: "All public functions have JSDoc comments"
- "User-friendly" → Instead: "Form validation shows clear error messages"

**Aesthetic judgments:**
- "Looks professional" → Instead: "Uses colors from design spec (#3498db, #2ecc71)"
- "Nice layout" → Instead: "Follows wireframe layout (header, sidebar, content)"
- "Beautiful UI" → Instead: "Implements all components from Figma design"

**Vague terms:**
- "Mostly working" → Instead: "All core features working (list specific features)"
- "Pretty good coverage" → Instead: "Test coverage >= 75%"
- "Few errors" → Instead: "0 TypeScript errors, 0 ESLint errors"
- "Almost done" → Instead: "4 of 5 features complete"

## Verification Methods

### 1. Automated Testing
```
Completion: All tests pass
Verification: npm test exits with code 0
```

### 2. Build Systems
```
Completion: Build succeeds without errors
Verification: npm run build exits with code 0
```

### 3. Linters/Type Checkers
```
Completion: No type errors
Verification: tsc --noEmit exits with code 0
```

### 4. Code Coverage Tools
```
Completion: Coverage >= 80%
Verification: Jest coverage report shows >= 80%
```

### 5. Functional Testing
```
Completion: API returns correct data
Verification: curl /api/users returns 200 and JSON array
```

### 6. File/Directory Checks
```
Completion: Required files exist
Verification: README.md, package.json, src/index.ts all exist
```

### 7. String/Pattern Matching
```
Completion: No error messages in logs
Verification: Log file contains 0 instances of "ERROR" or "FATAL"
```

### 8. Regression Testing
```
Completion: No breaking changes
Verification: All existing tests still pass
```

## Common Criteria Patterns

### Pattern 1: Test-Driven Criteria

```
Completion Criteria:
- All unit tests pass
- All integration tests pass
- Test coverage >= 80%
- No test warnings or skipped tests
```

**Why it works:** Tests provide automatic, objective verification.

### Pattern 2: Build-Driven Criteria

```
Completion Criteria:
- npm run build succeeds (exit code 0)
- No TypeScript errors
- No ESLint errors
- Bundle size < 500KB
```

**Why it works:** Build tools provide clear pass/fail signals.

### Pattern 3: Feature Checklist Criteria

```
Completion Criteria:
- [ ] User can register (POST /register works)
- [ ] User can login (POST /login returns JWT)
- [ ] User can view profile (GET /profile works with auth)
- [ ] User can update profile (PUT /profile works)
- [ ] All 4 features have tests
- [ ] All tests pass
```

**Why it works:** Explicit checklist prevents missed requirements.

### Pattern 4: Regression + New Feature Criteria

```
Completion Criteria:
- New feature: Search functionality works (returns filtered results)
- Regression: All 83 existing tests still pass
- New tests: 5+ tests for search feature added and passing
- Performance: Search responds in < 300ms
```

**Why it works:** Ensures new work doesn't break old work.

### Pattern 5: Quality Metrics Criteria

```
Completion Criteria:
- Code coverage >= 80%
- Cyclomatic complexity < 10 (per function)
- No functions > 50 lines
- No files > 300 lines
- 0 ESLint errors, 0 warnings
```

**Why it works:** Quantifiable quality thresholds.

### Pattern 6: Integration Criteria

```
Completion Criteria:
- Frontend can fetch data from new API endpoint
- Data displays correctly in UI
- Error states handled (network errors, 404s, etc.)
- Loading states implemented
- End-to-end test passes (login → fetch data → display)
```

**Why it works:** Verifies full integration, not just isolated components.

## Criteria Anti-Patterns

### ❌ Anti-Pattern 1: Single Vague Criterion

```
Completion Criteria:
- Task is complete
```

**Problem:** Not measurable, not verifiable.

**Fix:** Break down into specific, measurable criteria.

### ❌ Anti-Pattern 2: Impossible Standards

```
Completion Criteria:
- 100% test coverage (including generated files, node_modules)
- Zero bugs (impossible to verify)
- Perfect performance (no definition of "perfect")
```

**Problem:** Unrealistic goals prevent completion.

**Fix:** Set achievable, realistic thresholds.

### ❌ Anti-Pattern 3: External Dependencies

```
Completion Criteria:
- Deployed to production
- Product manager approves
- Passes security audit
```

**Problem:** Requires actions/approvals outside Claude's control.

**Fix:** Criteria should be verifiable within the loop environment.

### ❌ Anti-Pattern 4: Time-Based Criteria

```
Completion Criteria:
- Run for 1 hour without crashes
- Monitor logs for 24 hours
```

**Problem:** Ralph-loop can't wait hours between iterations.

**Fix:** Use iteration counts or immediate verification.

### ❌ Anti-Pattern 5: Human Judgment Required

```
Completion Criteria:
- Code looks good to senior developer
- Design matches brand guidelines (subjective interpretation)
- User experience is intuitive
```

**Problem:** Requires human assessment.

**Fix:** Use objective criteria or specific design specs.

### ❌ Anti-Pattern 6: Missing Verification Method

```
Completion Criteria:
- Feature works correctly
```

**Problem:** "Works correctly" - according to what test/verification?

**Fix:** Specify how to verify:
```
Completion Criteria:
- Feature works correctly (verified by: npm test shows all tests pass)
```

## Crafting Criteria Checklist

When writing completion criteria, ask yourself:

- [ ] Can this be verified automatically? (without human judgment)
- [ ] Is this specific enough? (no vague terms like "good", "clean", "nice")
- [ ] Is this measurable? (has numbers, percentages, or binary pass/fail)
- [ ] Is this achievable? (possible within the loop environment)
- [ ] Is this relevant? (directly related to task completion)
- [ ] How will I verify this? (what command/tool/test confirms it?)
- [ ] Could someone else read this and know exactly when the task is done?

If you answer "no" to any question, refine your criteria.

## Examples: Before and After

### Example 1: Development Task

**Before:**
```
Completion Criteria:
- Feature is done and working well
```

**After:**
```
Completion Criteria:
- User authentication feature implemented (login, logout, register)
- All authentication endpoints return correct status codes
- JWT tokens generated and validated correctly
- 15+ tests cover authentication flows
- All tests pass (npm test exits with 0)
- Test coverage >= 80%
- No TypeScript or ESLint errors
```

### Example 2: Bug Fix

**Before:**
```
Completion Criteria:
- Bug is fixed
```

**After:**
```
Completion Criteria:
- Clicking "Submit" on empty form no longer causes crash
- Form displays validation error message
- New regression test added (test_empty_form_submission)
- All 52 existing tests still pass
- Console logs show no errors during form interaction
```

### Example 3: Refactoring

**Before:**
```
Completion Criteria:
- Code is cleaner and better organized
```

**After:**
```
Completion Criteria:
- All API calls moved to dedicated service layer
- No API calls in component files (0 instances of axios/fetch in components/)
- Service layer has comprehensive tests (coverage >= 85%)
- All 73 existing tests still pass (no behavior changes)
- ESLint shows 0 errors, 0 warnings
```

## Summary

Good completion criteria are:
1. **Specific** - Clearly defined, no ambiguity
2. **Measurable** - Quantifiable or verifiable
3. **Achievable** - Possible within the environment
4. **Relevant** - Directly related to the task
5. **Verifiable** - Can be checked automatically

Always ask: "If I handed this prompt to someone else, would they know exactly when the task is complete?"
