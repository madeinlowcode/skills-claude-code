# Documentation Sync Protocol

This reference defines the exact protocol for the documentation-sync-agent that runs after every task completion.

---

## Trigger Conditions

The sync agent MUST be triggered when:

| Event | Priority | Sync Scope |
|-------|----------|-----------|
| Feature implemented | High | PROGRESS, FEATURES, CODEBASE-MAP, STATE, changelog |
| Bug fixed | High | BUGS, PROGRESS, CODEBASE-MAP, STATE, changelog |
| Bug found | Medium | BUGS, STATE |
| Architecture change | High | ARCHITECTURE, canvas, CODEBASE-MAP, DECISIONS, STATE |
| Database migration | High | DATABASE-SCHEMA, CODEBASE-MAP, DECISIONS, STATE |
| API endpoint added/changed | High | API-MAP, CODEBASE-MAP, STATE, changelog |
| Dependency added/removed | Medium | TECH-STACK, CODEBASE-MAP, STATE |
| Decision made | Medium | DECISIONS, STATE |
| Refactoring completed | Medium | CODEBASE-MAP, STATE, changelog |
| Sprint started/ended | Low | PROGRESS, sprints/, STATE |
| Session ending | High | STATE (always), changelog (if changes made) |

---

## Sync Process (Step by Step)

### Phase 1: Gather Changes

```
1. Review conversation context for:
   - Tasks completed
   - Decisions made
   - Problems encountered and solutions
   - Code written or modified
   - Dependencies changed

2. If git is available, check:
   - git diff --stat (files changed)
   - git log --oneline -10 (recent commits)
   - git diff --name-only HEAD~N (files in recent commits)

3. Build change manifest:
   {
     "session_date": "2026-03-18",
     "tasks_completed": ["Implemented auth flow", "Fixed N+1 query"],
     "files_created": ["src/features/auth/actions/login.ts"],
     "files_modified": ["src/app/layout.tsx", "prisma/schema.prisma"],
     "files_deleted": [],
     "dependencies_added": ["@clerk/nextjs"],
     "dependencies_removed": [],
     "decisions_made": [
       {
         "title": "Chose Clerk over Auth.js",
         "rationale": "Better DX, hosted UI, faster to integrate for MVP"
       }
     ],
     "bugs_found": [],
     "bugs_fixed": ["BUG-003: Dashboard N+1 query"],
     "architecture_changes": false,
     "database_changes": true,
     "api_changes": false
   }
```

### Phase 2: Read Current Vault State

```
For each document that needs updating:
1. Read current content from Obsidian vault via MCP
2. Parse the document structure
3. Identify where new content should be inserted
4. NEVER overwrite existing content - always merge/append
```

### Phase 3: Update Documents

```
For each document type, follow these update rules:

STATE.md:
- Update "Current Focus" section
- Prepend new session entry to "Recent Changes"
- Keep only last 10 sessions (archive older ones)
- Update "Active Blockers" list
- Update "Known Technical Debt" list
- Update "Development Patterns in Use" if new patterns adopted

PROGRESS.md:
- Move completed tasks from "In Progress" to "Completed This Sprint"
- Add completion date to each
- Update milestone percentages
- Add new tasks discovered during work

BUGS.md:
- Add new bugs with full template
- Update status of existing bugs
- Move fixed bugs to "Resolved" section with fix description

FEATURES.md:
- Update feature status (planned -> in-progress -> shipped)
- Add new features discovered during work
- Update ship dates

DECISIONS.md:
- Append new ADR with full template
- Auto-increment ADR number
- Link to related code/files

CODEBASE-MAP.json:
- Add new files with their metadata
- Update modified files (new exports, changed imports)
- Remove deleted files
- Update dependency graph

API-MAP.md:
- Add new endpoints
- Update existing endpoint documentation
- Mark deprecated endpoints

DATABASE-SCHEMA.md:
- Update schema with new models/fields
- Document migration history
- Update relationship diagram

TECH-STACK.md:
- Add new dependencies with version and purpose
- Remove dependencies that were removed
- Update version numbers if upgraded

changelog/{date}.md:
- Create new file if doesn't exist for today
- Append changes with timestamps
- Group by: features, fixes, refactoring, infrastructure
```

### Phase 4: Update Canvas (if needed)

```
IF architecture_changes OR significant new components:
1. Read current architecture.canvas
2. Add new nodes for new components
3. Add edges for new connections
4. Update labels on existing edges if communication changed
5. Write updated canvas back to vault

IF new complex feature:
1. Create {feature-name}.canvas
2. Map the feature flow with nodes and edges
3. Link from FEATURES.md

IF database schema changed:
1. Update data-flow.canvas
2. Add new entities as nodes
3. Update relationship edges
```

### Phase 5: Verify

```
1. Confirm all writes to vault succeeded (no MCP errors)
2. Check that no documents were accidentally truncated
3. Verify CODEBASE-MAP.json is valid JSON
4. Verify canvas files are valid JSON Canvas format
5. Report summary to user:

   "Documentation synced successfully:
    - STATE.md: updated with session summary
    - PROGRESS.md: 3 tasks marked complete
    - BUGS.md: 1 bug fixed (BUG-003)
    - CODEBASE-MAP.json: 2 new files mapped
    - changelog/2026-03-18.md: 4 entries added"
```

---

## Error Handling

```
IF Obsidian MCP is not available:
- Warn user: "Cannot sync to Obsidian vault - MCP server not connected"
- Offer to save documentation locally in project directory instead
- Suggest: "Run 'claude mcp add obsidian' to reconnect"

IF vault path changed or not found:
- Ask user for current vault path
- Update MCP configuration
- Retry sync

IF write fails for specific file:
- Log the error
- Continue with other files
- Report which files failed
- Offer to retry failed writes

IF CODEBASE-MAP.json is invalid:
- Regenerate from scratch using Operation 3 (Map Codebase)
- Never try to patch invalid JSON

IF canvas is invalid:
- Regenerate from ARCHITECTURE.md content
- Use architecture template as base
```

---

## Optimization Rules

```
1. Batch vault writes: collect all changes, write in one pass
2. Only update files that actually changed (don't rewrite unchanged docs)
3. Keep STATE.md under 500 lines (archive older sessions)
4. Keep CODEBASE-MAP.json focused on source code (ignore node_modules, .next, etc.)
5. Canvas nodes should be limited to ~20 per canvas (split complex diagrams)
6. Changelog entries should be concise (1-2 lines per change)
7. Use wikilinks liberally - they're cheap and improve navigation
```
