# Review 019y (2026-11-28), reviewer ag019y-review (Opus 5.5)

## Verdict: SHIP, 9/10

Every changed fact checks out on the maker's own page. No corrections made; providers-019y.json is untouched (no backup needed).

## Structure check (verified by script)
- providers-019y.json parses as a JSON list of 20 cards, exactly the 20 task ids; no card added, removed or renamed.
- Every card has the same field set as its card in providers.json.
- Only diffs vs providers.json: kling price_from; mindstudio free_tier, price_from, watch_out; rork price_from, watch_out; ideogram watch_out, watch_out_source; plus last_checked "2026-11-28" on all 20. Matches the worker's claim.
- File ends with "}\n]\n".

## Changed facts: all CONFIRMED
- kling price_from "$10/month": https://kling.ai/app/membership/membership-plan (real Chrome) "Standard | $6.5 / First 3 Months | $10 | 35% Off | $6.5/month for the First 3 Months, then $8.8/month." Countdown "04 Days 19 Hrs" and "Limited-Time 35% Off" / "Limited-Time 50% Off" tabs. $10 is the list price; no promo text published. Note for lead: the "then $8.8/month" line means the ongoing price after the promo is also below list; list price kept per the brief.
- mindstudio free_tier false: https://www.mindstudio.ai/pricing (curl 200) shows only "Remy 30-day free trial, then $99/month", "Legacy MindStudio plans ... Individual ... $20 /month + usage $16 /month + usage billed yearly", "Unlimited agents", "Unlimited runs", Business "Custom". No free plan card, and the FAQ has no free plan question. Extra search done: the docs index (docs.mindstudio.ai/llms.txt) and the Billing Settings and Usage Pricing docs have zero "free" mentions; www.mindstudio.ai/llms.txt says to cite the pricing page. The only "Free Plan" mention found is a staff forum reply from 2026-01-13 (community.mindstudio.ai/t/what-happened-to-the-free-plan/1902): "New users can now sign up for the Free Plan ... will need to top up their workspace balance to run copied Agents." That is 10 months old, not on the pricing page, and even then needed paid top-ups. The Remy trial is a trial, not free. Accept false.
- mindstudio price_from "$20/month ($16/month billed annually), plus usage": same page, quote above. Correct format.
- mindstudio watch_out: every sentence is on the pricing page ("Unlimited agents", "Unlimited runs", "+ usage", "$16 /month ... billed yearly", "30-day free trial, then $99/month", "Legacy MindStudio plans"). The "no longer lists a free plan" sentence is an absence claim, true on the page.
- rork price_from "Free (paid plans from $20/month)": https://rork.com/pricing (curl is JS-only; real Chrome): "Free ... $0", "Rork Max ... $20/mo", "Rork Max ... $200/mo". Both paid cards are titled "Rork Max"; no "Pro" anywhere. No annual option, no sale banner.
- rork watch_out: "35 design credits/mo, max 5/day"; "Build mode: turn designs into working apps"; "100 credits/mo"; "1 h free/mo for simulators, Xcode builds and rork sim"; "1,000 credits/mo"; "10 h free/mo". All present.
- ideogram watch_out + watch_out_source https://ideogram.ai/features/faq/ (curl 200): "On the free plan, images you generate are public. On Pay as you go, Plus, Pro, Team and Enterprise, new images stay private until you publish them"; "Free accounts that sign in with Google, Apple or Microsoft receive weekly credits, and the amount may vary. Accounts that sign up with an email and password get none." All three sentences present.

## Spot-checks of unchanged cards (8), all on the maker's own page
- cursor: https://cursor.com/pricing "Plus $8 /month ... Our introductory plan", "*Only Grok models are available on this plan", "Premium ... $30 /month ... Third-party models at API list price", "Third Party model usage in Cursor is not included in the monthly prices". $8/month and watch_out correct. No promo.
- ideogram (open weights): https://ideogram.ai/pricing (curl 403, real Chrome) "Plus ... $20 per month, $180 billed annually"; "You run Ideogram 4 public weights on your own infrastructure". HF API ideogram-ai/ideogram-4-fp8: license "other", gated "auto" (click-through). open_weights=true and price_from correct.
- deepseek (open weights): HF API deepseek-ai/DeepSeek-V4.1-Flash license "mit", not gated. Correct.
- suno: "Pro ... $10 $8 / month Billed $96/year"; Free "No commercial rights". Banner "Extra 30% off annual plans Black Friday Sale" not published. Correct.
- pika: "Starter ... $10 /mo Billed monthly", "Price / mo (annual, -20%) ... $8", Free "0 · credit packs only". Banner "Black Friday 60% off!" not published. Correct.
- devin: "Pro ... $20 per month", "light quota", "extra usage which is consumed at API pricing". Correct.
- github-copilot: "Free ... 2,000 completions per month", "Pro $10 per month". Banner "30% off Copilot Fusion usage until Dec 31" not published. Correct.
- kling watch_out: comparison table shows "-" for Basic on "Generated content is for commercial use" and "Brand watermark removal"; "$10" Standard. Correct.

Promo check: no promo, sale or first-month price appears in any of the 20 price_from or watch_out fields (read all 20).

## Ripples (checked myself)
questions.json title/meta_description/intro mentions: Kling (4 pages), Ideogram (5), MindStudio (1), Rork (0). None is made wrong by the new facts. MindStudio's only sentence ("MindStudio lets you build and run your own agents") claims no free plan.
free_tier filter pages, computed with build.py's matching rule:
- ai-for-small-business (agents + free_tier true): MindStudio drops off the list. Intro names only Zapier AI, Cursor, Manus. Nothing wrong.
- best-paid-ai-worth-the-money (free_tier false): MindStudio joins the list. Intro names only Midjourney and Claude Code. Nothing wrong.
- /start/free, /start/paid and category free/paid lists are computed from free_tier, so MindStudio moves to paid automatically and correctly.
Ripple sentences: none.

## Voice
Plain and short. Optional polish only (not required): rork watch_out sentence 2 is about 40 words and uses "simulators and Xcode builds" (the page's own words). A reader-friendlier split would be fine but nothing is wrong.

## Browser
Session ag019yr closed; its daemon lingered after "close" (pid 28501 + Chrome 28520), killed only those; `pgrep -f pw-aiguide-recheck` then printed nothing (exit 1).

## Exact edits
Required: none. Corrections made: none.
