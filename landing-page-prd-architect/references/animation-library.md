# Animation Library

## Bibliotecas Recomendadas

| Biblioteca | Uso | Framework |
|------------|-----|-----------|
| Framer Motion | Animações React | React/Next.js |
| GSAP | Animações avançadas | Qualquer |
| AOS | Scroll animations | Qualquer |
| Lottie | Animações vetoriais | Qualquer |
| Three.js | 3D | Qualquer |
| Particles.js | Partículas | Qualquer |

## Animações por Contexto

### Hero Section

**Entrada de elementos:**
```
- fadeInUp: Texto principal (delay: 0)
- fadeInUp: Subtítulo (delay: 0.2s)
- fadeInUp: CTAs (delay: 0.4s)
- fadeIn: Imagem/visual (delay: 0.3s)
- scaleIn: Badges/decorativos (delay: 0.5s)
```

**Background:**
```
- Gradient animation: Cores sutilmente transitando
- Particles: Pontos flutuantes lentos
- Blob animation: Shapes orgânicos movendo
- Parallax: Camadas com velocidades diferentes
```

### Cards/Features

**Entrada:**
```
- staggerFadeInUp: Cards aparecem em sequência
  - stagger: 0.1s entre cada
  - duration: 0.5s
```

**Hover:**
```
- translateY(-8px): Elevação sutil
- scale(1.02): Leve aumento
- shadow increase: Sombra mais profunda
- border-color change: Destaque de borda
```

### Scroll Animations

**Reveal on scroll:**
```
- fadeInUp: Padrão para texto
- fadeInLeft/Right: Elementos laterais
- scaleIn: Imagens/cards
- clipPath reveal: Efeito de cortina
```

**Parallax:**
```
- Velocidade 0.5x: Elementos de fundo
- Velocidade 1x: Conteúdo principal
- Velocidade 1.2x: Elementos decorativos
```

### Botões/CTAs

**Hover states:**
```
- scale(1.05): Leve aumento
- translateY(-2px): Micro-elevação
- background-position: Gradiente animado
- box-shadow expand: Glow effect
```

**Click/Active:**
```
- scale(0.98): Feedback de pressão
- brightness(0.95): Escurecimento sutil
```

### Textos

**Efeitos especiais:**
```
- Typing effect: Texto sendo digitado
- Split text: Letras/palavras animam individualmente
- Gradient text animation: Cores transitando
- Counter: Números incrementando
```

### Transições de Página/Seção

```
- Fade: Transição suave entre seções
- Slide: Deslizar horizontal/vertical
- Scale: Zoom in/out
- Clip-path: Formas revelando conteúdo
```

## Timing & Easing

**Durations:**
```
- Micro-interactions: 150-200ms
- UI elements: 200-300ms
- Page transitions: 400-600ms
- Complex animations: 600-1000ms
```

**Easing functions:**
```
- ease-out: Elementos entrando (desacelera no final)
- ease-in-out: Elementos transitando
- cubic-bezier(0.16, 1, 0.3, 1): Spring-like (bounce sutil)
- cubic-bezier(0.22, 1, 0.36, 1): Smooth deceleration
```

## Performance

**Boas práticas:**
```
- Usar transform e opacity (GPU accelerated)
- Evitar animar width/height/top/left
- will-change em elementos que animam frequentemente
- Lazy load de animações abaixo do fold
- Respeitar prefers-reduced-motion
```

**Código exemplo (CSS):**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Níveis de Intensidade

**Sutil:**
- Apenas fade e translate básicos
- Durations curtas (200-300ms)
- Sem partículas ou 3D

**Moderado:**
- Stagger animations
- Hover effects em cards
- Scroll reveal
- Background gradiente animado

**Impactante:**
- Partículas/Three.js
- Parallax complexo
- Animações de texto elaboradas
- Transições de página completas
- Micro-interactions em tudo
