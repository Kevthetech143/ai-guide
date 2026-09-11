# ROUND 2 — what the round-1 fixes broke (2026-09-11)
Reviewer: brutal design critic (senior product designer, consumer, phone-first).
Method: read static/style.css and built dist/ on the Mac; every claim checked against built HTML, not the fix list. No browser rendering.

## SCORE: 6/10
The two "this site is broken" bugs are genuinely fixed: the tile grid's explicit placement holds at the 34rem breakpoint, and `.biglink-label` keeps the arrow pinned right at narrow widths. Header nav depths check out; the stray badge space is gone. But the fixes repaired the look and broke the truth: one category wears three names, 109 breadcrumbs and two escape hatches point at a list that no longer exists, and the price template writes broken English on 14 cards. A trade.

## WHAT THE LAST ROUND'S FIXES GOT WRONG
**1. "Agents AIs" → "Task helpers".** Renamed on two surfaces only — the /start/ picker card and /start/agents/ h1. Still "Agents": home tile (`<span class="tile-name">Agents</span>`), /agents/ h1, every "Good for" row. And the exact string round 1 ordered killed survives: `<title>Agents AIs - AI Guide</title>`. Fix: one name on all five surfaces or the rename never happened.
**2. Free/$20 contradiction.** Built as a template — `Free tier available; paid plans from {price}` — with no branch for unknown prices. On 14 pages {price} is "Check site": `<div><span class="k">Price:</span> Free tier available; paid plans from Check site</div>`. Fix: unknown price renders "Free to try; check the provider's site for paid plans."
**3. Cut "All providers" from home.** Home now has 0 cards — and 109 pages still breadcrumb `<nav class="topnav"><a href="../index.html">&larr; All AIs</a></nav>` to it. The new escape hatches (`No preference — show everything`, `Either is fine — show everything`) both link to that card-less home. Fix: crumb → "← Home"; build a real everything page or stop promising one.
**4. Quiz-promise copy.** Visible copy fixed — but /start/ still ships `<meta name="description" content="Answer three quick questions and get a short plain-language list of AIs that fit.">` plus identical og:description. Fix: rewrite both tags.
**5. "Open"/"Closed" jargon.** Renamed to "Open source"/"Company-made" — but the only explanation lives on /about/, which claims `<p>If a technical word has to appear, it gets an explanation next to it.` No card explains its chips; false on ~60 cards. Fix: legend above the first card on list pages, as prescribed.
**6. Header nav everywhere.** Correct at all depths — but leaves an empty `<div class="crumbwrap"><div class="sitehead-inner"></div></div>` on home. Fix: skip the crumb wrapper when there is no crumb.

## TOP 5 FAILURES
**1. `<title>Agents AIs - AI Guide</title>` (dist/agents/index.html).** Fix: `<title>Task helpers - AI Guide</title>`, `<h1>Task helpers</h1>`, home tile `<span class="tile-name">Task helpers</span>`, "Good for" rows "Agents" → "Task helpers".
**2. 14 × "paid plans from Check site."** Fix: `<div><span class="k">Price:</span> Free to try; check the provider's site for paid plans</div>` via a template branch for unknown prices.
**3. The escape hatches are false promises.** `<span class="biglink-label">No preference &mdash; show everything<span class="hint">the full list, free and paid</span></span>` links to a home with zero cards. Fix: relabel `Skip this step` / `browse every category on the home page` (same for "Either is fine"), or build the everything page.
**4. 109 × "← All AIs" crumb to a home with no AI list.** `<nav class="topnav"><a href="../index.html">&larr; All AIs</a></nav>`. Fix: `&larr; All AIs` → `&larr; Home` everywhere.
**5. /start/ metadata still promises the quiz** (meta + og:description). Fix both: `content="Pick what you want to do, then narrow by free or paid — a short plain-language list of AIs that fit."`

## SAMENESS RISK
- The picker reads "Chat AIs, Image AIs, Video AIs, Voice AIs, Music AIs, Code AIs, Search AIs, Task helpers." The rename broke the parallel rhythm — the eye snags on the odd one out, while "Search AIs"/"Code AIs" are no plainer than "Agents" was. Plain language on all eight, or the pattern on all eight.
- /chat/, /start/chat/, and /best/&lt;slug&gt;/ now render the identical card stack — same badges, facts, "Heads up", buttons. The spec's DESIGN_VARIANCE dial wants "varied card rhythm"; the pages converged into one repeating unit, distinguishable only by h1.
- The two escape hatches look like a choice and behave as one: different labels, identical destination.

## MISSING
- **A real "everything" destination.** Two escape hatches + 109 breadcrumbs promise a full list; no page carries one. Build it, or delete the language.
- **A chip legend where chips appear.** "Company-made"/"Open source" unexplained on ~60 cards; definitions only on /about/. One line above the first card per list page, or link chips to the definitions.
- **One name for the agents category.** "Agents" (home tile, /agents/ h1, "Good for"), "Agents AIs" (/agents/ title), "Task helpers" (/start/ picker, /start/agents/ h1). Pick one; apply to all five surfaces.
- **An unknown-price branch.** 14 × "paid plans from Check site." Branch the template.

## CUT LIST
- Empty `<div class="crumbwrap"><div class="sitehead-inner"></div></div>` on dist/index.html.
- The "← All AIs" crumb label on all 109 pages → "← Home".
- The stale quiz promise in /start/'s meta + og descriptions.
- The footer self-link "How this guide works" on /about/ itself.

## ONE-LINE VERDICT
The pages stopped looking broken and started lying instead: the grid and cards are fixed, but one category wears three names, 109 breadcrumbs and two escape hatches point at a list that no longer exists, and the price template writes broken English on 14 cards.
