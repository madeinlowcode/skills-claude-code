
## Long-Running Agent Protocol

This project uses the Long-Running Agent Protocol for multi-session development.

### Session Start Checklist
1. Read `.claude/progress.md` for history
2. Read `.claude/features.xml` for pending work
3. Check `git log --oneline -10`
4. Validate environment works
5. Select ONE feature to work on

### Development Rules
- Work on ONE feature at a time
- Delegate to SubAgents for isolated execution
- Test before marking complete
- Commit after each feature
- Update progress files

### Session End Checklist
1. Code compiles and runs
2. All changes committed
3. progress.md updated
4. Next steps documented

### SubAgent Delegation
When delegating tasks, write `.claude/current-task.md` with acceptance criteria and use the standard SubAgent prompt pattern.