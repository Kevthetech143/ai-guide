# Breadth batch 7 — ai-guide-016g (DATA ONLY)

Date: 2026-09-30. Focus: music (thinnest at 16 cards), search (18), then code (19).
Open-weights/local-run tools favoured. Every fact below was read from the
provider's own site with a browser User-Agent and redirects followed.

## Verified survivors: 7

| id | name | price_from (plan table) | free_tier |
|---|---|---|---|
| brainfm | Brain.fm | $14.99/month (Monthly plan, billed monthly) | no — free trial only |
| ecrett-music | Ecrett Music | $7.99/month (Individual Plan, monthly billing) | yes — $0.00 plan |
| fadr | Fadr | $10/month (Fadr Plus; $100/yr annual option) | yes — Fadr Basic free for life |
| onyx | Onyx | $20 per user/month (billed annually) — Business plan | no — free trial only |
| cline | Cline | Free for individuals (usage-based AI inference credits) | yes |
| openhands | OpenHands | Free to run yourself (paid cloud offered, price not on site) | yes — Local Open Source |
| komo | Komo | Free ($0 forever plan; paid credit plans exist, prices not on page) | yes — $0 forever |

Category spread: music 3, search 2, code 2 (openhands also tagged agents).
open_weights is false on all 7 — none publish downloadable model weights
(open-source software alone does not count, per the brief's rule 12).

## Dropped candidates (11), with reasons

- **phind** — phind.com returns 404 on / and /search; the whole site is down.
  Rule 3 (site must be alive right now). Dropped.
- **riffusion** — riffusion.com now 301-redirects to www.flowmusic.app, which is
  Flow Music — already carded as `flow-music`. Keeping it would duplicate a
  card. Dropped (rule 2: we store where the browser ends).
- **moises** — studio.moises.ai/billing/pricing/ is a JS app shell; zero $ figures
  in the static HTML. Price unverifiable. Dropped (rule 4).
- **wavtool** — homepage reads as a coming-soon/waitlist relaunch notice
  ("it will be worth the wait… more to announce"), no pricing anywhere, not
  taking new users. Dropped (rules 4, 11).
- **pearai** — trypear.ai/pricing shows only a "20-30% off (forever)" promo
  framing; no standing list $ figures in the static HTML. Dropped (rules 4, 10).
- **cody** — sourcegraph.com/cody redirects to the docs site; sourcegraph.com/pricing
  shows only enterprise ("Starting at $16K minimum annual contract") — no Cody
  Pro plan table with $ figures in static HTML. Dropped (rule 4).
- **glean** — glean.com/pricing redirects back to the homepage; no public per-seat
  price anywhere on the site. Dropped (rule 4).
- **jina** — jina.ai/pricing 404s; no pricing figures on the homepage. Dropped (rule 4).
- **khoj** — khoj.dev homepage is marketing only; no cloud/self-host pricing figures
  on the page. Dropped (rule 4).
- **endel** — subscription is sold through the mobile/desktop apps; no web plan table
  with $ figures exists on endel.io. Dropped (rule 4).
- **jetbrains-ai** — jetbrains.com/ai/pricing/ 404s; no JetBrains AI $ figures on the
  /ai page. Dropped (rule 4).

## Pricing pages that were unclear (kept, with disclosure in the card)

- **komo.ai/pricing** — plan table renders the Free $0 plan in static HTML, but paid
  credit-tier prices are JS-only. Card prices the verified $0 plan and discloses the
  paid tiers.
- **openhands.dev/pricing** — "Local Open Source Free" is in the static plan table;
  the paid cloud plan has no listed price on the page. Card discloses this.
- **onyx.app/pricing** — shows "$20 per user / month" immediately followed by
  "Annual Billing"; no monthly-billing figure shown, so recorded as billed annually
  (rule 14). No seat minimum found ("for teams of any size").

## Rule-compliance notes

- Rule 5 (strip `<!-- -->`): applied to every page read; React-split prices (e.g.
  `$<!-- -->16` patterns) were rejoined before reading.
- Rule 9 ("Free" means the vendor sells nothing): cline, openhands, and komo all sell
  a paid component, so none is listed as a bare "Free" — each names the paid part.
- Rule 10: fadr's "50% Off" promo banners ignored; the $10/mo standing list price used.
- Rule 14: ecrett's $7.99 is the true monthly-billing rate (the $4.99 rate is annual-only
  and is disclosed); onyx's $20 is annual-only and marked "(billed annually)".
- Rule 15: "Fadr" and "Komo" have no separate legal entity on their footers — the brand
  name is used and this is disclosed in their `watch_out` fields (observed, not guessed).
- Nothing was tested; no history/ownership claims are made anywhere in the cards.

## Validation

The brief's validation script was run on the Mac after landing both files; its real
output is pasted in the task close (RESULT_SENT). No files were touched except the two
deliverables below.
