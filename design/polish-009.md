# Polish pass 009 — ai-guide-009 (impeccable-design-polish)

Decisive fixes only; layout and copy intent unchanged.

## Changes (all in static/style.css)

1. **Empty state (edge state):** filtered start/ lists with zero providers
   (`start/chat-paid/`, `start/music-paid/`, `start/search-paid/` — verified
   empty in data) previously rendered just the legend and whitespace. Added
   `main > .legend:last-child::after` empty-state block: the legend is the
   last element in main only when no cards were built, so it fires
   exclusively on empty lists. CSS-only because build.py is frozen for this
   task.
2. **Long-name edge state:** added `overflow-wrap: break-word` to
   `.card h2` and `.provider-head h1` so long provider names wrap instead of
   overflowing on narrow screens.
3. **Spacing scale:** `.card-links` margin normalized from the asymmetric
   `0.9rem 0 0.25rem` to `1rem 0 0.5rem` to match the card's 1rem rhythm.

## Checked, left alone

- Typography rhythm: h1/h2 scale, kicker, lede, card type sizes already
  consistent; `text-wrap: balance` on headings; no widows found in dist copy.
- Spacing scale: section/card/biglink margins use 0.75/1/1.25/1.5/2/2.5rem
  steps; no outliers besides item 3 above.
- Empty strings in data: no empty `good_for`/`watch_out`/names found in
  providers.json (60 entries).
- No AI tells introduced: no gradients, no new card grids, no decorative
  effects.
