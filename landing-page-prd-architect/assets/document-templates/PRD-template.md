# PRD: [Nome do Projeto] Landing Page

## 1. Visão Geral

### Objetivo
[Descrever objetivo principal da landing page - vender, captar leads, apresentar, lançar]

### Público-Alvo
- **Perfil:** [Descrição demográfica e psicográfica]
- **Dores:** [Problemas que o público enfrenta]
- **Desejos:** [O que buscam resolver]

### Proposta de Valor
[Uma frase que resume o diferencial único]

### KPIs Esperados
- Taxa de conversão: [X%]
- Tempo na página: [X min]
- Bounce rate: [X%]

---

## 2. Requisitos Funcionais

### Funcionalidades Principais
- [ ] [Funcionalidade 1]
- [ ] [Funcionalidade 2]
- [ ] [Funcionalidade 3]

### Formulários
| Campo | Tipo | Obrigatório | Validação |
|-------|------|-------------|-----------|
| Nome | text | Sim | Min 2 chars |
| Email | email | Sim | Email válido |
| ... | ... | ... | ... |

### Integrações
- [ ] [Sistema 1]: [Descrição da integração]
- [ ] [Sistema 2]: [Descrição da integração]

### Comportamentos Interativos
- [Descrever interações específicas]

---

## 3. Estrutura de Seções

### 3.1 Navbar
- Logo
- Links: [Home, Features, Pricing, Contact]
- CTA: [Texto do botão]
- Mobile: Hamburger menu

### 3.2 Hero Section
**Objetivo:** Capturar atenção e comunicar proposta de valor

**Layout:** [Centralizado/Split/Full-screen]

**Conteúdo:**
- Badge: [Texto opcional]
- Headline: [Texto principal]
- Subheadline: [Texto secundário]
- CTA Primário: [Texto]
- CTA Secundário: [Texto]
- Social Proof: [Descrição]

**Visual:**
- Background: [Descrição]
- Imagem principal: [Ver IMAGE-PROMPTS.md]
- Elementos decorativos: [Descrição]

**Animações:**
- [Lista de animações]

### 3.3 [Nome da Seção]
[Repetir estrutura para cada seção]

---

## 4. Requisitos Técnicos

### Stack
- **Framework:** [Next.js/Astro/etc]
- **Styling:** [Tailwind/etc]
- **Animações:** [Framer Motion/etc]
- **Icons:** [Lucide/etc]

### Performance
- Lighthouse Score: > 90
- LCP: < 2.5s
- FID: < 100ms
- CLS: < 0.1

### SEO
- Meta title: [Texto]
- Meta description: [Texto]
- Open Graph tags
- Schema markup

### Acessibilidade
- WCAG 2.1 AA compliance
- Keyboard navigation
- Screen reader support
- Color contrast ratios

---

## 5. Responsividade

### Breakpoints
- Mobile: 375px
- Tablet: 768px
- Desktop: 1024px
- Large: 1440px

### Adaptações por Dispositivo

**Mobile:**
- [Lista de adaptações]

**Tablet:**
- [Lista de adaptações]

---

## 6. Animações e Interações

### Por Seção
| Seção | Animação | Trigger | Duration |
|-------|----------|---------|----------|
| Hero | fadeInUp | load | 0.5s |
| Features | stagger | scroll | 0.3s |
| ... | ... | ... | ... |

### Hover States
- Buttons: [Descrição]
- Cards: [Descrição]
- Links: [Descrição]

### Scroll Behavior
- [Smooth scroll para âncoras]
- [Reveal animations]
- [Parallax se aplicável]

---

## 7. Conteúdo

### Textos por Seção
[Incluir todos os textos finais ou placeholders]

### CTAs
| Seção | Texto | Ação |
|-------|-------|------|
| Hero | [Texto] | [Ação] |
| ... | ... | ... |

### Microcopy
- Error messages: [Padrão]
- Success messages: [Padrão]
- Loading states: [Padrão]

---

## 8. Assets Necessários

### Imagens
| ID | Seção | Descrição | Arquivo |
|----|-------|-----------|---------|
| 1 | Hero | [Descrição] | hero-main.png |
| ... | ... | ... | ... |

Ver prompts completos em [IMAGE-PROMPTS.md]

### Ícones
[Lista de ícones necessários por seção]

### Vídeos
[Se aplicável]

---

## 9. Instruções para Gemini CLI

### Ordem de Implementação
1. Setup do projeto e estrutura de pastas
2. Configuração de Tailwind e tema
3. Componentes base (Button, Card, Input)
4. Layout (Navbar, Footer)
5. Seções em ordem de aparição
6. Animações
7. Responsividade
8. Otimizações e SEO

### Pontos de Atenção
- [Lista de cuidados específicos]

### Padrões a Seguir
- [Naming conventions]
- [Estrutura de componentes]
- [Organização de estilos]

---

## Changelog

| Data | Versão | Alterações |
|------|--------|------------|
| [Data] | 1.0 | Versão inicial |
