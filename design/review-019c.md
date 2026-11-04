# Review of ai-guide-019c (batch 15, the 20 oldest cards) — 2026-11-04

Verdict: SHIP (after one fix I already applied to the patch: hailuo price_from gets the site's discount note). Score: 9/10.

Why SHIP: the worker changed no field but last_checked, and every card I re-opened matches the provider's page today. The only miss is a convention one: hailuo is on sale and the site's shape for that (kling in 019b, boomy, ace-studio) is list price plus an inline discount note in price_from, not a bare list price. Fixed in the patch. Full field diff against providers.json at 211b3bf: last_checked on all 20, plus my hailuo price_from edit; nothing else. File equals json.dumps(indent=2, ensure_ascii=False)+"\n". The worker's browser session is closed (`pgrep -f pw-aiguide-recheck` empty).

How I checked: curl (desktop UA) for heygen, microsoft, developers.openai.com/codex/pricing, descript, lumalabs.ai/pricing and /dream-machine, ollama.com/pricing, huggingface.co/MiniMaxAI/MiniMax-H3 (+ raw LICENSE), n8n; real Chrome via playwright-cli session ag019c-rev (profile ~/.config/pw-aiguide-review, no sign-in) for hailuoai.video/subscribe, manus.im/pricing, n8n.io/pricing, openai.com/codex (403 to curl). Session closed; `pgrep -f pw-aiguide-review` prints nothing.

## 1. Spot-checks (free_tier, price_from, link) — all OK
- heygen | https://www.heygen.com/pricing (200) | "Free $0/mo ... 3 videos a month, watermarked"; "Monthly Yearly 2 months free Creator $29 / mo"; FAQ "generate up to 3 videos a month, no credit card required". free_tier true, "$29/month" hold.
- microsoft-copilot | https://www.microsoft.com/en-us/copilot/solutions/individuals (200) | "Monthly Yearly SAVE UP TO 17% Microsoft 365 Personal $9.99 /month"; Family "$12.99 /month"; Premium "$19.99 /month"; "chat with higher usage than free". free_tier true, "$9.99/month" hold.
- codex | https://developers.openai.com/codex/pricing (200) | "Free ... quick coding tasks. $0 /month"; "Go Use Codex for lightweight coding tasks. $8 /month"; "Plus ... $20 /month ... Codex on the web, in the CLI, in the IDE extension"; "Pro ... From $100 /month ... Plans at $100, $200, or $500". Card link https://openai.com/codex renders in Chrome (lands on /codex/, shows "$20 / month Get Plus"). free_tier true, "$8/month (with ChatGPT Go)" and the watch_out hold.
- descript | https://www.descript.com/pricing (200) | "Monthly Annual Saving up to 35% ... Hobbyist $ 16 $ 24 per person / month"; media table "60 minutes (1 hr) / month" in the Free column. free_tier true, "$16/month (billed annually; $24 monthly)" hold.
- hailuo | https://hailuoai.video/subscribe (Chrome, plan pop-up, Yearly view default) | "Free ... One-time free trial credits"; "Standard $14.99 44% OFF $8.40 /month $100.80 billed yearly". The Monthly view ($10.50, 30% off) is the worker's reading today and matched review-018q on 10-22; my Monthly click closed the pop-up, so I did not see it myself (unverified by me). Header "From $9.99 /mo". Link 200. free_tier true holds; price_from fixed (section 2).
- luma | https://lumalabs.ai/pricing (200) | "Monthly Yearly Individual plans Plus $30 /month $300 billed yearly ... 10,000 credits"; Pro "$90 /month"; the only "free" on the page is "Reference images: first 5 free". Cost table "20 credits/5 sec 60 credits/10 sec". free_tier false, "$30/month" hold. Link 200.
- ollama (extra) | https://ollama.com/pricing (200) | "Pay as you go $0 ... Run models locally"; "Pro ... $20 / mo. or $200/yr"; Max "$100 / mo.". "$20/month (Ollama Pro; local use free)" holds.
- n8n (extra) | https://n8n.io/pricing/ (Chrome) | "Monthly Annually (Save 17%) Starter ... $20 /mo, billed annually"; "Community Edition A standard, self-hosted version of n8n is available on GitHub". $24 monthly is the worker's reading (17% off $24 = $20, consistent). Holds.
- manus (extra) | https://manus.im/pricing (Chrome) | prices are animated digit reels ("$ 0 1 2 3 ... / month"), unreadable as text; the worker priced it from a screenshot. Not re-verified by me; card unchanged from HEAD so nothing is at risk.

## 2. Open decision 1: hailuo promo — FIX (applied)
Site convention since 019b: a current discount is shown in price_from as list price plus note (kling "$10/month (Standard list price; the page currently shows a 12% discount, ...)", boomy, ace-studio). hailuo had the bare "$14.99/month" with the discount only in recheck-019c.md, which the reader never sees.
Change made: id hailuo | price_from | "$14.99/month" -> "$14.99/month (Standard list price; the page currently shows a 30% discount, $10.50 a month, or $8.40 a month billed yearly)". Source https://hailuoai.video/subscribe: "$14.99" struck, "44% OFF", "$8.40 /month $100.80 billed yearly" (seen by me); "30% OFF $10.50 /month" (worker today + review-018q). watch_out keeps "costs $14.99 a month", same as kling keeps "$10 a month" in prose.
Backup: /Users/admin/agents/ai-guide-brain/site/data/providers-019c.json.bak-2026-11-04-review.

## 3. Open decision 2: hailuo open_weights — keep false (agree with worker)
Verified: https://huggingface.co/MiniMaxAI/MiniMax-H3 is public (not gated), safetensors present, license "minimax-h3-community-license-agreement"; raw LICENSE: "'Excluded Territories' means the European Union, the United Kingdom, the Republic of Korea and the United States of America"; "'Applicable Territory' means worldwide, excluding the Excluded Territories." The model card names hailuoai.video as the web app for H3.
Ruling: build.py explains the chip as "Open source — anyone can download and inspect how it works." For the site's US readers that is not true here. Every existing open_weights-true card with a license catch (f5-tts, musicgen non-commercial; yue, ltx-2 commercial license) still lets a US reader download and use it personally; none bans a territory. No precedent for a US-excluded license, so false is the honest chip. Lead's call if the site ever wants a "regional" note; I would not add text without a second source URL.

## 4. Open decision 3: luma free_tier — keep false (agree with worker)
Precedent: copy-ai ("Try for free", trial only, 018t), gumloop (018t), krisp ("Get Krisp for free" button, 018t), scite ("Start Free Trial", 018s) all stay false under the never-guess rule when no official page shows an ongoing free plan. lumalabs.ai/pricing lists Plus/Pro/Ultra only; /dream-machine's "Try now for free" is a button, not a plan. Same ruling here.

## 5. Unsourced watch_outs (manus, n8n, ollama) — keep, no edit
What the site has done before: the "cut" rule (018v: vane, gpt-researcher; 018r: duckduckgo) applies to a sentence that is not on the page a card cites. Cards with no watch_out_source at all (qwen, notebooklm) have been kept unchanged through 018p/018q/018r ("right call, hardware claim not on an official page"; "leave for a future batch or cut"). manus, n8n, ollama are in the same group (5 unsourced cards site-wide). Price facts in them hold today (manus $20 per worker, n8n $20/$24 + free self-host, ollama Pro $20); the soft sentences ("double-check its work", "built for technical users", "type commands / lots of memory") are not on the pricing pages. Keep as HEAD; no fact changed, so no rewrite under this batch's rule. Suggest a one-off cleanup batch for the 5 unsourced cards (add a source or trim), not a merge blocker.

## 6. Silent-change check — OK
Diff of all 20 cards in providers-019c.json vs providers.json at 211b3bf: last_checked only (15 cards 2026-10-22 -> 2026-11-04, 5 cards 2026-10-23 -> 2026-11-04) plus my hailuo price_from. No id/name/categories/link/free_tier/open_weights/runs_on_your_computer/good_for/watch_out/watch_out_source change. 20 ids all exist; none new.

## 7. Question-page ripples — none
Only hailuo price_from changed (shape, same $14.99). questions.json mentions Hailuo once (ai-that-turns-a-photo-into-a-video intro: "...Hailuo AI turn a photo or a written prompt into a short clip...") with no price, so nothing goes stale.

## Not verified by me (worker's claims taken as reported)
google-ai-mode, ideogram, leonardo, meta-ai, murf, replit, udio, zapier-ai, aider, amazon-q-developer, bolt-new: date bump only; pages not re-opened by me (outside the spot-check list). Ollama GitHub release v0.40.14 and aider v0.86.0 figures are the worker's.

Reviewer model: Fable 5.1 (claude-fable-5-1), the lead's named independent reviewer for this batch; a fresh-context cross-check against live pages is what the tier is for.
