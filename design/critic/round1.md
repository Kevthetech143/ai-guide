# ROUND 1 — does it do the job at all (2026-09-11)
Reviewer: brutal design critic (senior product designer, consumer, phone-first).
Method: read the CSS, the design spec, and built home /start/ a provider page on the Mac. No browser rendering — both suspected bugs were confirmed by tracing layout math, not screenshots.

## SCORE: 5/10
Why not higher: the numbered category index is broken at *every* width (arrow under the row number, hint in the wrong column) — a non-technical phone user reads that as "this site is broken." The /start/ cards have a sibling bug, and the hero promises a 3-question quiz the site doesn't deliver. 5 not 3: the prose is genuinely plain-language, the chip → lede → facts → "Heads up" → links card anatomy fits this audience, contrast is AA, tap targets are 44px+, and the trust microcopy ("Last checked", "no jargon without an explanation") is the right instinct.

## TOP 5 FAILURES

**1. Tile grid has 4 children in a 3-column grid — arrow wraps under the row number (suspected bug (a), CONFIRMED, all widths).**
`static/style.css`:
```css
.tile { display: grid; grid-template-columns: 3rem 1fr auto; ... }
```
Children are `::before` (number), `.tile-name`, `.tile-hint`, `::after` (arrow) — four grid items, three explicit columns. Auto-placement: number→row1col1, name→row1col2, hint→row1**col3**, arrow→row2col1. The hint lands to the *right* of the name; the arrow drops onto its own line under the row number. Fix with explicit placement (replaces nothing else):
```css
.tile::before { grid-column: 1; grid-row: 1 / span 2; }
.tile-name    { grid-column: 2; grid-row: 1; }
.tile-hint    { grid-column: 2; grid-row: 2; }
.tile::after  { grid-column: 3; grid-row: 1 / span 2; white-space: nowrap; }
```


**2. /start/ cards: hint is a third flex item, label wraps (suspected bug (b), CONFIRMED — and worse than reported).**
`dist/start/index.html`: `<a class="biglink" href="chat/">Chat AIs<span class="hint">ask questions, write things</span></a>` with `.biglink { display: flex; justify-content: space-between; }`. The label (anonymous flex item), the hint span, and the `::after` arrow are three *side-by-side* flex items: the hint renders beside the label, and at 390px the label shrinks and "Chat AIs" wraps across two lines.
```html
<a class="biglink" href="chat/"><span class="biglink-label">Chat AIs<span class="hint">ask questions, write things</span></span></a>
```
CSS: `.biglink-label { flex: 1 1 auto; } .biglink::after { flex: 0 0 auto; }`. Also rename the label "Agents AIs" → "Task helpers".

**3. The hero promises a 3-question quiz that doesn't exist.**
Home hero card: "Start here: answer 3 quick questions" + "then a short list that fits." But /start/ is three independent link lists, not a narrowing quiz — there is no path from "Chat" + "Free" to the combined `dist/start/chat-free/` page the build actually generates. Q3 ("Runs on my computer?") offers one lonely option with no "either is fine." An anxious user reads a broken promise as a trick. Fix the copy:
- Hero card → `<strong>Start here: pick what you want to do</strong><span class="hint">Chat, pictures, video, music — then filter by free or paid for a short plain-language list.</span>`
- /start/ subtitle → "Tap what you want to do first — then narrow by free or paid." Add an explicit "No preference — show everything" link so nobody feels cornered.

**4. "Closed" chip is unexplained jargon; "Free" badge contradicts "Price: $20/month".**
`dist/p/chatgpt.html`: `<span class="badge badge-free">Free</span>` … `<div><span class="k">Price:</span> $20/month</div>`. Is it free or $20? Fix the facts row to `<div><span class="k">Price:</span> Free to try, $20/month for Plus</div>`. And "Open"/"Closed" mean nothing to this audience — the spec's own rule is "no jargon without an explanation." Rename to "Open source"/"Company-made" or add a one-line legend above the first card: "Open source = anyone can download and inspect it. Company-made = a company runs it for you."

**5. No site navigation anywhere.**
Home has zero header links; subpages have only a breadcrumb. Once a phone user scrolls past the hero, "Start here" is gone. Fix: put the start link in the header on every page, inside `.sitehead-inner` after the brand:
```html
<nav class="topnav" aria-label="Site"><a href="start/index.html">Start here</a></nav>
```
(adjust relative depth per page).

## MISSING
- **About / who makes this.** This audience is deciding whether to trust AI buying advice from a stranger: add a one-page "How this guide works" (a human writes it, how providers get checked, no ads or affiliate links), linked from the footer.
- **A safety net for the remaining jargon.** "Open source", "agents", "runs on your computer" need inline `(= …)` explanations or one tiny glossary page.
- **"Show me everything" escape hatches on /start/.** Q2 has Free/Paid, Q3 has one option; an unsure user needs explicit "No preference" links so the quiz never feels like a trap.
- **Visible freshness on category pages.** Scanners need a page-level line like "Prices and plans checked September 2026" under the h1.

## CUT LIST
- The full "All providers" card stack on home: a duplicate of every card that turns the page into an endless scroll. Home should end at "Popular questions"; cards live on category pages.
- The stray space in `<span class="badge ">` — normalize badge classes in build.py.
- Trim "Popular questions" from 12 to the 6 most-asked. Twelve identical tappable rows is a wall, not a guide.

## ONE-LINE VERDICT
Good editorial instincts, broken execution: the tile-grid and /start/ layout bugs plus a quiz promise the site doesn't keep make it feel untrustworthy — fix the grid and the cards first, everything else is polish.
