# Icon Libraries

## Bibliotecas Recomendadas

| Biblioteca | Estilo | URL |
|------------|--------|-----|
| Lucide | Clean, consistente | https://lucide.dev/ |
| Phosphor | Versátil, 6 weights | https://phosphoricons.com/ |
| Heroicons | Tailwind oficial | https://heroicons.com/ |
| Tabler Icons | 4000+ ícones | https://tabler-icons.io/ |
| Feather Icons | Minimalista | https://feathericons.com/ |
| Radix Icons | UI components | https://icons.radix-ui.com/ |

## Quando Usar Cada Uma

### Lucide Icons
- **Melhor para:** Projetos React/Next.js modernos
- **Estilo:** Outline clean, 24x24 base
- **Instalação:** `npm install lucide-react`
```jsx
import { ArrowRight, Check, Star } from 'lucide-react'
```

### Phosphor Icons
- **Melhor para:** Projetos que precisam de múltiplos weights
- **Estilos:** Thin, Light, Regular, Bold, Fill, Duotone
- **Instalação:** `npm install @phosphor-icons/react`
```jsx
import { ArrowRight, Check } from '@phosphor-icons/react'
<ArrowRight weight="bold" />
```

### Heroicons
- **Melhor para:** Projetos Tailwind CSS
- **Estilos:** Outline (24x24), Solid (24x24), Mini (20x20)
- **Instalação:** `npm install @heroicons/react`
```jsx
import { ArrowRightIcon } from '@heroicons/react/24/outline'
import { ArrowRightIcon } from '@heroicons/react/24/solid'
```

### Tabler Icons
- **Melhor para:** Grande variedade de ícones
- **Estilo:** Stroke-based, customizável
- **Instalação:** `npm install @tabler/icons-react`
```jsx
import { IconArrowRight } from '@tabler/icons-react'
```

## Estilos de Ícones

### Outline
- Linhas finas, elegante
- Ideal para: UI clean, minimalismo
- Usar em: Navegação, features, listas

### Solid/Fill
- Preenchido, mais impacto visual
- Ideal para: Ações, destaques, estados ativos
- Usar em: CTAs, badges, indicadores

### Duotone
- Duas cores, profundidade
- Ideal para: Features, ilustrações
- Usar em: Cards, seções de destaque

## Tamanhos Padrão

```
Small: 16px (textos inline, badges)
Default: 20px (UI geral)
Medium: 24px (cards, features)
Large: 32px (destaques)
XLarge: 48px+ (ilustrações, hero)
```

## Consistência

**Regras para manter consistência:**
1. Usar apenas UMA biblioteca por projeto
2. Manter mesmo estilo (outline OU solid, não misturar)
3. Usar stroke-width consistente
4. Definir tamanhos padrão no design system

## Ícones Comuns por Contexto

### Navigation
```
Menu: Menu, MenuIcon
Close: X, XIcon
Back: ArrowLeft, ChevronLeft
Search: Search, MagnifyingGlass
```

### Actions
```
Add: Plus, PlusCircle
Edit: Pencil, Edit
Delete: Trash, Trash2
Save: Save, Check
Download: Download, ArrowDown
Share: Share, Share2
```

### Features/Benefits
```
Check: Check, CheckCircle
Star: Star, StarFilled
Shield: Shield, ShieldCheck
Zap: Zap, Lightning
Clock: Clock, Timer
Users: Users, UsersThree
```

### Social
```
GitHub: Github
Twitter/X: Twitter
LinkedIn: Linkedin
Instagram: Instagram
YouTube: Youtube
```

### Contact
```
Email: Mail, Envelope
Phone: Phone, Telephone
Location: MapPin, Map
Calendar: Calendar
```

## Cores de Ícones

```
Primary: Cor principal da marca (CTAs, destaques)
Muted: text-muted/gray-500 (navegação, labels)
Success: green-500 (checks, confirmações)
Warning: yellow-500 (alertas)
Error: red-500 (erros, delete)
```

## Exemplo de Configuração

```tsx
// icon-config.ts
export const iconConfig = {
  library: 'lucide-react',
  defaultSize: 20,
  defaultStrokeWidth: 2,
  sizes: {
    sm: 16,
    md: 20,
    lg: 24,
    xl: 32
  }
}
```
