# Review of ai-guide-019f (batch 18, the 20 oldest cards) — 2026-11-07

Verdict: SHIP (after one consistency fix I applied to the patch: 9 cards move from an annual-first price_from to the site's monthly-first shape, see section 3). Score: 9/10.
Reviewer: Fable 5.1, fresh context. Files edited: data/providers-019f.json (backup data/providers-019f.json.bak-2026-11-07-review) and this file only.

Why SHIP: the one worker rewrite (ltx-studio watch_out) matches the rendered page sentence by sentence, the 20-card diff against providers.json shows only last_checked plus that one field, and free_tier / price_from figures / links hold on every card I opened. The point off: 9 of the 20 cards led with the yearly-billed price (reclaim-ai with no label at all) while each page shows a monthly plan; the numbers were right, the shape was not, so I moved them to the claude/kimi/wisecut shape "$monthly/month ($yearly/month billed annually)".

How I checked: curl with a Chrome UA (all 200) for ltx.io/studio/pricing, relevanceai.com/docs/get-started/pricing, www.jasper.ai/pricing, krisp.ai/pricing/, soundraw.io/ and /pricing, www.nomic.ai/gpt4all, kits.ai/pricing (-> www.kits.ai/pricing), soundful.com/pricing/, reclaim.ai/pricing, rytr.me/pricing, www.flowmusic.app/pricing, www.lalal.ai/pricing/, comfy.org/pricing; api.github.com for nomic-ai/gpt4all. Real Chrome via playwright-cli session ag019fr (profile ~/.config/pw-aiguide-recheck, no sign-in) for ltx.io (Yearly + Monthly tabs), rytr.me (Monthly + Yearly), flowmusic.app (Yearly + Monthly radios), lalal.ai (Annually switch on and off). Session closed; `pgrep -f pw-aiguide-recheck` printed nothing (rc=1). Page texts under /tmp/ag019f/rv/.

## 1. Spot-checks (free_tier, price_from, link)
- ltx-studio | OK (shape fixed) | Rendered Yearly tab: "Lite $15 $12 Billed yearly $144 8,000 credits/month"; Monthly tab: "Lite $15 8,000 credits/month"; Free "800 credits (one time)". The raw HTML still carries hidden template strings ("Exclusive limited time offer", "Cyber Monday", "FLUX.2 promotional offer valid until December 12, 2025") but none render on the page, so the worker is right that the limited-time wording is gone. free_tier true holds. Link 200.
- relevance-ai | OK (shape fixed) | "Pro — $19 / month annual, $29 / month monthly"; "Includes: 30,000 Actions / year (or 2,500 / month) $240 Vendor Credits / year (or $20 / month)"; "The Free plan is retired for both new signups and existing accounts". free_tier false holds. Link 200.
- jasper-ai | OK (shape fixed) | "Pro: $59/month billed yearly or $69/month billed monthly (cancel anytime)"; "7-day free trial of the Pro plan"; no free plan. free_tier false holds. Link 200.
- krisp | OK (shape fixed) | "Monthly Annually Save 50% ... Free Trial ... $0 ... Core ... $16 /mo/user $8 /mo/user". Trial only, free_tier false holds (same rule as 019c). Link 200.
- soundraw | OK | "Creator ... $16.99/mo $11.04/mo"; format row "mp3 mp3 mp3, wav, stems" for Creator / Artist Starter / Artist Pro; FAQ "Artist Starter – lets you download up to 10 fully-mixed songs (.mp3 only)". Already monthly-first. Link 200.
- gpt4all | OK | Page: "Designed for developers, teams, and AI power-users, GPT4All runs open-source language models on Windows, macOS, and Linux"; installers for macOS, Windows, Windows ARM, Ubuntu listed. GitHub: MIT, archived false, latest release v3.10.0 (2025-02-25), pushed 2025-05-27. Link 200.
- reclaim-ai | OK (shape fixed) | Yearly view "Starter ... $10 per seat/month"; Monthly view "Starter ... $12 per seat/month"; "Lite ... Free Free forever". The stale "LAUNCH PROMO: Attendee Users ... free through July 31st" is on the page but not on the card. Link 200.
- rytr | OK (shape fixed) | Chrome, Monthly pressed: "Lite $9 /mo"; Yearly: "Lite $7.50 /mo billed annually"; "Free forever ... 10,000 characters per month". Link 200.
- flow-music | OK (shape fixed) | Chrome, Yearly checked (default): "Starter $ 6 / month Save 25%"; Monthly: "Starter $8 / month"; Free "$0 / month Daily top-up credits 2 concurrent generations". Link 200.
- lalal-ai | OK (shape fixed) | Chrome, "Annually • Save 3 Months" switch on: "Lite $7.5 /mo $90 billed annually", Pro $15; switch off: "Lite $9.99 /mo billed monthly", Pro $19.99; "90 Minutes/mo" / "250 Minutes/mo" fast queue. Link 200.
- comfyui | OK (shape fixed) | "STANDARD $16 $20 /month $192 billed yearly"; FAQ "Comfy Desktop itself is free". Link 200.
- kits-ai | OK | kits.ai/pricing 301s to www.kits.ai/pricing (200); watch_out_source already www. Not changed (works).

## 2. Rulings
(a) ltx-studio rewrite — KEEP, and price_from goes monthly-first (applied). Every sentence is on the rendered pricing page: $12/month billed yearly $144, Lite $15 on the Monthly tab, 8,000 credits/month, Free 800 credits one time. Plain words, no jargon. The old "limited-time offer" clause is not visible on the page today, so dropping it is right. New price_from "$15/month ($12/month billed annually)"; the watch_out already names both prices so it stays true.
(b) relevance-ai vendor credits — KEEP the "$20 of vendor credits a month" wording. The Pro plan box itself says "$240 Vendor Credits / year (or $20 / month)"; the comparison table's "10,000" is the same allowance in credit units (the top-up price on the same page is "$20 USD per 10,000 Vendor Credits", and Team shows "$70 / month" against "35,000" the same way). Not inconsistent, just two units; the dollar figure is what a reader can act on and is what the plan box says.
(c) gpt4all — NO CHANGE. Nothing on the card is wrong: the app is still free, downloadable for all three platforms, runs locally, MIT, repo not archived, and the watch_out quotes the page's own "developers, teams, and AI power-users" line. The last release being 2025-02-25 is a staleness signal with no card field to carry it; if the lead wants it surfaced, a watch_out sentence like "The last new version came out in February 2025" is on the GitHub releases page, not on the cited nomic.ai page, so it would need a second source. Not a merge blocker.

## 3. Fix applied to the patch (9 cards, price_from shape only)
Site rule (019a lead action on claude/kimi, 019e on wisecut): lead with the US monthly list price when a monthly plan exists, yearly in brackets. Both figures on every card below were read on the provider's own page today (section 1).
- relevance-ai | price_from | "$19/month (billed annually)" -> "$29/month ($19/month billed annually)"
- ltx-studio | price_from | "$12/month (billed annually)" -> "$15/month ($12/month billed annually)"
- krisp | price_from | "$8/month (billed annually)" -> "$16/month ($8/month billed annually)"
- reclaim-ai | price_from | "$10/month" -> "$12/month ($10/month billed annually)" (the old value was a yearly price with no label)
- jasper-ai | price_from | "$59/month (billed annually)" -> "$69/month ($59/month billed annually)"
- rytr | price_from | "$7.50/month (billed annually)" -> "$9/month ($7.50/month billed annually)"
- lalal-ai | price_from | "$7.50/month (billed annually)" -> "$9.99/month ($7.50/month billed annually)"
- flow-music | price_from | "$6/month (billed annually)" -> "$8/month ($6/month billed annually)"
- comfyui | price_from | "Free to run yourself (cloud from $16/month billed annually)" -> "Free to run yourself (cloud from $20/month, or $16/month billed annually)"
- Backup: /Users/admin/agents/ai-guide-brain/site/data/providers-019f.json.bak-2026-11-07-review. File re-checked equal to json.dumps(indent=2, ensure_ascii=False)+"\n".
- Each card's watch_out already states both prices (or no price, lalal-ai), so no watch_out edit rides along. Soundraw and soundful were already monthly-first; kagi, kits-ai, listnr, tabby, exa have no yearly plan on the card.

## 4. Silent-change check — OK
Diff of all 20 cards vs providers.json: last_checked on 20 cards -> 2026-11-07, plus exactly ltx-studio watch_out (listed in recheck-019f.md) and my 9 price_from edits. No id/name/categories/link/free_tier/open_weights/runs_on_your_computer change. All 20 ids exist; none new.

## 5. Watch_out sentences vs cited pages — all on page
- ltx-studio: $12 yearly, $144, Lite $15 monthly, 8,000 credits, Free 800 one time — ltx.io/studio/pricing (rendered).
- relevance-ai: free plan retired, $19 yearly / $29 monthly, 2,500 Actions, $20 vendor credits — relevanceai.com/docs/get-started/pricing.
- krisp: 7-day trial only, $8 yearly / $16 monthly, per user — krisp.ai/pricing/.
- reclaim-ai: $10 yearly per seat, $12 monthly — reclaim.ai/pricing.
- jasper-ai: $59 yearly / $69 monthly, built for teams ("AI built for better marketing results", Business plan) — www.jasper.ai/pricing.
- rytr: $7.50 yearly (~$90), $9 monthly — rytr.me/pricing.
- soundraw: Creator mp3 only, Artist Starter mp3 only, wav/stems from Artist Pro — soundraw.io.
- lalal-ai: 90 / 250 fast-queue minutes — www.lalal.ai/pricing/ (VST / local processing Pro-only: worker-verified, not re-read by me).
- flow-music: $6 yearly, opens on yearly view, $8 monthly, daily top-ups, 2 at a time — www.flowmusic.app/pricing.
- gpt4all: "developers, teams, and AI power-users" — www.nomic.ai/gpt4all.
- comfyui: desktop free, cloud $16 yearly / $20 monthly — comfy.org/pricing.
- Not re-read by me (worker-verified only): soundful, kagi, kits-ai, listnr, musicgen, exa, tabby, jan, anythingllm — all unchanged cards.

## 6. Side effects the lead should know
- schema.org Offer (first dollar figure in price_from) changes on 9 cards from the yearly to the monthly figure: relevance-ai 19->29, ltx-studio 12->15, krisp 8->16, reclaim-ai 10->12, jasper-ai 59->69, rytr 7.50->9, lalal-ai 7.50->9.99, flow-music 6->8, comfyui 16->20. Same effect the wisecut/claude moves had. No filter-page movement (free_tier unchanged everywhere; no price_from became or stopped being "Free").
- Ripple check (mine, grep of title/intro/meta_description/how_picked for all 20 names with a dollar figure): only ai-for-building-my-own-ai-helper names a price — "Relevance AI ... starts at $19 a month on a yearly plan" — still true after the flip. Worker's "Ripples: none" confirmed.
- 64 other cards site-wide still lead with an annual figure (e.g. perplexity, pictory, colossyan, copy-ai, fireflies-ai, fathom-ai); perplexity shows no monthly price on its page so it stays as is. The rest can move as their batches come due; not for this merge.
- Nothing else for the lead at merge beyond copying the 20 cards over.
