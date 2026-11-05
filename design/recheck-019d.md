# recheck-019d (2026-11-05) - batch 16, 20 oldest cards

Patch: /Users/admin/agents/ai-guide-brain/site/data/providers-019d.json (20 cards, merge by id). providers.json, build.py and pages untouched.

## Changed fields

- lm-studio | price_from | "Free" -> "Free (optional cloud plan, Bionic+, $20/month)" | https://lmstudio.ai/pricing | "Free $0 ... Bionic+ $20 USD / month ... Private, US-hosted OSS models" (a paid cloud plan now exists; the app and local models are still free)
- playground-ai | watch_out | "...limited to 10 images every 3 hours..." -> "The free plan is limited to 5 images every 3 hours and 6 credits a month, and runs slower at busy times, and the premium models use monthly credits." | https://playgroundai.com/design/pricing | "Free ... Create up to 5 images every 3 hours ... 6 monthly credits ... Slower generation during peak hours"
- elicit | price_from | "$11/month (billed annually)" -> "$11/month (Academic Plus plan, billed annually; $49/month on the Pro plan for everyone else)" | https://elicit.com/pricing | The page now opens on the "Industry" view: Basic free, Pro "$49 ... billed as $588 annually" ($75 monthly), no Plus plan. The "Academic" view in the same page's dropdown shows Plus "$11 ... billed as $132 annually" ($19 monthly).
- elicit | watch_out | -> "The free plan has limited usage for the Research Agent and Research Reports, and the $11/month Academic Plus price is billed as $132 a year; the Pro plan for everyone else is $49 a month, billed as $588 a year." | same page, same quotes
- invideo | free_tier | true -> false | https://invideo.io/pricing/ | The page lists only Starter / Plus / Max (+ Enterprise); no Free plan, no free credits shown. The docs (docs.invideo.io/account/plans, "Last updated Nov 2, 2026") say "Edits and exports are free. Generation and transcripts cost credits" and never mention a free plan. LOW CONFIDENCE: I could not open the sign-up flow (app.invideo.io returned Cloudflare 522), so unverified whether new accounts get free credits. Lead: keep false, or revert to true if you know better.
- invideo | price_from | "$20/month" -> "$20/month (Starter list price, billed monthly; the page currently shows 50% off with yearly billing, $10 a month)" | https://invideo.io/pricing/ | Monthly toggle: "$20 per seat/mo, billed monthly" (Plus $60, Max $250). Annual toggle: "50% OFF ... $20 $10 per seat/mo, billed annually" under a "Special offer" banner. Same $20 value as before, note added per the ace-studio rule.
- removebg | watch_out | "...until then, top quality needs credits ($3 for 3) or the $9-a-month plan." -> "The remove.bg website closes on 1 December 2026 and its background remover moves into Canva; subscriptions end then, and any unused pay-as-you-go credits expire." | https://www.remove.bg/faq | "From 1 December 2026 at 9:00am CET, remove.bg's standalone website will no longer be available. Background removal is moving to Canva and API access to Leonardo.ai"; "Your subscription will continue to work normally until 1 December 2026 at 9:00 a.m. CET and ends automatically after that. Any final renewal on or after 1 November is free."; "Any unused PAYG credits will expire on 1 December 2026."
- removebg | watch_out_source | https://www.remove.bg/pricing -> https://www.remove.bg/faq | the closing sentence is on both pages (banner), the subscription and credit facts only on the FAQ
- notebooklm | watch_out_source | (none) -> https://notebook.google/ | "The responses you get will always be grounded in the information you provide."
- all other 12 cards: only last_checked 2026-11-05.

## Flags for the lead (not applied)

- REMOVE.BG CLOSING (confirmed, official): standalone site ends 1 December 2026 at 9:00am CET (banner on https://www.remove.bg/pricing and https://www.remove.bg/faq). Card kept. Its pricing page no longer shows ANY price ($9/month, "$3 for 3" credits are gone; page now says "Free to try in HD", "Try Canva for Free", Enterprise API "Starts at 100,000 images per year"). Because price_from "$9/month" cannot be verified on the provider's own page, I left it unchanged AND left removebg last_checked at 2026-10-23 (so it is on the unverified list below). free_tier true is supported ("Basics, at no cost").
- NOTEBOOKLM RENAMED (official): notebook.google says "Yes. NotebookLM is now Gemini Notebook as of July 2026. It is the same product ... all of your existing notebooks remain fully accessible." (FAQ on https://notebook.google/). Site title now "Gemini Notebook"; link https://notebook.google.com/ still returns 200 (title "Gemini Notebook"). Card name NOT changed (rule: never rename). Free confirmed: help page says "Sign up free of charge by using your gmail account"; paid options are Google AI Plus / Pro / Ultra bundles (prices not on these pages). Lead decides on the name; if renamed, 6 question pages mention "NotebookLM" (see ripples).
- LM STUDIO: product now branded "LM Studio Bionic" (agent app); newest build Bionic 1.2.0, 5 Nov 2026 (lmstudio.ai/changelog). Free plan = local models via llama.cpp and MLX; the CLI repo lmstudio-ai/lms is MIT; open weights still downloadable (lmstudio-community on Hugging Face, e.g. Qwen3.8-27B-GGUF, apache-2.0, ~1.1M downloads). System requirements unchanged (16GB+ recommended, 8GB Macs possible with smaller models). Card name unchanged.
- HUGGINGCHAT: unchanged (PRO $9/month; free users get "None" monthly inference credits; HuggingChat page lists 127 models; Hugging Face hub up).
- ELICIT: the card previously showed the Academic price. If you prefer a single number, the non-academic cheapest paid plan is Pro $49/month billed annually.
- WINDSURF: still sold as Devin Desktop at devin.ai/desktop; Free $0, Pro $20/month, Max $200/month, Teams $80/month + $40/seat (devin.ai/pricing).
- PHOTOSHOP: $22.99/month annual billed monthly, 25 monthly generative credits; Creative Cloud Pro regular $69.99/month, intro promo $34.99 for 3 months, new subscribers only (card keeps list price).
- CHATSONIC: https://writesonic.com/chat still shows Free $0 and Individual $16/month billed annually, but its text names old models (GPT-4o, Claude 3.5) and Writesonic's main /pricing now sells GEO plans from $79; worth a later look at whether Chatsonic is being wound down. Price on the page is verified as written.
- POE: poe.com pricing is login-gated; only the official help article https://help.poe.com/hc/en-us/articles/19945140063636-Poe-Purchases-FAQs ("Poe offers access to all major models and more starting at $4.99/month", "Send far more messages than free users") was readable, shown as "Updated 4 months ago". $4.99 kept on that evidence.
- LINDY: Team $29.99/mo for 3,000 credits (cheapest paid, confirmed), Free = $50 credits for 7 days (free_tier false kept). FAQ now says "Monthly credits ... don't roll over. Top-up credits are yours until you use them." The card's "Credits do not roll over" is slightly loose; left as is.
- Watch items from earlier batches: none seen (hailuo, kling, v0, photoroom, onyx not in this batch).

## Per-card verification (all on the provider's own page, rendered in real Chrome where JS-only)

- duckduckgo-ai-chat: duckduckgo.com/pro Plus $9.99/month ($99.99/yr), Pro $19.99; Duck.ai help page lists free models plus Plus/Pro models. unchanged.
- huggingchat: unchanged (see above).
- lm-studio: price_from changed.
- lovable: Monthly toggle Pro "$25 / month"; Yearly toggle "$21 / month, billed annually"; FAQ "daily grant of 5 build credits (up to 30 a month)". unchanged.
- notebooklm: watch_out_source added.
- otter: Monthly toggle Pro $16.99; default Annual $8.33; Basic 300 monthly minutes, "3 lifetime audio/video file imports". unchanged.
- perplexity-comet: perplexity.ai/pro Pro "$17 /month when billed annually"; help table Free "Browser Agent (Comet Assistant) Queries: No". unchanged.
- photoshop-generative-fill: unchanged.
- playground-ai: watch_out changed. Pro Monthly "$15 / month", Annual "$15 $12 /mo" unchanged.
- poe: unchanged.
- removebg: see flags.
- windsurf: unchanged.
- aiva: Free EUR 0 (3 downloads/month), Standard "EUR 11 / month + VAT, billed annually", Pro EUR 33; copyright wording unchanged. The monthly-billing toggle would not switch for me (custom slider), so the monthly price is unseen; the card already says "billed annually". unchanged.
- botpress: Annual Plus "$150/mo billed annually"; Monthly toggle "$189/mo"; 250 conversations, packs of 100 for $65. unchanged.
- chatsonic: unchanged (see flags).
- colossyan: Professional yearly "$59/mo" (monthly toggle $89); Starter free; "No. ... your unused minutes will not roll over."; watermark removal listed on Professional. unchanged.
- elicit: changed.
- invideo: changed.
- kapwing: Pro annual "$16", Monthly toggle "$24"; Free "10 credits ... Unlimited exports with a watermark ... up to 4 minutes long ... 720p". unchanged.
- lindy: unchanged.

unchanged: duckduckgo-ai-chat, huggingchat, lovable, otter, perplexity-comet, photoshop-generative-fill, poe, windsurf, aiva, botpress, chatsonic, colossyan, kapwing, lindy
unreachable: none unreachable; removebg NOT stamped (price_from "$9/month" unverifiable on its own page, last_checked left at 2026-10-23)
checked: 19/20 fully verified and stamped 2026-11-05; removebg partly (shutdown date, free tier and FAQ verified, price not)

## Question-page ripples

Fields changed that appear in prose: lm-studio price_from, elicit price_from/watch_out, invideo free_tier/price_from, playground-ai watch_out, removebg watch_out. Searched intro, meta_description, title of data/questions.json.

- ai-that-runs-on-my-own-computer | lm-studio price_from | "Yes — Llama, Mistral, Stable Diffusion, and LM Studio run entirely on your own machine." | not wrong: the app and local models are still free; no fix needed | none
- ai-chatbot-on-my-computer | lm-studio price_from | "LM Studio, GPT4All, and Jan are desktop apps that let you chat with an AI on your own computer." | not wrong | none
- ai-that-keeps-what-i-type-private | lm-studio price_from | "(LM Studio also sells optional cloud models)" | still correct (Bionic+ $20/month cloud plan confirmed) | none
- ai-for-finding-scientific-papers | elicit | "Elicit builds evidence tables from over 138 million academic papers." | still correct ("more than 138 million papers" on the pricing page) | none
- ai-that-turns-a-blog-post-into-a-video | invideo free_tier | "InVideo makes a finished video from a text prompt. Pictory has no ongoing free plan, only a 14-day trial." | not wrong; InVideo also no longer shows a free plan, so the sentence is still true | none
- Filter pages (card lists, not prose): free-ai-video-generator (filter video + free_tier true) will drop InVideo; paid-ai-video-generator (video + free_tier false) will gain InVideo. Its intro says "None of them gives you free monthly videos, so expect to ..." which stays true for the named providers and for InVideo. No intro names InVideo there, so no fix.

Zero intros made wrong by the applied field changes. Advisory (only if the lead removes removebg or renames notebooklm):

- ai-that-removes-photo-backgrounds | removebg shutdown | "Remove.bg removes the background from a photo in seconds with one click. Photoroom, Pixelcut, and Clipdrop can do it too, and Clipdrop's free plan allows 20 uses per 24 hours." | the remove.bg site closes 1 Dec 2026 | "Photoroom, Pixelcut, and Clipdrop remove the background from a photo in seconds with one click, and Clipdrop's free plan allows 20 uses per 24 hours." (meta_description "Remove.bg, Photoroom, Pixelcut and Clipdrop" -> "Photoroom, Pixelcut and Clipdrop"; the filter ids list also needs removebg dropped)
- ai-for-editing-photos | removebg shutdown | "Remove.bg does one job brilliantly: cutting a person or product out of its background in seconds." (also meta "Adobe Firefly, Canva AI, Remove.bg and more") | site closes 1 Dec 2026 | drop the sentence; meta -> "Adobe Firefly, Canva AI and more"
- easiest-ai-image-generator | removebg shutdown | "Remove.bg and Photoroom help with photo jobs like removing a background." (meta lists Remove.bg? no) | site closes 1 Dec 2026 | "Photoroom helps with photo jobs like removing a background."
- NotebookLM name (if the card is renamed to Gemini Notebook): free-ai-voice-generator ("ElevenLabs, Murf AI, and NotebookLM all have free plans"), ai-for-homework-help ("Perplexity and NotebookLM also cite their sources"), ai-for-making-a-podcast ("NotebookLM can turn your notes into a lively two-host discussion"), ai-that-reads-documents-for-me, completely-free-ai-tools, ai-tools-from-google | the product name on the official site is now Gemini Notebook | replace "NotebookLM" with the new card name, same sentence otherwise (the replacement name is that card's own name, so it stays on the page).
