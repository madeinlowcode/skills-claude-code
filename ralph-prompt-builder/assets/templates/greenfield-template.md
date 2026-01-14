# Greenfield Project Template for Ralph-Loop

Use this template when building a project from scratch (greenfield development).

## Instructions

1. Replace all `[PLACEHOLDERS]` with your project specifics
2. Define tech stack clearly
3. Break project into logical phases
4. Set higher max-iterations (recommended: 100-150 for complete projects)
5. Copy the final prompt and run the ralph-loop command

---

## Prompt Template

```
Build [PROJECT_NAME] from scratch.

Project Description:
[Describe what you're building in 2-3 sentences]

Tech Stack:
- Backend: [e.g., Node.js + Express, Python + Flask, etc.]
- Database: [e.g., PostgreSQL, MongoDB, etc.]
- Frontend: [e.g., React, Vue, vanilla HTML/CSS/JS]
- Testing: [e.g., Jest, Pytest, Mocha, etc.]
- [Any other relevant technologies]

Core Features:
1. [Feature 1 - brief description]
2. [Feature 2 - brief description]
3. [Feature 3 - brief description]
[Add more as needed]

Database Schema (if applicable):
- [table/collection 1]: [fields]
- [table/collection 2]: [fields]
[Add more as needed]

Implementation Phases:

Phase 1: Project Setup
- [ ] Initialize project ([npm init, create-react-app, etc.])
- [ ] Setup folder structure
- [ ] Install dependencies
- [ ] Configure database connection
- [ ] Create database schema/migrations
- [ ] Setup testing framework
Verification: [Command to verify setup works]

Phase 2: [Core Feature Set 1]
- [ ] [Specific task 1]
- [ ] [Specific task 2]
- [ ] [Tests for feature set 1]
Verification: [How to verify Phase 2 complete]

Phase 3: [Core Feature Set 2]
- [ ] [Specific task 1]
- [ ] [Specific task 2]
- [ ] [Tests for feature set 2]
Verification: [How to verify Phase 3 complete]

Phase 4: [Integration & UI]
- [ ] [Frontend components]
- [ ] [Connect frontend to backend]
- [ ] [Styling]
Verification: [How to verify Phase 4 complete]

Phase 5: [Testing & Documentation]
- [ ] [End-to-end tests]
- [ ] [README with setup instructions]
- [ ] [API documentation]
Verification: [How to verify Phase 5 complete]

Completion Criteria:
- [ ] Project runs successfully ([start command])
- [ ] All [N] core features working
- [ ] [X]+ tests written and passing
- [ ] Test coverage >= [Y]%
- [ ] Build succeeds ([build command])
- [ ] No errors in console/logs
- [ ] README with setup instructions complete
- [ ] [Any additional criteria]

When all phases complete and all criteria met, output <promise>PROJECT_COMPLETE</promise>
```

---

## Ralph-Loop Command

```bash
/ralph-loop "[YOUR_PROMPT_HERE]" \
  --completion-promise "PROJECT_COMPLETE" \
  --max-iterations [100-150]
```

---

## Example: Blog Platform

```
Build minimal blog platform from scratch.

Project Description:
Create a simple blog platform where users can register, create blog posts, view all posts, and edit/delete their own posts. Authentication via JWT tokens.

Tech Stack:
- Backend: Node.js + Express
- Database: PostgreSQL
- Frontend: React (Create React App)
- Testing: Jest + React Testing Library
- Styling: CSS Modules

Core Features:
1. User authentication (register, login, logout)
2. Create blog posts (title, content, author)
3. List all posts (homepage with pagination)
4. View single post (full post page)
5. Edit/delete own posts (author-only)

Database Schema:
- users: id (PK), email (unique), password_hash, created_at
- posts: id (PK), title, content, author_id (FK to users), created_at, updated_at

Implementation Phases:

Phase 1: Project Setup
- [ ] Initialize Node.js project (npm init)
- [ ] Setup Express server
- [ ] Configure PostgreSQL connection
- [ ] Create database schema (users, posts tables)
- [ ] Run initial migration
- [ ] Setup Jest for testing
- [ ] Create basic project structure (routes/, controllers/, models/, tests/)
Verification: Server starts on port 3000, database connection successful

Phase 2: Authentication System
- [ ] POST /auth/register endpoint (create user, hash password)
- [ ] POST /auth/login endpoint (validate credentials, return JWT)
- [ ] Auth middleware (verify JWT token)
- [ ] Write tests for auth endpoints (10+ tests)
Verification: Can register user, login, receive token, protect routes

Phase 3: Posts API
- [ ] POST /posts endpoint (create post, authenticated)
- [ ] GET /posts endpoint (list all posts, public)
- [ ] GET /posts/:id endpoint (get single post, public)
- [ ] PUT /posts/:id endpoint (update own post, authenticated)
- [ ] DELETE /posts/:id endpoint (delete own post, authenticated)
- [ ] Write tests for posts endpoints (15+ tests)
Verification: All CRUD operations work, authorization enforced

Phase 4: Frontend
- [ ] Setup React app (create-react-app)
- [ ] Create Login/Register forms
- [ ] Create PostList component (homepage)
- [ ] Create PostDetail component (single post page)
- [ ] Create PostForm component (create/edit post)
- [ ] Connect frontend to API (axios/fetch)
- [ ] Basic styling with CSS Modules
Verification: Can navigate between pages, forms work, posts display

Phase 5: Integration & Testing
- [ ] End-to-end test: Register → Login → Create Post → View Post
- [ ] End-to-end test: Edit own post
- [ ] End-to-end test: Cannot edit other user's post
- [ ] Ensure all API tests pass
- [ ] Ensure all component tests pass
Verification: E2E tests pass, full user flow works

Phase 6: Documentation & Polish
- [ ] Create README.md with:
  - Project description
  - Setup instructions
  - Database schema
  - API endpoints documentation
  - Running tests
- [ ] Add error handling (display error messages in UI)
- [ ] Add loading states
Verification: README complete, error states handled

Completion Criteria:
- [ ] Server runs with npm start (backend on :3000, frontend on :3001)
- [ ] Database schema created successfully
- [ ] All 5 core features working end-to-end
- [ ] 30+ tests written (backend + frontend)
- [ ] All tests pass (npm test)
- [ ] Test coverage >= 75%
- [ ] Build succeeds (npm run build)
- [ ] No TypeScript or ESLint errors
- [ ] No errors in browser console or server logs
- [ ] README with complete setup instructions
- [ ] Can register → login → create post → view post → edit post → delete post (full flow)

When all phases complete and all criteria met, output <promise>PROJECT_COMPLETE</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "PROJECT_COMPLETE" --max-iterations 120
```

---

## Example: REST API Service

```
Build REST API service for task management from scratch.

Project Description:
Create a RESTful API service for managing tasks with user authentication, task CRUD operations, task assignment, and status tracking.

Tech Stack:
- Backend: Python + Flask
- Database: PostgreSQL + SQLAlchemy ORM
- Testing: Pytest
- Authentication: JWT (Flask-JWT-Extended)
- Documentation: Swagger/OpenAPI

Core Features:
1. User management (register, login)
2. Task CRUD (create, read, update, delete tasks)
3. Task assignment (assign tasks to users)
4. Task status management (todo, in_progress, done)
5. Filter tasks by status and assignee

Database Schema:
- users: id, username, email, password_hash, created_at
- tasks: id, title, description, status, assignee_id (FK), creator_id (FK), created_at, updated_at

Implementation Phases:

Phase 1: Project Setup
- [ ] Create Python virtual environment
- [ ] Initialize Flask app
- [ ] Setup SQLAlchemy with PostgreSQL
- [ ] Create database models (User, Task)
- [ ] Setup Flask-JWT-Extended
- [ ] Setup Pytest
- [ ] Create project structure (app/, models/, routes/, tests/)
Verification: Flask app runs, database connected, models created

Phase 2: User Authentication
- [ ] POST /auth/register (create user, hash password)
- [ ] POST /auth/login (validate credentials, return JWT)
- [ ] JWT middleware decorator for protected routes
- [ ] Write 8+ tests for auth
Verification: Can register, login, protect routes with JWT

Phase 3: Task Management API
- [ ] POST /tasks (create task, authenticated)
- [ ] GET /tasks (list tasks with filters, authenticated)
- [ ] GET /tasks/:id (get single task, authenticated)
- [ ] PUT /tasks/:id (update task, authenticated)
- [ ] DELETE /tasks/:id (delete task, creator only)
- [ ] PATCH /tasks/:id/assign (assign task to user)
- [ ] PATCH /tasks/:id/status (update task status)
- [ ] Write 20+ tests for task endpoints
Verification: All CRUD + assignment operations work

Phase 4: Query & Filtering
- [ ] GET /tasks?status=todo (filter by status)
- [ ] GET /tasks?assignee=user_id (filter by assignee)
- [ ] GET /tasks?created_by=user_id (filter by creator)
- [ ] Pagination support (limit, offset)
- [ ] Write tests for all filter combinations
Verification: Filtering and pagination work correctly

Phase 5: Documentation & Error Handling
- [ ] Add Swagger/OpenAPI documentation
- [ ] Standardize error responses (JSON format)
- [ ] Add input validation for all endpoints
- [ ] Add meaningful error messages
Verification: API documentation accessible, errors well-formatted

Phase 6: Integration Testing
- [ ] E2E test: Register → Login → Create Task → Assign Task → Update Status
- [ ] E2E test: Filter tasks by status
- [ ] E2E test: Delete task (permission check)
- [ ] Run full test suite
Verification: All E2E tests pass, full coverage >= 80%

Completion Criteria:
- [ ] Flask app runs (python app.py)
- [ ] Database tables created
- [ ] All 5 core features working
- [ ] 35+ tests written and passing (pytest)
- [ ] Test coverage >= 80% (pytest --cov)
- [ ] All endpoints documented in Swagger
- [ ] Input validation working (reject invalid data)
- [ ] Error responses standardized (JSON format)
- [ ] No security warnings (SQL injection protected, passwords hashed)
- [ ] README with API documentation and setup instructions

When all phases complete and all criteria met, output <promise>PROJECT_COMPLETE</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "PROJECT_COMPLETE" --max-iterations 100
```

---

## Tips for Greenfield Prompts

1. **Clear tech stack** - Specify exact versions if important
2. **Database schema upfront** - Define tables/collections early
3. **Logical phases** - Start with setup, then core features, then polish
4. **Phase verification** - How do you know each phase is done?
5. **High max-iterations** - Full projects need 100-150+ iterations
6. **Testing throughout** - Don't leave testing for the end
7. **Documentation phase** - Always include README creation
8. **Integration tests** - Verify everything works together

## Common Greenfield Criteria

- [ ] Project initializes and runs ([start command])
- [ ] Database schema created successfully
- [ ] All core features implemented and working
- [ ] [X]+ tests written (backend + frontend if applicable)
- [ ] All tests pass ([test command])
- [ ] Test coverage >= [Y]% (typically 75-85%)
- [ ] Build succeeds ([build command])
- [ ] No errors in console/logs
- [ ] No linting/type errors
- [ ] README complete with setup instructions
- [ ] API documentation (if backend)
- [ ] Basic error handling in place
- [ ] Security basics (password hashing, input validation, etc.)
