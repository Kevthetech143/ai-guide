# Review — breadth batch 6 (016f)

Reviewer: independent reviewer agent, 2026-09-28 (ET).
Method: curl with a Chrome UA and `-L` for every stored URL (status + final URL), HTML comments
and `<!-- -->` stripped before reading static text. Headless Chromium (Playwright) render for
JavaScript plan tables, with the Monthly / Yearly toggles (and Upscayl's credit slider) actually
clicked. Raw READMEs read for GitHub projects; GitHub API checked for archived / last push.
Every page scanned for sunset / shut down / joined / no longer accepting wording.
Nothing was edited except this file. data/providers-016f.json is untouched.

## Verdict: REVISE

4 keep, 13 fix, 6 cut. After fixes and cuts, 17 cards ship.

## Links
- 21 of 23 stored URLs returned HTTP 200 with final URL = stored URL.
- **vane**: github.com/ItzCrazyKns/Perplexica redirects to github.com/ItzCrazyKns/Vane (repo renamed).
- **invoke**: www.invoke.com redirects to `domaineasy.com/buy-domain/www.invoke.com` (HTTP 403, domain for sale).
- **topaz-photo**: topazlabs.com redirects to www.topazlabs.com.
- Consensus terms/help pages return 403 to curl and headless Chrome (Cloudflare); the terms-of-service page
  at /home/terms-of-service/ was readable and was used instead.

## Major defects the worker notes missed
- **Invoke is a dead product.** invoke.ai now says: "The Invoke.ai hosted platform has been shut down as the
  founding team joined Adobe." The $19 Starter plan no longer exists. The worker notes say "No sunset/shutdown
  language found on any surviving provider". That is wrong. This is exactly what rule 11 is for.
- **Two prices were read off the default Yearly view (rule 14):** Artbreeder (the page opens on Yearly; the monthly
  Starter is $8.99, not $7.49) and Upscayl (the "from" price uses the 300-credit slider default; 100 credits is $9.99).
- **Artbreeder is marked `free_tier: false`**, but its own page says it offers "unlimited usage for free".
- **Four wrong company names (rule 15):** Andi, Consensus, Fish Audio, Artbreeder (plus Orpheus and GPT Researcher).
- **Retell watch_out came from a competitor's page.** "$0.07/min covers voice infrastructure only" matches Bland's
  FAQ about Retell, not Retell's own pricing page.

## Verdicts

| id | verdict | what was checked / changed |
|---|---|---|
| vane | FIX | link -> `https://github.com/ItzCrazyKns/Vane` (renamed repo). Free confirmed: MIT, README asks only for donations/sponsors. README: "Using Docker is highly recommended" (Docker is not required) and it supports "local LLMs (Ollama) and cloud providers (OpenAI, Claude, Groq)". "No hosted support plan" is not on the page. watch_out -> "You install and run it yourself (the guide recommends Docker), then connect an AI model: Ollama on your own computer, or a paid key from a provider like OpenAI, Claude or Groq." |
| andi | FIX | Alive, AI search ("No ads, spam or tracking", "visual search results"). company -> `LazyWeb Inc.` (andiai.com/legal/terms-of-service: "operated by LazyWeb Inc."). Andi sells a paid **Search API** (andiai.com/api: "<1¢ Per query", "Outcome-Based Pricing"), so a bare "Free" breaks rule 9. The claims "No paid tier" and "unpublished usage caps" are false or unsupported. price_from -> "Free (a separate Search API for developers is paid per query)". watch_out -> "AI answers can contain mistakes (its terms say so), so check the sources it shows. Only the search site is free; the developer Search API is paid." |
| semantic-scholar | KEEP | "A free, AI-powered research tool for scientific literature, based at Ai2"; footer "The Allen Institute for AI". No paid tier. |
| consensus | FIX | Price verified by clicking Monthly: Pro "$20/mo" (Annual view: "$12/mo, $144 annually"). "15 Deep reviews per month" verified. "each reviewing up to 50 papers" is not on the pricing page; the help centre returns 403, so it can't be checked. company -> `Consensus NLP, Inc.` (terms: "Consensus NLP, Inc. Terms of Use"). watch_out -> "$20/month is the monthly price ($12/month if you pay for a year). Pro includes 15 Deep reviews a month; the Free plan gets 10 Pro messages and up to 3 Deep reviews a month." |
| brave-search-api | CUT | Developer-only. There is no app, only an API you must call from code, and a credit card is needed even for the free credits. A non-technical beginner can't use it. The facts are also incomplete: Answers is "$4 per 1,000 requests + $5 per million input/output tokens" (the token charge is missing). If the lead keeps it anyway: price_from -> "Answers from $4 per 1,000 requests plus $5 per million tokens ($5 free credits each month)", company -> `Brave Software, Inc.` (footer). |
| firecrawl | CUT | Developer-only. It's a scraping API that feeds web pages into AI programs, with no consumer use. Facts were correct: "Hobby: $19/month billed monthly, or $16/month billed annually", 5,000 credits, no rollover on Hobby, pay-as-you-go "Paid plans only". |
| gpt-researcher | FIX | Free confirmed: gptr.dev/pricing says "There is no SaaS subscription … No hosted SaaS from us today." Needs your own OpenAI + Tavily keys (README); "~5 minutes per deep research" and "Aggregate over 20 sources" are verified. company -> `GPT Researcher` (gptr.dev footer "© 2023–2026 GPT Researcher."; same pattern as aider/jan). |
| ace-studio | FIX | Artist rent-to-own: "$16.58/mo. 20% OFF $20.73 Billed yearly" under a "HOLIDAY DISCOUNT" banner. $20.73 (list price, billed yearly) is correct per rule 10. "2500 credits/mo" is verified. company -> `Timedomain Inc.` (footer "Copyright © 2026 Timedomain Inc."). |
| fish-audio | FIX | Monthly toggle clicked: Plus "$15 mo" (annual $11, "$132 billed annually"). Free plan is personal/non-commercial and minutes don't roll over: both verified. Downloadable weights confirmed (huggingface.co/fishaudio/s2-pro, s1-mini, not gated). company -> `Hanabi AI Inc.` (footer "Fish Audio © 2026 Hanabi AI Inc."). The homepage says "Speak 30+ languages", not 70+. good_for -> "Natural-sounding text-to-speech and voice cloning from as little as 10 seconds of audio, in 30+ languages; the company also shares downloadable models you can run yourself." |
| hume-ai | FIX | Starter "$3 / month" is verified. The Starter block lists "30,000 (~30 minutes)" of TTS and "40 minutes ($0.07/minute)" of EVI, and **no** "Additional EVI 3 cost" for Starter. The $0.07 is the per-minute value of the included minutes, not an overage rate. watch_out -> "Starter includes about 30 minutes of text-to-speech and 40 minutes of AI voice chat (EVI) a month; the price table shows no pay-for-more rate on Starter, so heavier use means upgrading." |
| deepgram | CUT | Developer-only speech API ("for your voice assistants and conversational AI applications"). Facts were correct: pre-recorded Nova-3 Monolingual $0.0043/min pay-as-you-go, and streaming rates are marked "Limited-time promotional". |
| assemblyai | CUT | Developer-only ("Try our API for free"). Facts were correct: Universal-2 "$0.15 /hr", Universal-3.5 Pro "$0.21 /hr", 99 languages. |
| retell-ai | FIX (keep with plain warning) | Kept because Retell's own homepage offers an "AI-powered no code studio" with a "drag-and-drop canvas". Price "$0.07-$0.31/minute" Pay-as-you-go, "$10 in free credits", "20 Free Concurrent Calls" are verified. The watch_out claim isn't on Retell's page: Retell lists "Retell Voice Infra $0.055/minute" and "Retell Platform Voices $0.015/minute". watch_out -> "Made for businesses building phone-answering bots. The real cost per minute depends on the parts you pick: Retell's voice engine is $0.055/minute, plus the AI model and the voice (Retell's own voices add $0.015/minute)." |
| bland-ai | CUT | Its own page labels the entry plan "FOR DEVELOPERS", and it overlaps Retell and the existing vapi card. Facts were correct ($0.14/min Start, $0 platform fee, 10 concurrent, 100 calls/day, Build $299/month). If the lead keeps it: company -> `Bland` (footer "© 2026 Bland."), free_tier -> `true` ("2 credits + an inbound number … No card required"). |
| orpheus-tts | FIX | Apache-2.0 weights on Hugging Face (canopylabs/orpheus-3b-0.1-ft, click-through gate) so open_weights true is right; Canopy sells nothing. company -> `Canopy Labs` (GitHub org name "Canopy Labs"; canopylabs.ai title "Canopy Labs"). The "needs a GPU / CPU is slower" claim isn't in the README; it offers a "No GPU inference using Llama cpp" path. watch_out -> "There is no app to click: you install it with Python commands and run it as code. The main models are English; other languages are only a research preview." |
| sonix | KEEP | Core "$25/mo" ($275/yr), "5 hrs/mo", "1 user included +$25/mo per extra seat" are verified; footer "© 2026 Sonix, Inc.". Optional: there is also a cheaper "Pay As You Go … $10/hr" option. |
| invoke | CUT | Rule 11. invoke.com is for sale; invoke.ai says "The Invoke.ai hosted platform has been shut down as the founding team joined Adobe." The priced $19 Starter plan no longer exists. The open-source app lives on and is community-run (Apache 2.0, pushed 2026-09-27), so it could be re-added as a free local app in a later batch. |
| upscayl | FIX | The Monthly tab is the default. The credit slider opens on 300 ($24.99); moving it to 100 credits shows "Pro Plan $9.99 100 credits / month". price_from -> "Free to run yourself (Pro cloud from $9.99/month)". The README says: "You'll need a Vulkan compatible GPU (Graphics Card) … Many iGPUs (integrated graphics) do not work". watch_out -> "The free desktop app needs a graphics card that supports Vulkan; many built-in (integrated) laptop graphics chips do not work." |
| automatic1111 | KEEP | AGPL, "4GB video card support", needs Python 3.10.6 and git (README). Not archived; last release v1.10.1 (2025-02). |
| fooocus | KEEP | README minimal requirements are 4GB Nvidia and 8GB RAM; "at least 40GB free space"; "Limited Long-Term Support (LTS) with Bug Fixes Only". All verified. |
| photoroom | FIX | The stored link is a blog comparison post, not the plan table. The real page https://www.photoroom.com/pricing (Monthly clicked) shows Pro "$12.99 Per month" (Yearly "$7.50 Per month, billed yearly"): price is correct. The 2000×2000 / 30 MB line comes from the blog's table, not the Pro plan. link -> `https://www.photoroom.com/pricing`. watch_out -> "Pro includes 8,000 AI credits and 1,000 exports a month; the Video Generator and 4K output are not included in Pro." |
| artbreeder | FIX | The page opens on Yearly. With Monthly clicked, starter shows "100 Credits / month $8.99". Yearly is "$7.49 x 12", 1200 credits/year. price_from -> "$8.99/month (Starter), or $7.49/month billed annually". The page says "Artbreeder is able to provide unlimited usage for free", so free_tier -> `true`. company -> `Morphogen, Inc.` (artbreeder.com/terms.pdf: "an agreement between you and Morphogen, Inc."). watch_out -> "Monthly Starter gives 100 credits a month (the page says about 1,000 images), and unused credits reset each billing period instead of rolling over." |
| topaz-photo | FIX | topazlabs.com/topaz-photo plan table: Monthly "Personal $39/mo"; Annual "Personal $17/mo $199 billed annually"; Annual-billed-monthly "$25/mo". The $1M revenue limit is verified. link -> `https://www.topazlabs.com/topaz-photo` (the stored link redirected). price_from -> "$39/month (Personal, billed monthly), or $199/year". |

## Developer-only APIs (asked to flag)
Cut: brave-search-api, firecrawl, deepgram, assemblyai, bland-ai. None of them has anything a
non-technical person can use without writing code. Their pricing is per 1,000 requests, per
minute or per hour of audio, and several need a credit card up front. Kept with a plain warning: retell-ai
(its own page has a no-code drag-and-drop builder). hume-ai is kept: it sells a $3 creator plan
priced by minutes of voice. The directory already has tavily, exa and vapi, so the lead may choose
differently. The facts on the cut cards were mostly correct; they were cut for audience fit, not accuracy.

## Not changed, for the lead to know
- Jargon for an 8th-grade reader: "TTS", "LLM", "DAW", "SDXL", "EVI" appear in several good_for lines
  (vane, ace-studio, hume-ai, automatic1111, fooocus). Suggest spelling them out at merge.
- Andi's search page currently shows "Apologies for search errors during recent upgrades!". It's alive, but worth a re-check.
- Batch count after this review: 17 cards (23 minus 6 cuts).
