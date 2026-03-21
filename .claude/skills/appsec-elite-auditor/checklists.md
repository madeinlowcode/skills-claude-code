# Checklists de Auditoria por Tipo de Aplicação

Checklists específicos para diferentes tipos de aplicação e framework.
Use como guia rápido durante auditorias focadas.

---

## 1. Next.js / React (Full-Stack)

### Autenticação & Sessão
- [ ] NextAuth/Auth.js configurado com `secret` forte
- [ ] Sessão com `httpOnly`, `secure`, `sameSite`
- [ ] Middleware protege TODAS as rotas privadas (dashboard, admin, API)
- [ ] `matcher` no middleware cobre todas as rotas protegidas
- [ ] Server Components não vazam dados sensíveis para o cliente

### Variáveis de Ambiente
- [ ] Nenhum secret em `NEXT_PUBLIC_*`
- [ ] `NEXT_PUBLIC_` contém apenas dados públicos (URLs, chaves públicas)
- [ ] `.env.local` no `.gitignore`
- [ ] Variáveis sensíveis apenas em Server Components e API Routes

### API Routes (App Router)
- [ ] Cada `route.ts` verifica autenticação
- [ ] Cada `route.ts` verifica autorização (role/ownership)
- [ ] Inputs validados com Zod/Yup antes de usar
- [ ] Responses não vazam campos sensíveis (`select` explícito no Prisma)
- [ ] Rate limiting em endpoints sensíveis

### Server Actions
- [ ] Server Actions validam autenticação
- [ ] Server Actions validam inputs
- [ ] Server Actions não expõem dados sensíveis no retorno

### Middleware
- [ ] Middleware cobre `/dashboard`, `/admin`, `/api/admin`, `/api/private`
- [ ] Middleware retorna 401 JSON para rotas API (não redirect)
- [ ] Middleware não pode ser bypassed por trailing slash ou encoding

---

## 2. Express.js / Node.js API

### Configuração Base
- [ ] Helmet.js instalado e configurado
- [ ] CORS com whitelist explícita de origins
- [ ] Rate limiting global (`express-rate-limit`)
- [ ] Body parser com limite de tamanho (`limit: '10kb'`)
- [ ] Sem `X-Powered-By` header

### Autenticação
- [ ] JWT com `verify()` (nunca `decode()`) e algoritmo explícito
- [ ] Segredo JWT com 256+ bits de entropia
- [ ] Access token com expiração curta (15min)
- [ ] Refresh token com rotação e revogação
- [ ] Rate limiting em `/login`, `/register`, `/reset-password`
- [ ] Bcrypt/Argon2 para hash de senhas (nunca MD5/SHA1)

### Autorização
- [ ] Middleware de auth em TODAS as rotas protegidas
- [ ] Middleware de role em rotas admin
- [ ] IDOR: queries filtram por `userId`
- [ ] Mass assignment: whitelist de campos no body

### Banco de Dados
- [ ] Queries parametrizadas (nunca concatenação)
- [ ] ORM usado corretamente (sem `queryRawUnsafe`)
- [ ] Transações para operações financeiras
- [ ] Campos sensíveis excluídos dos SELECTs

### Upload de Arquivos
- [ ] Validação de extensão (whitelist)
- [ ] Validação de MIME type
- [ ] Limite de tamanho
- [ ] Nome de arquivo sanitizado (`path.basename`)
- [ ] Path traversal prevenido
- [ ] Armazenamento fora do webroot ou em S3/CDN

---

## 3. Django / Python

### Configuração
- [ ] `DEBUG = False` em produção
- [ ] `SECRET_KEY` forte e do ambiente
- [ ] `ALLOWED_HOSTS` configurado (não `['*']`)
- [ ] `CSRF_COOKIE_SECURE = True`
- [ ] `SESSION_COOKIE_SECURE = True`
- [ ] `SESSION_COOKIE_HTTPONLY = True`
- [ ] `SECURE_BROWSER_XSS_FILTER = True`
- [ ] `SECURE_CONTENT_TYPE_NOSNIFF = True`
- [ ] `SECURE_HSTS_SECONDS > 0`

### Autenticação
- [ ] `django.contrib.auth` usado (não auth customizada fraca)
- [ ] Password validators configurados
- [ ] Rate limiting em login (`django-axes` ou `django-ratelimit`)
- [ ] 2FA disponível para admin

### Autorização
- [ ] `@login_required` ou `LoginRequiredMixin` em views protegidas
- [ ] `@permission_required` para ações específicas
- [ ] QuerySets filtrados por usuário (`request.user`)
- [ ] Admin Django protegido com 2FA

### Templates
- [ ] Auto-escape ativo (padrão do Django)
- [ ] `|safe` filter usado com cautela (verificar XSS)
- [ ] `mark_safe()` nunca com input do usuário

### ORM
- [ ] `extra()` e `raw()` evitados ou com parâmetros
- [ ] `RawSQL` com placeholders
- [ ] Input do usuário nunca concatenado em queries

---

## 4. FastAPI / Python API

### Configuração
- [ ] CORS com `allow_origins` explícito (não `["*"]`)
- [ ] Pydantic models para validação de input
- [ ] Rate limiting configurado
- [ ] Docs (`/docs`, `/redoc`) desabilitados em produção

### Autenticação
- [ ] OAuth2/JWT com `python-jose` ou `PyJWT`
- [ ] Dependência de auth (`Depends(get_current_user)`)
- [ ] Token com expiração e algoritmo explícito
- [ ] Bcrypt para hash de senhas

### Autorização
- [ ] Dependência de role para rotas admin
- [ ] Queries filtradas por user ID
- [ ] IDOR verificado em cada endpoint com path params

### Segurança
- [ ] `subprocess` sem `shell=True`
- [ ] `requests`/`httpx` com validação de URL (anti-SSRF)
- [ ] SQLAlchemy com parâmetros (nunca f-strings em queries)
- [ ] File upload com validação de tipo e tamanho

---

## 5. SaaS com Pagamentos

### Webhook de Pagamento
- [ ] Assinatura criptográfica verificada (Stripe `constructEvent`, etc.)
- [ ] Endpoint usa `raw body` (não parsed JSON) para verificação
- [ ] Idempotency: processamento idempotente por event ID
- [ ] Lógica de liberação APÓS confirmação (não antes)
- [ ] Status verificado na API do gateway como fallback
- [ ] Webhook secret no `.env` (não hardcoded)

### Lógica de Preços
- [ ] Preço calculado EXCLUSIVAMENTE no servidor
- [ ] Preço do body do request IGNORADO
- [ ] Cupom validado no servidor (existência, validade, uso máximo)
- [ ] Race condition em cupom prevenida com transação atômica
- [ ] Quantidade negativa rejeitada

### Gerenciamento de Acesso
- [ ] Acesso premium expira na data correta
- [ ] Job/cron verifica expiração regularmente
- [ ] Downgrade automático ao expirar
- [ ] Trial não pode ser re-ativado
- [ ] Conta cancelada perde acesso ao final do período

### Multi-tenancy
- [ ] Dados de tenant isolados em TODAS as queries
- [ ] Tenant ID derivado da sessão (nunca do request)
- [ ] Admin de tenant não acessa dados de outro tenant
- [ ] API keys com scope por tenant

---

## 6. API GraphQL

### Configuração
- [ ] Introspection desabilitada em produção
- [ ] Depth limit configurado (max 10-15)
- [ ] Complexity limit configurado
- [ ] Rate limiting por query/mutation
- [ ] Timeout de query configurado

### Autenticação & Autorização
- [ ] Resolvers verificam autenticação
- [ ] Resolvers verificam autorização
- [ ] Mutations sensíveis têm proteção adicional
- [ ] Nested queries não bypassed authorization

### Data Exposure
- [ ] Campos sensíveis não expostos no schema
- [ ] Paginação obrigatória em listas
- [ ] Filtros não permitem acesso a dados de outros usuários

---

## 7. Aplicação com Upload de Arquivos

### Validação
- [ ] Extensão validada por whitelist (não blacklist)
- [ ] MIME type verificado (magic bytes, não Content-Type header)
- [ ] Tamanho máximo validado no servidor
- [ ] Nome de arquivo sanitizado
- [ ] Path traversal prevenido
- [ ] Nenhuma extensão executável aceita (`.php`, `.jsp`, `.exe`, `.sh`, `.py`)

### Armazenamento
- [ ] Arquivos armazenados fora do webroot
- [ ] Ou em storage externo (S3, GCS, Azure Blob)
- [ ] URLs de download temporárias (signed URLs)
- [ ] Sem execução de scripts no diretório de upload

### Processamento
- [ ] Imagens re-processadas (strip metadata, resize)
- [ ] SVG sanitizado (pode conter JavaScript)
- [ ] PDF verificado (pode conter JavaScript)
- [ ] ZIP bomb protection (verificar tamanho descomprimido)

---

## 8. Checklist Rápido Universal (Top 20)

Use este checklist para uma verificação rápida de qualquer aplicação:

1. [ ] Secrets não estão hardcoded no código
2. [ ] `.env` está no `.gitignore` e nunca foi commitado
3. [ ] Autenticação presente em TODAS as rotas protegidas
4. [ ] Autorização verifica ownership/role (não apenas auth)
5. [ ] Inputs validados e sanitizados
6. [ ] Queries parametrizadas (zero concatenação)
7. [ ] Webhooks de pagamento verificam assinatura
8. [ ] Preço calculado no servidor (nunca do cliente)
9. [ ] Rate limiting em endpoints sensíveis
10. [ ] CORS com whitelist explícita
11. [ ] Cookies com `httpOnly`, `secure`, `sameSite`
12. [ ] Headers de segurança configurados (Helmet/equivalente)
13. [ ] XSS prevenido (auto-escape, DOMPurify)
14. [ ] CSRF protection em ações sensíveis
15. [ ] Upload com validação de tipo, tamanho e nome
16. [ ] Sem command injection (exec/spawn sem input do user)
17. [ ] SSRF prevenido (validação de URL contra IPs internos)
18. [ ] Campos sensíveis excluídos dos API responses
19. [ ] Dependências sem vulnerabilidades HIGH/CRITICAL
20. [ ] Stack traces e debug desabilitados em produção
