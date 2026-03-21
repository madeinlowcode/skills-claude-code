# Checklists de Auditoria AppSec

Checklists executivos para uso rápido durante auditorias. Cada item deve ser verificado e reportado.

---

## Checklist 1: Autenticação e Sessão

- [ ] JWT usa algoritmo explícito (não aceita `none`)
- [ ] Segredo JWT tem 256+ bits de entropia
- [ ] Usa `jwt.verify()` e nunca `jwt.decode()` para decisões de acesso
- [ ] Access token tem expiração curta (15-30 min)
- [ ] Refresh token tem rotação e revogação
- [ ] Senhas armazenadas com bcrypt/scrypt/argon2 (custo adequado)
- [ ] Rate limiting em login (máx 5-10 tentativas/minuto)
- [ ] Rate limiting em recuperação de senha
- [ ] Cookies de sessão têm `httpOnly`, `secure`, `sameSite`
- [ ] Sessão invalidada no logout (server-side)
- [ ] Tokens não expostos em URLs ou logs
- [ ] Registro não revela se email já existe (timing-safe)
- [ ] 2FA disponível para contas sensíveis
- [ ] Password reset tokens são single-use e expiram rapidamente

---

## Checklist 2: Autorização e Controle de Acesso

- [ ] Todas as rotas protegidas têm middleware de autenticação
- [ ] Rotas admin verificam role do usuário
- [ ] IDOR prevenido — ownership verificado em cada recurso
- [ ] IDs sequenciais substituídos por UUIDs onde possível
- [ ] Mass assignment prevenido — whitelist de campos aceitos
- [ ] Escalação horizontal bloqueada (user A não acessa dados de user B)
- [ ] Escalação vertical bloqueada (user não vira admin)
- [ ] API routes do Next.js têm autenticação própria (não dependem só do middleware)
- [ ] Server Actions do Next.js verificam autenticação
- [ ] Operações destrutivas requerem re-autenticação

---

## Checklist 3: Injeções

- [ ] Queries SQL usam parametrização (nunca concatenação)
- [ ] Prisma: nenhum uso de `$queryRawUnsafe` com input do usuário
- [ ] Sequelize: nenhum uso de `sequelize.literal()` com input do usuário
- [ ] MongoDB: inputs forçados a tipos primitivos (String, Number)
- [ ] Nenhum `eval()`, `Function()`, `vm.runInNewContext()` com input do usuário
- [ ] `child_process.exec()` substituído por `execFile()` ou `spawn()` sem shell
- [ ] Templates não usam interpolação direta de input (SSTI)
- [ ] React: nenhum `dangerouslySetInnerHTML` sem sanitização (DOMPurify)
- [ ] Express: responses HTML usam template engine com auto-escape
- [ ] Headers HTTP não injetáveis via input do usuário (CRLF)

---

## Checklist 4: Lógica de Negócio e Pagamentos

- [ ] Webhooks de pagamento verificam assinatura criptográfica
- [ ] Stripe: usa `stripe.webhooks.constructEvent()` com raw body
- [ ] Hotmart: verifica `x-hotmart-hottok` e confirma via API
- [ ] Preços e planos definidos server-side (nunca do client)
- [ ] Cupons/descontos com proteção contra race condition (transação atômica)
- [ ] Cupons não podem ser reutilizados além do limite
- [ ] Downgrade de plano revoga acessos imediatamente
- [ ] Trial não pode ser reiniciado (verificar por email, device, IP)
- [ ] Operações financeiras têm idempotency key
- [ ] Refunds processados via API do gateway (não manualmente)
- [ ] Logs de auditoria para todas as transações financeiras

---

## Checklist 5: APIs e Comunicação

- [ ] CORS configurado com whitelist de origins (não reflete `req.headers.origin`)
- [ ] Wildcard `*` não usado com `credentials: true`
- [ ] Rate limiting global configurado (express-rate-limit ou similar)
- [ ] Rate limiting específico para endpoints sensíveis
- [ ] Respostas de API não vazam dados sensíveis (passwordHash, tokens, keys)
- [ ] Paginação implementada com limite máximo (não retorna coleção inteira)
- [ ] GraphQL: depth limiting e query complexity configurados
- [ ] GraphQL: introspection desabilitada em produção
- [ ] Uploads validam tipo MIME, extensão e tamanho
- [ ] Uploads armazenados fora do webroot ou em storage externo (S3)
- [ ] SSRF prevenida — URLs de usuário validadas contra IPs internos
- [ ] Timeouts configurados para requests externos

---

## Checklist 6: Headers e Configuração de Segurança

- [ ] `Strict-Transport-Security` (HSTS) configurado
- [ ] `Content-Security-Policy` (CSP) configurado e restritivo
- [ ] `X-Content-Type-Options: nosniff` presente
- [ ] `X-Frame-Options: DENY` ou CSP `frame-ancestors 'none'`
- [ ] `Referrer-Policy: strict-origin-when-cross-origin` ou mais restritivo
- [ ] `Permissions-Policy` configurado (câmera, microfone, geolocalização)
- [ ] Servidor não expõe versão (remover `X-Powered-By`)
- [ ] Debug mode desabilitado em produção
- [ ] Stack traces não expostos em respostas de erro de produção
- [ ] HTTPS forçado em produção (redirect HTTP → HTTPS)
- [ ] Certificado TLS válido e atualizado

---

## Checklist 7: Secrets e Variáveis de Ambiente

- [ ] Nenhum secret hardcoded no código-fonte
- [ ] `.env` no `.gitignore`
- [ ] Nenhuma chave privada/secreta com prefixo `NEXT_PUBLIC_`
- [ ] Secrets gerenciados via vault ou variáveis de ambiente do hosting
- [ ] API keys têm escopo mínimo necessário
- [ ] Chaves de produção diferentes das de desenvolvimento
- [ ] Rotação de secrets documentada e praticada
- [ ] Git history verificado contra leaks anteriores (git-secrets, trufflehog)
- [ ] `npm audit` sem vulnerabilidades críticas ou altas
- [ ] Dependências atualizadas (sem versões com CVEs conhecidos)
- [ ] Lock file (package-lock.json / yarn.lock) commitado

---

## Checklist 8: Logging e Monitoramento

- [ ] Tentativas de login falhas são logadas (com IP, user-agent)
- [ ] Acessos a rotas admin são logados
- [ ] Alterações em dados sensíveis são logadas (audit trail)
- [ ] Logs NÃO contêm passwords, tokens, ou dados sensíveis
- [ ] Logs armazenados em sistema externo (não apenas no servidor)
- [ ] Alertas configurados para padrões anômalos (muitos 401/403, brute force)
- [ ] Logs de webhook de pagamento mantidos para reconciliação

---

## Formato do Relatório de Auditoria

```markdown
# Relatório de Auditoria AppSec
**Data:** YYYY-MM-DD
**Auditor:** AppSec Elite Auditor (AI-assisted)
**Escopo:** [nome do projeto/repositório]

## Resumo Executivo
- Total de vulnerabilidades encontradas: X
- Críticas: X | Altas: X | Médias: X | Baixas: X | Informativas: X
- Recomendação: [APROVADO PARA DEPLOY / DEPLOY COM RESSALVAS / BLOQUEADO]

## Vulnerabilidades Encontradas

### [CRÍTICA] Título da Vulnerabilidade
- **Localização:** `arquivo:linha`
- **OWASP:** A0X:2021 — Nome
- **CWE:** CWE-XXX
- **Descrição:** O que foi encontrado
- **Impacto:** O que um atacante pode fazer
- **Prova de Conceito:** Payload ou passos para reproduzir
- **Correção:** Código corrigido ou recomendação específica

### [ALTA] Título...
(mesmo formato)

## Itens Verificados sem Problemas
- [x] Item 1
- [x] Item 2

## Recomendações Gerais
1. Recomendação 1
2. Recomendação 2
```

---

## Classificação de Severidade

| Severidade | Critério | Exemplos |
|------------|----------|----------|
| **CRÍTICA** | Comprometimento total do sistema, RCE, acesso admin sem autenticação | SQLi com acesso ao banco, RCE via command injection, JWT alg:none em produção |
| **ALTA** | Acesso a dados de outros usuários, bypass de autenticação parcial | IDOR em dados sensíveis, SSRF a metadados cloud, XSS stored |
| **MÉDIA** | Impacto limitado ou requer interação do usuário | XSS reflected, CSRF em ações não-críticas, informação sensível em logs |
| **BAIXA** | Risco menor, boas práticas não seguidas | Headers de segurança faltando, verbose errors, cookies sem flags |
| **INFO** | Observações e recomendações preventivas | Dependências desatualizadas sem CVE, melhorias de arquitetura |
