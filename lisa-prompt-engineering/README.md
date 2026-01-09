# Lisa Prompt Engineering Skill

**Automated prompt preparation assistant for the [Lisa plugin](https://github.com/Arakiss/lisa)**

## What Does This Do?

You describe what you want → Skill asks questions → Generates all files → You run Lisa

**Zero manual work. Just describe your project.**

## The Problem It Solves

Creating effective Lisa prompts requires:
- Understanding spec-based verification
- Writing PROMPT.md with proper structure
- Creating detailed IMPLEMENTATION_PLAN.md
- Generating comprehensive specs/features.md
- Determining max iterations
- Choosing the right approach

**This is tedious when managing multiple projects.**

## The Solution

This skill automates everything:

```
You: "Crie um prompt Lisa para implementar autenticação JWT"

Skill: [Asks 4-6 smart questions]
       [Analyzes complexity]
       [Generates 3 files]
       [Provides ready-to-run command]

You: /lisa:loop PROMPT.md --max-iterations 40

Lisa: [Implements everything autonomously]
```

## How It Works

### 1. Discovery Phase
Skill asks about:
- What you want to build
- Tech stack
- Main features
- Quality requirements

### 2. Analysis Phase
Skill determines:
- Project complexity (Simple/Medium/Complex)
- Required files (1-3 files + directories)
- Verification approach (basic or spec-based)
- Estimated iterations

### 3. Generation Phase
Skill creates:
- `PROMPT.md` - Main Lisa instruction file
- `IMPLEMENTATION_PLAN.md` - Progress tracking
- `specs/features.md` - Detailed requirements (if needed)
- Directory structure (if needed)

### 4. Execution Phase
You get:
- All files ready to use
- Command to run: `/lisa:loop PROMPT.md --max-iterations X`
- Monitoring instructions
- Time estimate

## Usage Examples

### Example 1: Simple Feature
```
User: "Prepare Lisa prompt to add dark mode toggle"

Skill: Quick questions → Generates 2 files → Ready in 30 seconds
       Command: /lisa:loop PROMPT.md --max-iterations 20
```

### Example 2: Complex API
```
User: "Create Lisa files for a complete todo API with auth"

Skill: Detailed questions → Generates 3 files + specs → Ready in 2 minutes
       Command: /lisa:loop PROMPT.md --max-iterations 60
```

### Example 3: Full Application
```
User: "Setup Lisa for e-commerce app with cart, orders, payments"

Skill: Comprehensive questions → Generates 3 files + multi-phase plan → Ready in 3 minutes
       Command: /lisa:loop PROMPT.md --max-iterations 200
```

## Activation Phrases

Trigger this skill with:
- "Crie um prompt para Lisa"
- "Prepare arquivos Lisa"
- "Gerar PROMPT.md"
- "Setup Lisa loop"
- "Create Lisa prompt for..."
- "Generate specs for Lisa"

## Decision Matrix

| Project | Complexity | Files | Iterations | Time |
|---------|-----------|-------|------------|------|
| Bug fix | Simple | 1 | 10-20 | 15-30min |
| Small feature | Simple | 2 | 20-40 | 30-60min |
| API endpoint | Medium | 3 | 30-60 | 1-2h |
| Full CRUD API | Medium | 3 | 50-100 | 2-4h |
| Multi-feature | Complex | 3 + dirs | 100-200 | 4-8h |
| Full app | Complex | 3 + dirs | 150-300 | 8-16h |

## Benefits

✅ **Zero Manual Prompt Writing** - Skill generates everything
✅ **Smart Complexity Analysis** - Right approach every time
✅ **Multiple Projects** - Repeat process in minutes
✅ **Quality Assurance** - Built-in best practices
✅ **Time Saved** - 10-30 minutes per project setup
✅ **Consistency** - Same quality every time

## What Gets Generated

### PROMPT.md
- Clear mission statement
- Step-by-step iteration process
- Verification steps (spec-based if needed)
- Completion promise
- Constraints

### IMPLEMENTATION_PLAN.md
- Phased breakdown
- Task checkboxes
- Progress tracking
- Dependencies

### specs/features.md (Medium/Complex)
- Detailed requirements
- Acceptance criteria
- Technical specs
- Test requirements

## Workflow Diagram

```
┌─────────────────────────────────────┐
│   User describes project            │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│   Skill asks 4-8 questions          │
│   (tech stack, features, quality)   │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│   Skill analyzes complexity         │
│   (Simple/Medium/Complex)           │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│   Skill generates files             │
│   PROMPT.md + PLAN + specs (if req) │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│   User runs: /lisa:loop PROMPT.md  │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│   Lisa implements autonomously      │
│   (iterations until completion)     │
└─────────────────────────────────────┘
```

## Real-World Scenarios

### Scenario 1: Startup with Multiple MVPs
```
You're building 5 different MVP features this sprint.

Traditional: 2-3 hours writing prompts for all 5
With this skill: 15-20 minutes total (3-4 min each)

Time saved: 2+ hours
```

### Scenario 2: Agency with Multiple Clients
```
Managing 10 client projects, each needs features added.

Traditional: 5-6 hours prompt writing per week
With this skill: 30-45 minutes per week

Time saved: 4-5 hours/week
```

### Scenario 3: Solo Developer
```
Building side project with multiple modules.

Traditional: Write prompts, second-guess, rewrite
With this skill: Answer questions, get perfect prompts

Benefit: Confidence + consistency
```

## Quick Start

**Install:**
```bash
# This skill is already in your .claude/skills/ directory
# It activates automatically when you mention Lisa
```

**Use:**
```bash
# Just say what you want
"Create Lisa prompt for [your project]"

# Skill will guide you through the rest
```

**Run:**
```bash
# After generation, run the provided command
/lisa:loop PROMPT.md --max-iterations [provided]
```

## Tips for Best Results

1. **Be specific** in answers - Better input = better output
2. **Trust the analysis** - Skill knows which approach to use
3. **Review generated files** - Quick sanity check (optional)
4. **Use provided max-iterations** - Based on project analysis
5. **Multiple projects?** - Repeat process for each

## Advanced: Customization

After generation, you can customize:
- `PROMPT.md` - Adjust completion criteria
- `IMPLEMENTATION_PLAN.md` - Add/remove tasks
- `specs/features.md` - Modify requirements

Then re-run with adjusted parameters.

## Integration with Lisa

This skill is the **prep stage** for Lisa:

```
lisa-prompt-engineering → Generates files
         ↓
     /lisa:prep → (optional) Creates scaffolding
         ↓
     /lisa:loop → Executes implementation
         ↓
    /lisa:status → Monitors progress
```

## Support & Resources

- **Lisa Plugin:** https://github.com/Arakiss/lisa
- **Ralph Wiggum Technique:** https://ghuntley.com/ralph/
- **Skill Examples:** See `.claude/skills/lisa-prompt-engineering/examples/`

## FAQ

**Q: Do I need to know how to write prompts?**
A: No. The skill handles all prompt engineering.

**Q: What if I want to customize generated files?**
A: Edit them before running `/lisa:loop`. They're yours to modify.

**Q: Can I use this for non-coding projects?**
A: Yes! Works for any systematic, verifiable task.

**Q: How accurate is the iteration estimate?**
A: Based on complexity analysis, typically ±20% accurate.

**Q: Can I run multiple Lisa loops in parallel?**
A: Yes! Each project gets its own files/directory.

---

**Version:** 1.0.0
**Last Updated:** Janeiro 2026
**Compatibility:** Lisa v1.x+
**License:** MIT
