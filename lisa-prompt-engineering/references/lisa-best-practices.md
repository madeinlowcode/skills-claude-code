# Lisa Best Practices

Guia completo de melhores práticas para usar Lisa efetivamente.

## 1. Pre-Loop Planning (ANTES de executar)

### Checklist
- [ ] Objetivos finais bem definidos
- [ ] Critério de sucesso é mensurável
- [ ] Completion promise é específica
- [ ] --max-iterations definido (safety)
- [ ] Tentou /lisa:prep para scaffolding?
- [ ] IMPLEMENTATION_PLAN.md ou specs criados?

### Exemplo Ruim ❌
````bash
/lisa:loop "Build something cool" --max-iterations 50
````

### Exemplo Bom ✅
````bash
/lisa:loop PROMPT.md --max-iterations 30
# PROMPT.md tem:
# - Mission clara
# - Process Per Iteration definido
# - Verification steps
# - Completion promise específica
````

---

## 2. Arquivo PROMPT.md Structure (Sempre)
````markdown
# Mission
[UMA linha, objetivo claro]

# Process Per Iteration
1. [Passo específico]
2. [Verificação]
3. [Commit ou salvar]

# Completion Criteria
When [condição concreta e verificável]:
<promise>EXACT_COMPLETION_TEXT</promise>

# Constraints
- [O que evitar]
- [Limites]
````

**Pro Tip:** Mantenha PROMPT.md simples e direto. Complexidade vai para specs/features.md.

---

## 3. Spec-Based Verification (Para Trabalho Crítico)

### Quando USAR Specs
✅ API com múltiplos endpoints  
✅ Features com múltiplos requisitos  
✅ Código que múltiplos devs vão usar  
✅ Qualquer coisa com >5 requisitos  
✅ Projetos onde "feito" deve ser inequívoco  

### Quando NÃO usar Specs
❌ Bug fix simples  
❌ Arquivo único para refatoring  
❌ Tarefa muito curta  
❌ Prototipagem rápida  

### Estrutura Specs Recomendada
````markdown
## FEATURE-ID: Feature Name

### Requirements
- [ ] Requisito 1
- [ ] Requisito 2

### Tests Required
- [ ] Test 1
- [ ] Test 2
````

---

## 4. Arquivos de Memória Externa (Crucial!)

Claude PERDE memória entre iterações. Use arquivos como memória:

### IMPLEMENTATION_PLAN.md
````markdown
# Phase 1
- [x] Task 1
- [x] Task 2
- [ ] Task 3

# Phase 2
- [ ] Task 4
````

Lisa mostra progresso automaticamente:
````
🔄 Lisa iteration 15 | Progress: 2/6 items
````

### STATUS.md (Para tracking custom)
````markdown
# Iteration Progress

## Completed
- Task A (iteration 3)
- Task B (iteration 5)

## Current
- Working on Task C

## Next
- Task D
- Task E
````

**Golden Rule:** Se é importante para tracking, está em arquivo, não memória.

---

## 5. Completion Promises (A Arte)

### ❌ Promessas Ruins
````markdown
<promise>DONE</promise> when finished
<promise>COMPLETE</promise> when it looks good
<promise>READY</promise> when tests pass (vago!)
<promise>SUCCESS</promise> (sem contexto)
````

### ✅ Promessas Boas
````markdown
<promise>ALL_REQUIREMENTS_VERIFIED</promise> when:
- specs/features.md shows 15/15 [x]
- npm test passes with exit code 0
- Code coverage >85%

<promise>API_COMPLETE</promise> when:
- All 5 endpoints implemented
- All tests passing
- npm run build succeeds

<promise>BUGFIXES_COMPLETE</promise> when:
- tsc --noEmit exits with code 0
- All 12 reported issues fixed
- Test suite passes 100%
````

### Regra
**Promessa deve incluir:** O QUÊ + COMO VERIFICAR

---

## 6. Verification Steps (NUNCA Pule!)

Template de verificação para PROMPT.md:
````markdown
# Mandatory Verification (NUNCA PULE)

Before outputting completion promise:

1. Re-read [external file] from disk (not memory)
   Example: Re-read specs/features.md

2. For EACH requirement:
   - Verify [specific artifact] exists
   - Verify [test/check] passes
   - Mark [x] if completed

3. Run verification command:
   Example: npm test, tsc --noEmit, npm run build

4. If ANY requirement unchecked [ ]:
   Continue working

5. If ALL requirements [x] AND verification passes:
   Output promise
````

---

## 7. Iteration Discipline

### Anatomia de Uma Boa Iteração
````
1. LEITURA: Ler arquivo externo (spec, plan, status)
2. IDENTIFICAÇÃO: Encontrar próximo item a fazer
3. EXECUÇÃO: Implementar/corrigir
4. VERIFICAÇÃO: Testar que funciona
5. MARCAÇÃO: Marcar [x] se completo
6. COMMIT: Fazer commit com mensagem clara
7. LOOP: Volta para 1
````

### Exemplo Real
````markdown
# Iteration 5

1. Read IMPLEMENTATION_PLAN.md
   → Found: [ ] Implement DELETE endpoint

2. Create handler for DELETE /api/todos/:id

3. Write tests for DELETE endpoint

4. Run: npm test
   → All DELETE tests pass ✓

5. Mark [x] next to "Implement DELETE endpoint"

6. Commit: "feat: add DELETE /todos/:id endpoint"

→ Loop continues
````

---

## 8. Commits (Frequentes e Claros)

### Convenção Recomendada
````
feat: add new feature
fix: resolve bug
refactor: restructure code
test: add test coverage
docs: update documentation
chore: maintenance task
````

### Bom Commit por Iteração
````bash
git commit -m "feat: implement FEATURE-1 requirement"
git commit -m "feat: add validation to X endpoint"
git commit -m "test: add unit tests for auth"
````

### Commits Frequentes = Progresso Claro
- Fácil ver o que foi feito
- Fácil reverter se necessário
- Progress visível no git log

---

## 9. Safety Limits

### --max-iterations Setting

| Tipo de Tarefa | Recomendação |
|---|---|
| Bug fix simples | 10-20 |
| Feature pequena | 20-40 |
| Refactor | 20-50 |
| API com specs | 50-100 |
| App completo | 100-200 |
| Complexo | 150-300 |

**Regra:** Melhor ser generoso e parar cedo do que ficar sem limite.

---

## 10. Debugging Loop Issues

### Loop Não Para (Roda infinito)
**Causa:** Sem completion promise ou --max-iterations

**Solução:**
````bash
# Verify PROMPT.md has <promise>
grep "<promise>" PROMPT.md

# Or add --max-iterations
/lisa:loop PROMPT.md --max-iterations 30

# Cancel active loop
/lisa:cancel
````

### Loop Para Cedo
**Causa:** Completion promise muito vaga ou acionada prematuramente

**Solução:**
````markdown
# ❌ Ruim
<promise>DONE</promise> (aparece no meio do trabalho)

# ✅ Bom
<promise>DONE</promise> QUANDO:
- specs/features.md shows 10/10 [x]
- npm test passes
- Code coverage >85%
````

### Claude Perde Context
**Causa:** Memory loss entre iterações

**Solução:**
Coloque TUDO em arquivos:
- specs/features.md → requisitos
- IMPLEMENTATION_PLAN.md → progresso
- STATUS.md → contexto custom

Diga ao Claude para "re-read from disk each iteration"

---

## 11. Advanced: Dynamic Stop Conditions

Ao invés de completion promise, use comando externo:
````bash
/lisa:loop PROMPT.md \\
  --stop-command "npm test > /dev/null 2>&1 && echo pass || echo fail" \\
  --stop-when "pass" \\
  --max-iterations 50
````

**Quando usar:**
- Tests devem passar (não subjetivo)
- Build deve suceder
- Linting deve passar
- Qualquer coisa com exit code

---

## 12. Performance Tips

### Acelere Loops

1. **Torne iterações atômicas:** Uma coisa por iteração
2. **Use specs:** Pré-define requisitos, menos volta e meia
3. **Teste dentro iteração:** Não deixa pra depois
4. **Commits após cada iteração:** Claro o progresso
5. **Clear instructions:** Reduza interpretação de Claude

### Desacelere Loop (Caso de Qualidade)
````markdown
# Qual iteração falha?
- Iterations 1-5: OK
- Iteration 6: Falha em verificação
- Iteration 7-8: Debug

/lisa:status mostra iteration 6, vê o problema
````

---

## 13. Anti-Patterns (O que NÃO fazer)

### ❌ Tudo em Uma Iteração
````markdown
# Ruim:
# "Build API, write tests, deploy, document everything"

# Bom:
1. Build endpoint
2. Write tests
3. Verify tests pass
4. Document
````

### ❌ Confiar em Claude Lembrar
````markdown
# Ruim:
"Did you already implement X?"

# Bom:
"Read IMPLEMENTATION_PLAN.md and check for [x]"
````

### ❌ Completion Promise Vaga
````markdown
# Ruim:
<promise>DONE</promise>

# Bom:
<promise>ALL_5_ENDPOINTS_WITH_TESTS_PASSING</promise>
````

### ❌ Sem Verificação Externa
````markdown
# Ruim:
"Check if tests pass in your mind"

# Bom:
"When npm test exits with code 0"
````

---

## 14. Project Setup Checklist

Antes de /lisa:loop:
````
□ PROMPT.md criado com:
  □ Mission clara
  □ Process Per Iteration definido
  □ Completion Criteria com promise específica
  □ Constraints listados

□ IMPLEMENTATION_PLAN.md (se multi-fase):
  □ Tarefas com [ ] unchecked

□ specs/features.md (se crítico):
  □ Requisitos com [ ] unchecked
  □ Tests listados

□ Max iterations definido (--max-iterations)

□ Completion promise é específica e mensurável

□ Verificação steps definidos no prompt
````

---

## 15. Post-Loop Cleanup

Após loop completar:
````bash
# Review que foi feito
git log --oneline | head -20

# Cleanup scaffolding
/lisa:clean --all

# Verify final state
npm test
npm run build
````

---

## Summary: Os 5 Pilares

1. **Clear Requirements** → PROMPT.md + specs/features.md
2. **External Memory** → IMPLEMENTATION_PLAN.md, STATUS.md
3. **Atomic Iterations** → Uma coisa por iteração
4. **Verification Steps** → Sempre check before promising
5. **Specific Promises** → Baseadas em critério mensurável


---