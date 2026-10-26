SHIP
Reviewer: Fable 5.1 (independent, fresh context). Date 2026-10-26. Read + verify only; no site file edited besides this one.
Why SHIP: all 6 changed cards and all 13 date-only cards match the provider's own page today (every one re-opened). The diff of providers-018u.json against providers.json contains exactly the fields listed in recheck-018u.md (6 watch_out, 1 price_from, 1 free_tier, 19 last_checked, 19 watch_out_source); nothing undeclared. No link changed and every link returns 200 or renders in Chrome. One small mechanical edit is listed under Required fixes (a pre-existing flow-music good_for clause the worker itself flagged as not on the page); it does not block the batch. iask-ai: the card's price can no longer be seen anywhere on iask.ai, so I recommend a fix (exact values below), not keep-old and not remove. Accuracy score: 9/10.

How I checked: curl with a Chrome UA for all 19 cards (30 URLs incl. pricing, home, docs and the Jan README; all 200 except vocalremover.org 403). Real Chrome (playwright-cli session ag018ur, headed, profile ~/.config/pw-aiguide-recheck, no sign-in anywhere) for stableaudio.com/pricing (+ roll-over FAQ opened), vocalremover.org and /next/pricing, mureka.ai/subscribe (Yearly default + Monthly toggle), loudly.com/music/pricing (Annual default + Monthly), boomy.com/pricing, flowmusic.app/pricing (Yearly default + Monthly), iask.ai/pricing. Session closed with `playwright-cli -s=ag018ur close`; `pgrep -f pw-aiguide-recheck` printed nothing (exit 1). Note: one playwright daemon hung after a `click "text=Monthly"` on Mureka; I killed only my own ag018ur daemon and its Chrome and reopened. Page texts under /tmp/ag018u/rv/ (curl *.txt, Chrome ch-*.txt). Progress log /tmp/ag018u/review-progress.log.

## Per-card lines (id | verdict | quote + URL)

exa | OK | "Search From $4 /1k requests"; endpoint table "Lite Search Auto Search Deep Search ... Base price, with up to 10 results (per 1k requests) $4 $7 $12"; "Starter Free $10 credits every month plus a $10 onboarding bonus. No payment method required"; "Start for free with over $120 in credits per year" https://exa.ai/pricing. Cheapest paid rate is Lite at $4, so the price_from change is right; the old "$20 at sign-up" is gone from the page, so the watch_out rewrite is right. free_tier true holds.

stable-audio | OK | "Free $0 50 credits a month About 12 full-mix generations or 8 multi-track generations a month Commercial license Start free"; "Solo $12/mo ... 660 credits/mo"; "The credit amount will reset to the monthly allocated amount every month."; FAQ opened: "Do my unused credits in one month roll over to the next? No, your unused credits don't roll over." https://stableaudio.com/pricing (Chrome; curl gets an empty JS shell). free_tier false -> true is right; price_from "$12/month (Solo)" is the cheapest paid plan (Session $30, Producer $90, Studio $199).

flow-music | OK | Chrome, Yearly (default): "Free $0 / month ... Daily top-up credits 2 concurrent generations ... Starter $6 / month Save 25%"; Monthly: "Starter $8 / month ... Plus $24 / month ... Member $64 / month" https://www.flowmusic.app/pricing. New watch_out matches; cutting "small" was right (word not on page). See Required fixes for the pre-existing good_for clause.

jan | OK | README: "macOS: 13.6+ (8GB RAM for 3B models, 16GB for 7B, 32GB for 13B)"; "Cloud Integration: Connect to GPT models via OpenAI, Claude models via Anthropic, Mistral, Groq, MiniMax, and others" https://github.com/janhq/jan. Home: "Download for Mac 7M + downloads, Free & Open source"; "v0.8.7 is now live on GitHub" https://www.jan.ai/. Free, open_weights true (open source), runs_on_your_computer true all hold. The new wording is more grounded than the old; fine to keep.

comfyui | OK | "Try Comfy Cloud for free. Upgrade when ready. 5 free runs on real GPUs ... STANDARD $16 $20 /month $192 billed yearly" https://comfy.org/pricing (Standard is the cheapest; Creator $28/$35). Cutting "takes real learning" was right (not on the page; skill_level "hard" keeps the warning). comfy.org home 200.

replicate | OK | "Free limits You can run select models on Replicate for free, but after a bit you'll be asked to set up billing. Some features are only available to customers with billing set up." https://replicate.com/docs/topics/billing; "You only pay for what you use on Replicate."; "black-forest-labs / flux-dev ... $0.025 / output image"; "black-forest-labs / flux-1.1-pro ... $0.04 / output image" https://replicate.com/pricing. "no flat monthly plan" is on no page, so cutting it was right. free_tier false is defensible: a few free runs before billing is a trial, not a plan (same call as Krisp in 018t).

musicgen | OK | "License: Code is released under MIT, model weights are released under CC-BY-NC 4.0."; "Downloads last month 155,155" https://huggingface.co/facebook/musicgen-small. Free, open_weights true, runs on your computer, non-commercial warning all hold.

tabby | OK | "Community Perfect for individuals, freelancers, and small teams Free Open Source ... Up to 5 users Local deployment"; "Team ... $19 /mo per seat ... Up to 50 users" https://www.tabbyml.com/pricing. Page also sells "Pochi" with "$20 in free monthly credits"; a different product, card unaffected.

gpt4all | OK | "Designed for developers, teams, and AI power-users, GPT4All runs open-source language models on Windows, macOS, and Linux"; "no cloud required, no data leaves your machine"; "Download for macOS ... Download for Windows ... Download for Ubuntu" https://www.nomic.ai/gpt4all. Nomic's "$20/month" banner is for its separate Individual plan, not GPT4All. Staleness (last release Feb 2025) is the lead's call; the card's facts hold.

anythingllm | OK | Home: "A private AI assistant that runs entirely on your computer. No accounts, no API keys, no token limits. Download Free"; "MIT Licensed. Open Source." https://anythingllm.com/. Cloud: "Self-host with Docker for free"; "Basic ... $50 /monthly"; "Pro ... $99 /monthly" https://anythingllm.com/cloud.

diffusionbee | OK | "DiffusionBee needs macOS 13.1 on higher. Machines with Apple silicon are recommended."; "Yes, DiffusionBee works with Intel based machines. Although it is very slow compared to M1 machines if you don't have a dedicated graphics chip."; "Download for macOS" https://diffusionbee.com/. The page states no price; "Free" rests on the download with no plan or price shown and the open-source license; pre-existing and acceptable. Footer "© 2024".

vocal-remover | OK | Chrome: "Free 10 minutes 8 minutes 100Mb"; "Month US$12.95"; "Year US$99" https://vocalremover.org/next/pricing; home banner "New version with better algorithms — currently available for subscribers only." https://vocalremover.org (403 to curl, renders in Chrome).

tavily | OK | "Researcher Free / month ... 1,000 API credits / month No credit card required"; "Pay As You Go $0.008 / credit"; "Project $30 / month" https://www.tavily.com/pricing.

goose | OK | "Open Source · Apache 2.0 · Agentic AI Foundation"; "Use API keys or your existing Claude, ChatGPT, or Gemini subscriptions via ACP" https://goose-docs.ai.

qodo | OK | "Pro Team $30 ... Free 14 Day Trial no credit card"; "$.012/credit, pooled across the team"; "~18 Reviews/Mo 2,500 credits ~36 Reviews/Mo 5,000 credits"; "Free for open source projects" https://www.qodo.ai/pricing/. The card's "$60/month for about 36 reviews" is 5,000 x $0.012, the page's own rate; acceptable arithmetic, not a guess.

pieces | OK | "$18.99 per user / month · billed monthly Save 25% yearly"; "Is Pieces free to use? No."; "Starting the 7-day Pro trial takes a card on file." https://pieces.app/pricing; home: "Pieces forms memories every 2 seconds from the apps you already use" https://pieces.app.

mureka-ai | OK | Chrome, Yearly (default): "Pro Plan $ 8.00 /month ... Billed $96 yearly"; Monthly: "Pro Plan $ 10.00 /month ... Cancel anytime"; "Premier Plan $ 30.00 /month"; compare table "4 songs, daily / 500 songs, monthly"; "Free model (v7.5-all)"; Pro "Unlimited MP3 downloads"; Premier "Unlimited downloads: WAV, Stems, MIDI & DAW session" https://www.mureka.ai/subscribe.

loudly | OK | Chrome, Annual (default): "Personal ... $8 / month Billed annually ($96/year)"; Monthly: "$10 / month Billed monthly"; "2,500 credits, refreshes monthly"; Free: "$0 / month No credit card required ... 1 download per day ... Non-commercial use"; "Get your music on Spotify, Apple Music, Amazon Music, YouTube Music" https://www.loudly.com/music/pricing.

boomy | OK | Chrome: "FREE $0.00 /mo ... 25 song saves No downloads No commercial use"; "CREATOR 33% off$14.99/mo $9.99 /mo ... 25 WAV downloads per month Full commercial use" https://boomy.com/pricing. Card shows the $14.99 list price with the discount note, same convention as dzine in 018t. Footer "© 2019-2023".

Spot-check for "entry price is really a higher tier" (the lindy error): none. Every price_from is the cheapest paid plan on its page (exa Lite $4, stable-audio Solo $12, comfy Standard $16, tabby Team $19, anythingllm Basic $50, mureka Pro, loudly Personal, boomy Creator, qodo Pro Team, pieces Pro, vocal-remover Month).

Plain words: the 6 new watch_out sentences read at 8th-grade level and stay inside their cited page. "Credits", "full-mix", "concurrent generations" are the pages' own words ("2 generations at a time" is a fair plain rendering of "2 concurrent generations").

## Required fixes

1. id: flow-music | field: good_for | new value: "Chat with an AI co-producer to make full songs with vocals, then publish and share them - the free plan tops up credits daily." | source: https://www.flowmusic.app/pricing shows "Free $0 / month ... Daily top-up credits" and nowhere says "no credit card"; the words "credit card" and "card" are absent from the page text (Yearly and Monthly views). Pre-existing clause, flagged by the worker in recheck-018u.md; under the never-guess rule it should go. Not a blocker for the other 18 cards.

No other field edits. All 19 cards in providers-018u.json can merge as written.

## iask-ai

Recommendation: FIX (not keep-old, not remove).
Evidence: https://iask.ai/pricing answers HTTP 302 "location: /" to curl, and in real Chrome `location.href` after loading it is "https://iask.ai/". /pro, /plans, /premium, /subscribe, /terms, /faq, /about, /help all redirect to the home page too. The home page text has 0 hits for "Pro", "Upgrade", "Premium", "subscri", "per month", "/mo" or "$9.95"; /privacy has no price either. The home page says: "iAsk AI is a free question AI search engine and AI homework helper"; "Download the iAsk app for fast, accurate, ad-free answers wherever you're working." So free_tier true is supportable; "$9.95/month (iAsk Pro)", "300 daily Pro searches" and "free tier has limited ads and uses the non-Pro model" are not visible anywhere on iask.ai today. Under the 2026-09-14 lesson (a price you cannot verify on the provider's own page is reverted, never guessed) the card should stop stating a Pro price. The service is live and free, so removal is too much.
Exact field values:
- id: iask-ai | field: price_from | new value: "Free (a paid Pro plan is not shown on the site)" | source: iask.ai home "iAsk AI is a free question AI search engine"; /pricing redirects to the home page.
- id: iask-ai | field: watch_out | new value: "iAsk calls itself a free AI search engine. Its pricing page now just sends you to the home page, so we could not confirm what the Pro plan costs." | source: same as above.
- id: iask-ai | field: link | new value: "https://iask.ai/" | source: /pricing returns 302 to /, so the home page is the page a reader actually lands on.
- id: iask-ai | field: watch_out_source | new value: "https://iask.ai/".
- id: iask-ai | field: last_checked | new value: "2026-10-26".
free_tier true, open_weights false, runs_on_your_computer false, good_for unchanged. If the lead prefers keep-old for one more cycle instead, the card stays at last_checked 2026-09-26 and is 30 days old today; I would not do that, because the $9.95 claim is now unsupported from the source.

## Ripples

Grepped data/questions.json (title, seo_title, meta_description, intro, how_picked, filter) for exa, stable-audio / stable audio, flow music / flow-music, jan, comfy, replicate. 94 pages.
CONFIRMED | free-ai-music-maker | filter {"categories": ["music"], "free_tier": true, "skill_level": "easy"} | stable-audio (music, easy, now free_tier true) joins this page automatically. Intro "Every tool here has a free tier, so you can try one before you pay." and how_picked "music AIs that have a free tier" stay true ("Free $0 50 credits a month ... Start free"). No edit needed.
CONFIRMED | ai-background-music-for-my-videos | intro | Names Mubert, Soundful, Ecrett Music only; nothing about Stable Audio's free plan, so nothing is wrong. The worker's optional add ("Stable Audio's free plan gives 50 credits a month with a commercial license.") is accurate and names only a provider already in the filter; lead's choice.
CONFIRMED | ai-site-with-many-picture-and-video-models | intro | "Replicate has thousands of models ... built for developers and billed per use." still matches "You only pay for what you use on Replicate." No edit.
CONFIRMED | ai-chatbot-on-my-computer, ai-that-keeps-what-i-type-private | intro + meta_description | Jan lines say it runs on your own computer and what you type stays there when you use local models; the new Jan watch_out (outside providers such as OpenAI and Anthropic for online models) agrees. No edit.
CONFIRMED | ai-that-writes-a-song-with-lyrics, ai-tools-from-google | intro + meta_description | Flow Music lines state no price or free-plan fact. No edit. (If the lead applies the flow-music good_for fix, no question page repeats the "no credit card" claim; grep for "credit card" near Flow Music: 0 hits.)
MISSED | none. No page names Exa or ComfyUI in any text field or filter.
