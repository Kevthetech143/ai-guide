# ROUND 5 — adversarial non-technical user: a 60-year-old on a phone (2026-09-11)
Reviewer: brutal design critic playing a 60-year-old first-time visitor.
Method: real click-throughs in Chromium on the Mac (playwright, 390px) plus a
jargon grep over all built copy. Round 4 scored 8/10.

## THE TEST: "free AI to make a picture" in under 3 taps
- **Path A — popular question (1 tap, PASS).** Home → tap "What's a good free
  AI image generator?" → question page with 7 cards, every one wearing a
  green "Free" badge. One tap. She is done.
- **Path B — the guided flow (3 taps, PASS with a caveat).** Home → "Start
  here: pick what you want to do" (1) → "Image — make pictures from words"
  (2) → "Free ones — costs nothing to try" (3) → /start/image-free/ with 6
  free image AIs. Three taps, not under three — but every step labels itself
  in her words ("make pictures from words", "costs nothing to try"), so she
  never feels lost. The strict "<3 taps" bar is met by paths A and C; path B
  is one tap over and reads clearly.
- **Path C — the home tile (1 tap + scan, PASS).** Home → "Image" tile (1) →
  /image/ category page. Round-4's free-first ordering means the first card
  she sees is Adobe Firefly with a green "Free" badge, and the legend above
  now defines "Free — you can use the main features without paying." She does
  not need to scroll past paid options. One tap plus a glance.

## JARGON AUDIT (what she reads)
Swept all 111 built pages for: LLM, large language model, diffusion,
prompt engineering, freemium, token, SaaS, API key, fine-tune, open weights.
Found exactly one offender in visible copy — and it was on the fact row she
cares about most:
- **Flux's price row read "Free (open weights); usage-based API pricing."**
  A 60-year-old asking "is it free?" got developer jargon on the one row
  that answers her question. Fixed in build.py `price_line()` (template-side
  scrub, data untouched): now reads **"Free; pay-per-use options."** Verified
  on dist/p/flux.html and 11 card instances.
- "Chatbot" (one question title) and "open-source" (defined inline in the
  legend) are mainstream enough to keep. "AIs" as a noun is the site's own
  vocabulary and is defined by context everywhere it appears.

## WHAT STILL SOUNDS TECHNICAL (out of scope, noted for data work)
- Provider blurbs come from data/ (untouchable this round) and a few still
  lean technical ("trained on licensed content" is fine; a couple of watch-out
  lines mention "API" in data copy). A future data pass could plain-language
  the watch-out fields.
- Category ledes ("AIs you talk to") are template-adjacent via CATEGORY_BLURBS
  in build.py — plain enough to ship.

## SCORE JUSTIFICATION
Path A and C hit the bar at 1 tap; path B is 3 clear taps. The one piece of
jargon on the money question is gone. Nothing in the flow asks her to know a
technical word to proceed.

## ONE-LINE VERDICT
She finds a free picture-maker in one tap two different ways, and the price
rows finally speak her language. The site is shippable for its audience.

FINAL SCORE: 9/10
