# Spec-Driven Lisa Prompt Example

Exemplo completo usando spec-based verification para um projeto crítico.

## Estrutura de Arquivos
````
project/
├── PROMPT.md
├── IMPLEMENTATION_PLAN.md
├── specs/
│   └── features.md
├── src/
│   └── ...
└── tests/
    └── ...
````

## Arquivo: specs/features.md
````markdown
# Todo API Specifications

## API-1: Create Todo

### Requirements
- [ ] POST /api/todos accepts { title, description }
- [ ] Title is required, min 3 chars, max 100 chars
- [ ] Description is optional, max 500 chars
- [ ] Returns 201 with created todo object
- [ ] Returns 400 with error message for validation failures
- [ ] Todo has: id, title, description, completed (default false), createdAt, updatedAt

### Tests Required
- [ ] POST with valid data returns 201
- [ ] POST with missing title returns 400
- [ ] POST with title <3 chars returns 400
- [ ] POST with title >100 chars returns 400
- [ ] POST with description >500 chars returns 400
- [ ] Returns correct todo object structure

---

## API-2: Get All Todos

### Requirements
- [ ] GET /api/todos returns array of all todos
- [ ] Results ordered by createdAt descending (newest first)
- [ ] Returns empty array [] if no todos
- [ ] Returns 200 with todos array

### Tests Required
- [ ] GET returns all todos
- [ ] Todos ordered by createdAt descending
- [ ] Empty array when no todos
- [ ] Correct structure for each todo

---

## API-3: Get Single Todo

### Requirements
- [ ] GET /api/todos/:id returns single todo
- [ ] Returns 404 if todo not found
- [ ] Returns 200 with todo object if found
- [ ] ID parameter must be validated

### Tests Required
- [ ] GET with valid ID returns 200
- [ ] GET with invalid ID returns 404
- [ ] Returned object has correct structure

---

## API-4: Update Todo

### Requirements
- [ ] PUT /api/todos/:id updates todo
- [ ] Can update title, description, completed (all optional)
- [ ] Validation same as create (min/max lengths)
- [ ] Returns 200 with updated todo
- [ ] Returns 400 for validation errors
- [ ] Returns 404 if todo not found
- [ ] updatedAt field is updated

### Tests Required
- [ ] Update title only
- [ ] Update description only
- [ ] Toggle completed flag
- [ ] Update multiple fields
- [ ] Validation errors return 400
- [ ] Not found returns 404

---

## API-5: Delete Todo

### Requirements
- [ ] DELETE /api/todos/:id removes todo
- [ ] Returns 204 No Content
- [ ] Returns 404 if todo not found
- [ ] Deleted todo cannot be retrieved

### Tests Required
- [ ] DELETE returns 204
- [ ] TODO no longer exists after delete
- [ ] Not found returns 404

---

## TEST-1: Full Test Coverage

### Requirements
- [ ] All endpoints have passing tests
- [ ] All validation paths tested
- [ ] All error paths tested
- [ ] Code coverage >85%
- [ ] Specific endpoints (API-1 through API-5) >95% coverage

### Tests Required
- [ ] Happy path for each endpoint
- [ ] Error path for each endpoint
- [ ] Edge cases covered
- [ ] Coverage report generated
````

## Arquivo: IMPLEMENTATION_PLAN.md
````markdown
# Todo API Implementation Plan

## Phase 1: Project Setup
- [ ] Initialize Node.js project
- [ ] Install express, body-parser, jest
- [ ] Setup project structure (src/, tests/)
- [ ] Configure test runner

## Phase 2: Core API Implementation
- [ ] Implement POST /api/todos (create)
- [ ] Implement GET /api/todos (read all)
- [ ] Implement GET /api/todos/:id (read one)
- [ ] Implement PUT /api/todos/:id (update)
- [ ] Implement DELETE /api/todos/:id (delete)

## Phase 3: Validation & Error Handling
- [ ] Add input validation middleware
- [ ] Implement error response format
- [ ] Handle missing/invalid parameters

## Phase 4: Testing
- [ ] Write tests for all endpoints
- [ ] Write tests for all validation paths
- [ ] Write tests for all error cases
- [ ] Achieve >85% code coverage
- [ ] All tests passing

## Phase 5: Documentation
- [ ] Document all API endpoints
- [ ] Document error responses
- [ ] Create usage examples
````

## Arquivo: PROMPT.md
````markdown
# Mission
Build a complete REST API for Todo management with full CRUD operations, validation, and comprehensive testing according to specs/features.md

# Source of Truth
The ONLY definition of "done" is specs/features.md. Your subjective sense of completion is IRRELEVANT. If specs/features.md says something must be done, it must be done and checked [x].

# Process Per Iteration
1. Read specs/features.md from disk (not from memory)
2. Find the FIRST unchecked requirement (- [ ])
3. Identify which feature/test it belongs to
4. Implement that specific requirement
5. Write or update tests as needed
6. Run `npm test` to verify the requirement passes
7. Mark [x] next to the requirement in specs/features.md
8. Commit with message: "feat: implement [REQ-NAME]"

# Mandatory Verification (NEVER SKIP THIS)
Before outputting ANY completion promise:

1. Run command: `cat specs/features.md`
   → Re-read the ENTIRE spec from disk (not memory)

2. Count all checked [x] and unchecked [ ] requirements
   → Format: "X requirements checked, Y unchecked"

3. For EACH section in specs/features.md:
   - Verify code implementation exists
   - Verify test exists and passes
   - Verify requirement is checked [x]

4. Run verification:
```bash
   npm test
```
   → All tests must pass with exit code 0

5. Check code coverage:
```bash
   npm test -- --coverage
```
   → Must show >85% coverage

6. DECISION:
   - IF any [ ] unchecked: Go back to step 1, find next item
   - IF all [x] AND all tests pass AND coverage >85%: Output promise below

# Completion Criteria
When ALL of the following are true:
- specs/features.md shows 100% requirements checked [x]
- `npm test` passes with all tests passing
- Code coverage >85% for API functions
- No TypeScript or linting errors
- All endpoints respond correctly

OUTPUT THIS PROMISE:
<promise>ALL_API_SPECIFICATIONS_VERIFIED_AND_TESTED</promise>

# Constraints
- One requirement per iteration (systematic progress)
- Do NOT skip ahead - follow specs order
- Each requirement must have passing test
- Commit after each requirement completed
- Re-read specs from disk, not memory