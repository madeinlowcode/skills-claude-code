# TDD Development Template for Ralph-Loop

Use this template when implementing features using Test-Driven Development methodology.

## Instructions

1. Replace all `[PLACEHOLDERS]` with your specific details
2. Adjust test coverage percentage to your needs (recommended: 75-85%)
3. Set max-iterations based on complexity (recommended: 30-50 for most TDD tasks)
4. Copy the final prompt and run the ralph-loop command

---

## Prompt Template

```
Implement [FEATURE_NAME] following TDD workflow:

Feature Description:
[Describe what you're building in 2-3 sentences]

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
- [Add more as needed]

TDD Workflow:
1. Write failing test for [specific behavior/component]
2. Run test suite (npm test or equivalent)
3. Confirm test fails (expected failure)
4. Implement minimal code to pass the test
5. Run test suite again
6. If any tests fail:
   - Debug and identify the root cause
   - Fix the implementation
   - Re-run tests
7. If all tests pass:
   - Refactor if needed (while keeping tests green)
   - Move to next behavior
8. Repeat steps 1-7 for each requirement
9. When all requirements implemented and all tests pass, output <promise>ALL_TESTS_PASS</promise>

Behaviors/Components to Test:
- [Behavior/Component 1]
- [Behavior/Component 2]
- [Behavior/Component 3]
- [Add more as needed]

Completion Criteria:
- [ ] All requirements implemented
- [ ] Each requirement has corresponding tests
- [ ] All tests pass (npm test exits with code 0)
- [ ] Test coverage >= [X]% (run coverage report to verify)
- [ ] No linting errors ([linter command] exits with code 0)
- [ ] Code follows project conventions
- [ ] [Any additional criteria specific to your project]

When all criteria above are met, output <promise>ALL_TESTS_PASS</promise>
```

---

## Ralph-Loop Command

```bash
/ralph-loop "[YOUR_PROMPT_HERE]" \
  --completion-promise "ALL_TESTS_PASS" \
  --max-iterations [30-50]
```

---

## Example: REST API for Todo Management

```
Implement REST API for todo management following TDD workflow:

Feature Description:
Create a RESTful API that allows users to manage their todo items with full CRUD operations.

Requirements:
- GET /todos - retrieve all todos
- POST /todos - create new todo (requires: title, optional: description, completed)
- PUT /todos/:id - update existing todo
- DELETE /todos/:id - delete todo
- Input validation for all endpoints
- Error handling with appropriate HTTP status codes

TDD Workflow:
1. Write failing test for endpoint behavior
2. Run test suite (npm test)
3. Confirm test fails (expected failure)
4. Implement minimal code to pass the test
5. Run test suite again
6. If any tests fail:
   - Debug and identify the root cause
   - Fix the implementation
   - Re-run tests
7. If all tests pass:
   - Refactor if needed (while keeping tests green)
   - Move to next endpoint
8. Repeat steps 1-7 for each endpoint
9. When all endpoints implemented and all tests pass, output <promise>ALL_TESTS_PASS</promise>

Endpoints to Test:
- GET /todos (returns array of todos)
- GET /todos (empty array when no todos)
- POST /todos (creates todo with valid data)
- POST /todos (rejects empty title)
- PUT /todos/:id (updates existing todo)
- PUT /todos/:id (returns 404 for non-existent ID)
- DELETE /todos/:id (deletes existing todo)
- DELETE /todos/:id (returns 404 for non-existent ID)

Completion Criteria:
- [ ] All 4 CRUD endpoints implemented
- [ ] Each endpoint has tests for success and error cases
- [ ] All tests pass (npm test exits with code 0)
- [ ] Test coverage >= 80%
- [ ] No ESLint errors (npm run lint exits with code 0)
- [ ] Input validation working (empty titles rejected)
- [ ] Error responses have correct status codes (400, 404, 500)
- [ ] All endpoints follow RESTful conventions

When all criteria above are met, output <promise>ALL_TESTS_PASS</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "ALL_TESTS_PASS" --max-iterations 40
```

---

## Tips for TDD Prompts

1. **Be specific about test cases** - List the specific scenarios to test (happy path + edge cases)
2. **Include coverage target** - Specify minimum acceptable test coverage percentage
3. **Define "passing" clearly** - Specify the exact command to run tests and expected exit code
4. **List edge cases** - Don't just test happy paths; include error conditions
5. **Set realistic iterations** - TDD requires multiple cycles; 30-50 iterations is typical
6. **Use descriptive promise** - "ALL_TESTS_PASS" is clearer than generic "DONE"

## Common TDD Completion Criteria

- [ ] All unit tests passing
- [ ] Test coverage >= [75-85]%
- [ ] No linting errors
- [ ] No TypeScript errors (if using TypeScript)
- [ ] Each function/component has tests
- [ ] Edge cases covered (null, undefined, empty, invalid input)
- [ ] Error handling tested
- [ ] Integration tests passing (if applicable)
