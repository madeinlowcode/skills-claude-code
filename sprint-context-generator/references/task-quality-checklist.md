# Checklist de Qualidade de Tasks

Este documento define os critérios para criar tasks de alta qualidade na skill `sprint-context-generator`.

**Objetivo:** Garantir que todas as tasks geradas sejam específicas, atômicas, acionáveis e completáveis em 15-30 minutos.

---

## Índice

1. [Critérios de uma Task Bem Definida](#critérios-de-uma-task-bem-definida)
2. [Red Flags (Tasks RUINS - Evitar)](#red-flags-tasks-ruins---evitar)
3. [Green Signals (Tasks BOAS)](#green-signals-tasks-boas)
4. [Validação Automática](#validação-automática)
5. [Processo de Refinamento](#processo-de-refinamento)
6. [Exemplos Detalhados](#exemplos-detalhados)
7. [Checklist Final](#checklist-final)

---

## Critérios de uma Task Bem Definida

Uma task de alta qualidade DEVE atender a TODOS os critérios abaixo:

### ✅ 1. Específica
- **Menciona arquivo, componente ou função exata**
- **Não usa termos genéricos** como "módulo", "sistema", "funcionalidade"
- **Define o QUE será criado/modificado**

**Exemplo BOM:**
```markdown
- [ ] 💻 Criar componente `LoginForm.tsx` em `src/components/auth/` com campos email e senha
```

**Exemplo RUIM:**
```markdown
- [ ] Implementar módulo de autenticação
```

---

### ✅ 2. Atômica
- **Completável em 15-30 minutos**
- **Uma única responsabilidade** (princípio Single Responsibility)
- **Não combina múltiplas ações não relacionadas**

**Exemplo BOM:**
```markdown
- [ ] 💻 Adicionar validação de email usando Zod no `LoginForm.tsx`
- [ ] 💻 Adicionar validação de senha (mínimo 8 caracteres) no `LoginForm.tsx`
```

**Exemplo RUIM:**
```markdown
- [ ] Implementar validação completa do formulário de login com todas as regras
```

---

### ✅ 3. Critério de Conclusão Claro
- **É óbvio quando a task está completa**
- **Tem resultado mensurável/verificável**

**Exemplo BOM:**
```markdown
- [ ] ✅ Escrever teste E2E: Usuário faz login com credenciais válidas e é redirecionado para /dashboard
```

**Exemplo RUIM:**
```markdown
- [ ] Testar login
```

---

### ✅ 4. Verbo de Ação Específico
- **Usa verbos concretos:** criar, adicionar, escrever, implementar [X específico]
- **Evita verbos vagos:** configurar, implementar (sem objeto), fazer

**Exemplos de verbos específicos:**
- ✅ **Criar** componente `Button.tsx`
- ✅ **Adicionar** validação de email em `form.ts`
- ✅ **Escrever** teste unitário para `AuthService.login()`
- ✅ **Implementar** endpoint POST /api/auth/login
- ✅ **Configurar** Husky pre-commit hook em `.husky/pre-commit`
- ✅ **Extrair** lógica de validação para `validators/email.ts`
- ✅ **Refatorar** `UserService` para usar Repository pattern

**Exemplos de verbos vagos (evitar):**
- ❌ Implementar autenticação (muito amplo)
- ❌ Configurar projeto (vago)
- ❌ Fazer testes (vago)

---

## Red Flags (Tasks RUINS - Evitar)

### ❌ 1. Tasks Muito Amplas
**Problema:** Impossível completar em 15-30 minutos

**Exemplos:**
```markdown
❌ Implementar módulo de autenticação
❌ Criar sistema de notificações
❌ Adicionar funcionalidade de pagamento
❌ Desenvolver dashboard completo
```

**Por que é ruim:**
- Não é claro quando está completo
- Provavelmente levará horas ou dias
- Dificulta rastreamento de progresso

---

### ❌ 2. Tasks Vagas
**Problema:** Não é claro o que fazer

**Exemplos:**
```markdown
❌ Configurar projeto
❌ Melhorar performance
❌ Atualizar componentes
❌ Corrigir bugs
```

**Por que é ruim:**
- Falta especificação do QUE configurar/melhorar/atualizar
- Múltiplas interpretações possíveis
- Impossível validar se está completo

---

### ❌ 3. Tasks com <40 Caracteres
**Problema:** Provavelmente falta contexto

**Exemplos:**
```markdown
❌ Criar API
❌ Adicionar testes
❌ Configurar ESLint
```

**Por que é ruim:**
- Falta especificação de QUAL API, QUAIS testes, QUAL configuração
- Muito genérico

**Exceções válidas:**
- Tasks de documentação simples: "Atualizar CHANGELOG"
- Tasks de configuração com arquivo específico: "Criar .env.example"

---

### ❌ 4. Tasks que Combinam Múltiplas Ações
**Problema:** Viola princípio atômico

**Exemplos:**
```markdown
❌ Criar componente LoginForm, adicionar validação e escrever testes
❌ Implementar endpoint de login e configurar autenticação JWT
❌ Adicionar botão de logout, criar página de perfil e atualizar navbar
```

**Por que é ruim:**
- Difícil rastrear progresso parcial
- Se uma parte falhar, toda task fica bloqueada
- Viola Single Responsibility

**Correção:**
```markdown
✅ Criar componente `LoginForm.tsx` com campos email e senha
✅ Adicionar validação de email usando Zod no `LoginForm.tsx`
✅ Escrever teste unitário para validação de `LoginForm`
```

---

### ❌ 5. Tasks sem Menção a Arquivo/Componente
**Problema:** Falta especificidade

**Exemplos:**
```markdown
❌ Adicionar autenticação
❌ Criar serviço de usuário
❌ Implementar validação
```

**Por que é ruim:**
- Não é claro ONDE implementar
- Dificulta navegação no código
- Ambíguo

**Correção:**
```markdown
✅ Criar `src/services/auth.service.ts` com método `login(email, password)`
✅ Criar `src/services/user.service.ts` com método `getUserById(id)`
✅ Adicionar validação de email em `src/utils/validators.ts`
```

---

## Green Signals (Tasks BOAS)

### ✅ 1. Tasks Específicas com Arquivo/Componente

**Exemplos excelentes:**
```markdown
✅ 💻 Criar componente `LoginForm.tsx` em `src/components/auth/` com campos email e senha
✅ 💻 Adicionar validação de email usando Zod em `src/lib/validators/auth.ts`
✅ 💻 Implementar endpoint POST /api/auth/login no `src/controllers/auth.controller.ts`
✅ 🎨 Criar botão `LogoutButton.tsx` em `src/components/common/`
✅ 🏗️ Configurar Husky pre-commit hook em `.husky/pre-commit` para rodar ESLint
```

**Por que é bom:**
- Caminho exato do arquivo
- Componente/função específica mencionada
- Tecnologia/biblioteca especificada
- Claro o que será criado

---

### ✅ 2. Tasks com Critério de Conclusão

**Exemplos excelentes:**
```markdown
✅ ✅ Escrever teste E2E: Usuário faz login com credenciais válidas e é redirecionado para /dashboard
✅ ✅ Testar `AuthService.login()` retorna JWT válido quando credenciais corretas
✅ ✅ Validar que formulário exibe erro "Email inválido" quando email mal formatado
✅ 📝 Documentar método `login()` em `AuthService` com JSDoc (params, returns, throws)
```

**Por que é bom:**
- Critério de sucesso explícito
- Resultado esperado claro
- Fácil validar se está completo

---

### ✅ 3. Tasks Atômicas (15-30 minutos)

**Exemplos excelentes:**
```markdown
✅ 💻 Criar modelo `User` em `src/models/user.model.ts` com campos: id, email, passwordHash, createdAt
✅ 💻 Implementar método `hashPassword(password): Promise<string>` em `src/lib/auth/password.ts` usando bcrypt custo 12
✅ 💻 Adicionar tratamento de erro 401 (Unauthorized) no `AuthController`
✅ 🎨 Adicionar loading spinner no `LoginButton` enquanto request está em andamento
```

**Por que é bom:**
- Cada task leva ~15-30 minutos
- Uma única responsabilidade
- Progresso mensurável

---

### ✅ 4. Tasks com Tecnologia/Biblioteca Especificada

**Exemplos excelentes:**
```markdown
✅ 🏗️ Instalar dependências: zod, bcryptjs, jsonwebtoken
✅ 💻 Criar schema de validação Zod para login em `src/schemas/auth.schema.ts`
✅ 💻 Implementar hash de senha usando bcrypt custo 12 em `src/lib/auth/password.ts`
✅ 💻 Gerar JWT usando jsonwebtoken com expiração de 1h em `src/lib/auth/jwt.ts`
✅ ✅ Configurar Playwright para testes E2E em `playwright.config.ts`
```

**Por que é bom:**
- Não há ambiguidade sobre qual biblioteca usar
- Facilita implementação
- Consistência no projeto

---

### ✅ 5. Tasks de Setup/Configuração Detalhadas

**Exemplos excelentes:**
```markdown
✅ 🏗️ Criar `.env.example` com variáveis: JWT_SECRET, DATABASE_URL, PORT
✅ 🏗️ Configurar ESLint em `.eslintrc.json` com rules: no-console (warn), no-unused-vars (error)
✅ 🏗️ Adicionar script `lint` no package.json: "eslint . --ext .ts,.tsx"
✅ 🏗️ Configurar Prettier em `.prettierrc` com: tabWidth 2, semi true, singleQuote true
✅ 🏗️ Criar hook pre-commit em `.husky/pre-commit` para rodar lint-staged
```

**Por que é bom:**
- Configuração exata especificada
- Arquivo de configuração mencionado
- Valores/regras específicas definidas

---

## Validação Automática

A skill `sprint-context-generator` valida automaticamente tasks usando os critérios abaixo:

### Critérios de Validação Automática

1. **Tamanho mínimo:** Task deve ter ≥40 caracteres
   - Se <40 chars → Marcar como `[NEEDS_REFINEMENT]`

2. **Verbos específicos:** Detectar verbos vagos
   - ❌ "Implementar" (sem objeto específico)
   - ❌ "Configurar" (sem arquivo/tool específico)
   - ❌ "Fazer", "Criar" (sem objeto)
   - ✅ "Criar componente X", "Implementar método Y"

3. **Menção a arquivo/componente:** Task deve conter:
   - Nome de arquivo (ex: `LoginForm.tsx`, `auth.service.ts`)
   - OU nome de componente/classe específica
   - OU endpoint específico (ex: POST /api/auth/login)
   - OU configuração específica (ex: Husky pre-commit)

4. **Palavras-chave genéricas:** Detectar e alertar
   - ❌ "módulo", "sistema", "funcionalidade" (sem especificação)
   - ❌ "completo", "total", "todos" (muito amplo)

### Exemplo de Validação

**Input (task vaga):**
```markdown
- [ ] Implementar autenticação
```

**Validação detecta:**
- ❌ Tamanho: 28 chars (<40)
- ❌ Verbo vago: "Implementar" sem objeto específico
- ❌ Sem menção a arquivo/componente
- ❌ Palavra genérica: "autenticação" (muito amplo)

**Output (refinamento automático):**
```markdown
[NEEDS_REFINEMENT] Task muito vaga. Sugestão de refinamento:
- [ ] 💻 Criar `src/services/auth.service.ts` com método `login(email, password): Promise<{token: string}>`
- [ ] 💻 Implementar endpoint POST /api/auth/login no `src/controllers/auth.controller.ts`
- [ ] 💻 Adicionar middleware de autenticação em `src/middleware/auth.middleware.ts`
- [ ] 🎨 Criar componente `LoginForm.tsx` em `src/components/auth/`
```

---

## Processo de Refinamento

Quando uma task é detectada como vaga, siga este processo:

### Passo 1: Identificar o Escopo
**Pergunta:** O que exatamente precisa ser feito?

**Exemplo:**
```
Task vaga: "Implementar autenticação"

Escopo refinado:
- Login com email/senha
- Registro de novos usuários
- Reset de senha
- Proteção de rotas
```

### Passo 2: Quebrar em Componentes
**Pergunta:** Quais arquivos/componentes serão criados/modificados?

**Exemplo:**
```
Componentes:
- AuthService (backend)
- AuthController (backend)
- LoginForm (frontend)
- ProtectedRoute (frontend)
- auth.middleware.ts (middleware)
```

### Passo 3: Criar Tasks Específicas
**Pergunta:** Para cada componente, o que exatamente será feito?

**Exemplo:**
```markdown
Backend:
- [ ] 💻 Criar `src/services/auth.service.ts` com método `login(email, password)`
- [ ] 💻 Implementar `hashPassword()` em `src/lib/auth/password.ts` usando bcrypt
- [ ] 💻 Implementar `generateJWT()` em `src/lib/auth/jwt.ts`
- [ ] 💻 Criar endpoint POST /api/auth/login no `auth.controller.ts`

Frontend:
- [ ] 🎨 Criar `LoginForm.tsx` em `src/components/auth/` com campos email e senha
- [ ] 🎨 Adicionar validação de formulário usando Zod
- [ ] 🎨 Criar componente `ProtectedRoute.tsx` que verifica token JWT

Middleware:
- [ ] 💻 Criar `src/middleware/auth.middleware.ts` que valida JWT em headers
```

### Passo 4: Validar Atomicidade
**Pergunta:** Cada task leva 15-30 minutos?

- Se SIM → Task está boa
- Se NÃO → Quebrar ainda mais

**Exemplo de task que precisa ser quebrada:**
```markdown
❌ Criar LoginForm.tsx com validação, estados, API call e error handling

Refinamento:
✅ Criar `LoginForm.tsx` com campos email e senha (estrutura básica)
✅ Adicionar validação de formulário usando Zod no `LoginForm.tsx`
✅ Implementar estado de loading e disabled no botão submit
✅ Adicionar chamada à API POST /api/auth/login
✅ Adicionar tratamento de erros (401, 500) com mensagens ao usuário
```

---

## Exemplos Detalhados

### Exemplo 1: Refatorando Task Vaga de Setup

**❌ ANTES (task vaga):**
```markdown
- [ ] Configurar projeto
```

**✅ DEPOIS (tasks refinadas):**
```markdown
- [ ] 🏗️ Instalar dependências: eslint, prettier, husky, lint-staged
- [ ] 🏗️ Criar `.eslintrc.json` com config para TypeScript: @typescript-eslint/recommended
- [ ] 🏗️ Criar `.prettierrc` com: tabWidth 2, semi true, singleQuote true
- [ ] 🏗️ Adicionar scripts no package.json: lint, format, type-check
- [ ] 🏗️ Configurar Husky pre-commit hook em `.husky/pre-commit` para rodar lint-staged
- [ ] 🏗️ Criar `.lintstagedrc.json` com: "*.{ts,tsx}": ["eslint --fix", "prettier --write"]
```

---

### Exemplo 2: Refatorando Task Vaga de Feature

**❌ ANTES (task vaga):**
```markdown
- [ ] Implementar sistema de notificações
```

**✅ DEPOIS (tasks refinadas):**
```markdown
Backend:
- [ ] 💻 Criar modelo `Notification` em `src/models/notification.model.ts` com campos: id, userId, message, read, createdAt
- [ ] 💻 Criar `NotificationService` em `src/services/notification.service.ts` com `createNotification()`
- [ ] 💻 Implementar endpoint GET /api/notifications no `notification.controller.ts`
- [ ] 💻 Implementar endpoint PATCH /api/notifications/:id/read para marcar como lida
- [ ] 💻 Adicionar filtro por usuário em `NotificationService.getByUserId()`

Frontend:
- [ ] 🎨 Criar componente `NotificationBell.tsx` no header com ícone e contador
- [ ] 🎨 Criar `NotificationList.tsx` com lista de notificações
- [ ] 🎨 Adicionar botão "Marcar como lida" em cada notificação
- [ ] 🎨 Implementar polling a cada 30s para buscar novas notificações
- [ ] 🎨 Adicionar animação de entrada para novas notificações

Testes:
- [ ] ✅ Testar `NotificationService.createNotification()` salva no DB
- [ ] ✅ Testar GET /api/notifications retorna apenas do usuário autenticado
- [ ] ✅ E2E: Usuário recebe notificação e marca como lida
```

---

### Exemplo 3: Refatorando Task Vaga de Teste

**❌ ANTES (task vaga):**
```markdown
- [ ] Adicionar testes
```

**✅ DEPOIS (tasks refinadas):**
```markdown
Testes Unitários:
- [ ] ✅ Testar `AuthService.login()` retorna JWT válido quando credenciais corretas
- [ ] ✅ Testar `AuthService.login()` lança erro 401 quando credenciais inválidas
- [ ] ✅ Testar `hashPassword()` gera hash bcrypt válido
- [ ] ✅ Testar `validateEmail()` aceita emails válidos
- [ ] ✅ Testar `validateEmail()` rejeita emails inválidos

Testes de Integração:
- [ ] ✅ Testar POST /api/auth/login retorna 200 e token quando credenciais válidas
- [ ] ✅ Testar POST /api/auth/login retorna 401 quando credenciais inválidas
- [ ] ✅ Testar rotas protegidas retornam 401 sem token JWT

Testes E2E (Playwright):
- [ ] ✅ E2E: Usuário faz login com credenciais válidas e é redirecionado para /dashboard
- [ ] ✅ E2E: Usuário vê mensagem de erro quando credenciais inválidas
- [ ] ✅ E2E: Usuário não autenticado é redirecionado para /login ao acessar rota protegida
- [ ] ✅ E2E: Usuário faz logout e token é removido
```

---

## Checklist Final

Use esta checklist para validar cada task gerada:

### ✅ Checklist de Validação de Task

- [ ] **Específica**: Menciona arquivo, componente ou função exata?
- [ ] **Atômica**: Pode ser completada em 15-30 minutos?
- [ ] **Critério claro**: É óbvio quando a task está completa?
- [ ] **Verbo específico**: Usa verbo de ação concreto (criar, adicionar, escrever, implementar [X])?
- [ ] **Tamanho adequado**: Tem ≥40 caracteres?
- [ ] **Sem ambiguidade**: Não há múltiplas interpretações possíveis?
- [ ] **Tecnologia especificada**: Quando relevante, menciona biblioteca/framework usado?
- [ ] **Caminho de arquivo**: Inclui caminho completo ou relativo do arquivo?
- [ ] **Sem palavras genéricas**: Evita "módulo", "sistema", "funcionalidade" sem especificação?
- [ ] **Uma responsabilidade**: Faz apenas UMA coisa (não combina múltiplas ações)?

### Pontuação de Qualidade

**10/10** → Task perfeita, pronta para implementação
**8-9/10** → Task boa, pequenos ajustes possíveis
**6-7/10** → Task aceitável, mas pode ser melhorada
**<6/10** → Task precisa de refinamento (marcar `[NEEDS_REFINEMENT]`)

---

## Resumo

### ❌ Evitar (Red Flags)
- Tasks muito amplas (>30 minutos)
- Tasks vagas sem especificação
- Tasks <40 caracteres
- Tasks que combinam múltiplas ações
- Tasks sem menção a arquivo/componente
- Verbos genéricos: "implementar", "configurar" (sem objeto)

### ✅ Fazer (Green Signals)
- Mencionar arquivo/componente específico
- Usar verbos de ação concretos
- Especificar tecnologia/biblioteca
- Definir critério de conclusão claro
- Manter atomicidade (15-30 minutos)
- Uma única responsabilidade por task

### 🔧 Processo de Refinamento
1. Identificar escopo
2. Quebrar em componentes
3. Criar tasks específicas
4. Validar atomicidade

---

**Este checklist é usado automaticamente pela skill na Fase 5.2 (Validação de Qualidade de Tasks).**
