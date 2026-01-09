# Basic Lisa Prompt Example

Exemplo simples de prompt para uma tarefa straightforward.

## Arquivo: PROMPT.md
````markdown
# Mission
Fix all ESLint errors in the src/ directory

# Process Per Iteration
1. Run `eslint src/` to identify errors
2. Fix the first error in the output
3. Re-run `eslint src/` to verify the fix
4. Commit with message: "fix: resolve eslint error in [file]"

# Completion Criteria
When `eslint src/` shows no errors (exit code 0):
<promise>ALL_ESLINT_ERRORS_RESOLVED</promise>

# Constraints
- Don't disable eslint rules with comments
- Follow the codebase style guide
- Each iteration fixes one error or one file
````

## Como Executar
````bash
# Verificar que o arquivo existe
ls PROMPT.md

# Iniciar o loop
/lisa:loop PROMPT.md --max-iterations 30

# Verificar status
/lisa:status

# Se precisar cancelar
/lisa:cancel
````

## Iterações Esperadas
````
Iteration 1: Fix error in src/index.ts
Iteration 2: Fix error in src/utils.ts
Iteration 3: Fix error in src/api.ts
...
Final: eslint src/ passes → Promise triggered
````

## Cleanup
````bash
# Após completo
/lisa:clean --all

# Verify final state
eslint src/
npm run test
````

---

## Variações

### Variação 1: TypeScript Errors
````markdown
# Mission
Resolve all TypeScript compilation errors

# Process Per Iteration
1. Run `tsc --noEmit` to see current errors
2. Fix the first error shown
3. Re-run to verify fix
4. Commit

# Completion Criteria
When `tsc --noEmit` exits with code 0:
<promise>ALL_TYPESCRIPT_ERRORS_FIXED</promise>
````

### Variação 2: Test Fixes
````markdown
# Mission
Make all failing tests pass

# Process Per Iteration
1. Run `npm test` to see failing tests
2. Fix one failing test
3. Re-run to verify
4. Commit

# Completion Criteria
When `npm test` passes 100%:
<promise>ALL_TESTS_PASSING</promise>
````

---