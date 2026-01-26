---
name: hero-visual-prompt-generator
description: |
  Generate premium AI image and video prompts for landing page hero sections.
  Creates cinematic, commercial-quality visual prompts optimized for tools like
  Nano Banana, FreePik AI, Google Veo Flow, Runway ML, and Pika Labs.

  Use when user mentions:
  - "Criar prompt para hero" / "Hero image prompt" / "Hero video prompt"
  - "Prompt para landing page" / "Imagem para hero section"
  - "Video para landing page" / "Visual premium para LP"
  - "Prompt Nano Banana" / "Prompt para FreePik AI" / "Prompt para Veo Flow"
  - "Animar imagem de produto"
  - Any request for premium product visuals for websites

  Supports: Beverages, Food, Technology, Cosmetics, Fashion, Lifestyle products.
  Outputs: Structured prompts in English with desktop (16:9) and mobile (9:16) versions.
---

# Hero Visual Prompt Generator

Generate premium AI prompts for hero section images and videos.

## Workflow

### Phase 1: Information Gathering

**Always ask before generating:**
1. "Qual é o produto/objeto principal da landing page?"
2. "Pode enviar uma imagem de referência do produto?"
3. "Estamos criando para desktop, mobile ou ambos?"
4. "Qual sensação queremos transmitir? (premium, energético, natural, sofisticado)"

**Required inputs:**
- Product type and reference image
- Target platform (Desktop/Mobile/Both)
- Desired style/mood
- Dominant color palette (extract from image or ask)

### Phase 2: Image Prompt Generation

**Structure (always in English):**
```
Subject: [Dynamic product/ingredient description in action]
Composition: [Photography type - macro, commercial, high-speed, etc.]
Key Elements: [Main visual elements - textures, particles, liquids, etc.]
Environment: [Background - monochrome void, gradient, studio, etc.]
Lighting: [Dramatic lighting - backlight, rim light, golden hour, etc.]
Style & Details: [Technical quality - hyper-realistic, 8K, cinematic, etc.]
Aspect Ratio: [Platform-based ratio]
```

**Required technical elements:**
- Hyper-realistic, 8K resolution, Ultra-sharp focus
- Cinematic color grading, Textural detail emphasis
- Professional commercial photography style

**Aspect ratios:**
- Desktop: 16:9 or 21:9
- Mobile: 9:16 or 4:5

### Phase 3: Review and Selection

After user generates images and returns with favorites:
1. Request the generated images they liked most
2. Analyze composition, implied movement, highlighted elements
3. Use selected images as base for video prompts

### Phase 4: Video Prompt Generation

**Structure (always in English):**
```
Sequence: [Sequence type - product assembly, reveal, explosion, etc.]
Visuals:
- Start: [Initial state]
- Middle: [Main transition/action]
- End: [Final composition]
Lighting & Camera: [Light transitions and camera movement]
Style: [Technical quality - 4K, slow motion, commercial videography]
Duration: [Suggested duration - 3-5 seconds for hero]
Aspect Ratio: [Platform-based ratio]
```

**Video aspect ratios:**
- Desktop: 16:9 (1920x1080) or 21:9 (2560x1080)
- Mobile: 9:16 (1080x1920) or 4:5 (1080x1350)

## References

- **Category-specific formulas:** See [references/image-prompt-formulas.md](references/image-prompt-formulas.md)
- **Video patterns:** See [references/video-prompt-formulas.md](references/video-prompt-formulas.md)
- **Lighting techniques:** See [references/lighting-techniques.md](references/lighting-techniques.md)
- **Camera movements:** See [references/camera-movements.md](references/camera-movements.md)
- **Aspect ratio guide:** See [references/aspect-ratios.md](references/aspect-ratios.md)
- **Style keywords:** See [references/style-keywords.md](references/style-keywords.md)

## Output Format

### For Images:
```markdown
## IMAGE PROMPT - [PRODUCT] - [PLATFORM]

### Desktop Version (16:9)
[Complete prompt in English]

### Mobile Version (9:16)
[Adapted prompt for vertical ratio]

---
**Recommended tool:** Nano Banana / Midjourney / DALL-E
**Style keywords:** [keyword list]
**Technical notes:** [generation observations]
```

### For Videos:
```markdown
## VIDEO PROMPT - [PRODUCT] - [PLATFORM]

### Desktop Version (16:9)
[Complete prompt in English]

### Mobile Version (9:16)
[Adapted prompt for vertical ratio]

---
**Compatible tools:** FreePik AI, Google Veo Flow, Runway ML, Pika Labs
**Suggested duration:** [X seconds]
**Main movement:** [movement type]
**Animation notes:** [tips for best results]
```

## Rules

1. **ALWAYS in English** - All prompts for AI tool compatibility
2. **ALWAYS ask platform** - Desktop, Mobile, or Both before generating
3. **ALWAYS request reference image** - To understand product and extract colors
4. **ALWAYS generate dual versions** - When user chooses "Both"
5. **ALWAYS use technical terminology** - 8K, hyper-realistic, cinematic
6. **ALWAYS describe lighting** - Crucial for premium quality
7. **NEVER generate generic prompts** - Each prompt unique to the product

## Validation

Use `scripts/prompt-validator.py` to check prompt completeness:
```bash
python scripts/prompt-validator.py "prompt text" --type image
python scripts/prompt-validator.py "prompt text" --type video
```
