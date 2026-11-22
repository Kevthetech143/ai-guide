# Review 019s (2026-11-22) — reviewer ag019s-review (Opus 5.5)

## Verdict: SHIP, 8.5/10 — the lead applies the 3 sonix edits below at merge time

The patch matches HEAD b30438a except the one declared change (warp-dev watch_out) and last_checked on all 20 cards. I checked this with a field-by-field diff of data/providers-019s.json against data/providers.json. No hidden edits. The one point taken off: sonix kept Core $25 as price_from while the same page sells a cheaper paid option with no monthly fee. The worker did flag it for the lead.

## 1. Changed card
- warp-dev | watch_out: verified at https://www.warp.dev/pricing (Warp Agent tab, curl 200). The Build block reads: "Build Monthly Annual ... $20 /month ... $20 of agent usage included each month at API rates ... Add-on agent usage, auto-reload, and team-wide spend cap". The annual view shows "$18 /month". "1,500" appears nowhere on the page. The new sentence and the price_from "$20/month (Build; $18/month billed annually)" are both right. OK.

## 2. Unchanged cards re-checked: 19 of 19 (on the providers' own pages)
- stable-audio: https://stableaudio.com/pricing (Chrome): "Free $0/mo 50 credits a month About 12 full-mix generations"; "Solo $12/mo ... 660 credits/mo"; "The credit amount will reset to the monthly allocated amount every month." The FAQ question "Do my unused credits in one month roll over to the next?" is listed (answer is folded). OK.
- iask-ai: https://iask.ai/pricing redirects to https://iask.ai/ (200). The home page says "iAsk AI is a free question AI search engine". No plans are shown, so the watch_out is accurate. OK.
- recraft-ai: https://www.recraft.ai/pricing (Chrome). After clicking "Pay monthly": "Basic ... $12 billed monthly 1,000 credits per month". The annual view: "Regular price: $10 ... Black Friday price: $6.00". The Black Friday price is not published. FAQ: "Images generated on the Free plan ... are publicly visible ... not licensed for commercial use". OK.
- v0: https://v0.app/pricing (curl): "7 message/day limit"; "Plus Popular $30 <del>$90</del> /user/month". The "$90" is inside a <del> tag with no promo text. This is the same treatment the lead accepted in 018v/019g, so $30 stays. OK.
- zed-editor: https://zed.dev/pricing: "Pro Free Trial $10 per month ... $5 of tokens included"; "Zed Pro bills at API list price +10%". OK.
- vane: GitHub API: MIT, not archived, release v1.12.2 (2026-04-10), pushed 2026-09-01. README: "Using Docker is highly recommended"; "local LLMs (Ollama) and cloud providers (OpenAI, Claude, Groq)". OK.
- andi: https://andiai.com/: "Free forever. Andi Pro coming soon."; "Andi AI Search API ... $5 free credit included ... Auto top-up & pre-paid credits ... Team $49 /month". Terms (https://andiai.com/legal/terms-of-service): "AI-generated content may have errors". OK. (The card's link is andisearch.com, which is the search app itself and loads fine.)
- semantic-scholar: https://www.semanticscholar.org/ (200): "A free, AI-powered research tool for scientific literature". OK.
- consensus: https://consensus.app/pricing/ (Chrome). After clicking "Monthly": "Pro ... $20/mo". Annual: "$12/mo $144 annually". "15 Deep reviews per month"; Free "10 Pro messages per month ... Up to 3 Deep reviews per month". OK.
- gpt-researcher: Apache-2.0, release v3.8.0 (2026-11-09), pushed 2026-11-12. README: "Takes ~5 minutes per deep research"; "OPENAI_API_KEY ... TAVILY_API_KEY". OK.
- ace-studio: https://acestudio.ai/pricing/ (Chrome): "HOLIDAY DISCOUNT 20% OFF"; "Artist RENT-TO-OWN ... $16.58/mo. 20% OFF $20.73 Billed yearly"; "Credit-Based Features 2500 credits/mo Music/SFX Generative Kits Music Video Video Composer Stem Splitter". The BUY tab is one-time only ("Artist $398 20% OFF $497.5"), so it is not a cheaper entry. No free plan shown. The list price is kept and the sale price is not published. OK.
- fish-audio: https://fish.audio/plan/ (Chrome). With "Billed Annually" switched off: "Plus ... $7.5 $15 mo First month 50% off". The card keeps the $15 list price, and the promo is not published. FAQ: "Free plan users can only use generated content for personal, non-commercial projects"; "Unused minutes do not roll over". Hugging Face: fishaudio/s2-pro and fishaudio/drama-3 are public (not gated), so open_weights stays true. OK.
- retell-ai: https://www.retellai.com/pricing: "$0.07-$0.31 / min for AI Voice Agents"; "$10 in free credits"; "Retell Voice Infra $0.055/minute"; "Retell Platform Voices $0.015/minute". OK.
- orpheus-tts: Apache-2.0, no releases, pushed 2025-12-05. README: "pip install orpheus-speech"; "family of multilingual models ... in a research preview". OK.
- sonix: see section 3.
- upscayl: https://upscayl.org/pricing (Chrome). With the slider at 100 credits, Monthly: "Pro Plan $9.99 100 credits / month". One-Time Purchase: "50 Credits $9.99". So $9.99 is the cheapest either way. README: "You'll need a Vulkan compatible GPU ... Many iGPUs (integrated graphics) do not work". AGPL-3.0, last release v2.15.0 (2024-12-25). OK.
- automatic1111: AGPL-3.0, release v1.10.1 (2025-02-09), pushed 2026-03-02. README: "4GB video card support (also reports of 2GB working)"; "you still must install python and git". OK.
- fooocus: GPL-3.0, release v2.5.5 (2024-08-12), pushed 2025-12-01. README: "Limited Long-Term Support (LTS) with Bug Fixes Only"; "4GB Nvidia GPU memory (4GB VRAM) and 8GB system memory (8GB RAM)"; "at least 40GB free space on each drive if you still see 'RuntimeError: CPUAllocator'". OK.
- photoroom: https://www.photoroom.com/pricing (Chrome). With the toggle on Monthly: "Pro ... $12.99 Per month 8,000 AI credits • 1,000 exports"; "Not included: Video for ads and product pages ... Not included: 4K images + HD video". Help center (https://help.photoroom.com/en/articles/12523455-free-accounts-and-commercial-use, 200): "You cannot use free accounts for commercial use", so a free account exists and free_tier true stands. OK.
- No promo price was published. No price comes only from a meta tag or JSON-LD.

## 3. sonix — price_from must change to Pay as you go; watch_out updated to match
https://sonix.ai/pricing (curl 200) lists "Pay As You Go For occasional projects $10/hr ... AI workspace usage: Not available" before "Core For individuals with steady needs $25/mo $275/yr ... 5 hrs/mo ... 1 user included +$25/mo per extra seat". It also says "Additional hours on any subscription plan are billed at $10/hr." Pay as you go is a real paid plan with no monthly fee, so it is the cheapest way to pay. The rule is that price_from is always the cheapest paid plan, and retell-ai and vapi already use this per-use shape. "30 min free trial No credit card required" is a trial, not a free plan, so free_tier stays false. The current watch_out is still true, but once price_from names Pay as you go it would describe only Core. The new text below keeps the Core facts and adds the one thing a reader loses on Pay as you go.

## Edits for the lead (apply on top of providers-019s.json)
- sonix | price_from | $10/hour of audio (Pay as you go, no monthly fee)
- sonix | watch_out | Pay as you go does not include the AI workspace tools. The Core plan is $25/month ($275/year) for 1 user and 5 hours a month; extra hours are $10/hour and extra seats are $25/month each.
- sonix | watch_out_source | https://sonix.ai/pricing (unchanged)
- All other 19 cards: apply as written in providers-019s.json.

## 4. Question-page ripples: none
I searched data/questions.json (every field) for "Sonix" and "Warp". Warp has no hits. Sonix appears on ai-that-transcribes-an-audio-file ("Sonix transcribes audio in 54+ languages and lets you edit the text in your browser") and on ai-that-adds-subtitles-to-videos ("Submagic and Sonix have no free plan"). Both stay true after the sonix edit, because free_tier stays false and no price is quoted.

## Housekeeping
- Browser: my own session ag019s-review (profile ~/.config/pw-aiguide-recheck). `close` printed "Browser 'ag019s-review' closed". `pgrep -f pw-aiguide-recheck` then printed nothing (exit 1).
- Read-only apart from this file and scratch files in /tmp/ag019s-review. I did not touch providers*.json, questions.json, any page, or /tmp/ai-wrapper/. No commit or push.
- Rung: Opus 5.5. An independent final review of published facts fits the Opus tier.
