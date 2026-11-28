# Recheck 019y (2026-11-28)

Changes (old -> new, source, quote):
- kling | price_from | "$10/month (Standard list price; the page currently shows a 12% discount, $8.80 a month, plus 30% off the first month)" -> "$10/month" | https://kling.ai/app/membership/membership-plan | Monthly tab: Standard "$10 ... 35% Off ... $6.5/month for the First 3 Months, then $8.8/month"; Yearly tab: "$120 ... Then $79.2/year". List price $10 only; promo text removed. (Flag: page shows $8.80/month ongoing after the promo; list kept per brief. No annual saving at list, so no bracket.)
- mindstudio | free_tier | true -> false | https://www.mindstudio.ai/pricing | page (default view and "legacy MindStudio plans" view) lists only Remy "30-day free trial, then $99/month", Individual $20/$16, Business Custom. No Free plan card and no "1,000 runs" text anywhere on the page or its FAQ. (Flag for lead: a 30-day trial is not a free tier. If a free signup still exists it is not on the pricing page.)
- mindstudio | price_from | "Free (Individual plan $20/month plus usage)" -> "$20/month ($16/month billed annually), plus usage" | same | "Individual ... $20 /month + usage" (Pay monthly), "$16 /month + usage billed yearly" (Pay yearly)
- mindstudio | watch_out | "The free plan allows one agent and 1,000 runs a month. Unlimited agents and runs need the Individual plan at $20/month on monthly billing, and both plans add usage charges on top. The pricing page now puts a newer product called Remy first ($99/month after a 30-day free trial) and calls the plans above its older \"legacy MindStudio plans\"." -> "The pricing page no longer lists a free plan. The Individual plan has unlimited agents and runs for $20/month on monthly billing ($16/month if you pay yearly), and AI model usage is charged on top. The page now puts a newer product called Remy first ($99/month after a 30-day free trial) and calls the Individual plan one of its \"legacy MindStudio plans\"." | same | "Unlimited agents / $20 /month + usage"; "Unlimited runs / month"; "Legacy MindStudio plans"; "30-day free trial, then $99/month"
- rork | price_from | "Free (Rork Pro plan $20/month)" -> "Free (paid plans from $20/month)" | https://rork.com/pricing | the $20/mo card is now titled "Rork Max" (same title as the $200/mo card); no plan named "Pro" appears.
- rork | watch_out | old: "...needs Rork Pro at $20/month; Rork Max for iOS, iPad and Apple Watch apps costs $200/month." (also claimed private projects and 100 credits) -> "The free plan is design-only, with 35 design credits a month and at most 5 a day. Build mode, which turns designs into working apps, needs a paid plan: $20/month gives 100 credits a month and 1 free hour of simulators and Xcode builds, and $200/month gives 1,000 credits and 10 free hours." | same | "35 design credits/mo, max 5/day"; "$20/mo ... Build mode: turn designs into working apps ... 100 credits/mo ... 1 h free/mo for simulators, Xcode builds"; "$200/mo ... 1,000 credits/mo ... 10 h free/mo". "Private projects" is no longer on the page, so dropped.
- ideogram | watch_out | "Pictures you make are public by default, and only the paid Plus and Pro plans can keep them private; Plus costs $20 a month, or $15 a month if you pay for a year. Free accounts get weekly credits, but the amount can change." -> "Everything you make on the free plan is public. Paid plans and pay-as-you-go credits keep new pictures private until you publish them. Free accounts only get weekly credits if they sign in with Google, Apple or Microsoft, and the amount can change." | https://ideogram.ai/features/faq/ | "On the free plan, images you generate are public. On Pay as you go, Plus, Pro, Team and Enterprise, new images stay private until you publish them"; "Free accounts that sign in with Google, Apple or Microsoft receive weekly credits, and the amount may vary. Accounts that sign up with an email and password get none."
- ideogram | watch_out_source | https://ideogram.ai/pricing -> https://ideogram.ai/features/faq/ (the public/private fact is on the FAQ, not the pricing page)

All 20: last_checked set to 2026-11-28.

Verified unchanged (price, free_tier, flags, watch_out re-read against source):
- suno: Pro "$10 / $8, Billed $96/year"; Free "No commercial rights". Black Friday banner "Extra 30% off annual plans" (not published).
- runway: monthly toggle Standard $15, yearly $12; "Gen-4.5 uses 12 credits per second". Promos seen: extra 30% off first year, Kling 25% off until Nov 30 (not published).
- cursor: https://cursor.com/pricing shows Plus $8/month ("Our introductory plan", "*Only Grok models are available on this plan"), Premium $30, Free $0. $8 is verified; no annual option, no promo.
- pika: Starter $10 monthly, $8 yearly; Free "0 · credit packs only". free_tier stays false. Banner "Black Friday 60% off!" (not published).
- devin: Pro $20/month, Free "light quota", "extra usage ... consumed at API pricing".
- github-copilot: Free $0 (2,000 completions per month), Pro $10/month; no promo.
- veo: flow.google.com/about Google AI Plus $4.99/mo* ("Prices may vary by market"), free "50 daily Google Flow credits".
- google-ai-mode: still free, signed-in only for history. Note: page says limits depend on Google AI subscription plan; price_from "Free" kept.
- deepseek: chat.deepseek.com sign-up only, no consumer paid plan; privacy policy "store ... in People's Republic of China". HF deepseek-ai/DeepSeek-V4.1-Flash license MIT, updated 2026-11-10: open weights confirmed.
- kimi: Plus $19 monthly, $15 annual ($180/yr). HF moonshotai/Kimi-K3.1-Pro (created 2026-11-02, license "other", not gated): open weights confirmed. Banner: "K3.1 Pro requests may queue or fail at launch".
- wondercraft: Free 150 credits, 720p; Creator $25 monthly / $21 yearly.
- hermes-agent: repo NousResearch/hermes-agent not archived, MIT, latest release v0.23.5 (2026-11-28); Portal Free $0 pay-as-you-go, Plus $20/month.
- openclaw: repo openclaw/openclaw not archived, MIT, latest release v2026.11.10 (2026-11-25); site "No subscription. No hosted tier."
- whisper: repo openai/whisper not archived, MIT, last push 2026-08-31, latest release v20250625 (2025-06-26). Note only: no release in 17 months (commits within 12), not "going quiet" by commit rule. Still pip-installable and needs ffmpeg.
- qwant: qwant.com still shows "Get answers instantly with Flash Answers", "Free"; help article (4 months old) confirms AI answer appears only for some searches.
- reddit-ai-search: help article: 10/week logged out, 50/day logged in, 100/day Premium; Premium $5.99/Month on reddit.com/premium.
- ideogram: open_weights=true CONFIRMED: ideogram.ai/pricing "You run Ideogram 4 public weights on your own infrastructure" (self-host license), HF ideogram-ai/ideogram-4-fp8 (license ideogram-4-non-commercial). Price Plus $20/month, $180 billed annually ($15/month).

unchanged: suno, runway, kimi, wondercraft, hermes-agent, openclaw, qwant, reddit-ai-search, cursor, whisper, veo, pika, devin, github-copilot, google-ai-mode, deepseek (field values; last_checked bumped)
unreachable: none
checked: 20/20

## Question-page ripples

None found. Searched data/questions.json (title, meta_description, intro) for MindStudio, Rork, Ideogram, Kling. No sentence claims a MindStudio free plan, a Rork plan name or price, an Ideogram privacy rule, or a Kling price. Lead note: mindstudio free_tier flipped to false; if build.py builds any "free" list or filter from free_tier, MindStudio drops out of it.
