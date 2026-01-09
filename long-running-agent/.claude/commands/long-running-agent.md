# Long-Running Agent Command

Este comando implementa o **Long-Running Agent Protocol** para desenvolvimento de features complexas, sprints ou refatorações.

## Tarefa Solicitada
$ARGUMENTS

---

## Instruções de Execução

### 1. Verificar Estrutura do Projeto

Primeiro, verifique se a estrutura `.claude/` existe:

```bash
ls -la .claude/
```

- Se **existir**: Leia `.claude/progress.md` para entender o estado atual
- Se **não existir**: Inicialize usando a skill `long-running-agent`

### 2. Ler Estado Atual (se existir)

```bash
# Ler progresso
cat .claude/progress.md

# Ler features pendentes
cat .claude/features.xml

# Ver commits recentes
git log --oneline -5
```

### 3. Processar a Tarefa

**Se uma tarefa foi especificada acima:**

1. Analise a tarefa e identifique se é:
   - **Nova Feature**: Adicione ao `features.xml` com status="pending"
   - **Sprint**: Quebre em múltiplas features e adicione ao `features.xml`
   - **Refatoração**: Crie uma feature de refatoração no `features.xml`

2. Prepare o arquivo `.claude/current-task.md` com:
   ```markdown
   # Current Task

   ## Feature: FEAT-XXX
   **Descrição**: [Descrição da tarefa]

   ## Critérios de Aceitação
   - [ ] Critério 1
   - [ ] Critério 2
   - [ ] Critério 3

   ## Arquivos a Modificar
   - path/to/file1.ts
   - path/to/file2.ts

   ## Contexto Técnico
   [Detalhes técnicos relevantes]

   ## Sinal de Conclusão
   Quando todos os critérios forem atendidos: **TASK_COMPLETE**
   Se bloqueado: **TASK_BLOCKED: [motivo]**
   ```

3. Execute a tarefa como SubAgent:
   - Trabalhe em UMA feature por vez
   - Teste cada mudança antes de prosseguir
   - Não modifique arquivos fora do escopo
   - Atualize o progresso após conclusão

**Se nenhuma tarefa foi especificada:**

1. Leia `.claude/features.xml`
2. Selecione a próxima feature com `status="pending"` e maior prioridade
3. Siga o fluxo de execução acima

### 4. Após Conclusão de Cada Feature

1. Atualize `.claude/features.xml`:
   - Mude status de "pending" para "complete"
   - Adicione o número da sessão

2. Atualize `.claude/progress.md`:
   - Adicione entrada no histórico da sessão
   - Atualize contador de features completas

3. Commit das mudanças:
   ```bash
   git add -A
   git commit -m "feat: [descrição da feature]"
   ```

4. Atualize `.claude/session-log.md`

### 5. Fim da Sessão

Antes de encerrar:
- Verifique se o código compila e executa
- Faça commit final se houver mudanças pendentes
- Atualize `.claude/progress.md` com resumo da sessão
- Documente próximos passos

---

## Regras Críticas

### NUNCA:
- Implementar múltiplas features simultaneamente
- Marcar features como completas sem testar
- Pular a fase de orientação
- Ignorar bugs existentes para adicionar novas features
- Encerrar sessão com código quebrado

### SEMPRE:
- Ler arquivos de progresso antes de qualquer trabalho
- Trabalhar em UMA feature por vez
- Testar completamente antes de marcar como completo
- Fazer commit após cada feature concluída
- Atualizar arquivos de progresso após cada tarefa
- Deixar código em estado funcional
