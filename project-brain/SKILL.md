---
name: project-brain
description: Second Brain for Claude Code - maintains complete project context, documentation, architecture mapping, progress tracking, and knowledge persistence using Obsidian as the knowledge vault. Automatically syncs documentation after every task. Supports BMAD, OpenSpec, GSD, and SpecKit methodologies. Uses Obsidian Canvas for architecture visualization. Invoke this skill to CREATE or UPDATE project documentation, map the codebase, track progress, or sync knowledge.
---

# Project Brain - Second Brain for Claude Code

This skill transforms Claude Code into a **persistent second brain** for your software projects. It maintains complete context about architecture, progress, bugs, features, decisions, and codebase mapping — all stored in your Obsidian vault for cross-session persistence.

**Philosophy:** Documentation and context are the foundation of solid software development. Without them, every new session starts from zero. With Project Brain, every session starts with full knowledge.

---

## ENVIRONMENT VERIFICATION (Run First)

When this skill is invoked, ALWAYS perform these checks before any operation:

### Step 1: Verify Obsidian MCP Server

```
CHECK: Is the Obsidian MCP server installed and accessible?

HOW TO VERIFY:
- Check if MCP tools for Obsidian are available in current session
- Look for tools like: obsidian_read, obsidian_write, obsidian_search, or similar
- Check Claude Code MCP config: cat ~/.claude/settings.json | grep -i obsidian

IF NOT INSTALLED:
- Ask the user: "Where is your Obsidian Vault located? (full path)"
- Then install:
  claude mcp add obsidian --scope user -- npx -y "@mauricio.wolff/mcp-obsidian@latest" "<VAULT_PATH>"
- Verify installation succeeded
- Inform user they may need to restart Claude Code for MCP to activate
```

### Step 2: Verify Obsidian Skills (kepano/obsidian-skills)

```
CHECK: Are the Obsidian Skills installed?

REQUIRED SKILLS:
- obsidian-markdown: Create/edit Obsidian Flavored Markdown (wikilinks, embeds, callouts, properties)
- json-canvas: Create/edit .canvas files (nodes, edges, groups for architecture visualization)
- obsidian-bases: Work with .base files (views, filters, formulas)
- obsidian-cli: Interact with vault via CLI
- defuddle: Extract clean markdown from web pages

HOW TO VERIFY:
- Check for skills in: .claude/skills/ or ~/.claude/skills/
- Look for folders: obsidian-markdown, json-canvas, obsidian-bases, obsidian-cli, defuddle

IF NOT INSTALLED:
- Install via: npx skills add git@github.com:kepano/obsidian-skills.git
- OR manually clone to ~/.claude/skills/obsidian-skills/
- Verify all 5 skills are present after installation
```

### Step 3: Verify Project Vault Structure

```
CHECK: Does the project have a brain folder in the Obsidian vault?

EXPECTED STRUCTURE in vault:
projects/
└── {project-name}/
    ├── README.md              # Project overview and quick reference
    ├── ARCHITECTURE.md        # System architecture documentation
    ├── PROGRESS.md            # Sprint/milestone progress tracking
    ├── DECISIONS.md           # Architecture Decision Records (ADRs)
    ├── BUGS.md                # Known bugs and resolutions
    ├── FEATURES.md            # Feature backlog and status
    ├── CODEBASE-MAP.json      # Complete codebase mapping
    ├── CONTEXT.md             # Current development context (GSD-style)
    ├── STATE.md               # Cross-session state and memory
    ├── TECH-STACK.md          # Technologies and dependencies
    ├── API-MAP.md             # API endpoints documentation
    ├── DATABASE-SCHEMA.md     # Database schema documentation
    ├── METHODOLOGY.md         # Development methodology in use
    ├── canvas/
    │   ├── architecture.canvas    # System architecture visual
    │   ├── feature-flow.canvas    # Feature workflows
    │   └── data-flow.canvas       # Data flow diagrams
    ├── sprints/
    │   └── sprint-{N}.md         # Sprint-specific documentation
    ├── research/
    │   └── {topic}.md            # Research notes
    └── changelog/
        └── {date}.md            # Daily change logs

IF NOT EXISTS: Create the full structure using the templates in this skill.
```

---

## CORE OPERATIONS

### Operation 1: INITIALIZE PROJECT BRAIN (`create`)

When the user invokes this skill to set up a new project brain:

```
WORKFLOW:
1. Run environment verification (Step 1-3 above)
2. Ask the user:
   - Project name
   - Brief description
   - Tech stack being used
   - Development methodology preference (BMAD, OpenSpec, GSD, SpecKit, or hybrid)
   - Vault path (if not already known)
3. Scan the project codebase:
   - Identify all source files, their purposes, and relationships
   - Map the directory structure
   - Identify key functions, components, APIs, database models
   - Detect tech stack from package.json, requirements.txt, etc.
4. Generate all documentation files from templates (see TEMPLATES section)
5. Create the architecture canvas with system overview
6. Generate CODEBASE-MAP.json with complete codebase mapping
7. Write STATE.md with initial context
8. Confirm everything is saved in Obsidian vault via MCP
```

### Operation 2: UPDATE PROJECT BRAIN (`update`)

When the user invokes this skill to update existing documentation:

```
WORKFLOW:
1. Read current STATE.md and CONTEXT.md from vault
2. Analyze what changed in the conversation context:
   - New features implemented
   - Bugs found or fixed
   - Architecture decisions made
   - Code changes (new files, modified files, deleted files)
   - New dependencies added
   - Database schema changes
   - API endpoint changes
3. Update ALL relevant documentation files:
   - PROGRESS.md: mark completed tasks, add new ones
   - BUGS.md: add new bugs, update status of existing
   - FEATURES.md: update feature status
   - DECISIONS.md: add new ADRs
   - CODEBASE-MAP.json: reflect code changes
   - ARCHITECTURE.md: if architecture changed
   - API-MAP.md: if endpoints changed
   - DATABASE-SCHEMA.md: if schema changed
   - TECH-STACK.md: if dependencies changed
4. Update STATE.md with current session summary
5. Create/update changelog entry for today
6. Update canvas files if architecture changed
7. Verify all updates saved via MCP
```

### Operation 3: MAP CODEBASE (`map`)

Deep scan and map the entire codebase:

```
WORKFLOW:
1. Recursively scan all source directories
2. For each file, extract:
   - File path and type
   - Exports (functions, classes, components, types)
   - Imports (dependencies, internal modules)
   - Purpose/description
   - Key functions with signatures
3. Generate relationship graph (who imports whom)
4. Identify:
   - Entry points (pages, API routes, scripts)
   - Shared utilities and components
   - Database models and schemas
   - Configuration files
   - Test files and their coverage targets
5. Output: CODEBASE-MAP.json (see template)
6. Output: Update architecture.canvas with component visualization
```

### Operation 4: SYNC DOCUMENTATION (`sync`)

Post-task documentation synchronization:

```
WORKFLOW:
1. Review all work done in current session
2. Extract from conversation context:
   - Code written or modified
   - Decisions made and their rationale
   - Problems encountered and solutions
   - New patterns or approaches used
   - Dependencies added or removed
3. Update relevant vault documents
4. Append to STATE.md session log
5. Update PROGRESS.md with task completions
6. Update changelog with today's changes
7. If methodology tracking is active:
   - BMAD: update backlog, milestones, architecture docs
   - OpenSpec: update spec files, decision log
   - GSD: update STATE.md, ROADMAP.md, phase docs
   - SpecKit: update specifications, implementation status
```

---

## METHODOLOGY SUPPORT

### BMAD (Backlog, Milestones, Architecture, Decisions)

```
When using BMAD methodology, maintain:

BACKLOG.md:
- Prioritized list of all work items
- Each item: title, description, priority, status, estimate
- Categories: feature, bug, tech-debt, research

MILESTONES.md:
- Version-based milestones with target dates
- Features included in each milestone
- Status: planned, in-progress, completed, shipped

ARCHITECTURE.md:
- System architecture with diagrams (canvas)
- Component responsibilities
- Integration points
- Data flow

DECISIONS.md:
- ADR format for every significant decision
- Context, decision, alternatives, consequences
```

### OpenSpec

```
When using OpenSpec methodology, maintain:

SPEC.md:
- Complete product specification
- User stories and acceptance criteria
- Technical requirements
- Non-functional requirements

DECISION-LOG.md:
- Chronological decision tracking
- Each entry: date, decision, rationale, impact

IMPLEMENTATION-STATUS.md:
- Spec items mapped to implementation status
- Coverage tracking
```

### GSD (Get Shit Done)

```
When using GSD methodology, maintain:

PROJECT.md - Vision statement
REQUIREMENTS.md - Scoped v1/v2 features
ROADMAP.md - Phase breakdown with status
STATE.md - Decisions, blockers, position (cross-session memory)
{phase}-CONTEXT.md - Implementation decisions per phase
{phase}-RESEARCH.md - Investigated patterns per phase
VERIFICATION.md - Test and verification results

GSD Phases:
1. new-project: Clarify vision, research, create roadmap
2. discuss-phase: Capture preferences, identify gray areas
3. plan-phase: Create atomic task plans
4. execute-phase: Parallel execution with atomic commits
5. verify-work: Test deliverables, debug failures
```

### SpecKit

```
When using SpecKit methodology, maintain:

SPEC/ directory:
- overview.md: Product overview and goals
- features/: Individual feature specifications
- api/: API specifications
- data/: Data model specifications

IMPLEMENTATION/ directory:
- status.md: Implementation status per spec item
- deviations.md: Where implementation differs from spec and why
```

---

## CODEBASE MAP FORMAT (JSON)

The CODEBASE-MAP.json follows this structure:

```json
{
  "project": {
    "name": "project-name",
    "description": "Brief description",
    "version": "1.0.0",
    "techStack": {
      "framework": "Next.js 15",
      "language": "TypeScript",
      "database": "PostgreSQL (Neon)",
      "orm": "Prisma",
      "auth": "Clerk",
      "styling": "Tailwind CSS",
      "deployment": "Vercel"
    },
    "lastUpdated": "2026-03-18T00:00:00Z"
  },
  "structure": {
    "src/app": {
      "type": "directory",
      "purpose": "Next.js App Router pages and API routes",
      "children": {
        "(auth)/login/page.tsx": {
          "type": "page",
          "purpose": "Login page",
          "components": ["LoginForm"],
          "imports": ["@/features/auth/components/LoginForm"]
        },
        "api/webhooks/stripe/route.ts": {
          "type": "api-route",
          "purpose": "Stripe webhook handler",
          "methods": ["POST"],
          "imports": ["@/lib/stripe", "@/lib/db"]
        }
      }
    },
    "src/features": {
      "type": "directory",
      "purpose": "Feature modules",
      "children": {
        "auth/": {
          "type": "feature-module",
          "purpose": "Authentication feature",
          "components": ["LoginForm", "SignupForm", "AuthGuard"],
          "hooks": ["useAuth", "useSession"],
          "actions": ["login", "signup", "logout"],
          "schemas": ["loginSchema", "signupSchema"]
        }
      }
    }
  },
  "dependencies": {
    "internal": [
      { "from": "src/app/(auth)/login/page.tsx", "to": "src/features/auth/components/LoginForm" },
      { "from": "src/features/auth/actions/login.ts", "to": "src/lib/db" }
    ],
    "external": {
      "next": "15.x",
      "react": "19.x",
      "@clerk/nextjs": "5.x",
      "prisma": "6.x"
    }
  },
  "apiEndpoints": [
    {
      "method": "POST",
      "path": "/api/webhooks/stripe",
      "purpose": "Handle Stripe webhooks",
      "auth": "stripe-signature",
      "file": "src/app/api/webhooks/stripe/route.ts"
    }
  ],
  "databaseModels": [
    {
      "name": "User",
      "file": "prisma/schema.prisma",
      "fields": ["id", "email", "name", "createdAt"],
      "relations": ["orders", "subscriptions"]
    }
  ],
  "entryPoints": [
    { "type": "page", "path": "/", "file": "src/app/page.tsx" },
    { "type": "page", "path": "/dashboard", "file": "src/app/(dashboard)/page.tsx" },
    { "type": "api", "path": "/api/webhooks/stripe", "file": "src/app/api/webhooks/stripe/route.ts" }
  ]
}
```

---

## OBSIDIAN CANVAS ARCHITECTURE

Use the **json-canvas** skill to create visual architecture diagrams. Each canvas file follows the JSON Canvas spec:

### Architecture Canvas Template

```json
{
  "nodes": [
    {
      "id": "client",
      "type": "text",
      "x": 0, "y": 0,
      "width": 200, "height": 80,
      "text": "## Client\nNext.js App\n(Vercel)",
      "color": "1"
    },
    {
      "id": "api",
      "type": "text",
      "x": 300, "y": 0,
      "width": 200, "height": 80,
      "text": "## API Layer\nAPI Routes\nServer Actions",
      "color": "4"
    },
    {
      "id": "db",
      "type": "text",
      "x": 600, "y": 0,
      "width": 200, "height": 80,
      "text": "## Database\nPostgreSQL\n(Neon/Supabase)",
      "color": "5"
    },
    {
      "id": "auth",
      "type": "text",
      "x": 300, "y": -150,
      "width": 200, "height": 80,
      "text": "## Auth\nClerk / Auth.js",
      "color": "6"
    },
    {
      "id": "services",
      "type": "text",
      "x": 300, "y": 150,
      "width": 200, "height": 80,
      "text": "## External Services\nStripe, Resend, etc.",
      "color": "3"
    }
  ],
  "edges": [
    { "id": "e1", "fromNode": "client", "toNode": "api", "label": "HTTP/RSC" },
    { "id": "e2", "fromNode": "api", "toNode": "db", "label": "Prisma ORM" },
    { "id": "e3", "fromNode": "api", "toNode": "auth", "label": "Auth Check" },
    { "id": "e4", "fromNode": "api", "toNode": "services", "label": "API Calls" }
  ]
}
```

### Canvas Usage Rules

```
WHEN TO CREATE/UPDATE CANVAS:
- Project initialization: create architecture.canvas
- New feature with complex flow: create feature-flow.canvas
- Database schema changes: update data-flow.canvas
- New external service integration: update architecture.canvas
- Major refactoring: update all affected canvases

CANVAS TYPES:
1. architecture.canvas: System overview (components, services, databases)
2. feature-flow.canvas: User journey and feature interactions
3. data-flow.canvas: How data moves through the system
4. deployment.canvas: Infrastructure and deployment topology
5. {feature-name}.canvas: Complex feature-specific diagrams

NODE COLORS:
- 1 (red): Client/Frontend
- 2 (orange): Middleware/Gateway
- 3 (yellow): External Services
- 4 (green): API/Backend
- 5 (cyan): Database/Storage
- 6 (purple): Auth/Security
```

---

## STATE MANAGEMENT (Cross-Session Memory)

### STATE.md Format

```markdown
---
project: project-name
lastSession: 2026-03-18
methodology: GSD
currentPhase: phase-2-core-features
---

# Project State

## Current Focus
What we are actively working on right now.

## Recent Changes (Last 5 Sessions)
### Session 2026-03-18
- Implemented user authentication with Clerk
- Added Stripe webhook handler
- Fixed N+1 query in dashboard
- Decision: chose Prisma over Drizzle for ORM (see DECISIONS.md #5)

### Session 2026-03-17
- Initial project setup
- Created database schema
- Set up CI/CD pipeline

## Active Blockers
- [ ] Waiting for Stripe webhook testing in production
- [ ] Need to resolve CORS issue with external API

## Key Decisions Pending
- Caching strategy for dashboard analytics
- Email template engine selection

## Development Patterns in Use
- Feature-based folder structure (src/features/)
- Server Components by default, Client Components only when needed
- Server Actions for mutations
- Zod for all input validation
- TanStack Query for client-side data fetching

## Known Technical Debt
- [ ] Dashboard queries need optimization (added indexes but not verified)
- [ ] Error boundary missing on payment flow
- [ ] Missing E2E tests for checkout flow

## Environment Notes
- Node.js 20.x, pnpm as package manager
- Vercel for deployment (auto-deploy on push to main)
- Neon PostgreSQL (production), SQLite (local dev)
```

---

## DOCUMENTATION-SYNC-AGENT

After Claude Code completes any delegated task, it MUST trigger documentation sync:

### Auto-Sync Protocol

```
WHEN TO TRIGGER:
- After completing any feature implementation
- After fixing any bug
- After any refactoring
- After any architecture change
- After any dependency change
- After any database migration
- At the end of every work session
- When user explicitly requests /project-brain update

SYNC PROCESS:
1. Gather all changes from current session:
   - Git diff since session start
   - Conversation context (decisions, problems, solutions)
   - New files created, files modified, files deleted
   - Dependencies added or removed

2. Update vault documents via Obsidian MCP:
   - STATE.md: append session summary
   - PROGRESS.md: update task statuses
   - BUGS.md: add new bugs, mark fixed bugs
   - FEATURES.md: update feature progress
   - CODEBASE-MAP.json: reflect structural changes
   - DECISIONS.md: add any new ADRs
   - changelog/{date}.md: detailed change log
   - ARCHITECTURE.md: if architecture changed
   - API-MAP.md: if endpoints changed
   - DATABASE-SCHEMA.md: if schema changed

3. Update canvas if architecture or data flow changed

4. Verify all writes succeeded

5. Output summary to user:
   "Documentation synced: X files updated in vault"
```

### Sync Triggers via Hook

```
To automate documentation sync, configure a Claude Code hook:

Settings path: ~/.claude/settings.json

Add to hooks configuration:
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'SYNC_REMINDER: Remember to run /project-brain sync before ending session'"
          }
        ]
      }
    ]
  }
}

This serves as a reminder. The actual sync is performed by this skill
when invoked with the "sync" or "update" operation.
```

---

## TEMPLATES

### README.md Template

```markdown
---
project: {name}
status: active
created: {date}
methodology: {methodology}
---

# {Project Name}

## Overview
{Brief description of the project}

## Tech Stack
{Auto-generated from codebase scan}

## Quick Start
{Commands to run the project locally}

## Architecture
![[architecture.canvas]]

## Key Links
- Repository: {git-url}
- Production: {production-url}
- Staging: {staging-url}
- Design: {figma-url}

## Documentation Index
- [[ARCHITECTURE]] - System architecture
- [[PROGRESS]] - Current progress
- [[FEATURES]] - Feature backlog
- [[BUGS]] - Known issues
- [[DECISIONS]] - Architecture decisions
- [[STATE]] - Current state and context
- [[CODEBASE-MAP.json]] - Codebase mapping
```

### DECISIONS.md Template (ADR Format)

```markdown
# Architecture Decision Records

## ADR-001: {Title}
**Date:** {date}
**Status:** accepted | proposed | deprecated | superseded

### Context
{What is the issue that we're seeing that motivates this decision?}

### Decision
{What is the change that we're proposing and/or doing?}

### Alternatives Considered
1. {Alternative 1}: {pros/cons}
2. {Alternative 2}: {pros/cons}

### Consequences
**Positive:**
- {benefit}

**Negative:**
- {trade-off}

**Neutral:**
- {side effect}

---
```

### PROGRESS.md Template

```markdown
---
project: {name}
currentSprint: sprint-{N}
methodology: {methodology}
---

# Progress Tracker

## Current Sprint: Sprint {N}
**Goal:** {sprint goal}
**Period:** {start} - {end}

### In Progress
- [ ] {task description} - {assignee/agent}

### Completed This Sprint
- [x] {task} - {date completed}

### Blocked
- [ ] {task} - BLOCKED: {reason}

## Milestone Progress
### v1.0 - MVP ({percentage}%)
- [x] Project setup and scaffolding
- [x] Authentication
- [ ] Core features
- [ ] Payment integration
- [ ] Deploy to production

## Velocity Log
| Sprint | Planned | Completed | Notes |
|--------|---------|-----------|-------|
| 1      | 8       | 7         | Setup took longer |
```

### BUGS.md Template

```markdown
# Bug Tracker

## Open Bugs

### BUG-001: {Title}
**Severity:** critical | high | medium | low
**Found:** {date}
**Component:** {component}
**Status:** open | investigating | fix-in-progress | resolved

**Description:**
{What happened}

**Steps to Reproduce:**
1. {step}
2. {step}

**Expected Behavior:**
{What should happen}

**Root Cause:**
{If known}

**Fix:**
{Description of fix or PR link}

---

## Resolved Bugs
{Moved here when fixed, with resolution date and fix description}
```

### FEATURES.md Template

```markdown
# Feature Backlog

## Shipped
- [x] **{Feature}** - {brief description} (shipped {date})

## In Development
- [ ] **{Feature}** - {brief description}
  - Status: {in-progress | blocked}
  - Priority: {P0 | P1 | P2 | P3}
  - Sprint: {sprint-N}

## Planned
- [ ] **{Feature}** - {brief description}
  - Priority: {priority}
  - Estimate: {S | M | L | XL}

## Icebox (Future)
- {Feature idea} - {notes}
```

---

## INVOCATION GUIDE

This skill responds to these intents:

| Intent | Action |
|--------|--------|
| "create project brain" / "initialize brain" | Run Operation 1: Initialize |
| "update documentation" / "sync brain" | Run Operation 2: Update + Operation 4: Sync |
| "map the codebase" / "scan project" | Run Operation 3: Map Codebase |
| "sync docs" / "update docs" | Run Operation 4: Sync Documentation |
| "show project status" | Read and present STATE.md + PROGRESS.md |
| "add decision" / "record ADR" | Add entry to DECISIONS.md |
| "log bug" | Add entry to BUGS.md |
| "add feature" | Add entry to FEATURES.md |
| "update architecture" | Update ARCHITECTURE.md + architecture.canvas |
| "what's the context?" | Read and present STATE.md + CONTEXT.md |

### Slash Command Integration

```
To create a convenient /brain command, add to your Claude Code hooks:

The skill can be invoked naturally in conversation:
- "Hey, update the project brain with what we just did"
- "Initialize the brain for this project"
- "Sync the documentation"
- "Map the codebase"
- "What's our current project status?"
```

---

## RULES & PRINCIPLES

```
1. ALWAYS verify Obsidian MCP is available before any vault operation
2. ALWAYS verify obsidian-skills are installed before using canvas/markdown features
3. NEVER skip documentation sync after completing tasks
4. NEVER overwrite vault files without reading current content first (merge, don't replace)
5. ALWAYS use Obsidian wikilinks for cross-referencing ([[PAGE]])
6. ALWAYS maintain CODEBASE-MAP.json accuracy - it's the source of truth for structure
7. ALWAYS update STATE.md at end of every session
8. Canvas files should reflect the CURRENT architecture, not aspirational
9. Keep documentation concise but complete - avoid bloat
10. Use Obsidian callouts for important notices (> [!warning], > [!info], etc.)
11. Respect the methodology the user chose (BMAD, OpenSpec, GSD, SpecKit)
12. Changelog entries are APPEND-ONLY (never edit past entries)
13. When in doubt about what changed, check git diff
14. ALWAYS ask before creating the initial vault structure (confirm project name and path)
15. The documentation-sync-agent MUST run after every significant task completion
```
