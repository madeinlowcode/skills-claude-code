# Prompts para Geração de Imagens

## Instruções para Gemini CLI

Usar MCP Nano Banana para gerar cada imagem.
Salvar em: `/assets/images/[nome-descritivo].png`

Configurações recomendadas:
- Quality: High
- Style: [Definido por projeto]

---

## 1. Hero Principal

**Arquivo:** `hero-main.png`
**Seção:** Hero
**Uso:** Visual principal da hero section

### Versão Desktop (16:9)

```
[PROMPT DETALHADO AQUI]

Subject: [Descrição detalhada do que deve aparecer na imagem]

Composition: [Enquadramento, ângulo, disposição dos elementos]

Style: [Fotográfico realista / Ilustração 3D / Flat design / etc.]

Color Palette: [Cores específicas que devem predominar - usar HEX da identidade visual]

Lighting: [Tipo de iluminação - studio, natural, dramática, suave]

Mood: [Atmosfera/sensação - profissional, acolhedor, futurista, premium]

Background: [Descrição do fundo]

Technical Specs:
- Aspect Ratio: 16:9
- Resolution: 1920x1080 minimum
- Format: PNG with transparency (if applicable)

Additional Notes: [Observações específicas para contexto da landing page]
```

### Versão Mobile (9:16)

```
[PROMPT ADAPTADO PARA VERTICAL]

Subject: [Mesma cena adaptada para formato vertical]

Composition: [Ajustes para formato retrato - foco central]

[Demais campos iguais...]

Technical Specs:
- Aspect Ratio: 9:16
- Resolution: 1080x1920 minimum
```

---

## 2. Feature Illustration 1

**Arquivo:** `feature-[nome]-illustration.png`
**Seção:** Features
**Uso:** Ilustração do feature [Nome]

```
Subject: [Descrição]

Style: [Consistente com identidade visual]

Color Palette: [Usar cores do projeto]

Composition: [Enquadramento]

Technical Specs:
- Aspect Ratio: 1:1
- Resolution: 800x800 minimum
- Background: Transparent (PNG)
```

---

## 3. Feature Illustration 2

**Arquivo:** `feature-[nome]-illustration.png`
**Seção:** Features
**Uso:** Ilustração do feature [Nome]

```
[Mesmo formato anterior]
```

---

## 4. Feature Illustration 3

**Arquivo:** `feature-[nome]-illustration.png`
**Seção:** Features
**Uso:** Ilustração do feature [Nome]

```
[Mesmo formato anterior]
```

---

## 5. Product Screenshot/Mockup

**Arquivo:** `product-mockup.png`
**Seção:** Hero ou Showcase
**Uso:** Mostrar o produto/interface

```
Subject: [Descrição do produto sendo mostrado]

Device: [Laptop / Phone / Tablet / Browser window]

Screen Content: [O que deve aparecer na tela - pode ser placeholder]

Environment: [Contexto ao redor - mesa, fundo limpo, etc.]

Style: [Realista / Clean mockup / Floating]

Angle: [Frontal / Isométrico / Perspectiva]

Technical Specs:
- Aspect Ratio: 16:9 ou 4:3
- Resolution: 1920x1080 minimum
- Shadow: Soft drop shadow
```

---

## 6. Testimonial Avatars

**Arquivos:** `avatar-[nome].png`
**Seção:** Testimonials
**Uso:** Fotos dos clientes

```
Subject: Professional headshot of [descrição da pessoa - gênero, idade aparente, expressão]

Style: Professional portrait photography

Lighting: Soft studio lighting, Rembrandt style

Background: Neutral gradient or solid color matching brand

Expression: Friendly, approachable, confident

Technical Specs:
- Aspect Ratio: 1:1
- Resolution: 400x400 minimum
- Format: PNG or JPG
```

**Avatar 1:** [Descrição específica]
**Avatar 2:** [Descrição específica]
**Avatar 3:** [Descrição específica]

---

## 7. Background Pattern/Texture

**Arquivo:** `bg-pattern.png` ou `bg-texture.png`
**Seção:** [Seção onde será usado]
**Uso:** Background decorativo

```
Subject: [Tipo de padrão - geométrico, orgânico, abstrato]

Style: [Subtle / Bold / Minimalist]

Color Palette: [Usar tons sutis da paleta do projeto]

Opacity suggestion: [20% / 30% / 50%]

Technical Specs:
- Tileable: Yes (seamless repeat)
- Resolution: 500x500 minimum
- Format: PNG with transparency
```

---

## 8. Icon Set Custom (se necessário)

**Arquivos:** `icon-[nome].svg`
**Seção:** Features / Benefits
**Uso:** Ícones customizados

```
Style: [Line art / Filled / Duotone]

Stroke Width: [2px consistent]

Color: Single color (will be colored via CSS)

Theme: [Descrição do tema dos ícones]

Icons needed:
1. [Nome do ícone] - [Descrição visual]
2. [Nome do ícone] - [Descrição visual]
3. [Nome do ícone] - [Descrição visual]

Technical Specs:
- Size: 24x24 base
- Format: SVG
- Viewbox: 0 0 24 24
```

---

## 9. CTA Section Background

**Arquivo:** `cta-bg.png`
**Seção:** CTA Final
**Uso:** Background da seção de call-to-action

```
Subject: [Gradiente abstrato / Padrão decorativo / Imagem temática]

Style: [Consistente com marca]

Color Palette: [Cores vibrantes da marca para destacar]

Mood: [Energético / Inspirador / Urgente]

Technical Specs:
- Aspect Ratio: 21:9 (ultrawide)
- Resolution: 2560x1080 minimum
- Format: JPG (for solid backgrounds) or PNG
```

---

## 10. Logo Placeholder (se necessário)

**Arquivo:** `logo-placeholder-[numero].png`
**Seção:** Logo Bar / Social Proof
**Uso:** Logos de clientes/parceiros

```
Style: Grayscale, minimalist company logo style

Dimensions: Horizontal, varying widths

Technical Specs:
- Height: 40px consistent
- Format: PNG with transparency
- Color: Single gray (#9CA3AF)
```

---

## Checklist de Imagens

- [ ] Hero principal (desktop)
- [ ] Hero principal (mobile)
- [ ] Feature illustrations (quantidade: ___)
- [ ] Product mockup
- [ ] Testimonial avatars (quantidade: ___)
- [ ] Background patterns
- [ ] Custom icons (se necessário)
- [ ] CTA background
- [ ] Logo placeholders (se necessário)

---

## Notas de Produção

### Consistência Visual
- Todas imagens devem usar a paleta de cores definida
- Manter estilo consistente (fotográfico OU ilustração, não misturar)
- Iluminação similar em todas as fotos

### Otimização
- Comprimir imagens antes de usar (TinyPNG, Squoosh)
- Usar WebP como formato principal (com fallback PNG/JPG)
- Implementar lazy loading para imagens abaixo do fold

### Responsividade
- Preparar versões diferentes para mobile quando necessário
- Usar srcset para servir tamanhos apropriados
- Art direction para crops diferentes por breakpoint
