---
name: ralph-prompt-builder
description: Assists in creating optimized, well-structured prompts for the ralph-loop plugin. Use this skill when (1) about to use /ralph-loop and need to craft an effective prompt, (2) need to validate a prompt for ralph-loop compatibility, (3) want templates for common ralph-loop use cases (TDD, feature dev, bug fixing, greenfield projects), or (4) need to ensure prompts have clear completion criteria and proper <promise> tags. Ensures prompts follow ralph-loop best practices with measurable success criteria and prevents errors that could compromise project execution.
---

# Ralph Prompt Builder

Build optimized prompts for the ralph-loop plugin with built-in validation and templates.

## Quick Start

When the user wants to use ralph-loop, follow this workflow:

### 1. Determine the Use Case

Ask the user which scenario applies:

- **Create new prompt** - Guide them through interactive prompt building
- **Validate existing prompt** - Run validation on their prompt
- **Use template** - Provide pre-built template for their task type

### 2. Interactive Prompt Building

If creating a new prompt, ask these questions in sequence:

**Question 1: Task Type**
"What type of task is this?
1. TDD Development (test-driven development workflow)
2. Feature Implementation (new functionality)
3. Bug Fix (fixing existing issues)
4. Greenfield Project (starting from scratch)
5. Other (custom workflow)"

**Question 2: Task Description**
"Describe the task in 1-2 sentences. Be specific about what needs to be accomplished."

**Question 3: Completion Criteria**
"What are the measurable criteria for completion? List specific, verifiable conditions (e.g., 'all tests pass', 'build succeeds', 'coverage >= 80%')."

**Question 4: Max Iterations**
"How many iterations should ralph-loop attempt before stopping? (Recommended: 20-50 for most tasks, 100+ for complex greenfield projects)"

**Question 5: Completion Promise**
"What phrase should Claude output when complete? (Recommended: 'COMPLETE', 'DONE', 'ALL_TESTS_PASS', etc.)"

### 3. Generate the Prompt

Based on answers, construct a structured prompt following this pattern:

```
[Task Description]

[Detailed Requirements/Workflow Steps]

Completion Criteria:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

When all criteria are met, output <promise>[COMPLETION_PHRASE]</promise>
```

### 4. Validate the Prompt

Run `scripts/validate-prompt.py` to check:
- Completion promise is present
- Criteria are measurable
- Max iterations is set
- No subjective language
- Task doesn't require human judgment

If validation fails, fix issues and re-validate.

### 5. Present Final Command

Show the user the complete command:

```bash
/ralph-loop "[PROMPT_TEXT]" --completion-promise "[PHRASE]" --max-iterations [N]
```

## Template Usage

For common use cases, load the appropriate template from `assets/templates/`:

- **TDD Development** → `tdd-template.md`
- **Feature Implementation** → `feature-dev-template.md`
- **Bug Fixing** → `bug-fix-template.md`
- **Greenfield Projects** → `greenfield-template.md`

Read the template, guide the user through filling placeholders, then validate.

## Validation Only

If the user provides an existing prompt to validate:

1. Run `scripts/validate-prompt.py` with their prompt
2. Present the quality score and findings
3. If issues found, offer to fix them
4. Re-validate after fixes
5. Present the final command

## Reference Documentation

For detailed guidance, consult these references as needed:

- **[ralph-loop-best-practices.md](references/ralph-loop-best-practices.md)** - Comprehensive patterns and anti-patterns for ralph-loop prompts
- **[completion-criteria.md](references/completion-criteria.md)** - Guide for defining measurable, achievable completion criteria
- **[examples.md](references/examples.md)** - 20+ real-world examples with good vs bad comparisons

**When to read references:**
- User asks "what makes a good ralph-loop prompt?" → read best-practices.md
- User struggles with completion criteria → read completion-criteria.md
- User wants to see examples → read examples.md
- For complex or unusual tasks → read all three for comprehensive guidance

## Multi-Project Context

If the user mentions running multiple projects simultaneously:

1. Ask: "Does this prompt depend on state from other running projects?"
2. If yes: Guide them to reference existing context rather than repeating it
3. Add a "Context" section to the prompt that references shared state
4. Ensure the prompt is self-contained but not redundant

## Error Prevention

Never generate a prompt that:
- Lacks a `<promise>` tag
- Has no max iterations set (unless user explicitly requests unlimited)
- Uses subjective criteria ("make it good", "improve quality")
- Requires human judgment or design decisions
- Cannot be verified automatically

If any of these conditions exist, fix them before presenting the final command.

## Workflow Summary

```
User wants ralph-loop
    ↓
Determine: Create/Validate/Template?
    ↓
[CREATE PATH]              [VALIDATE PATH]           [TEMPLATE PATH]
Ask 5 questions      →     Run validator      →      Load template
Generate prompt            Present findings           Guide fill-in
Validate                   Offer fixes                Validate
Present command            Re-validate                Present command
                          Present command
```

## Important Notes

- Always validate prompts before presenting the final command
- Always set `--max-iterations` unless user explicitly wants unlimited
- Always use exact `<promise>TEXT</promise>` format
- Keep prompts focused and measurable
- Prioritize automated verification over manual checks
