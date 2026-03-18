# Obsidian Integration Guide

This reference covers how Project Brain integrates with Obsidian and its tools.

---

## MCP Server Setup

### Obsidian MCP Server

The Obsidian MCP server enables Claude Code to read and write files directly in your Obsidian vault.

**Installation:**
```bash
claude mcp add obsidian --scope user -- npx -y "@mauricio.wolff/mcp-obsidian@latest" "<VAULT_PATH>"
```

**Capabilities:**
- Read notes from vault
- Write/create notes in vault
- Search vault content
- List vault structure
- Modify existing notes

**Verification:**
```bash
# Check if MCP is configured
cat ~/.claude/settings.json | jq '.mcpServers.obsidian'
```

---

## Obsidian Skills (kepano/obsidian-skills)

### Installation

```bash
# Via npx skills
npx skills add git@github.com:kepano/obsidian-skills.git

# Manual: clone to Claude Code skills directory
git clone https://github.com/kepano/obsidian-skills.git ~/.claude/skills/obsidian-skills/
```

### Available Skills

#### 1. obsidian-markdown
Create and edit Obsidian Flavored Markdown with:
- **Wikilinks**: `[[Page Name]]` or `[[Page Name|Display Text]]`
- **Embeds**: `![[Image.png]]` or `![[Note#Section]]`
- **Callouts**: `> [!info]`, `> [!warning]`, `> [!tip]`, `> [!bug]`
- **Properties** (frontmatter): YAML metadata at top of file
- **Tags**: `#tag` inline or in properties
- **Dataview fields**: `key:: value` inline fields

**Usage in Project Brain:**
- All vault documents use Obsidian Markdown
- Cross-reference documents with wikilinks
- Use callouts for important notices
- Properties for metadata (project, status, date)

#### 2. json-canvas
Create and edit JSON Canvas files (.canvas) with:
- **Text nodes**: Markdown content in positioned boxes
- **File nodes**: Embed existing vault files
- **Link nodes**: Embed web URLs
- **Groups**: Visual grouping of nodes
- **Edges**: Connections between nodes with labels

**Node colors:**
| Color | Code | Meaning in Project Brain |
|-------|------|-------------------------|
| Red | "1" | Client/Frontend |
| Orange | "2" | Middleware/Gateway |
| Yellow | "3" | External Services |
| Green | "4" | API/Backend |
| Cyan | "5" | Database/Storage |
| Purple | "6" | Auth/Security |

**Usage in Project Brain:**
- architecture.canvas: System overview diagram
- feature-flow.canvas: User flows and feature interactions
- data-flow.canvas: Data movement through the system
- deployment.canvas: Infrastructure topology

#### 3. obsidian-bases
Work with Obsidian Bases (.base files) - a database-like view:
- **Views**: Table, board, gallery, calendar
- **Filters**: Filter notes by properties
- **Formulas**: Computed columns
- **Summaries**: Aggregations

**Usage in Project Brain:**
- Create a base to track bugs (filter by severity, status)
- Create a base to track features (board view by status)
- Create a base for sprint planning (table view)

#### 4. obsidian-cli
Interact with vault via Obsidian CLI:
- Open vault, navigate notes
- Plugin management
- Theme management

#### 5. defuddle
Extract clean markdown from web pages:
- Reduces noise and unnecessary content
- Preserves meaningful structure
- Saves tokens by cleaning HTML

**Usage in Project Brain:**
- Research: save clean web content to research/ folder
- Documentation: import external docs into vault

---

## Obsidian Markdown Conventions for Project Brain

### Frontmatter Properties (YAML)

Every Project Brain document should have frontmatter:

```yaml
---
project: my-saas-app
type: architecture | progress | bug | feature | decision | state | map
status: active | archived
created: 2026-03-18
lastUpdated: 2026-03-18
methodology: BMAD | OpenSpec | GSD | SpecKit | hybrid
---
```

### Wikilink Conventions

```markdown
# Cross-referencing
See [[ARCHITECTURE]] for system design.
Related bug: [[BUGS#BUG-003]]
Decision context: [[DECISIONS#ADR-005]]
Component map: [[CODEBASE-MAP.json]]

# Embedding
![[architecture.canvas]]       # Embed canvas in note
![[PROGRESS#Current Sprint]]   # Embed section from another note
```

### Callout Usage

```markdown
> [!info] Context
> This decision was made during sprint 3 planning.

> [!warning] Breaking Change
> This migration requires downtime.

> [!bug] Known Issue
> The webhook handler doesn't retry on 5xx errors.

> [!tip] Performance
> Use cursor-based pagination for this endpoint.

> [!example] Code Reference
> See `src/features/auth/actions/login.ts` for implementation.

> [!success] Completed
> Feature shipped to production on 2026-03-15.

> [!danger] Security
> Never expose this endpoint without rate limiting.
```

### Tags Convention

```markdown
# In properties
tags: [mvp, auth, p0]

# Inline
Implemented the login flow #auth #sprint-3
Fixed critical bug #bug #p0 #hotfix
```

---

## Vault Folder Structure

```
Obsidian Vault/
├── projects/                    # All project brains
│   ├── my-saas-app/            # One project
│   │   ├── README.md
│   │   ├── ARCHITECTURE.md
│   │   ├── PROGRESS.md
│   │   ├── DECISIONS.md
│   │   ├── BUGS.md
│   │   ├── FEATURES.md
│   │   ├── CODEBASE-MAP.json
│   │   ├── CONTEXT.md
│   │   ├── STATE.md
│   │   ├── TECH-STACK.md
│   │   ├── API-MAP.md
│   │   ├── DATABASE-SCHEMA.md
│   │   ├── METHODOLOGY.md
│   │   ├── canvas/
│   │   │   ├── architecture.canvas
│   │   │   ├── feature-flow.canvas
│   │   │   └── data-flow.canvas
│   │   ├── sprints/
│   │   │   ├── sprint-1.md
│   │   │   └── sprint-2.md
│   │   ├── research/
│   │   │   └── auth-providers.md
│   │   └── changelog/
│   │       ├── 2026-03-17.md
│   │       └── 2026-03-18.md
│   └── another-project/
├── daily/                       # Daily notes (optional)
├── templates/                   # Obsidian templates
└── inbox/                       # Quick capture
```

---

## Troubleshooting

### MCP Server Not Connected
```
1. Verify vault path is correct
2. Restart Claude Code after adding MCP
3. Check: claude mcp list
4. Reinstall: claude mcp remove obsidian && claude mcp add obsidian --scope user -- npx -y "@mauricio.wolff/mcp-obsidian@latest" "<PATH>"
```

### Skills Not Found
```
1. Verify skills directory: ls ~/.claude/skills/
2. Reinstall: npx skills add git@github.com:kepano/obsidian-skills.git
3. Check skill recognition: skills should appear in Claude Code context
```

### Canvas Not Rendering
```
1. Ensure file extension is .canvas (not .json)
2. Verify JSON is valid (use jsonlint)
3. Canvas must be in vault directory structure
4. Open Obsidian app to view canvas rendering
```

### Write Conflicts
```
1. ALWAYS read current content before writing
2. Merge changes, don't overwrite
3. If conflict detected, ask user which version to keep
4. Use append operations for logs and changelogs
```
