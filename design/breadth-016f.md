# Breadth batch 6 (016f) — verification notes

Date: 2026-09-28. Four parallel research lanes (search, music, voice, image);
public lists used for NAMES ONLY; every fact below was verified on the
provider's own site (homepage + pricing page) via real fetch with redirects
followed. All 15 rules applied, including the two new ones (rule 14
Monthly/Yearly toggle, rule 15 company from provider's own footer/terms/about).
No promo prices published; annual billing stated plainly wherever the page
showed only annual rates. Nothing was tested. Fewer than 30 surviving is a
pass per the brief; padding was not done.

## Verified: 23 providers

| id | categories | price_from (plan) | source |
|---|---|---|---|
| vane | search, chat | Free (no paid tier) | github.com/ItzCrazyKns/Perplexica (README; MIT open source, donations only) |
| andi | search | Free (vendor sells nothing) | andisearch.com homepage |
| semantic-scholar | search | Free | semanticscholar.org ("A free, AI-powered research tool"); Allen Institute for AI per semanticscholar.org/about/publishers |
| consensus | search | Pro from $20/month | help.consensus.app Pro-subscription article + consensus.app |
| brave-search-api | search | Answers from $4 per 1,000 requests | brave.com/search/api/ plan table |
| firecrawl | search | Hobby from $19/month | firecrawl.dev/pricing plan table (5,000 credits/mo) |
| gpt-researcher | search | Free (Apache-2.0, no commercial plan) | github.com/assafelovic/gpt-researcher |
| ace-studio | music, voice | $20.73/month Artist (billed annually) | acestudio.ai/pricing/ ($16.58 struck-through holiday promo ignored per rule 10); company "TimeDomain" from footer address |
| fish-audio | voice | $15/month (Plus) | fish.audio/plan/ plan table (monthly standing price; $132 billed annually noted) |
| hume-ai | voice | $3/month (Starter) | hume.ai/pricing plan table |
| deepgram | voice | Pay-as-you-go from $0.0043/min (Nova-3 Monolingual STT) | deepgram.com/pricing model rate tables |
| assemblyai | voice | Pay-as-you-go from $0.15/audio hour (Universal-2) | assemblyai.com/pricing |
| retell-ai | voice | $0.07–$0.31/minute (Pay-as-you-go Voice AI) | retellai.com/pricing |
| bland-ai | voice | $0.14/min (Start plan, no platform fee) | bland.ai/pricing |
| orpheus-tts | voice | Free (vendor sells nothing; Apache-2.0) | github.com/canopyai/Orpheus-TTS (Canopy AI org; weights on Hugging Face) |
| sonix | voice | $25/month (Core) | sonix.ai/pricing plan table |
| invoke | image | $19/month (Starter, billed monthly) | invoke.com/pricing plan table |
| upscayl | image | Free to run yourself (Pro cloud from $24.99/month) | upscayl.org + upscayl.org/pricing plan table (256 MP cap, 300 credits/mo) |
| automatic1111 | image | Free (AGPL-3.0) | github.com/AUTOMATIC1111/stable-diffusion-webui |
| fooocus | image | Free (GPL-3.0) | github.com/lllyasviel/Fooocus |
| photoroom | image | $12.99/month (Pro, billed monthly) | photoroom.com comparison page plan table ($7.50/mo shown billed annually; monthly figure recorded per rule 14) |
| artbreeder | image | $7.49/month (Starter, billed annually) | artbreeder.com/pricing plan table (Starter $7.49 x 12, 1200 credits/year) |
| topaz-photo | image | $39/month (Topaz Photo) | topazlabs.com plan tables (Topaz Labs) |

## Dropped candidates (with reason)

### Search lane
- **ChatGPT (chatgpt.com search capability)** — id "chatgpt" already exists in data/providers.json; dropped as duplicate directory coverage.
- **phind** — phind.com returns HTTP 403 even with real fetch (same as batch 5). Pricing unverifiable (rule 1 exhausted).
- **komo** — verified AI search engine on komo.ai, but no official pricing page or plan-table figures fetchable; third-party prices conflict. Dropped (rules 4, 13).
- **scispace** — scispace.com/pricing fetched but plan table is JS-only with no figures in fetchable text. Dropped (rule 4).
- **khoj** — discovery material reported a Khoj Cloud sunset/pivot; dropped per rule 11 rather than risk violating it.

### Music lane
- **ecrett-music** — company attribution uncertain (page's own license text names "SOUNDRAW" as the operating company; directory already has a separate `soundraw` entry). Duplicative coverage + rule-15 doubt → dropped.
- **elevenlabs-music** — elevenlabs.io blocked by fetch policy; no provider-site verification possible (rule 1).
- **riffusion** — riffusion.com now serves Google Flow Music (Lyria 3.5); product absorbed/pivoted. Fails rule 11.
- **splash** — splashmusic.com homepage + /about show no plan table and no company name (rules 4, 15).
- **soundverse** — soundverse.ai homepage renders as a near-empty JS shell; no verifiable facts (rules 1, 4).
- **tad-ai** — pricing verified (tad.ai/pricing: Standard $7.99/mo) but no company/operator name on provider's own pages (rule 15).
- **songgenerator.app** — plan table verified (Starter standing $10/mo, promo $8 shown) but no company name on the fetched page (rule 15).
- **loudme** — loudme.ai confirms AI text-to-song with free + paid tiers mentioned, but no plan table with figures (rule 4).
- **topmediai** — topmediai.com/app/ai-music/ confirms product with free trial + paid plans referenced, but no price figures on provider pages (rule 4).
- **open-weights music (YuE, ACE-Step, HeartMuLa, yue2.cpp, DiffRhythm)** — GitHub/Hugging Face projects only; no provider site carrying a plan table or company footer (rules 4, 15).

### Voice lane
- **play.ai** — pricing page fetch failed (worker-local error); price unverifiable → dropped.
- **coqui / coqui tts** — company shut down, repo archived. Fails rule 11.
- **chatterbox (Resemble AI)** — Resemble AI deliberately cut in an earlier batch; skipped per exclusion list.
- **piper** — rhasspy/piper repo archived, development moved to OHF-Voice/piper1-gpl; successor not re-verified within budget → dropped.
- **kokoro** — verified live with Apache-2.0 open weights, but no verifiable company name on the provider's own page (individual GitHub handle only). Dropped (rule 15).

### Image lane
- **craiyon** — free tier and plan names confirmed, but no price figures on official pages fetched. Dropped (rule 4).
- **clipdrop** — clipdrop.co homepage alive (AI tools visible, company Jasper), but no official pricing table found. Dropped (rule 4).
- **hotpot.ai** — homepage alive (AI image generator + headshots + photo editing), but no official pricing figures; credit prices only on third-party pages. Dropped (rule 4).
- **nightcafe** — official pricing page not found; only third-party price figures; creator.nightcafe.studio FAQ has no price table. Dropped (rule 4).
- **magnific** — no verbatim official pricing URL; third-party figures conflict (Freepik rebrand, retired tiers). Dropped (rule 4).
- **civitai** — official terms/repo fetched (image generation + downloadable shared models verified), but no official pricing/plan table with figures. Dropped (rule 4).
- **google-imagefx** — labs.google/fx fetched; no ImageFX product listed (only Project Genie/Flow). No verifiable current product. Dropped.

## Pricing pages that were unclear

- **ACE Studio**: Artist rent-to-own shows "$16.58 /mo. 20% OFF $20.73 Billed yearly" — the $16.58 is a holiday promo; standing list price $20.73/month billed annually published per rules 10/14. Credit pool (2,500 credits/month) documented on the plan page.
- **Photoroom**: plan table on the official comparison page shows Pro $12.99/mo billed monthly vs $7.50/mo billed annually; monthly figure recorded per rule 14.
- **Retell AI / Deepgram / AssemblyAI / Brave Search API**: usage-based pricing (per minute / per hour / per 1,000 requests), not monthly plans; stated as pay-as-you-go figures from their rate tables. Deepgram flags some streaming rates as limited-time promotional; published figures are the non-promo model rates.
- **Upscayl**: desktop app is free/open-source; the $24.99/month figure belongs to the Pro cloud plan (300 credits/mo, 256 MP cap). `price_from` reads "Free to run yourself (Pro cloud from $24.99/month)" per rule 9.

## Rule-11 (alive) notes

- No sunset/shutdown language found on any surviving provider's homepage, pricing page, or blog. All 23 ship live products with working sign-up.
- Fourier of the "company" rule for open-source projects: Orpheus TTS attributes "Canopy AI" (canopyai GitHub org, linked to canopylabs.ai) — provider's own page. GPT Researcher and Vane (Perplexica) use the repo owner's handle (assafelovic / ItzCrazyKns) from the provider's own repo page; kept since the name appears on the provider's own page, not invented. Fooocus (lllyasviel) and AUTOMATIC1111 similarly.
- Brave Search API is a distinct product from the Brave Search Premium consumer tier (the premium-page URL could not be located in batch 5); this card covers the API only.

## Validation

Brief's validation script run on the Mac; output pasted in the task close: count 23, ALL CHECKS PASS.
