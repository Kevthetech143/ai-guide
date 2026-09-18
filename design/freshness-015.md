# Freshness stamp (ai-guide-015)

Stamp date: 2026-09-18.

## What changed
- `build.py`: BUILD_DATE = 2026-09-18. `LAST_FULL_REVIEW` = newest `last_checked`
  across all 60 providers (data-only, never claims "checked today").
  A card is overdue when `last_checked` is 7+ days before BUILD_DATE.
- Home, category, all, start-here (picker + filtered lists) and every question
  page now print one line directly under the h1:
  `Last full review: 2026-09-14` (8th-grade plain words).
- Card template and provider page: overdue items show a visible line
  `Needs a new check`, and the existing `Last checked DATE` line is kept.
- `static/style.css`: `.review-stamp` and `.stale` styles with real contrast
  (ink text, amber-bordered box for stale), plus a phone media query.

## Overdue provider ids (last_checked 2026-09-11, 7 days before 2026-09-18)
- gemini
- playht
- kimi

(57 providers at 2026-09-14 are current.)

## Files touched (each backed up as <name>.bak-20260918-fresh)
- build.py
- templates/card.html
- templates/provider.html
- static/style.css

## Acceptance (run on the Mac)
- `python3 build.py` exit 0 (60 providers, 8 categories, 31 start pages, 36 question pages)
- `python3 linkcheck.py` 0 broken (136 pages, 2517 internal links)
- dist/index.html contains "Last full review: 2026-09-14"
- "Needs a new check" present on overdue cards (gemini, playht, kimi)
- 60 provider pages still present
