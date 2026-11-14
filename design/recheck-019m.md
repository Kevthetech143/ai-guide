# ai-guide-019m re-check (2026-11-14), batch 25

## Changes
- mindstudio | watch_out | "...and both plans add usage charges on top." -> same text + " The pricing page now also promotes a newer product called Remy ($99/month after a 30-day free trial) and lists these plans as legacy MindStudio plans." | https://www.mindstudio.ai/pricing : "MindStudio is now Remy ... 30-day free trial, then $99/month ... Legacy MindStudio plans" (Free $0, Individual $20/month, $16 billed yearly still listed)
- hermes-agent | watch_out | "The free Nous Portal plan includes free AI models only and $0 of monthly credits. Access to 200+ models and hosted tools starts with the Plus plan at $20/month." -> "The free Nous Portal plan is pay-as-you-go and includes free AI models only, with no hosted tools. Access to 200+ models and hosted tools starts with the Plus plan at $20/month." | https://hermes-agent.nousresearch.com/ : "Free: $0, pay as you go ... Models: Free models only ... Plus $20 / month"; the "$0 of monthly credits" wording is no longer on the page, so it was cut.
- last_checked -> 2026-11-14 on all 20 cards.

No change to free_tier, price_from, open_weights, runs_on_your_computer or link on any card.

## Verified facts (own pages)
gemini: Free $0; Google AI Plus $4.99, Pro $19.99 (gemini.google/subscriptions/). grok: Free, Plus $8, Premium $30 (x.ai/pricing). perplexity: Free; Pro $17/mo billed annually (perplexity.ai/hub/pricing). kimi: Plus $19/mo, $15 billed annually; K3.1 Pro open weights on Hugging Face moonshotai, license "other" (kimi.com/membership/pricing). wondercraft: Free 150 credits, 720p; Creator $25/$21 (wondercraft.ai/pricing). rork: Free 35 credits/mo max 5/day; Pro $20; Max $200 (rork.com/pricing). openclaw: "No subscription. No hosted tier."; MIT, release v2026.11.3 on 2026-11-10 (GitHub). hermes-agent: MIT, release v0.23.1 on 2026-11-10 (GitHub). qwant: Flash Answer help page unchanged. reddit-ai-search: 10/week logged out, 50/day logged in, 100/day Premium (support.reddithelp.com). llama: dev.meta.ai/llama still lists Llama 4 as newest; Hugging Face meta-llama newest upload is 2025 (upkeep is slow, unverified whether newer Meta models exist elsewhere). mistral: Free; Pro $14.99 (students $5.99); newest open model on HF Mistral-Large-4 (2026-11-02). qwen: "free to use"; open-source Qwen-Image-2.1 (2026-09-20), Qwen3.8 on HF updated 2026-11-07. midjourney: Basic $10, Stealth only on Pro and Mega. stable-diffusion: SD 3.5 page unchanged, Community License free under $1M revenue; Stability HF repos updated 2026-11. flux: bfl.ai now headlines FLUX 3 (FLUX 3 Image Klein open weights, gated on HF); card's cited FLUX.2-klein-4B page is Apache-2.0 and says ~13GB VRAM, so kept. elevenlabs: Free; Starter $6 monthly / $5 annual (first month $1 promo, not published). suno: Free no commercial rights; Pro $10 / $8 annual. runway: Free 125 one-time credits; Standard $15 / $12 annual.

Pages that blocked curl (grok, reddit, midjourney, kimi pricing, qwen, hermes table) were read in real Chrome (profile pw-aiguide-recheck, session closed, pgrep proved empty after killing own ag019m daemon).

Watch items seen: MindStudio rebrand to "Remy" (above); ElevenLabs $1 first-month Starter promo (list price kept).

unchanged: gemini, grok, perplexity, kimi, wondercraft, rork, openclaw, qwant, reddit-ai-search, llama, mistral, qwen, midjourney, stable-diffusion, flux, elevenlabs, suno, runway (only last_checked moved)
unreachable: none
checked: 20/20

## Question-page ripples
Changed watch_out only (mindstudio, hermes-agent); no free_tier, price_from or good_for changes. Searched intro, meta_description, title.
- ai-for-building-my-own-ai-helper | MindStudio | "MindStudio lets you build and run your own agents..." | still true, no price claim about MindStudio | none needed
- ai-that-browses-websites-for-me, ai-i-can-use-in-whatsapp, ai-that-runs-jobs-on-a-schedule, ai-that-remembers-what-i-worked-on | Hermes Agent | sentences describe install and features only, no free-plan or credits claim | still true | none needed
Ripples: 0
