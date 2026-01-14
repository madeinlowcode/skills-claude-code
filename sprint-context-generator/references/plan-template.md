# Plano Técnico: FEAT-XXX - [Nome da Feature]

📂 **Documentação Relacionada:**
- [Especificação](spec.md) - Requisitos e análise de personas
- [Lista de Tasks](tasks.md) - Tarefas detalhadas (XX tasks)
- [Pesquisa](research.md) - Documentação e referências

---

## Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura Proposta](#arquitetura-proposta)
3. [Stack Tecnológica](#stack-tecnológica)
4. [Estrutura de Diretórios](#estrutura-de-diretórios)
5. [Componentes e Módulos](#componentes-e-módulos)
6. [APIs e Contratos](#apis-e-contratos)
7. [Modelos de Dados](#modelos-de-dados)
8. [Fluxo de Dados](#fluxo-de-dados)
9. [Variáveis de Ambiente](#variáveis-de-ambiente)
10. [Setup e Configurações](#setup-e-configurações)
11. [Decisões Técnicas](#decisões-técnicas)
12. [Riscos Técnicos e Mitigações](#riscos-técnicos-e-mitigações)
13. [Estratégia de Testes](#estratégia-de-testes)
14. [Performance e Otimizações](#performance-e-otimizações)
15. [Segurança](#segurança)
16. [Deployment](#deployment)

---

## Visão Geral

**Feature:** [Nome da feature]

**Objetivo Técnico:**
[O que será construído do ponto de vista técnico]

**Abordagem de Alto Nível:**
[Resumo de como a feature será implementada - principais componentes, integrações, fluxo geral]

---

## Arquitetura Proposta

### Padrão de Arquitetura

**Padrão escolhido:** [Ex: Clean Architecture, MVC, Hexagonal, Microservices, etc.]

**Diagrama de Arquitetura:**

```
[Inserir diagrama ASCII ou descrição visual da arquitetura]

Exemplo para Clean Architecture:
┌─────────────────────────────────────────────────────────┐
│                    Presentation Layer                   │
│  (Controllers, Components, UI)                          │
├─────────────────────────────────────────────────────────┤
│                    Application Layer                    │
│  (Use Cases, Services, Business Logic)                  │
├─────────────────────────────────────────────────────────┤
│                      Domain Layer                       │
│  (Entities, Value Objects, Domain Logic)                │
├─────────────────────────────────────────────────────────┤
│                  Infrastructure Layer                   │
│  (Database, External APIs, File System)                 │
└─────────────────────────────────────────────────────────┘
```

**Camadas e Responsabilidades:**

1. **[Nome da Camada 1]**:
   - Responsabilidade: [O que esta camada faz]
   - Componentes: [Principais componentes desta camada]
   - Dependências: [De quais outras camadas depende]

2. **[Nome da Camada 2]**:
   [Repetir estrutura acima]

### Diagrama de Componentes

```
[Mostrar como os componentes se relacionam]

Exemplo:
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  LoginForm   │─────>│AuthService   │─────>│   AuthAPI    │
│  (Component) │      │  (Service)   │      │ (Controller) │
└──────────────┘      └──────────────┘      └──────────────┘
                             │                      │
                             v                      v
                      ┌──────────────┐      ┌──────────────┐
                      │  JWTService  │      │  UserRepo    │
                      │   (Util)     │      │ (Repository) │
                      └──────────────┘      └──────────────┘
```

### Princípios Aplicados

**Clean Code:**
- [Como o código seguirá princípios de clean code]
- [Nomenclatura, organização, simplicidade]

**SOLID:**
- **S** - Single Responsibility: [Como aplicado]
- **O** - Open/Closed: [Como aplicado]
- **L** - Liskov Substitution: [Como aplicado]
- **I** - Interface Segregation: [Como aplicado]
- **D** - Dependency Inversion: [Como aplicado]

**DRY (Don't Repeat Yourself):**
- [Que código/lógica será compartilhado]
- [Onde criar abstrações/helpers]

---

## Stack Tecnológica

### Frontend

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| [Framework] | [X.Y.Z] | [Para que serve] |
| [Biblioteca 1] | [X.Y.Z] | [Para que serve] |
| [Biblioteca 2] | [X.Y.Z] | [Para que serve] |

**Exemplo:**
| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| Next.js | 14.0.0 | Framework React |
| Zod | 3.22.0 | Validação de schemas |
| Tailwind CSS | 3.3.0 | Estilização |

### Backend

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| [Runtime/Framework] | [X.Y.Z] | [Para que serve] |
| [Biblioteca 1] | [X.Y.Z] | [Para que serve] |
| [Biblioteca 2] | [X.Y.Z] | [Para que serve] |

### Database

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| [Database] | [X.Y.Z] | [Banco principal/cache/etc] |

### Testing

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| Playwright | [X.Y.Z] | Testes E2E |
| [Framework de teste unitário] | [X.Y.Z] | Testes unitários |
| [Biblioteca de mocking] | [X.Y.Z] | Mocks e stubs |

### DevOps/Tools

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| ESLint | [X.Y.Z] | Linting |
| Prettier | [X.Y.Z] | Formatação |
| Husky | [X.Y.Z] | Git hooks |

---

## Estrutura de Diretórios

### Estrutura Completa

```
[Mostrar árvore completa de diretórios com todos os arquivos a serem criados/modificados]

Exemplo:
src/
├── features/
│   └── auth/
│       ├── components/
│       │   ├── LoginForm.tsx
│       │   ├── LogoutButton.tsx
│       │   └── ProtectedRoute.tsx
│       ├── services/
│       │   └── auth.service.ts
│       ├── hooks/
│       │   ├── useAuth.ts
│       │   └── useSession.ts
│       ├── types/
│       │   └── auth.types.ts
│       ├── schemas/
│       │   └── auth.schema.ts
│       └── utils/
│           └── validators.ts
├── lib/
│   └── auth/
│       ├── jwt.ts
│       ├── password.ts
│       └── session.ts
├── api/
│   ├── routes/
│   │   └── auth.routes.ts
│   ├── controllers/
│   │   └── auth.controller.ts
│   └── middleware/
│       └── auth.middleware.ts
├── models/
│   └── user.model.ts
├── repositories/
│   └── user.repository.ts
└── config/
    ├── jwt.config.ts
    └── auth.config.ts
```

### Arquivos Novos vs. Modificados

**Arquivos NOVOS (a criar):**
- `[caminho/arquivo1.ts]` - [Propósito]
- `[caminho/arquivo2.ts]` - [Propósito]
- `[caminho/arquivo3.tsx]` - [Propósito]

**Arquivos MODIFICADOS (existentes):**
- `[caminho/arquivo1.ts]` - [O que será modificado]
- `[caminho/arquivo2.ts]` - [O que será modificado]

---

## Componentes e Módulos

### Backend

#### Módulo 1: [Nome do Módulo]

**Arquivo:** `[caminho/do/arquivo]`

**Responsabilidade:**
[O que este módulo faz]

**Dependências:**
- [Módulo/Serviço 1]
- [Módulo/Serviço 2]

**Interface/API Pública:**
```typescript
// [Assinaturas de funções/métodos principais]

export class [ModuleName] {
  constructor(dependencies: Dependencies) {}

  async method1(param: Type): Promise<ReturnType> {
    // [Descrição do que faz]
  }

  async method2(param: Type): Promise<ReturnType> {
    // [Descrição do que faz]
  }
}
```

**Exemplo de Uso:**
```typescript
const [instance] = new [ModuleName]([dependencies])
const result = await [instance].method1([params])
```

**Testes:**
- [Que testes serão criados para este módulo]

---

#### Módulo 2: [Nome do Módulo]
[Repetir estrutura acima para cada módulo backend]

---

### Frontend

#### Componente 1: [Nome do Componente]

**Arquivo:** `[caminho/do/arquivo]`

**Responsabilidade:**
[O que este componente faz]

**Props:**
```typescript
interface [ComponentName]Props {
  prop1: Type1;  // [Descrição]
  prop2?: Type2; // [Descrição, opcional]
  onEvent: (param: Type) => void;  // [Descrição do callback]
}
```

**Estado Interno:**
```typescript
// [Estados que o componente gerencia]
const [stateName, setStateName] = useState<Type>(initialValue)
```

**Hooks Utilizados:**
- `useState`: [Para que estado]
- `useEffect`: [Para que side effect]
- `useCustomHook`: [Para que]

**Estrutura do Componente:**
```tsx
export function [ComponentName]({ prop1, prop2, onEvent }: [ComponentName]Props) {
  // [Lógica principal]

  return (
    // [JSX estrutura básica]
  )
}
```

**Testes:**
- [Renderização básica]
- [Interações (click, change)]
- [Estados (loading, error, success)]

---

#### Componente 2: [Nome do Componente]
[Repetir estrutura acima para cada componente]

---

### Utilitários/Helpers

#### Util 1: [Nome do Util]

**Arquivo:** `[caminho/do/arquivo]`

**Responsabilidade:**
[O que esta função/classe utilitária faz]

**API:**
```typescript
export function [utilName](param: Type): ReturnType {
  // [Descrição]
}
```

**Casos de Uso:**
- [Onde será usado 1]
- [Onde será usado 2]

---

## APIs e Contratos

### Endpoint 1: [Nome do Endpoint]

**URL:** `[METHOD] /api/[path]`

**Autenticação:** [Requerida/Não requerida] [Tipo: JWT Bearer, API Key, etc.]

**Headers:**
```
Authorization: Bearer [JWT_TOKEN]  // Se autenticação requerida
Content-Type: application/json
```

**Request Body:**
```typescript
interface [RequestBodyName] {
  field1: Type1;  // [Descrição, validações]
  field2: Type2;  // [Descrição, validações]
}
```

**Exemplo de Request:**
```json
{
  "field1": "valor1",
  "field2": "valor2"
}
```

**Response (Success - 200/201):**
```typescript
interface [ResponseBodyName] {
  field1: Type1;  // [Descrição]
  field2: Type2;  // [Descrição]
}
```

**Exemplo de Response:**
```json
{
  "field1": "valor1",
  "field2": "valor2"
}
```

**Response (Error - 4xx/5xx):**
```typescript
interface ErrorResponse {
  error: string;       // Código do erro
  message: string;     // Mensagem legível
  statusCode: number;  // HTTP status code
  details?: any;       // Detalhes adicionais (ex: validation errors)
}
```

**Códigos de Status:**
- `200 OK`: [Quando retornado]
- `201 Created`: [Quando retornado]
- `400 Bad Request`: [Quando retornado - validação falhou]
- `401 Unauthorized`: [Quando retornado - não autenticado]
- `403 Forbidden`: [Quando retornado - não autorizado]
- `404 Not Found`: [Quando retornado]
- `500 Internal Server Error`: [Quando retornado - erro no servidor]

**Validações:**
- [ ] [Validação 1: Ex: Email deve ser válido]
- [ ] [Validação 2: Ex: Senha mínimo 8 caracteres]
- [ ] [Validação 3: Ex: Campo X é obrigatório]

**Tratamento de Erros:**
```typescript
// Exemplo de resposta de erro de validação (400)
{
  "error": "VALIDATION_ERROR",
  "message": "Dados inválidos",
  "statusCode": 400,
  "details": {
    "email": "Email inválido",
    "password": "Senha deve ter no mínimo 8 caracteres"
  }
}
```

**Implementação:**
- **Controller:** `[caminho/do/controller]`
- **Service:** `[caminho/do/service]`
- **Validação:** `[caminho/do/schema]`

---

### Endpoint 2: [Nome do Endpoint]
[Repetir estrutura acima para cada endpoint]

---

## Modelos de Dados

### Model 1: [Nome do Model]

**Arquivo:** `[caminho/do/model]`

**Descrição:**
[O que este modelo representa]

**Schema/Interface:**
```typescript
interface [ModelName] {
  id: string;              // [Descrição: UUID, auto-gerado]
  field1: Type1;           // [Descrição]
  field2: Type2;           // [Descrição]
  createdAt: Date;         // [Timestamp de criação]
  updatedAt: Date;         // [Timestamp de última atualização]
}
```

**Relacionamentos:**
- **Relação com [Model2]**: [1:1, 1:N, N:M] - [Descrição]
- **Relação com [Model3]**: [1:1, 1:N, N:M] - [Descrição]

**Índices:**
- `field1` - [Por que este índice é necessário]
- `field2, field3` - [Índice composto para queries X]

**Validações:**
- `field1`: [Tipo, obrigatório/opcional, formato, constraints]
- `field2`: [Tipo, obrigatório/opcional, formato, constraints]

**Exemplo:**
```json
{
  "id": "uuid-v4",
  "field1": "valor1",
  "field2": "valor2",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

---

### Model 2: [Nome do Model]
[Repetir estrutura acima para cada model]

---

## Fluxo de Dados

### Fluxo 1: [Nome do Fluxo]

**Descrição:**
[O que acontece neste fluxo, ex: "Usuário faz login"]

**Diagrama de Sequência:**

```
[Mostrar sequência de chamadas entre componentes]

Exemplo:
User          LoginForm       AuthService       AuthAPI       Database
  │               │               │               │               │
  │─── submit ───>│               │               │               │
  │               │─── login() ──>│               │               │
  │               │               │─── POST ─────>│               │
  │               │               │               │─── query ────>│
  │               │               │               │<─── user ─────│
  │               │               │<─── token ────│               │
  │               │<─── token ────│               │               │
  │<─ redirect ───│               │               │               │
```

**Passo a passo:**

1. **[Passo 1]**:
   - Componente/Ator: [Quem]
   - Ação: [O que faz]
   - Dados: [Que dados envia/recebe]

2. **[Passo 2]**:
   [Repetir estrutura acima]

3. **[Passo 3]**:
   [Repetir estrutura acima]

**Tratamento de Erros:**
- **Erro em [Passo X]**: [O que acontece, como é tratado]
- **Erro em [Passo Y]**: [O que acontece, como é tratado]

---

### Fluxo 2: [Nome do Fluxo]
[Repetir estrutura acima para cada fluxo principal]

---

## Variáveis de Ambiente

### Novas Variáveis

**Categoria: [Ex: Authentication]**

```env
# [Descrição da categoria]

# [Descrição da variável 1]
VAR_NAME_1=valor_exemplo
# Tipo: string
# Obrigatório: sim/não
# Padrão: [valor padrão se opcional]
# Exemplo: exemplo_de_valor

# [Descrição da variável 2]
VAR_NAME_2=valor_exemplo
# Tipo: number
# Obrigatório: sim/não
# Padrão: [valor padrão]
```

**Categoria: [Ex: Database]**

```env
# [Descrição da categoria]
VAR_NAME_3=valor_exemplo
# ...
```

### Variáveis Existentes (a usar)

- `[VAR_EXISTENTE_1]`: [Como será usada nesta feature]
- `[VAR_EXISTENTE_2]`: [Como será usada nesta feature]

### Validação de Variáveis

**Validação na Inicialização:**
```typescript
// Validar variáveis obrigatórias
const requiredEnvVars = ['VAR_NAME_1', 'VAR_NAME_2']

for (const varName of requiredEnvVars) {
  if (!process.env[varName]) {
    throw new Error(`Missing required environment variable: ${varName}`)
  }
}

// Validar formato
if (!/^[0-9]+$/.test(process.env.VAR_NAME_2)) {
  throw new Error('VAR_NAME_2 must be a number')
}
```

### Arquivo .env.example

**Atualizar `.env.example` com:**
```env
# [Comentário explicativo]
VAR_NAME_1=example_value
VAR_NAME_2=3000
```

---

## Setup e Configurações

### 1. Instalação de Dependências

**Comando:**
```bash
npm install [package1] [package2] [package3]
npm install -D [dev-package1] [dev-package2]
```

**Dependências:**
- `[package1]@[version]`: [Para que serve]
- `[package2]@[version]`: [Para que serve]

---

### 2. ESLint

**Arquivo de configuração:** `.eslintrc.json`

**Configuração:**
```json
{
  "extends": ["[preset]"],
  "rules": {
    "[rule1]": "error",
    "[rule2]": "warn",
    "[rule3]": "off"
  }
}
```

**Regras importantes:**
- `[rule1]`: [Por que esta regra]
- `[rule2]`: [Por que esta regra]

**Script no package.json:**
```json
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "eslint . --ext .ts,.tsx --fix"
  }
}
```

---

### 3. Prettier

**Arquivo de configuração:** `.prettierrc`

**Configuração:**
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 80
}
```

**Script no package.json:**
```json
{
  "scripts": {
    "format": "prettier --write \"src/**/*.{ts,tsx,json,md}\"",
    "format:check": "prettier --check \"src/**/*.{ts,tsx,json,md}\""
  }
}
```

---

### 4. Husky (Git Hooks)

**Instalação:**
```bash
npx husky install
```

**Pre-commit Hook:** `.husky/pre-commit`
```bash
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx lint-staged
```

**Lint-staged:** `.lintstagedrc.json`
```json
{
  "*.{ts,tsx}": [
    "eslint --fix",
    "prettier --write"
  ],
  "*.{json,md}": [
    "prettier --write"
  ]
}
```

**Pre-push Hook:** `.husky/pre-push`
```bash
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npm run test
```

---

### 5. Playwright (Testes E2E)

**Instalação:**
```bash
npm install -D @playwright/test
npx playwright install
```

**Arquivo de configuração:** `playwright.config.ts`

**Configuração:**
```typescript
import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './tests/e2e',
  timeout: 30000,
  use: {
    baseURL: 'http://localhost:3000',
    headless: true,
    viewport: { width: 1280, height: 720 },
  },
  projects: [
    {
      name: 'chromium',
      use: { browserName: 'chromium' },
    },
  ],
})
```

**Script no package.json:**
```json
{
  "scripts": {
    "test:e2e": "playwright test",
    "test:e2e:ui": "playwright test --ui"
  }
}
```

---

### 6. TypeScript

**Atualizar `tsconfig.json`:**
```json
{
  "compilerOptions": {
    "paths": {
      "@/features/*": ["./src/features/*"],
      "@/lib/*": ["./src/lib/*"],
      "@/api/*": ["./src/api/*"]
    }
  }
}
```

---

## Decisões Técnicas

### Decisão 1: [Título da Decisão]

**Data:** [YYYY-MM-DD]

**Contexto:**
[Qual é o problema ou questão que precisa ser resolvida]

**Opções Consideradas:**

**Opção A: [Nome da Opção]**
- **Descrição**: [Como funcionaria]
- **Prós**:
  - [Vantagem 1]
  - [Vantagem 2]
- **Contras**:
  - [Desvantagem 1]
  - [Desvantagem 2]
- **Complexidade**: [Baixa/Média/Alta]
- **Custo**: [Baixo/Médio/Alto]

**Opção B: [Nome da Opção]**
[Repetir estrutura acima]

**Decisão Escolhida:**
**[Opção X]** foi escolhida

**Justificativa:**
[Por que esta opção é a melhor para este contexto específico]

**Consequências:**
- [Consequência positiva 1]
- [Consequência positiva 2]
- [Trade-off aceito 1]

**Alternativas rejeitadas:**
- [Opção Y]: [Por que foi rejeitada]

---

### Decisão 2: [Título da Decisão]
[Repetir estrutura acima]

---

## Riscos Técnicos e Mitigações

### Risco 1: [Título do Risco]

**Probabilidade:** [Alta / Média / Baixa]
**Impacto:** [Alto / Médio / Baixo]
**Severidade:** [Crítica / Alta / Média / Baixa]

**Descrição:**
[O que pode dar errado tecnicamente]

**Indicadores:**
[Como saber se o risco está se concretizando]

**Mitigação:**
[Ações para reduzir probabilidade ou impacto]

**Plano de Contingência:**
[O que fazer se o risco se concretizar]

---

### Risco 2: [Título do Risco]
[Repetir estrutura acima]

---

## Estratégia de Testes

### Pirâmide de Testes

```
        /\
       /E2E\        10% - Playwright (jornadas críticas)
      /______\
     /        \
    /Integração\    20% - Testes de API, serviços
   /____________\
  /              \
 /   Unitários    \ 70% - Funções, métodos, componentes
/__________________\
```

### Testes Unitários

**Framework:** [Jest, Vitest, etc.]

**Cobertura esperada:** 95%

**O que testar:**
- Funções utilitárias: [Todas as funções em /lib/, /utils/]
- Serviços: [Lógica de negócio em /services/]
- Componentes: [Renderização, interações em /components/]
- Validações: [Schemas, validators]

**Padrão de nomenclatura:**
- Arquivo de teste: `[nome-do-arquivo].test.ts`
- Localização: Mesmo diretório do arquivo testado

**Exemplo:**
```
src/features/auth/services/auth.service.ts
src/features/auth/services/auth.service.test.ts
```

### Testes de Integração

**Framework:** [Jest, Vitest, etc.]

**Cobertura esperada:** 85%

**O que testar:**
- APIs: [Todos os endpoints em /api/routes/]
- Serviços com dependências: [Serviços que chamam DB, APIs externas]
- Fluxos completos: [Ex: Login completo (controller → service → repository)]

**Setup:**
- [Como mockar database]
- [Como mockar APIs externas]

### Testes E2E (Playwright)

**Cobertura esperada:** 80% das jornadas críticas

**O que testar:**
- Jornadas críticas do usuário: [Ex: Login, Registro, Checkout]
- Fluxos completos: [Integração frontend + backend]
- Validações visuais: [Elementos aparecem corretamente]

**Localização:** `tests/e2e/[feature-name].e2e.spec.ts`

**Exemplo de teste:**
```typescript
test('[Feature] - [Cenário]', async ({ page }) => {
  // 1. Setup
  await page.goto('/[url]')

  // 2. Ação
  await page.fill('[selector]', '[valor]')
  await page.click('[selector]')

  // 3. Verificação
  await expect(page.locator('[selector]')).toHaveText('[texto esperado]')
})
```

### TDD (Test-Driven Development)

**Workflow Red-Green-Refactor:**

1. **Red**: Escrever teste que falha
   ```typescript
   test('AuthService.login() deve retornar JWT válido', async () => {
     const result = await authService.login('user@example.com', 'password123')
     expect(result.token).toBeDefined()
     expect(result.token).toMatch(/^eyJ/)  // JWT pattern
   })
   ```

2. **Green**: Implementar código mínimo para passar
   ```typescript
   async login(email: string, password: string) {
     // Implementação mínima
     return { token: 'eyJ...' }
   }
   ```

3. **Refactor**: Melhorar código mantendo testes passando
   ```typescript
   async login(email: string, password: string) {
     const user = await this.userRepo.findByEmail(email)
     if (!user || !await this.verifyPassword(password, user.passwordHash)) {
       throw new UnauthorizedError('Invalid credentials')
     }
     const token = this.jwtService.sign({ userId: user.id })
     return { token }
   }
   ```

**Aplicar TDD em:**
- Todas as funções críticas de negócio
- Algoritmos complexos
- Validações
- Lógica de autenticação/autorização

---

## Performance e Otimizações

### Métricas de Performance

**Frontend:**
- **FCP (First Contentful Paint)**: < 1.8s
- **LCP (Largest Contentful Paint)**: < 2.5s
- **TTI (Time to Interactive)**: < 3.8s
- **CLS (Cumulative Layout Shift)**: < 0.1

**Backend:**
- **API Response Time (P95)**: < 200ms
- **Database Query Time (P95)**: < 50ms
- **Throughput**: > 100 requests/segundo

### Estratégias de Otimização

#### Frontend

**1. Code Splitting:**
- [Onde aplicar lazy loading]
- [Quais componentes carregar sob demanda]

```typescript
const LazyComponent = lazy(() => import('./components/HeavyComponent'))
```

**2. Caching:**
- [Que dados cachear no browser (localStorage, sessionStorage)]
- [Cache de API calls (SWR, React Query)]

**3. Otimização de Assets:**
- [Compressão de imagens (WebP, lazy loading)]
- [Minificação de CSS/JS]

#### Backend

**1. Database Optimization:**
- [Índices necessários]
- [Queries otimizadas (evitar N+1)]
- [Connection pooling]

**2. Caching (Redis):**
- [Que dados cachear]
- [TTL (Time to Live) de cada cache]
- [Estratégia de invalidação]

```typescript
// Exemplo: Cache de sessões
await redis.set(`session:${userId}`, JSON.stringify(session), 'EX', 3600)
```

**3. Rate Limiting:**
- [Limites por endpoint]
- [Estratégia de throttling]

```typescript
// Exemplo: Max 100 requests/min por IP
const rateLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100
})
```

---

## Segurança

### Autenticação

**Método:** [JWT, OAuth, Session-based, etc.]

**Implementação:**
- [Como tokens são gerados]
- [Como tokens são validados]
- [Tempo de expiração]
- [Refresh token strategy]

**Exemplo:**
```typescript
// Gerar JWT
const token = jwt.sign(
  { userId: user.id, email: user.email },
  process.env.JWT_SECRET,
  { expiresIn: '1h', algorithm: 'RS256' }
)
```

### Autorização

**Modelo:** [RBAC, ABAC, etc.]

**Roles:**
- `[Role1]`: [Permissões]
- `[Role2]`: [Permissões]

**Implementação:**
```typescript
// Middleware de autorização
function requireRole(role: string) {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.status(403).json({ error: 'Forbidden' })
    }
    next()
  }
}
```

### Proteções

**1. Senhas:**
- Hashing: bcrypt com custo 12
- Salt: automático no bcrypt
- Nunca armazenar plaintext

```typescript
const hash = await bcrypt.hash(password, 12)
```

**2. Dados Sensíveis:**
- Criptografia em repouso: AES-256
- Criptografia em trânsito: HTTPS/TLS 1.3
- Logs: nunca incluir passwords, tokens, PII

**3. Validação de Input:**
- Sempre validar no backend (nunca confiar só no frontend)
- Usar biblioteca de validação (Zod, Joi, Yup)
- Sanitização de SQL (usar ORM ou prepared statements)

**4. OWASP Top 10:**
- [ ] Injection: [Como prevenir - usar ORM, prepared statements]
- [ ] Broken Authentication: [Como prevenir - JWT seguro, rate limiting]
- [ ] Sensitive Data Exposure: [Como prevenir - HTTPS, criptografia]
- [ ] XML External Entities: [Não aplicável ou como prevenir]
- [ ] Broken Access Control: [Como prevenir - autorização em cada endpoint]
- [ ] Security Misconfiguration: [Como prevenir - vars de ambiente, sem defaults inseguros]
- [ ] XSS: [Como prevenir - sanitização, CSP headers]
- [ ] Insecure Deserialization: [Como prevenir - validação de JSON]
- [ ] Using Vulnerable Components: [Como prevenir - npm audit, Dependabot]
- [ ] Insufficient Logging: [Como prevenir - logs estruturados, monitoramento]

**5. Headers de Segurança:**
```typescript
// Helmet.js ou equivalente
helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'"],
    },
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
  },
})
```

---

## Deployment

### Ambientes

**1. Development (Local):**
- URL: `http://localhost:3000`
- Database: Local PostgreSQL/SQLite
- Variáveis: `.env.development`

**2. Staging:**
- URL: `https://staging.example.com`
- Database: [Database de staging]
- Variáveis: `.env.staging`
- Deploy: [Manual/CI/CD]

**3. Production:**
- URL: `https://example.com`
- Database: [Database de produção]
- Variáveis: `.env.production`
- Deploy: [CI/CD automático]

### CI/CD Pipeline

**Tool:** [GitHub Actions, GitLab CI, Jenkins, etc.]

**Pipeline:**
```yaml
# Exemplo de GitHub Actions
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: npm install
      - name: Run linter
        run: npm run lint
      - name: Run tests
        run: npm run test
      - name: Run E2E tests
        run: npm run test:e2e

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: [comando de deploy]
```

### Estratégia de Deploy

**Tipo:** [Blue-Green, Canary, Rolling, etc.]

**Rollback:**
[Como fazer rollback em caso de falha]

**Health Checks:**
```typescript
// Endpoint de health check
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
  })
})
```

### Monitoramento

**Ferramentas:**
- [Ex: Sentry para error tracking]
- [Ex: DataDog para metrics]
- [Ex: LogRocket para session replay]

**Métricas a monitorar:**
- Taxa de erro (4xx, 5xx)
- Tempo de resposta (P50, P95, P99)
- Throughput (requests/segundo)
- Uso de recursos (CPU, memória)

**Alertas:**
- [Quando disparar alerta 1]
- [Quando disparar alerta 2]

---

**Documento criado em:** [Data]
**Última atualização:** [Data]
**Versão:** 1.0
