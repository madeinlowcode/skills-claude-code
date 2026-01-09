# CLAUDE.md

## Regras do Projeto

Este projeto utiliza o **Long-Running Agent Protocol**. 

### Obrigatório em TODA sessão:
1. Sempre verificar se existe `.claude/` na raiz do projeto
2. Se existir, ler `.claude/progress.md` ANTES de qualquer trabalho
3. Se não existir, inicializar a estrutura usando a skill `long-running-agent`
4. Trabalhar em UMA feature por vez
5. Delegar tarefas complexas para SubAgents
6. Atualizar arquivos de progresso após cada tarefa concluída
7. Fazer git commit após cada feature

### Arquivos de Controle
- `.claude/progress.md` - Histórico e status do projeto
- `.claude/features.xml` - Lista de funcionalidades
- `.claude/current-task.md` - Tarefa atual para SubAgent
- `.claude/session-log.md` - Log da sessão

### Nunca faça:
- Implementar múltiplas features simultaneamente
- Ignorar os arquivos de progresso
- Marcar feature como completa sem testar
- Deixar código quebrado ao fim da sessão