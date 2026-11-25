# Recheck 019v (2026-11-25), batch 34

Changed fields:
- audimee | watch_out | "The free plan gives 15 minutes of conversions, MP3 downloads only and personal use only, with no harmony maker, and you cannot save your conversions. Starter includes 1 hour of conversions a month." -> "The free plan gives 15 minutes of voice conversion in total (one time), MP3 quality and personal use only, with no harmony maker, and you cannot save your conversions. Text to Vocals can only be played in the app on the free plan, not downloaded. Starter includes 1 hour of conversions and 15 minutes of Text to Vocals downloads a month." | https://audimee.com/pricing | "Audio exports per month: Listen in the app only | 15 min | 60 min"; "Conversion time per month: 15 min, one-time | 1 hr"; "Save conversions: Not included"
- antigravity | watch_out | "The free Individual plan has basic weekly rate limits, so heavy users will hit the cap. Higher limits come with the paid Google AI Pro and Ultra plans." -> "The free Individual plan has a baseline agent quota that refreshes weekly. Higher quotas come with the paid Google AI Pro and Ultra plans." | https://antigravity.google/pricing | "Baseline agent quota refreshed weekly" (cut "heavy users will hit the cap", not on the page)
- all 20 | last_checked | -> 2026-11-25

Verified, no change (price_from, free_tier, open_weights, runs_on_your_computer, watch_out all match the cited page):
typecast ($5 Basic, free 3,000 lifetime credits ~5 min, Basic ~35 min), brave-leo (Premium $14.99/month, $149.99/year, account.brave.com checkout; 7-day trial not published), crush (Hyper plans from $10/month on hyper.charm.land, prepaid from $5 and free allowance retired on /faq), autogpt (Pro $50/month, 7-day trial, card required), dyad (Pro $20, Free 20 agent messages/day), clipdrop (Pro $15, free limits 20/24h and 50/24h), domoai ($13 Basic, $42 Standard monthly), yue, msty ($149/yr, $349 lifetime), open-webui, lumo ($12.99, $9.99 yearly), morphic, submagic ($19, $12 yearly), vidu ($10, $8.25 yearly), musicgpt (Plus $11.99 monthly, $9.99 yearly), stability-matrix (Supporter $5, 4,000 credits), pixlr ($2.49, $1.99 yearly).

Promos seen, NOT published (list prices kept):
- domoai: Black Friday banner, up to 37% off (Basic $8.10, Standard $26.10 yearly first year); ends in ~5 days.
- musicgpt: Black Friday 50% off yearly (Plus $4.99, Pro $8.99, Ultra $16.99 /month billed annually); list yearly Plus $9.99, monthly Plus $11.99.
- audimee: Black Friday up to 50% off yearly plans (Starter was $12, now $8.50 yearly).
- msty: Nexus Pro lifetime $399 offer through Nov 30 (a different product, not Studio).
- vidu: "Limited-time offer" on credit price (100 credits = $1.03) on paid plans.
- No promo found inside any existing watch_out; none carried forward.

Open-source / local checks (GitHub API, 2026-11-25; none archived, none downloaded):
- crush: v0.102.0 2026-11-19, license not recognized by GitHub (NOASSERTION), pushed today.
- autogpt: platform beta v0.12.0 2026-11-19, NOASSERTION, pushed today.
- dyad: v1.24.0 2026-11-23, NOASSERTION, pushed 11-24.
- yue: yue2-v0.1.6 2026-09-09, code Apache-2.0, weights CC BY-NC 4.0 (README); pushed 11-01. Needs Linux, NVIDIA 24 GB (README).
- open-webui: v0.13.5 2026-11-25, NOASSERTION, desktop app, pip and Docker per quick start.
- morphic: v1.10.0 2026-11-09, Apache-2.0, Docker + one AI provider key per README.
- stability-matrix: v2.17.0 2026-11-24, AGPL-3.0.
- basic-pitch: GOING QUIET (note only): last release v0.4.0 2024-08-16, last push 2025-11-13 (about 12.4 months); Apache-2.0; online tool still works. No paid hosted version found for any of the 9.
- msty: closed-source desktop app, pricing page checked.

Notes: pixlr is free_tier false and its page shows only paid plans; the page mentions "Ad-Free" in Plus, so an ad-supported free version may exist (not stated on the pricing page; left unchanged, lead may want to check). submagic says "Try For Free, no credit card" but the pricing page lists no free plan (free_tier false left as is).

unchanged: typecast, brave-leo, crush, autogpt, dyad, clipdrop, domoai, yue, msty, open-webui, lumo, morphic, submagic, vidu, musicgpt, stability-matrix, pixlr, basic-pitch (watch_out and facts; last_checked bumped)
unreachable: none
checked: 20/20

## Question-page ripples

None. Searched data/questions.json intro, meta_description, title for Audimee and Antigravity: Audimee appears in ai-that-sings-in-another-voice and ai-that-splits-a-song-into-instruments with no free-plan or price claim that the new watch_out contradicts. Antigravity is not named in any of those fields.
