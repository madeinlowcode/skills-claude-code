# Claude Code Skills Collection

Uma coleção de skills especializadas para estender as capacidades do Claude Code em diversos domínios e workflows.

## 📚 Índice

- [Sobre Skills](#sobre-skills)
- [Skills Disponíveis](#skills-disponíveis)
  - [Desenvolvimento](#desenvolvimento)
  - [Segurança](#segurança)
  - [Design](#design)
  - [Planejamento e Gestão](#planejamento-e-gestão)
  - [Criação de Skills](#criação-de-skills)
- [Como Usar](#como-usar)
- [Estrutura de uma Skill](#estrutura-de-uma-skill)
- [Contribuindo](#contribuindo)

## Sobre Skills

Skills são pacotes modulares e auto-contidos que estendem as capacidades do Claude fornecendo conhecimento especializado, workflows e integrações de ferramentas. Pense nelas como "guias de integração" para domínios ou tarefas específicas - elas transformam o Claude de um agente de propósito geral em um agente especializado equipado com conhecimento procedural.

### O que as Skills Fornecem

1. **Workflows especializados** - Procedimentos multi-etapas para domínios específicos
2. **Integrações de ferramentas** - Instruções para trabalhar com formatos de arquivo ou APIs específicas
3. **Expertise de domínio** - Conhecimento específico da empresa, schemas, lógica de negócios
4. **Recursos agrupados** - Scripts, referências e assets para tarefas complexas e repetitivas

## Skills Disponíveis

### Desenvolvimento

#### fullstack-dev
**Descrição:** Skill especializada para desenvolvimento fullstack com foco em arquitetura moderna e boas práticas.

**Quando usar:**
- Desenvolvimento de aplicações fullstack completas
- Implementação de arquiteturas modernas
- Integração de frontend e backend

**Recursos:**
- Guias de stack tecnológica
- Padrões de arquitetura
- Boas práticas de desenvolvimento

---

#### long-running-agent
**Descrição:** Sistema de agente de longa duração para desenvolvimento autônomo de features complexas seguindo metodologia Spec-Driven Development.

**Quando usar:**
- Implementação de features complexas que requerem múltiplas etapas
- Desenvolvimento autônomo com verificação contínua
- Projetos que seguem Spec-Driven Development

**Recursos:**
- Templates de features
- Sistema de progresso e verificação
- Scripts de inicialização de projeto
- Configuração de regras e comandos

**Características especiais:**
- Executa tarefas em múltiplas iterações
- Verifica progresso automaticamente
- Segue documentação estruturada (spec.md, plan.md, tasks.md)

---

#### lisa-prompt-engineering
**Descrição:** Framework para criação de prompts otimizados e estruturados para engenharia de prompts avançada.

**Quando usar:**
- Criação de prompts complexos para projetos
- Otimização de instruções para Claude
- Documentação de especificações de projeto

**Recursos:**
- Exemplos de prompts básicos e complexos
- Padrões de prompts
- Melhores práticas LISA
- Exemplos de specs

**Conteúdo:**
- `examples/` - Exemplos de prompts (básico, complexo, spec-driven)
- `references/` - Guias de melhores práticas e padrões

---

#### ralph-prompt-builder
**Descrição:** Assistente para criação de prompts otimizados para o plugin ralph-loop com validação integrada e templates.

**Quando usar:**
- Antes de usar /ralph-loop e precisar criar um prompt efetivo
- Validar um prompt para compatibilidade com ralph-loop
- Usar templates para casos comuns (TDD, feature dev, bug fixing, greenfield projects)
- Garantir que prompts tenham critérios claros de conclusão e tags `<promise>` adequadas

**Recursos:**
- Workflow interativo para construção de prompts
- Templates pré-construídos para casos comuns
- Validação automática de qualidade
- Scripts de validação de prompts

**Templates disponíveis:**
- TDD Development
- Feature Implementation
- Bug Fixing
- Greenfield Projects

---

#### sprint-context-generator
**Descrição:** Gera documentação completa de sprint (spec.md, plan.md, tasks.md, research.md, features.xml) seguindo metodologia Spec-Driven Development com análise multi-persona.

**Quando usar:**
- Planejar novas features para um projeto
- Refatorar features existentes com documentação adequada
- Criar contexto estruturado para desenvolvimento prolongado
- Preparar trabalho para delegação a SubAgents
- Garantir que todos os stakeholders tenham input
- Gerar documentação compatível com `long-running-agent`

**Características especiais:**
- Análise multi-perspectiva (6 personas: Arquiteto, Dev, QA, Designer, PM, BA)
- Coleta interativa de requisitos
- Pesquisa automatizada de documentação (WebSearch/WebFetch)
- Geração de 50-100 tasks granulares
- Geração de IDs sequenciais de features (FEAT-XXX)
- Criação automática de branch e commit

**Documentos gerados:**
1. **spec.md** - Especificação detalhada com análises das 6 personas
2. **plan.md** - Plano técnico de arquitetura
3. **tasks.md** - Lista de 50-100 tasks granulares
4. **research.md** - Pesquisa de documentação e melhores práticas
5. **features.xml** - Arquivo de controle de features

---

### Segurança

#### ffuf-skill
**Descrição:** Skill especializada para fuzzing web usando a ferramenta ffuf (Fuzz Faster U Fool).

**Quando usar:**
- Testes de segurança em aplicações web
- Descoberta de diretórios e arquivos
- Fuzzing de parâmetros e endpoints
- Brute force de autenticação

**Recursos:**
- Script helper em Python para automação
- Templates de requisições
- Wordlists especializadas
- Guia completo de uso

**Conteúdo:**
- `ffuf_helper.py` - Script auxiliar para operações comuns
- `resources/REQUEST_TEMPLATES.md` - Templates de requisições HTTP
- `resources/WORDLISTS.md` - Guia de wordlists recomendadas

---

### Design

#### design-principles
**Descrição:** Enforça um sistema de design preciso e minimalista inspirado em Linear, Notion e Stripe. Use ao construir dashboards, interfaces admin ou qualquer UI que precise de precisão nível Jony Ive - limpo, moderno, minimalista com bom gosto.

**Quando usar:**
- Construção de dashboards e interfaces admin
- Desenvolvimento de SaaS e aplicações enterprise
- Criar interfaces que exigem alta qualidade visual
- Implementar sistemas de design consistentes

**Princípios fundamentais:**
- Grid de 4px para espaçamento
- Padding simétrico
- Consistência de border radius
- Estratégia de profundidade e elevação
- Hierarquia tipográfica
- Uso de ícones Phosphor
- Animações sutis (150-250ms)

**Direções de design suportadas:**
- Precision & Density (Linear, Raycast)
- Warmth & Approachability (Notion, Coda)
- Sophistication & Trust (Stripe, Mercury)
- Boldness & Clarity (Vercel)
- Utility & Function (GitHub)
- Data & Analysis (Analytics tools)

**Considerações especiais:**
- Dark mode com abordagem diferenciada
- Controles isolados com tratamento de container
- Cards com layouts variados mas superfície consistente
- Navegação com contexto adequado

---

### Planejamento e Gestão

#### software-architecture
**Descrição:** Guia para design e análise de arquitetura de software com foco em decisões arquiteturais e trade-offs.

**Quando usar:**
- Planejamento de arquitetura de novos sistemas
- Análise e refatoração de arquiteturas existentes
- Tomada de decisões arquiteturais
- Documentação de padrões arquiteturais

**Foco:**
- Padrões de arquitetura
- Trade-offs e decisões técnicas
- Escalabilidade e performance
- Manutenibilidade

---

### Criação de Skills

#### skill-creator
**Descrição:** Guia completo para criação de skills efetivas que estendem as capacidades do Claude com conhecimento especializado, workflows e integrações de ferramentas.

**Quando usar:**
- Criar uma nova skill do zero
- Atualizar uma skill existente
- Aprender sobre estrutura e boas práticas de skills
- Empacotar e distribuir skills

**Processo de criação:**
1. **Entender a skill** com exemplos concretos
2. **Planejar conteúdos reutilizáveis** (scripts, referências, assets)
3. **Inicializar a skill** (usar init_skill.py)
4. **Editar a skill** (implementar recursos e escrever SKILL.md)
5. **Empacotar a skill** (usar package_skill.py)
6. **Iterar** baseado no uso real

**Princípios fundamentais:**
- **Concisão** - Context window é um bem público
- **Graus de liberdade apropriados** - Balancear especificidade com flexibilidade
- **Progressive disclosure** - Carregar informações apenas quando necessário

**Scripts disponíveis:**
- `init_skill.py` - Inicializa nova skill com template
- `package_skill.py` - Valida e empacota skill para distribuição

**Referências:**
- `references/workflows.md` - Padrões para processos multi-etapa
- `references/output-patterns.md` - Padrões para formatos de saída

---

## Como Usar

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/madeinlowcode/skills-claude-code.git
```

2. As skills podem ser usadas diretamente no Claude Code através do sistema de skills

### Usando uma Skill

Cada skill é automaticamente carregada pelo Claude Code quando relevante. O sistema analisa a descrição da skill e determina quando ela deve ser ativada.

### Estrutura de Diretórios

```
skills/
├── skill-name/
│   ├── SKILL.md              # Arquivo principal (obrigatório)
│   ├── scripts/              # Scripts executáveis (opcional)
│   ├── references/           # Documentação de referência (opcional)
│   └── assets/               # Arquivos usados na saída (opcional)
```

## Estrutura de uma Skill

Cada skill consiste em:

### SKILL.md (obrigatório)

Arquivo principal contendo:

**Frontmatter YAML:**
```yaml
---
name: skill-name
description: Descrição detalhada de quando e como usar a skill
---
```

**Corpo em Markdown:**
- Instruções de uso
- Workflows e procedimentos
- Referências a recursos adicionais

### Recursos Opcionais

**scripts/** - Código executável (Python/Bash/etc.)
- Use quando o mesmo código é reescrito repetidamente
- Garante confiabilidade determinística
- Eficiente em tokens

**references/** - Documentação de referência
- Carregada sob demanda no contexto
- Schemas, documentação de API, conhecimento de domínio
- Mantém SKILL.md enxuto

**assets/** - Arquivos usados na saída
- Não são carregados no contexto
- Templates, imagens, ícones, boilerplates
- Usados diretamente na produção de conteúdo

## Princípios de Design

### Progressive Disclosure

As skills usam um sistema de carregamento em três níveis:

1. **Metadata (name + description)** - Sempre em contexto (~100 palavras)
2. **SKILL.md body** - Quando a skill é ativada (<5k palavras)
3. **Bundled resources** - Conforme necessário (ilimitado, pode ser executado sem ler)

### Concisão

O context window é compartilhado. Apenas adicione contexto que o Claude não possui. Desafie cada informação: "O Claude realmente precisa desta explicação?"

### Graus de Liberdade Apropriados

- **Alta liberdade** - Instruções baseadas em texto para abordagens múltiplas
- **Média liberdade** - Pseudocódigo ou scripts com parâmetros
- **Baixa liberdade** - Scripts específicos para operações frágeis

## Versionamento

Este repositório usa tags semânticas para versionamento:

- `v1.0.0` - Versão inicial com skills básicas
- `v1.1.0` - Adição de novas skills
- `v1.1.1` - Correções e melhorias

Para ver todas as versões:
```bash
git tag
```

## Contribuindo

Contribuições são bem-vindas! Para adicionar uma nova skill:

1. Use o `skill-creator` para guiar o processo
2. Siga os princípios de design documentados
3. Teste a skill em casos de uso reais
4. Envie um Pull Request com a nova skill

## Licença

Ver arquivo LICENSE.txt em cada skill para detalhes específicos.

## Links Úteis

- [Repositório GitHub](https://github.com/madeinlowcode/skills-claude-code)
- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [Anthropic Developer Docs](https://docs.anthropic.com)

---

**Última atualização:** Janeiro 2025

**Skills no repositório:** 9
- fullstack-dev
- long-running-agent
- lisa-prompt-engineering
- ralph-prompt-builder
- sprint-context-generator
- ffuf-skill
- design-principles
- software-architecture
- skill-creator
