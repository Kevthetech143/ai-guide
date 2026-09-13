# Design audit 009 — ai-guide-009 (web-design-guidelines checklist)

Site: ai-guide static build. Pages audited: home (`dist/index.html`), category
(`dist/chat/index.html`), provider (`dist/p/chatgpt.html`), best/ question
(`dist/best/best-free-ai-chatbot/index.html`), start picker
(`dist/start/index.html`) plus filtered lists (`dist/start/chat-paid/index.html`)
and `/all/` (`dist/all/index.html`).

## Pass (observed, verified against dist/ + templates/ + static/)

- Contrast, WCAG AA: computed ratios all >= 4.5:1 — muted #5F5A54 on
  #FBFAF6 6.53, link #0B4FD6 6.48, teal kicker #0E6B5C 6.14, amber heads-up
  #B45309 4.81, free/paid/open badges 6.16/6.40/6.80, white on teal 6.41,
  teal-deep nav 9.08, body ink 16.62.
- Tap targets >= 44px: site-nav links 44px, tiles 56px, biglinks 56px,
  buttons 44px, jump links 44px, start-card 44px min-height.
- Focus states: global `:focus-visible` 3px teal outline (no bare
  `outline: none` anywhere); skip link visible on keyboard focus.
- Heading order: exactly one h1 per page, then h2s (home, category,
  provider, best/, start/, filtered lists, about).
- Forms: none exist (no inputs, no onPaste, no autocomplete needed).
- Reduced motion: `@media (prefers-reduced-motion: reduce)` kills all
  transitions/animations.
- Layout shift: zero images, no external requests, explicit grid placement;
  no CLS risk.
- Animation hygiene: properties listed explicitly (no `transition: all`),
  transform/opacity only.
- Touch: `touch-action: manipulation` on links.
- Typography: `text-wrap: balance` on h1/h2, tabular-nums on tile counters,
  no `...` (ellipsis char only), no straight quotes in copy data, mdash
  entities used.
- Semantics: skip link to #main, nav aria-labels, `aria-current="page"`,
  article elements for cards, external links use rel="noopener".
- Meta: viewport has no `user-scalable=no` / `maximum-scale`, color-scheme:
  light set, theme-color matches background.

## Fixed (2 items)

1. `static/style.css` — anchors from the `/all/` jump list (`<h2 id="chat">`
   etc.) slammed into the viewport top on jump. Added
   `h2[id] { scroll-margin-top: 1rem; }` per the heading-anchors rule.
2. `static/style.css` — tap highlight was never set intentionally; added
   `-webkit-tap-highlight-color: rgb(14 107 92 / 0.18)` on links (teal,
   matches brand).
