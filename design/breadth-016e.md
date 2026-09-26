# Breadth batch 5 (016e) — verification notes

Date: 2026-09-26. Method: curl with a real Chrome User-Agent following redirects
(rule 1+2), HTML comments stripped before reading prices (rule 5); JavaScript-only
plan tables rendered in headless Chromium via playwright-cli and read back as
rendered text. Every price below was read out of the named plan on the plan
table (rule 4) and paired with that plan name (rule 13). No promo prices
published (rule 10); annual billing stated plainly wherever the page showed
only annual rates.

## Verified: 9 providers

| id | categories | price_from (plan) | source |
|---|---|---|---|
| mureka-ai | music, video | $8/month billed annually (Basic Music & Speech) | mureka.ai homepage plan descriptions |
| loudly | music | $8/month billed annually (Personal) | loudly.com/music/pricing (rendered) |
| boomy | music | $14.99/month (Creator; $9.99 shown with 33% off) | boomy.com/pricing (rendered) |
| stable-audio | music | $12/month (Solo) | stableaudio.com/pricing (rendered) |
| iask-ai | search | $9.95/month (iAsk Pro) | iask.ai/pricing (rendered) |
| recraft-ai | image, video | $10/month billed annually (Basic) | recraft.ai/pricing (rendered) |
| v0 | code | $30/user/month (Plus) | v0.app/pricing (v0.dev 301 to v0.app; final URL stored) |
| warp-dev | code | $20/month (Build) | warp.dev/pricing |
| zed-editor | code | $10/month (Pro) | zed.dev/pricing |

## Dropped candidates (with reason)

- **riffusion** — riffusion.com 301-redirects to flowmusic.app; `flow-music` is
  already one of the 121 ids in data/providers.json. Dropped as already covered.
- **phind** — phind.com returns HTTP 403 even with a real browser User-Agent and
  redirect-following. Pricing unverifiable from its own site (rule 1 exhausted).
- **freepik / magnific** — https://www.freepik.com/pricing 301-redirects to
  https://www.magnific.com/pricing, which renders Freepik's plan table with
  promo pricing ($7.25 struck from $20, "50% OFF"). Cannot cleanly attribute the
  price to one product or name a standing list price with confidence
  (rules 2, 10, 13). Dropped.
- **komo** — only the Free ($0) plan is verifiable in static HTML; a $10 figure
  exists in JS page data but no plan name pairs with it (rule 13). Dropped.
- **topaz-labs** — homepage shows several unpaired prices ($12/mo, $19/mo,
  $29/mo, $39/mo, $199 one-time) across Photo/Video/Gigapixel products; could
  not pair one price to one named plan in the available time (rule 13). Dropped.
- **brave-search** — Brave Search Premium page URL not located during this run;
  premium price unverifiable. Dropped (revisit with the premium URL in hand).

## Pricing pages that were unclear

- **Mureka**: no dedicated pricing page found (mureka.ai/pricing is 404, no
  pricing link in nav). Plan prices ($8/mo Basic, $24/mo Pro, billed annually)
  come from the homepage's own plan descriptions; monthly-billing rates are not
  shown. Stated plainly in `price_from` / `watch_out`.
- **Boomy**: Creator shows "33% off $14.99/mo -> $9.99/mo". Standing list price
  $14.99 published per rule 10, with the shown discount noted.
- **Loudly / Recraft**: plan tables default to the annual-billing view; only
  annual rates shown. `price_from` says "(billed annually)" explicitly.
- **Stable Audio**: no free plan on the pricing page (Solo $12/mo is the entry);
  `free_tier` is false. Not the open-weights "Stable Audio Open" product, so
  `open_weights` is false (rule 12/13).

## Rule-11 (alive) notes

- "Sunset" string hits were false positives: a Stable Audio track titled
  "Stay Til Sunset" and Brave Search's weather-widget "Sunrise"/"Sunset"
  labels. No sunset/shutdown language found on any candidate homepage or
  pricing page. All 9 ship live products with working sign-up.
- Boomy footer copyright reads "(c) 2019-2023 Boomy Corporation" (stale footer)
  but the site, pricing page and sign-up are live and functional.

## Validation

Brief's validation script run on the Mac; output pasted in the task close.
