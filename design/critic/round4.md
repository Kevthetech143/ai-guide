# ROUND 4 — would a top consumer-product designer sign it (2026-09-11)
Reviewer: brutal design critic (senior product designer, consumer, phone-first).
Method: rendered in REAL Chromium on the Mac via playwright (viewport 390x844,
device_scale_factor 2, file:// dist) and judged the actual pixels — home, /start/,
/chat/, /image/, /all/, and a provider page. Screenshots in goal hidden_files
(ai-guide-006c-shots/: *-top.png before, *2-top.png after). Round 3 scored 7/10;
all round-3 fixes were verified present in dist before starting.

## SCORE: 8/10
Why 8 and not 7: the felt experience changed, not just the copy. The header went
from a 200px stacked lockup (brand + tagline + nav + rule) to a single 64px row —
the first viewport now shows the hero AND the first two category rows peeking,
which is the oldest phone-conversion trick there is. The dead air between the
"← All AIs" crumb and the content on subpages is gone. One category name now
wears one name on all eight surfaces (round 2's sameness warning, finally closed).
Why not 9: the legend is now an honest but heavy six-definition paragraph, and
the category ledes still say "AIs that…" — "AI" is fine, but the plural noun is
doing branding work, not clarity work. A 9 would need a typographic pass on the
legend and one voice edit across the eight blurbs.

## WHAT THE SCREENSHOTS SHOWED (observed, not inferred)
1. **Header ate the fold.** Before: ~200px of brand/tagline/nav/rule before any
   content; home's first viewport was hero-only, zero category rows visible.
   Fixed: `.sitehead-inner` is now a flex row — "AI Guide" left, "Start here"
   right — ~64px tall. Tagline removed from the header (it repeated the hero
   kicker + lede a third time). After: hero + CTA + "01 Chat / 02 Image" peek
   above the fold. (templates/base.html, static/style.css)
2. **Subpage dead air.** Before: ~150px of nothing between "← All AIs" and the
   kicker. Fixed: `.topnav` padding 0.9→0.5rem, h1 top margin 2→1.25rem, kicker
   2.5→1.5rem, hero paddings tightened. Verified on /chat/ and /image/.
3. **One name per category, finally.** Before: home tiles said "Chat" / "Image"
   but the picker, category h1s, titles, /all/ headings and jump list said
   "Chat AIs" / "Image AIs" — two names for one thing on adjacent pages.
   Fixed: `start_label()` in build.py now returns the plain CATEGORY_NAMES on
   every surface. Verified: /start/ picker reads "Chat, Image, Video, Voice,
   Music…", category h1s read "Chat", "Image". Round 2's sameness warning closed.
4. **Legend heading is honest now.** Before: "Badges, in plain words:" defined 4
   of the 6 worn badge types — Free and Paid, the two a non-technical user
   cares about most, undefined. Fixed: legend defines all six (Free, Paid, Open
   source, Company-made, Runs on your computer, Easy/Medium/Hard).
5. **Category pages were paid-first.** Before: /image/ opened with Midjourney
   (Paid badge) — a free-hunting user scrolled past the paid wall. Fixed:
   free-first ordering (free, then alphabetical) in build.py. After: /image/
   opens with Adobe Firefly (Free), /chat/ with Character AI (Free).

## RHYTHM / HIERARCHY / TAP COMFORT (390px, observed)
- Tap targets: tiles 56px+, biglinks 56px+, buttons 44px+, header nav 44px
  line-height. Comfort is good; no change needed.
- Hierarchy: kicker → h1 → freshness → lede → legend → cards reads clean on
  category pages after the spacing fix. Provider pages: kicker → h1 → badges →
  lede → fact rows — good.
- First-5-seconds clarity: "Which AI should I use?" + "Pick what you want to
  do" + teal Start-here card + category rows peeking = the whole proposition
  is visible without scrolling. This is the round's headline win.

## STILL NOT DESIGNER-GRADE
- The legend is a six-definition wall; a designer would typeset it as two
  compact lines or move Free/Paid into a shorter inline form.
- The teal CTA card duplicates the header "Start here" label on every page —
  acceptable (it is the primary action), but the wording could differ from nav.
- No fold tease on /all/ beyond the jump list; acceptable at 8/10.

## CUT LIST
- The header tagline (removed — triple-repeated the "plain language" claim).
- The "X AIs" naming pattern (removed — one plain name everywhere).

## ONE-LINE VERDICT
The screenshots finally look like a product: one-row header, content in the
first viewport, one name per category, free options first. 8/10 = a designer
would sign the structure and quibble the typography.

FINAL SCORE: 8/10
