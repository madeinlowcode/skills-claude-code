# Aspect Ratio Guide for Hero Sections

## Desktop Ratios

### 16:9 (Standard Widescreen)
**Resolution:** 1920x1080 (Full HD), 3840x2160 (4K)
**Use case:** Standard desktop hero sections, most common
**Composition:** Horizontal spread, product can be left/center/right with supporting elements across width
**Keywords:** `16:9 aspect ratio`, `widescreen composition`, `horizontal format`

### 21:9 (Ultrawide/Cinematic)
**Resolution:** 2560x1080, 3440x1440
**Use case:** Premium immersive heroes, cinematic feel
**Composition:** Extra horizontal space for environmental storytelling, product typically centered with expansive surroundings
**Keywords:** `21:9 ultrawide ratio`, `cinematic aspect ratio`, `panoramic composition`

### 3:2 (Classic Photo)
**Resolution:** 1920x1280, 2400x1600
**Use case:** Photo-forward heroes, slightly more vertical than 16:9
**Composition:** Balanced, works well for product + minimal environment
**Keywords:** `3:2 classic ratio`, `photographic aspect ratio`

---

## Mobile Ratios

### 9:16 (Vertical Full Screen)
**Resolution:** 1080x1920 (Full HD), 1440x2560 (2K)
**Use case:** Full-screen mobile heroes, Stories-style presentations
**Composition:** Vertical stacking, product center with elements above/below
**Keywords:** `9:16 vertical ratio`, `portrait full-screen`, `mobile-first composition`

### 4:5 (Instagram Portrait)
**Resolution:** 1080x1350
**Use case:** Social-optimized heroes, slightly less tall than 9:16
**Composition:** Tall but not extreme, good balance of vertical and horizontal space
**Keywords:** `4:5 portrait ratio`, `social media optimized`, `Instagram-style composition`

### 1:1 (Square)
**Resolution:** 1080x1080, 1200x1200
**Use case:** Versatile, works on mobile and desktop, social media friendly
**Composition:** Centered product, symmetrical arrangements work well
**Keywords:** `square 1:1 ratio`, `equal dimensions`, `centered composition`

---

## Composition Adaptation Guidelines

### Converting 16:9 (Desktop) to 9:16 (Mobile)

**Horizontal to Vertical Translation:**

| Desktop (16:9) | Mobile (9:16) |
|----------------|---------------|
| Product left, elements spread right | Product center, elements above/below |
| Horizontal splash/explosion | Vertical pour/rise/fall |
| Wide environmental context | Tight crop, vertical depth layers |
| Side-by-side ingredient arrangement | Stacked ingredient arrangement |
| Horizontal motion (track) | Vertical motion (rise/fall) |

**Example Adaptation:**

Desktop (16:9):
```
Left third: floating ingredients
Center: product bottle with splash
Right third: more ingredients, brand elements
Composition: horizontal energy flow left-to-right
```

Mobile (9:16):
```
Top third: floating ingredients descending
Center: product bottle with splash
Bottom third: base ingredients, grounding elements
Composition: vertical energy flow top-to-bottom
```

### Key Principles for Adaptation

1. **Maintain product prominence** - Product should be equally visible in both
2. **Rebalance supporting elements** - Spread horizontally → Stack vertically
3. **Adjust motion direction** - Horizontal movements → Vertical movements
4. **Consider thumb zone** - Mobile CTAs often bottom third
5. **Text overlay space** - Both need room for headlines/copy

---

## Resolution Recommendations

### For Image Generation

| Use Case | Desktop | Mobile |
|----------|---------|--------|
| Standard quality | 1920x1080 | 1080x1920 |
| High quality | 2560x1440 | 1440x2560 |
| Print/Maximum | 3840x2160 | 2160x3840 |

### For Video Generation

| Use Case | Desktop | Mobile |
|----------|---------|--------|
| Web optimized | 1920x1080 | 1080x1920 |
| High quality | 2560x1440 | 1440x2560 |
| Future-proof | 3840x2160 | 2160x3840 |

---

## Prompt Ratio Specifications

### For Image Prompts
```
Aspect Ratio: 16:9 (Desktop)
```
```
Aspect Ratio: 9:16 (Mobile)
```
```
Aspect Ratio: 21:9 (Ultrawide Desktop)
```
```
Aspect Ratio: 4:5 (Mobile Portrait)
```

### For Video Prompts
```
Aspect Ratio: 16:9 (1920x1080)
```
```
Aspect Ratio: 9:16 (1080x1920)
```
```
Aspect Ratio: 21:9 (2560x1080)
```
```
Aspect Ratio: 4:5 (1080x1350)
```

---

## Tool-Specific Ratio Support

### Image Tools
| Tool | Supported Ratios |
|------|------------------|
| Midjourney | 16:9, 9:16, 4:5, 1:1, 21:9, custom |
| DALL-E 3 | 16:9, 9:16, 1:1 |
| Nano Banana | 16:9, 9:16, 4:5, 1:1 |

### Video Tools
| Tool | Supported Ratios |
|------|------------------|
| Runway ML | 16:9, 9:16, 1:1 |
| Pika Labs | 16:9, 9:16, 1:1 |
| Google Veo | 16:9, 9:16 |
| FreePik AI | 16:9, 9:16, 4:5, 1:1 |

---

## Responsive Design Considerations

### Both Versions Needed When:
- Building responsive landing page (different hero per breakpoint)
- A/B testing desktop vs mobile experiences
- Social media repurposing planned
- Maximum engagement across devices required

### Single Version Acceptable When:
- Fixed single-platform deployment
- Specific campaign with known audience device
- Quick prototype/concept phase
- Budget constraints require single version
