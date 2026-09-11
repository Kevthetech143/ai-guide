# DESIGN-READ.md — ai-guide redesign (2026-09-11, ai-guide-006a)

**Design Read:** "Reading this as: a consumer field-guide site for non-technical adults on phones, anxious about AI jargon, with a warm, calm, human editorial language, leaning toward native CSS + print-inspired editorial typography + restrained warmth."

## The three dials (design-taste-frontend §1)
- `DESIGN_VARIANCE: 5` — calm asymmetry: left-aligned editorial flow, numbered category index, varied card rhythm. Not a card-grid-of-sameness, not chaos.
- `MOTION_INTENSITY: 2` — near-static. Hover lift + color shifts only; zero animation that moves content. Works fully with JS off (no JS shipped).
- `VISUAL_DENSITY: 3` — airy. One idea per screen region; generous whitespace; max line length ~62ch.

## Palette (all pairs WCAG AA)
| Token | Value | Use |
|---|---|---|
| `--paper` | `#FBFAF6` | page background (warm, not beige-luxury) |
| `--card` | `#FFFFFF` | provider cards |
| `--ink` | `#1C1A17` | body text (on paper ≈ 14:1) |
| `--muted` | `#5F5A54` | secondary text (on paper ≈ 5.2:1) |
| `--line` | `#E6E0D4` | hairlines, card borders |
| `--teal` | `#0E6B5C` | brand accent: header rule, active states, key buttons (on paper ≈ 5.6:1; white on teal ≈ 5.4:1) |
| `--link` | `#0B4FD6` | links (on paper ≈ 8:1) |
| `--amber` | `#B45309` | sparing highlight: "watch out" flag, kicker accents (on paper ≈ 4.6:1) |
| `--free-bg`/`--free-ink` | `#E3F2E8` / `#166534` | "Free" chip |
| `--paid-bg`/`--paid-ink` | `#FBEEDF` / `#9A3412` | "Paid" chip |
| `--open-bg`/`--open-ink` | `#E4EEFB` / `#1D4E9E` | "Open" chip |

## Type scale
- Display (home h1): `clamp(2.5rem, 9vw, 3.75rem)`, weight 800, letter-spacing -0.02em, line-height 1.05
- Page h1: 2rem / 1.15; Section h2: 1.375rem / 1.25; Body: 1.125rem / 1.7; Small: 0.95rem
- Stack: `ui-rounded, "SF Pro Rounded", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` — friendly rounded grotesque where available, clean fallback elsewhere. No webfonts, no external requests (constraint).
- Never: serif-by-default prestige voice, all-caps shouting, centered hero blobs.

## Spacing
- Base unit 0.25rem; section rhythm 3rem desktop / 2rem mobile; content column max 44rem (readable, phone-first); card padding 1.25rem; 8px radius cards, 999px chips.

## Components
- **Site header:** brand wordmark "AI Guide" + human tagline "plain answers for real people"; thin teal rule beneath. No logo image.
- **Hero (home):** kicker line ("A plain-language guide"), huge left-aligned question, one-sentence lede, featured "Start here" card with 3-question promise. No centered mesh gradient.
- **Category index:** numbered editorial list (01 Chat — ask questions, write things →), hairline separators, not a tile grid. 44px+ tap rows.
- **Provider card:** name + plain-language chips (Free/Paid, Easy/Medium/Hard, Open/Closed, Runs on your computer) → one-sentence "good for" lede → facts row (price, difficulty) → official-site + details links → "Last checked" microcopy.
- **Question links:** large tappable rows with arrow affordance.
- **Footer:** quiet colophon line, hairline top border.

## Do / Don't
- DO: one accent (teal) used with intent; left-aligned type; real hierarchy; generous touch targets; `:focus-visible` rings everywhere; `prefers-reduced-motion` respected (nothing moves anyway).
- DON'T: AI-purple gradients, glassmorphism, emoji, beige/brass luxury cues, three-equal-cards grids, centered hero, Inter+slate defaults, external fonts/CDN/JS, touching `data/` or URLs/routes.
