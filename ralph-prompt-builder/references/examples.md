# Ralph-Loop Prompt Examples

20+ real-world examples comparing ineffective (❌) vs effective (✅) prompts.

## Table of Contents

1. [TDD Development](#tdd-development)
2. [Bug Fixing](#bug-fixing)
3. [Feature Implementation](#feature-implementation)
4. [Greenfield Projects](#greenfield-projects)
5. [Refactoring](#refactoring)
6. [Multi-Phase Projects](#multi-phase-projects)
7. [Performance Optimization](#performance-optimization)
8. [Documentation](#documentation)
9. [Testing](#testing)
10. [Multi-Project Context](#multi-project-context)

---

## TDD Development

### Example 1: REST API with TDD

❌ **Bad Prompt:**
```
Build a REST API for todos using TDD.

/ralph-loop "Build a REST API for todos using TDD" --completion-promise "DONE"
```

**Problems:**
- No specific requirements
- No completion criteria
- No max iterations
- Vague "using TDD" without workflow

✅ **Good Prompt:**
```
Build a REST API for todos following TDD workflow:

Endpoints Required:
- GET /todos - list all todos
- POST /todos - create todo (requires: title, optional: description, completed)
- PUT /todos/:id - update todo
- DELETE /todos/:id - delete todo

TDD Workflow:
1. Write failing test for endpoint behavior
2. Run tests (npm test)
3. Implement minimal code to pass test
4. Run tests again
5. If tests fail, debug and fix
6. If tests pass, refactor if needed
7. Repeat for next endpoint/behavior
8. When all endpoints implemented and all tests pass, output <promise>ALL_TESTS_PASS</promise>

Completion Criteria:
- All 4 endpoints implemented and working
- Each endpoint has tests covering success and error cases
- Test coverage >= 80%
- All tests pass (npm test exits with 0)
- No ESLint errors

/ralph-loop "[prompt]" --completion-promise "ALL_TESTS_PASS" --max-iterations 40
```

**Why it's better:**
- Specific endpoints listed
- Clear TDD workflow
- Measurable criteria
- Max iterations set
- Tests provide automatic feedback loop

### Example 2: Authentication Service

❌ **Bad Prompt:**
```
Create authentication with TDD.

/ralph-loop "Create authentication with TDD" --completion-promise "COMPLETE"
```

✅ **Good Prompt:**
```
Implement JWT authentication following TDD:

Features:
1. User registration (POST /auth/register)
2. User login (POST /auth/login)
3. Token validation middleware
4. Protected route example (GET /auth/me)

TDD Process for each feature:
1. Write test describing expected behavior
2. Run test - confirm it fails
3. Implement feature
4. Run test - if fails, debug and fix
5. Run test - if passes, move to next feature
6. After all features: run full test suite

Completion Criteria:
- All 4 features implemented
- Registration creates user and returns token
- Login validates credentials and returns token
- Middleware correctly validates tokens
- Protected route rejects invalid tokens
- 20+ tests covering all auth flows
- All tests pass (npm test)
- Test coverage >= 85%
- No security warnings from npm audit

When all criteria met, output <promise>AUTH_COMPLETE</promise>

/ralph-loop "[prompt]" --completion-promise "AUTH_COMPLETE" --max-iterations 50
```

---

## Bug Fixing

### Example 3: Form Validation Bug

❌ **Bad Prompt:**
```
Fix the bug in the form.

/ralph-loop "Fix the bug in the form" --completion-promise "FIXED"
```

**Problems:**
- Which bug?
- Which form?
- How to verify it's fixed?

✅ **Good Prompt:**
```
Fix bug: Form submission crashes when email field is empty.

Reproduction:
1. Navigate to /register
2. Fill username field
3. Leave email field empty
4. Click "Submit"
5. Result: App crashes with "Cannot read property 'includes' of undefined"

Fix Workflow:
1. Create test that reproduces the bug
2. Run test - confirm it fails (bug exists)
3. Implement fix (add null check before .includes())
4. Run test - if fails, refine fix
5. Run all tests - ensure no regressions
6. When bug test passes AND all other tests pass, output <promise>BUG_FIXED</promise>

Completion Criteria:
- Bug no longer reproducible (empty email doesn't crash)
- Form displays validation error for empty email
- New test added (test_email_validation_empty_field)
- All 47 existing tests still pass
- Console shows no errors when submitting empty email

/ralph-loop "[prompt]" --completion-promise "BUG_FIXED" --max-iterations 15
```

### Example 4: Memory Leak

❌ **Bad Prompt:**
```
There's a memory leak, fix it.

/ralph-loop "There's a memory leak, fix it" --completion-promise "FIXED" --max-iterations 20
```

✅ **Good Prompt:**
```
Fix memory leak in real-time dashboard component.

Symptoms:
- Memory usage grows from 50MB to 500MB+ over 10 minutes
- Browser tab becomes unresponsive
- Leak occurs when dashboard is open

Investigation Steps:
1. Use Chrome DevTools heap snapshot to identify leak
2. Likely cause: WebSocket connection not closed on unmount
3. Check for event listeners not removed

Fix Workflow:
1. Add cleanup in useEffect return (close WebSocket, remove listeners)
2. Test: Open dashboard, monitor memory for 2 minutes
3. Test: Navigate away, verify memory is released
4. Run all component tests
5. When memory stable AND tests pass, output <promise>LEAK_FIXED</promise>

Completion Criteria:
- Memory usage stays below 100MB after 5 minutes
- Memory is released when navigating away from dashboard
- All component tests pass
- No console errors or warnings
- WebSocket connection properly closes on unmount

/ralph-loop "[prompt]" --completion-promise "LEAK_FIXED" --max-iterations 20
```

---

## Feature Implementation

### Example 5: Search Functionality

❌ **Bad Prompt:**
```
Add search to the app.

/ralph-loop "Add search to the app" --completion-promise "DONE" --max-iterations 30
```

✅ **Good Prompt:**
```
Implement search functionality for products page.

Requirements:
- Search input field in header
- Search by product name or description
- Real-time filtering (update results as user types)
- Debounce input (300ms delay)
- Display "No results" message when appropriate
- Show result count "Showing X of Y products"

Implementation:
1. Add search input component
2. Implement debounced search function
3. Filter products based on search term (case-insensitive)
4. Update UI to display results
5. Handle empty results state
6. Add tests for search functionality
7. When all requirements met, output <promise>SEARCH_COMPLETE</promise>

Completion Criteria:
- Search input visible on products page
- Typing filters products in real-time
- Search is case-insensitive
- Debouncing works (verified: doesn't filter on every keystroke)
- Empty results shows "No products match 'term'"
- Result count displays correctly
- 8+ tests covering search scenarios
- All tests pass
- No performance issues (search completes in < 100ms)

/ralph-loop "[prompt]" --completion-promise "SEARCH_COMPLETE" --max-iterations 35
```

### Example 6: File Upload

❌ **Bad Prompt:**
```
Let users upload files.

/ralph-loop "Let users upload files" --completion-promise "COMPLETE"
```

✅ **Good Prompt:**
```
Implement file upload functionality for user avatars.

Requirements:
- Upload button on profile page
- Accept only: .jpg, .jpeg, .png
- Max file size: 5MB
- Preview image before upload
- Resize to 200x200px on server
- Save to /uploads/avatars directory
- Update user profile with avatar URL
- Show upload progress

Implementation Phases:
Phase 1: Frontend Upload UI
- File input with validation
- Image preview
- Upload progress indicator

Phase 2: Backend Processing
- Multer middleware for file uploads
- Image resizing with sharp library
- Save file with unique name
- Update user record with avatar path

Phase 3: Integration & Testing
- Connect frontend to backend
- Test upload flow end-to-end
- Error handling (file too large, wrong type)

Completion Criteria:
- Users can select image file
- Preview shows selected image
- Upload progress displays (0-100%)
- Server receives and resizes image to 200x200px
- Image saved to /uploads/avatars/[unique-name].jpg
- User profile shows uploaded avatar
- Rejects files > 5MB (shows error message)
- Rejects non-image files (shows error message)
- 12+ tests covering upload scenarios
- All tests pass

When all criteria met, output <promise>UPLOAD_COMPLETE</promise>

/ralph-loop "[prompt]" --completion-promise "UPLOAD_COMPLETE" --max-iterations 45
```

---

## Greenfield Projects

### Example 7: Blog Platform

❌ **Bad Prompt:**
```
Build a blog platform.

/ralph-loop "Build a blog platform" --completion-promise "DONE" --max-iterations 100
```

✅ **Good Prompt:**
```
Build a minimal blog platform from scratch.

Tech Stack:
- Backend: Node.js + Express
- Database: PostgreSQL
- Frontend: React
- Testing: Jest

Core Features:
1. User authentication (register, login, logout)
2. Create blog posts (title, content, author)
3. List all posts (homepage)
4. View single post
5. Edit/delete own posts

Database Schema:
- users: id, email, password_hash, created_at
- posts: id, title, content, author_id, created_at, updated_at

Implementation Plan:
Phase 1: Project Setup
- Initialize Node.js project
- Setup Express server
- Configure PostgreSQL connection
- Create database schema

Phase 2: Authentication
- User registration endpoint
- Login endpoint (JWT tokens)
- Auth middleware
- Tests for auth

Phase 3: Posts API
- Create post endpoint (authenticated)
- List posts endpoint
- Get single post endpoint
- Update post endpoint (own posts only)
- Delete post endpoint (own posts only)
- Tests for posts API

Phase 4: Frontend
- Login/Register forms
- Post list view
- Single post view
- Create/Edit post forms
- Basic styling

Phase 5: Integration
- Connect frontend to API
- End-to-end tests
- Error handling

Completion Criteria:
- Project runs with npm start
- Database schema created
- All 5 core features working
- 30+ tests covering backend and frontend
- All tests pass (npm test)
- Test coverage >= 75%
- No TypeScript or ESLint errors
- Build succeeds (npm run build)
- README with setup instructions

When all criteria met, output <promise>BLOG_COMPLETE</promise>

/ralph-loop "[prompt]" --completion-promise "BLOG_COMPLETE" --max-iterations 120
```

---

## Refactoring

### Example 8: State Management Migration

❌ **Bad Prompt:**
```
Refactor to use Redux instead of Context.

/ralph-loop "Refactor to use Redux instead of Context" --completion-promise "DONE"
```

✅ **Good Prompt:**
```
Migrate state management from Context API to Redux Toolkit.

Current State:
- 3 Context providers: AuthContext, CartContext, ThemeContext
- Used in 15+ components

Migration Plan:
1. Install Redux Toolkit
2. Create Redux store with 3 slices (auth, cart, theme)
3. Migrate AuthContext → authSlice
4. Migrate CartContext → cartSlice
5. Migrate ThemeContext → themeSlice
6. Update all components to use useSelector/useDispatch
7. Remove old Context files
8. Test thoroughly

Refactoring Rules:
- All existing tests must still pass (no behavior changes)
- No breaking changes to component interfaces
- Maintain same state shape (to minimize component changes)

Completion Criteria:
- Redux store configured with 3 slices
- All Context providers removed
- All components using Redux hooks (no Context imports)
- All 73 existing tests still pass
- No console errors or warnings
- Redux DevTools working (can inspect state)
- State persistence works (if previously implemented)
- Build succeeds
- No TypeScript errors

When all criteria met, output <promise>REDUX_MIGRATION_COMPLETE</promise>

/ralph-loop "[prompt]" --completion-promise "REDUX_MIGRATION_COMPLETE" --max-iterations 60
```

---

## Multi-Phase Projects

### Example 9: E-commerce Checkout Flow

❌ **Bad Prompt:**
```
Build checkout for e-commerce site.

/ralph-loop "Build checkout for e-commerce site" --completion-promise "COMPLETE" --max-iterations 80
```

✅ **Good Prompt:**
```
Implement complete checkout flow for e-commerce site.

Checkout Flow (3 phases):

Phase 1: Shopping Cart Summary
- Display cart items with quantities
- Show subtotal, tax, total
- "Edit cart" button returns to cart page
- "Proceed to shipping" button advances

Completion for Phase 1:
- Cart summary displays all items correctly
- Prices calculated correctly
- Navigation works
- 5+ tests for cart summary

Phase 2: Shipping Information
- Form: name, address, city, state, zip, phone
- Validation for all fields
- "Back to cart" and "Continue to payment" buttons
- Save shipping info to order object

Completion for Phase 2:
- Form validates all fields
- Required field validation works
- Shipping info saves correctly
- 8+ tests for shipping form

Phase 3: Payment & Confirmation
- Mock payment form (card number, expiry, CVV)
- Order review (items, shipping, total)
- "Place order" creates order record
- Redirect to confirmation page
- Show order number and details

Completion for Phase 3:
- Payment form validates card info
- Order created in database
- Confirmation page shows order details
- 10+ tests for payment/confirmation

Overall Completion Criteria:
- All 3 phases complete and connected
- User can complete checkout from cart to confirmation
- Order data saved correctly
- All validation working
- 25+ tests total (all passing)
- End-to-end test completes full checkout
- No errors in console
- Build succeeds

When all phases complete and criteria met, output <promise>CHECKOUT_COMPLETE</promise>

/ralph-loop "[prompt]" --completion-promise "CHECKOUT_COMPLETE" --max-iterations 90
```

---

## Performance Optimization

### Example 10: Database Query Optimization

❌ **Bad Prompt:**
```
Optimize the slow queries.

/ralph-loop "Optimize the slow queries" --completion-promise "OPTIMIZED" --max-iterations 30
```

✅ **Good Prompt:**
```
Optimize slow database queries in user dashboard.

Current Performance:
- Dashboard loads in 3-5 seconds
- Users table: 100,000 rows
- Posts table: 500,000 rows
- Orders table: 1,000,000 rows

Target Performance:
- Dashboard loads in < 500ms

Optimization Process:
1. Enable query logging
2. Identify queries taking > 100ms
3. For each slow query:
   - Analyze with EXPLAIN
   - Add appropriate indexes
   - Rewrite if needed (reduce N+1, use joins)
   - Test new performance
   - Verify query still returns correct data
4. Measure overall dashboard load time
5. When all queries < 100ms and dashboard < 500ms, output <promise>QUERIES_OPTIMIZED</promise>

Completion Criteria:
- All queries execute in < 100ms
- Dashboard loads in < 500ms (measured)
- Indexes added to: users(email), posts(author_id), orders(user_id, created_at)
- N+1 queries eliminated (use eager loading)
- All data still correct (all tests pass)
- No performance regressions in other pages
- Query plan analysis shows index usage

/ralph-loop "[prompt]" --completion-promise "QUERIES_OPTIMIZED" --max-iterations 40
```

---

## Documentation

### Example 11: API Documentation

❌ **Bad Prompt:**
```
Document the API.

/ralph-loop "Document the API" --completion-promise "DOCUMENTED" --max-iterations 20
```

✅ **Good Prompt:**
```
Create comprehensive API documentation for REST API.

Documentation Requirements:
1. README.md with:
   - API overview
   - Authentication (how to get/use tokens)
   - Base URL
   - Response formats (success/error)
   - Rate limiting

2. For each endpoint document:
   - HTTP method and path
   - Description
   - Authentication required (yes/no)
   - Request parameters (path, query, body)
   - Request example (curl)
   - Response example (success)
   - Error responses (400, 401, 404, 500)

Endpoints to document (15 total):
- POST /auth/register
- POST /auth/login
- GET /auth/me
- GET /users
- GET /users/:id
- PUT /users/:id
- DELETE /users/:id
- GET /posts
- POST /posts
- GET /posts/:id
- PUT /posts/:id
- DELETE /posts/:id
- GET /posts/:id/comments
- POST /posts/:id/comments
- DELETE /comments/:id

Documentation Format:
Use clear markdown with code blocks for examples.

Completion Criteria:
- API_DOCS.md file exists
- All 15 endpoints documented
- Each endpoint has: method, path, description, auth requirement, parameters, request example, response examples (success + errors)
- Authentication section complete
- Code examples are valid (can copy-paste and run)
- Table of contents for easy navigation
- No spelling or grammar errors

When all criteria met, output <promise>DOCS_COMPLETE</promise>

/ralph-loop "[prompt]" --completion-promise "DOCS_COMPLETE" --max-iterations 25
```

---

## Testing

### Example 12: Test Coverage Improvement

❌ **Bad Prompt:**
```
Improve test coverage.

/ralph-loop "Improve test coverage" --completion-promise "DONE"
```

✅ **Good Prompt:**
```
Increase test coverage from 45% to >= 80%.

Current Coverage:
- Statements: 45%
- Branches: 38%
- Functions: 52%
- Lines: 44%

Uncovered Areas (from coverage report):
- src/services/payment.ts (0% coverage)
- src/services/notification.ts (12% coverage)
- src/utils/validation.ts (35% coverage)
- src/controllers/order.ts (28% coverage)
- Error handling branches throughout

Testing Process:
1. Run npm run test:coverage to see current state
2. Start with payment.ts (highest priority, 0% coverage):
   - Write tests for all exported functions
   - Cover success cases
   - Cover error cases
   - Run coverage, verify improvement
3. Move to notification.ts, then validation.ts, then order.ts
4. Focus on uncovered branches (error handling, edge cases)
5. Run full test suite after each file
6. When coverage >= 80%, output <promise>COVERAGE_IMPROVED</promise>

Completion Criteria:
- Overall coverage >= 80% (all metrics: statements, branches, functions, lines)
- payment.ts: >= 85% coverage
- notification.ts: >= 85% coverage
- validation.ts: >= 85% coverage
- order.ts: >= 80% coverage
- All tests pass (new and existing)
- No flaky tests (run suite 3 times, all pass)
- Tests run in < 30 seconds total

/ralph-loop "[prompt]" --completion-promise "COVERAGE_IMPROVED" --max-iterations 50
```

---

## Multi-Project Context

### Example 13: Microservice (Shared Context)

❌ **Bad Prompt (Repetitive):**
```
Project 1:
Build User Service using Node.js, Express, PostgreSQL, Jest, follows RESTful patterns, uses JWT auth, has CI/CD, etc...

Project 2:
Build Product Service using Node.js, Express, PostgreSQL, Jest, follows RESTful patterns, uses JWT auth, has CI/CD, etc...

Project 3:
Build Order Service using Node.js, Express, PostgreSQL, Jest, follows RESTful patterns, uses JWT auth, has CI/CD, etc...
```

**Problem:** Repeats same context 3 times, wastes tokens.

✅ **Good Prompt (Shared Context):**

**First Project (establishes pattern):**
```
Build User Service (microservices architecture).

Tech Stack:
- Node.js + Express
- PostgreSQL
- Jest testing
- JWT authentication
- Docker
- CI/CD: GitHub Actions

Structure:
services/user-service/
  ├── src/
  │   ├── controllers/
  │   ├── models/
  │   ├── routes/
  │   ├── middleware/
  │   └── utils/
  ├── tests/
  ├── Dockerfile
  ├── package.json
  └── README.md

Features:
- CRUD for users
- Email/password registration
- JWT token generation
- Input validation
- Error handling

[... completion criteria ...]

/ralph-loop "[prompt]" --completion-promise "USER_SERVICE_COMPLETE" --max-iterations 60
```

**Subsequent Projects (reference pattern):**
```
Build Product Service following User Service patterns.

Shared Context:
- Use same tech stack as User Service
- Follow same directory structure
- Use same testing approach (Jest)
- Use same Docker setup
- Use same CI/CD pipeline

Product Service Specifics:
- Products table: id, name, description, price, stock, created_at
- CRUD endpoints for products
- Additional: GET /products/search?query=X (search by name/description)
- Additional: GET /products/low-stock (stock < 10)

Differences from User Service:
- No authentication features (assumes API gateway handles auth)
- Additional search functionality
- Stock management logic

[... completion criteria ...]

/ralph-loop "[prompt]" --completion-promise "PRODUCT_SERVICE_COMPLETE" --max-iterations 50
```

**Why it's better:**
- References existing pattern instead of repeating
- Highlights only differences
- Saves context tokens
- Clearer what's unique to this service

---

### Example 14: Feature Across Multiple Services

✅ **Good Prompt (Cross-Service Feature):**
```
Add logging to all services (User, Product, Order services).

Context:
- 3 existing services already running
- Each uses Express.js
- Logs currently go to console only

Logging Requirements:
- Use winston library (consistent across all services)
- Log levels: error, warn, info, debug
- Log format: JSON with timestamp, service name, level, message
- Save logs to: logs/[service-name]-[date].log
- Rotate logs daily (keep 7 days)

Implementation (same for all 3 services):
1. Install winston
2. Create logger config in src/utils/logger.ts
3. Replace console.log/error with logger.info/error
4. Test logging (check file creation, format, rotation)

Completion Criteria (per service):
- Winston configured correctly
- All console.log replaced with logger calls
- Logs save to correct file
- Log format is JSON
- Log rotation works (verified by setting test date)
- No console.log statements remain (grep check)

Overall Completion:
- All 3 services logging correctly
- Log files exist for each service
- All tests still pass for all services
- Build succeeds for all services

When all 3 services complete, output <promise>LOGGING_COMPLETE</promise>

/ralph-loop "[prompt]" --completion-promise "LOGGING_COMPLETE" --max-iterations 40
```

---

## Advanced Examples

### Example 15: Integration Testing

✅ **Good Prompt:**
```
Create end-to-end integration tests for user registration flow.

Flow to test:
1. User visits /register
2. Fills form (email, password, confirm password)
3. Submits form
4. Backend validates, creates user, returns token
5. Frontend stores token
6. User redirected to /dashboard
7. Dashboard displays user info

Test Setup:
- Use Cypress for E2E testing
- Test against local dev server
- Use test database (reset before each test)

Test Cases:
1. Successful registration (happy path)
2. Email already exists (should show error)
3. Passwords don't match (should show error)
4. Invalid email format (should show error)
5. Password too short (should show error)
6. Network error (should show error message)

Implementation:
1. Install Cypress
2. Create test database reset script
3. Write test for each case
4. Run tests
5. Fix any failures
6. When all tests pass, output <promise>E2E_TESTS_COMPLETE</promise>

Completion Criteria:
- 6 E2E tests written
- All tests pass
- Tests run in < 60 seconds
- Test database resets before each test
- Tests can run multiple times without issues
- Screenshots captured on failure
- CI/CD configured to run E2E tests

/ralph-loop "[prompt]" --completion-promise "E2E_TESTS_COMPLETE" --max-iterations 35
```

### Example 16: Security Audit Fix

✅ **Good Prompt:**
```
Fix all high-severity security vulnerabilities reported by npm audit.

Current State:
- npm audit shows 8 high-severity vulnerabilities
- 3 in production dependencies
- 5 in dev dependencies

Fix Process:
1. Run npm audit to see current vulnerabilities
2. For each vulnerability:
   - Read the advisory
   - Check if fix is available (npm audit fix)
   - If auto-fix fails, update manually
   - Test that app still works after update
   - Run tests
3. After all fixes, run npm audit again
4. When 0 high-severity vulnerabilities, output <promise>AUDIT_CLEAN</promise>

Completion Criteria:
- npm audit reports 0 high-severity vulnerabilities
- npm audit reports 0 critical vulnerabilities
- All tests still pass (no breaking changes from updates)
- App runs without errors
- Build succeeds
- package-lock.json updated
- Document any manual fixes in CHANGELOG.md

/ralph-loop "[prompt]" --completion-promise "AUDIT_CLEAN" --max-iterations 25
```

### Example 17: Database Migration

✅ **Good Prompt:**
```
Create database migration to add user roles.

Current Schema:
- users: id, email, password_hash, created_at

New Schema:
- users: id, email, password_hash, role, created_at
- roles: 'admin', 'moderator', 'user' (default: 'user')

Migration Requirements:
- Add 'role' column to users table
- Set default value 'user'
- Update existing users to 'user' role
- Add index on role column
- Create migration file (reversible)
- Update User model
- Update seed data

Implementation:
1. Create migration file: YYYYMMDDHHMMSS_add_user_roles.js
2. Write 'up' migration (add column, set defaults, add index)
3. Write 'down' migration (remove column, remove index)
4. Run migration on test database
5. Test rollback (down migration)
6. Test migration again (up migration)
7. Update User model to include 'role' field
8. Update tests to include role
9. When migration works both ways and tests pass, output <promise>MIGRATION_COMPLETE</promise>

Completion Criteria:
- Migration file exists
- Migration runs successfully (up)
- Rollback works successfully (down)
- User model includes 'role' field
- Existing users have 'user' role
- New users default to 'user' role
- Index exists on role column
- All tests pass with new schema
- Seed data includes roles

/ralph-loop "[prompt]" --completion-promise "MIGRATION_COMPLETE" --max-iterations 30
```

### Example 18: Error Handling Standardization

✅ **Good Prompt:**
```
Standardize error handling across all API endpoints.

Current State:
- 20 API endpoints
- Inconsistent error responses
- Some return HTML, some JSON
- No standard error format

Target Error Format:
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": {...}
  }
}

Error Codes to Implement:
- VALIDATION_ERROR (400)
- UNAUTHORIZED (401)
- FORBIDDEN (403)
- NOT_FOUND (404)
- CONFLICT (409)
- INTERNAL_ERROR (500)

Implementation:
1. Create error handling middleware (src/middleware/errorHandler.ts)
2. Create custom error classes for each error type
3. Update all endpoints to use custom errors
4. Test each endpoint's error responses
5. When all endpoints use standard format, output <promise>ERRORS_STANDARDIZED</promise>

Completion Criteria:
- Error middleware implemented
- 6 custom error classes created
- All 20 endpoints use custom errors (not raw throw/res.status)
- All error responses match standard format
- Tests updated for new error format
- All tests pass
- Documentation updated with error codes
- No endpoints return HTML errors

/ralph-loop "[prompt]" --completion-promise "ERRORS_STANDARDIZED" --max-iterations 40
```

### Example 19: Component Library Creation

✅ **Good Prompt:**
```
Create reusable component library for UI components.

Components to Create:
1. Button (variants: primary, secondary, danger)
2. Input (with validation states)
3. Card
4. Modal
5. Dropdown
6. Alert (info, success, warning, error)

Requirements per Component:
- TypeScript with proper types
- Styled with CSS modules
- Accessible (ARIA labels, keyboard nav)
- Storybook story
- Unit tests
- Documentation in README

Implementation:
1. Setup component library structure
2. Create each component with:
   - Component file (e.g., Button.tsx)
   - Styles file (Button.module.css)
   - Test file (Button.test.tsx)
   - Story file (Button.stories.tsx)
3. Test component
4. Document in README
5. When all 6 components complete, output <promise>LIBRARY_COMPLETE</promise>

Completion Criteria:
- 6 components implemented
- Each component fully typed (TypeScript)
- Each component has tests (100% coverage per component)
- Each component has Storybook story
- All tests pass
- Storybook builds successfully (npm run storybook)
- Components are accessible (no a11y warnings)
- README documents all components with examples
- Build succeeds (npm run build)

/ralph-loop "[prompt]" --completion-promise "LIBRARY_COMPLETE" --max-iterations 70
```

### Example 20: Caching Implementation

✅ **Good Prompt:**
```
Implement Redis caching for frequently accessed data.

Data to Cache:
- User profiles (GET /users/:id) - cache 5 min
- Product listings (GET /products) - cache 1 min
- Blog posts (GET /posts/:id) - cache 10 min

Cache Strategy:
- Check cache first
- If miss, query database
- Store result in cache
- Return result
- Invalidate cache on updates/deletes

Implementation:
1. Install and configure Redis client
2. Create cache middleware
3. Add cache to GET /users/:id endpoint
4. Add cache to GET /products endpoint
5. Add cache to GET /posts/:id endpoint
6. Add cache invalidation to PUT/DELETE endpoints
7. Test cache hits/misses
8. When all endpoints cached correctly, output <promise>CACHING_COMPLETE</promise>

Completion Criteria:
- Redis client connected
- Cache hits reduce database queries (verified by query logging)
- GET /users/:id: cache hit serves from Redis
- GET /products: cache hit serves from Redis
- GET /posts/:id: cache hit serves from Redis
- PUT/DELETE endpoints invalidate cache
- Cache TTLs set correctly (5min, 1min, 10min)
- All tests pass (including cache tests)
- Performance improved (measured: 50%+ faster for cached requests)
- No stale data served (invalidation works)

/ralph-loop "[prompt]" --completion-promise "CACHING_COMPLETE" --max-iterations 45
```

---

## Summary

**Key Patterns in Good Prompts:**

1. **Specific requirements** - Not "build X" but "build X with features A, B, C"
2. **Measurable criteria** - "All tests pass", "Coverage >= 80%", not "code works well"
3. **Clear workflow** - Step-by-step process for complex tasks
4. **Automatic verification** - Tests, builds, linters provide feedback
5. **Max iterations set** - Always include safety limit
6. **Promise tag** - Always explicit `<promise>PHRASE</promise>` instruction
7. **Phased approach** - Break complex tasks into phases
8. **No subjective terms** - Avoid "good", "clean", "nice", "beautiful"
9. **Context efficiency** - Reference shared context, don't repeat
10. **Escape conditions** - For tasks that might get stuck

**Use these examples as templates** - Replace specifics with your task details while maintaining the structure.
