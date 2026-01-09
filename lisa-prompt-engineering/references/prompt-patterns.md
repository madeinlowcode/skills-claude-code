# Lisa Prompt Patterns

Padrões reutilizáveis e testados para criar prompts efetivos com Lisa.

## Pattern 1: Simple Loop (Sem Specs)

Ideal para tarefas simples, diretas e bem-definidas.
```markdown
# Mission
[Objetivo simples e claro]

# Process Per Iteration
1. [Ação específica]
2. [Verificação]
3. [Commit]

# Completion Criteria
When [condição verificável]:
<promise>EXACT_TEXT</promise>

# Constraints
- [Limites]
```

**Quando usar:**
- Bugs simples para corrigir
- Refatoração de arquivo único
- Features pequenas com critério claro

**Exemplo:**
```markdown
# Mission
Fix all TypeScript compilation errors in src/

# Process Per Iteration
1. Run `tsc --noEmit` to see current errors
2. Fix the first error shown
3. Commit with message: "fix: resolve ts error [error-name]"

# Completion Criteria
When `tsc --noEmit` exits with code 0:
<promise>ALL_TS_ERRORS_FIXED</promise>
```

---

## Pattern 2: Iterative Development (Com IMPLEMENTATION_PLAN)

Para projetos que precisam de múltiplas fases ou componentes.
```markdown
# Mission
[Objetivo geral]

# Process Per Iteration
1. Read IMPLEMENTATION_PLAN.md
2. Find first unchecked task
3. Implement that task
4. Mark [x] in IMPLEMENTATION_PLAN.md
5. Commit changes

# Completion Criteria
When all items in IMPLEMENTATION_PLAN.md are checked [x]:
<promise>IMPLEMENTATION_COMPLETE</promise>
```

**Quando usar:**
- Projetos multi-fase
- Features com múltiplos componentes
- Work que pode ser dividido em checkpoints

**Exemplo:**
```markdown
# Mission
Build a complete CLI tool for project scaffolding

# Process Per Iteration
1. Read IMPLEMENTATION_PLAN.md - find first [ ]
2. Implement that specific component
3. Test it works correctly
4. Mark [x] and commit

# Completion Criteria
When all items in IMPLEMENTATION_PLAN.md are [x]:
<promise>CLI_TOOL_COMPLETE_WITH_ALL_COMPONENTS</promise>
```

---

## Pattern 3: Spec-Based Verification (Para crítico)

Para trabalho crítico que requer verificação sistemática contra requisitos.
```markdown
# Mission
[Objetivo com referência clara]

# Source of Truth
specs/features.md define COMPLETAMENTE o "feito". Nada mais conta.

# Process Per Iteration
1. Ler specs/features.md do disco (não memória)
2. Encontrar PRIMEIRO [ ] unchecked
3. Implementar com testes
4. Marcar [x] em specs/features.md
5. Commit: "feat: implement [REQ-ID]"

# Mandatory Verification (NUNCA PULE)
Antes de prometer:
1. Re-ler specs/features.md do disco
2. Para CADA requisito:
   - Verificar código existe
   - Verificar teste existe
   - Verificar teste passa
3. Se qualquer [ ] vazio: continuar
4. Se todas [x] E testes passam: prometer

# Completion Criteria
Quando TODAS specs/features.md [x] E testes passam:
<promise>ALL_REQUIREMENTS_VERIFIED</promise>
```

**Quando usar:**
- APIs/serviços com múltiplos requisitos
- Código crítico (auth, pagamentos)
- Projetos em equipe onde "feito" deve ser inequívoco
- Qualquer coisa com >5 requisitos

---

## Pattern 4: Quality-Based Completion

Quando a qualidade é tão importante quanto funcionalidade.
```markdown
# Mission
[Objetivo com métricas de qualidade]

# Quality Gates (Todos DEVEM passar)
1. Code passes linting: `eslint .`
2. All tests pass: `npm test` (code coverage >80%)
3. TypeScript: `tsc --noEmit`
4. No security issues: `npm audit`

# Process Per Iteration
1. Implement feature or fix
2. Run all quality gates
3. Only commit if ALL gates pass
4. Mark progress in IMPLEMENTATION_PLAN.md

# Completion Criteria
When:
- [ ] All IMPLEMENTATION_PLAN.md items [x]
- [ ] `eslint .` passes (no errors)
- [ ] `npm test` passes with >80% coverage
- [ ] `tsc --noEmit` passes
- [ ] `npm audit` shows no vulnerabilities

<promise>COMPLETE_WITH_ALL_QUALITY_GATES_PASSED</promise>
```

**Quando usar:**
- Produção/código crítico
- Projetos open-source
- Quando qualidade é explicitamente importante

---

## Pattern 5: File-Based Progress Tracking

Quando você quer rastrear progresso sem IMPLEMENTATION_PLAN.
```markdown
# Mission
[Objetivo]

# Tracking
Status será salvo em STATUS.md (atualizado cada iteração)

# Process Per Iteration
1. Ler STATUS.md para context
2. Fazer próximo passo logicamente
3. Atualizar STATUS.md com progresso
4. Commit changes

# Completion Criteria
Quando STATUS.md mostra todos os passos completos:
<promise>PROJECT_COMPLETE_AS_DOCUMENTED_IN_STATUS</promise>
```

---

## Pattern 6: External Command Stopping

Usar comando externo para determinar quando parar.
```markdown
# Mission
[Objetivo]

# Stop Condition (Usar com --stop-command flag)
Loop para quando comando externo retorna valor esperado

# Process Per Iteration
1. Implementar/corrigir
2. Comando de stop é executado automaticamente
3. Se retorna valor esperado: loop para
4. Se não: continua

# Example Usage
/lisa:loop PROMPT.md \\
  --stop-command "npm test > /dev/null 2>&1 && echo pass || echo fail" \\
  --stop-when "pass" \\
  --max-iterations 50
```

**Quando usar:**
- Quando completion é externa (tests, CI, etc.)
- Integração com task trackers
- Builds que precisam passar

---

## Pattern 7: Phased Approach (Multi-fase)

Para projetos que têm fases distintas.
```markdown
# Mission
[Grande objetivo com fases]

# Phase 1: [Setup/Planning]
[Tarefas da fase 1]

# Phase 2: [Implementation]
[Tarefas da fase 2]

# Phase 3: [Testing]
[Tarefas da fase 3]

# Process Per Iteration
1. Ler qual fase ainda está em progresso
2. Fazer próxima tarefa dessa fase
3. Quando fase completa, mover para próxima
4. Marcar progresso em IMPLEMENTATION_PLAN.md

# Completion Criteria
Quando todas as fases estão [x]:
<promise>ALL_PHASES_COMPLETE</promise>
```

---

## Pattern 8: Continuous Improvement Loop

Para refactoring ou otimização contínua.
```markdown
# Mission
Melhorar [métrica específica] de [estado atual] para [estado desejado]

# Metric Definition
- Métrica: [o que medir]
- Baseline: [valor atual]
- Target: [valor desejado]
- Verificar com: [comando]

# Process Per Iteration
1. Rodar comando de métrica para ver baseline
2. Implementar melhoria
3. Medir novo resultado
4. Se melhorou: commit
5. Se atingiu target: prometer

# Completion Criteria
Quando métrica atinge [valor target]:
<promise>TARGET_METRIC_ACHIEVED_AT_[VALUE]</promise>

# Example
Métrica: Tempo de build
Baseline: 45s
Target: <10s
Verificar: `time npm run build`
```

---

## Anti-Patterns: O Que NÃO Fazer

### ❌ Vague Completion
```markdown
# Ruim:
<promise>DONE</promise> when finished

# Bom:
<promise>DONE</promise> when:
- All tests pass
- Code coverage >80%
- No TypeScript errors
```

### ❌ Trusting Memory Across Iterations
```markdown
# Ruim:
If you already implemented X, skip it

# Bom:
Read IMPLEMENTATION_PLAN.md from disk each iteration
Look for first unchecked [ ] item
```

### ❌ No Verification Steps
```markdown
# Ruim:
Implement the feature
<promise>COMPLETE</promise>

# Bom:
Implement feature
Run tests to verify
Only mark [x] if tests pass
```

### ❌ Single Long Iteration
```markdown
# Ruim:
Do everything in one go

# Bom:
Break into atomic, verifiable steps
One step per iteration ensures progress visibility
```

### ❌ Promises Based on Subjective Assessment
```markdown
# Ruim:
<promise>DONE</promise> when you think it looks good

# Bom:
<promise>DONE</promise> when:
- test coverage: `npm test` shows >85%
- linting: `eslint .` shows no errors
- types: `tsc --noEmit` exits 0
```

---

## Choosing the Right Pattern

| Scenario | Pattern | Max Iterations |
|----------|---------|---|
| Bug fix | Simple Loop | 10-20 |
| Small feature | Simple Loop | 15-30 |
| Refactoring | Simple Loop | 20-40 |
| API with specs | Spec-Based | 50-100 |
| Full application | Phased | 100-150 |
| Quality focus | Quality-Based | 50-100 |
| External deps | External Command | 30-60 |
| Continuous improvement | Improvement Loop | 50-100 |

---

## Pro Tips

1. **Start with Simple:** Use Simple Loop primeiro, upgrade se precisar
2. **Specs Save Time:** 5 min creating specs saves 30 min in loops
3. **Atomic Steps:** Cada iteração = 1 passo verificável
4. **External State:** Use arquivos (`IMPLEMENTATION_PLAN.md`, `STATUS.md`) como memória externa
5. **Test Early:** Testes devem passar DENTRO da iteração, não depois
6. **Commit Often:** Cada iteração completada = 1 commit
7. **Specific Promises:** Quanto mais específico, mais confiável
8. **Check Disk:** Sempre "re-read from disk" em verificação, não confie em memória

---