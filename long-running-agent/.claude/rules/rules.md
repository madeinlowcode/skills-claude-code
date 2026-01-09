# Project Rules

## Long-Running Agent Protocol - MANDATORY

This project follows the Long-Running Agent Protocol. These rules are NON-NEGOTIABLE.

### Session Start (ALWAYS FIRST)
```
1. Check: does .claude/ directory exist?
2. If YES: read .claude/progress.md immediately
3. If NO: initialize using long-running-agent skill
4. Read .claude/features.xml to identify pending work
5. Run git log --oneline -5 for recent context
6. Validate environment before new work
```

### During Development
```
- Work on exactly ONE feature at a time
- Delegate to SubAgent for isolated execution
- Test thoroughly before marking complete
- Update .claude/current-task.md before SubAgent delegation
```

### Session End (ALWAYS LAST)
```
1. Ensure code compiles and runs
2. Commit all changes with descriptive message
3. Update .claude/progress.md with session summary
4. Update .claude/features.xml with completion status
5. Document next steps clearly
```

### Enforcement
If these rules are not followed, STOP and correct before proceeding.