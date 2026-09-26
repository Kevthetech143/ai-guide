# Review — breadth batch 5 (016e)

Reviewer: independent reviewer agent, 2026-09-26 (ET).
Method: curl with a Chrome UA and `-L` for every stored URL (status + final URL), then
headless Chromium (Playwright) render of every page, because most plan tables are
JavaScript-only. HTML comments and JSON-LD stripped before reading static HTML. Billing
toggles clicked (Monthly / Annually) to read both rates. Homepages scanned for sunset /
shutdown / wind-down / limited-time wording.

## Links
All 9 stored URLs returned HTTP 200 and the final URL equalled the stored URL.
Mureka's link was changed (see below); the new one also returns 200 with no redirect.

## Verdicts: 2 keep, 7 fix, 0 cut

| id | verdict | what was checked / changed |
|---|---|---|
| mureka-ai | FIX | Muse's "Basic Music & Speech $8" came from a stale SEO paragraph in the homepage HTML, not a plan table. The real plan table is at /subscribe: **Pro** $10/month, or $8/month billed yearly ($96); Premier $30 / $24. Plan name corrected, monthly rate added, link changed to https://www.mureka.ai/subscribe, watch_out rewritten from the compare table (free = 4 songs/day on the free model; Pro = MP3 only, WAV/stems need Premier). |
| loudly | FIX | Page defaults to Annual. Personal is $10/month monthly, $8/month billed annually ($96). Monthly rate added in house style. watch_out verified (2,500 credits; free = non-commercial, 1 download/day). |
| boomy | FIX | Creator shows "33% off $14.99/mo -> $9.99/mo". Rule 10: the promo figure removed from price_from; list price $14.99 kept with a note that a discount is shown. watch_out verified. Alive: sign-up page works. Risk noted: footer still says "(c) 2019-2023" and the footer Blog link 404s; no sunset language found anywhere. Worth a re-check next batch. |
| stable-audio | FIX | Solo $12/month, 660 credits, credits reset monthly; no free plan; no annual toggle. Company corrected "Stable Audio" -> "Stability AI" (page footer: "by Stability AI"). open_weights false is right for this hosted app. |
| iask-ai | FIX | iAsk Pro $9.95/month, 300 daily Pro searches, free = limited ads, unlimited non-Pro searches: all verified. Company corrected to "Ai Search Inc." (page footer). The "limited time" text on the page is a student offer, not the listed price. |
| recraft-ai | FIX | Page defaults to annual. Basic is $12/month monthly, $10/month billed annually ($120). Monthly rate added. 1,000 credits, free images public / no commercial use, video only on Pro: all verified. |
| v0 | KEEP | Plus $30/user/month, one user can buy, free = $5 credits and 7 messages/day: verified. The page shows a struck-through "$90" next to Plus's $30; the FAQ says "we do not offer discounts at this time", so $30 is the standing price (the $90 appears to be the credit value). v0.app is the final URL. |
| warp-dev | KEEP | Page is set to Monthly by default: Build $20/month ($18 annually). 1,500 credits = $20 of agent usage: verified. |
| zed-editor | FIX | Pro $10/month, $5 of tokens, then API list price +10%: verified. Company corrected "Zed" -> "Zed Industries" (page: "Zed Industries, Inc."). |

No banned ids, no collisions (121 old ids + 9 new = 130 unique).

## Not changed, for the lead to know
- runs_on_your_computer is false for Warp and Zed (both are desktop apps, but paid AI is
  hosted; the site defines the flag as "nothing sent to the cloud"). Existing entries are
  not consistent on this: cursor, github-copilot and claude-code are marked true. Out of
  scope for this batch; flagged only.

## Merge
- Backup: data/providers.json.bak-20260926-016e (121 entries). Verified the first 121
  entries of the new providers.json equal the backup exactly; 9 appended, same key order,
  same formatting (indent 2, ASCII-escaped, trailing newline).
- data/providers-016e.json rewritten with the fixed entries.

## Build + linkcheck (real output)
```
Built 36 SEO question pages
Built 130 providers, 8 categories, 31 start pages, 36 question pages -> /Users/admin/agents/ai-guide-brain/site/dist
pages: 206, internal links checked: 4485, broken: 0
```
Not deployed, not committed.
