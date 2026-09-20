# ai-guide-016a — batch 1 breadth notes (DATA ONLY)

Verified: **30 of 30 shipped**, every price read from the provider's own official
pricing/product page this run (2026-09-19). Verification was split across four
research workers plus the assembler, each restricted to official domains only.
No prices from review sites, directories, or memory. `good_for`/`watch_out` are
original plain-English lines; nothing was claimed as tested.

Category spread: chat 4, voice 7, code 4, image 1, video 7, music 2, search 2, agents 3.

## Dropped candidates (name + reason)

- **Codeium** — codeium.com/pricing now shows Devin's pricing; the brand was absorbed into Devin (already in the directory), no standalone product remains.
- **Cody by Sourcegraph** — official pricing page lists no paid tier or price; enterprise-only, no public pricing.
- **Continue.dev** — discontinued after the Cursor acquisition; no live product or paid tier.
- **v0 by Vercel** — official pricing page shows only per-token model pricing ($0.20/1M tokens etc.), no subscription tier price.
- **Blackbox AI** — pricing page moved to a sales-commit token model; no self-serve paid tier price.
- **Recraft** — official pricing page shows plan names and FAQ only, no prices displayed.
- **Getimg.ai** — official pricing page shows plan names and credit amounts but no prices.
- **NightCafe** — pricing page unreachable this run (fetch failed).
- **StarryAI** — pricing page unreachable this run (fetch failed).
- **Phind** — phind.com failed to load three times this run; pricing unreachable.
- **Replika** — /pricing unreachable and the homepage shows no prices.
- **Khanmigo** — khanacademy.org/khan-labs sits behind a client-challenge bot wall; no official pricing verifiable.
- **ChatPDF** — FAQ confirms a "ChatPDF Plus" plan exists, but the pricing page was unreachable and no price appears on the official homepage.
- **Copy.ai** — official pricing page loaded but prices never render (JavaScript-only); no verifiable paid-tier number.
- **Vidnoz** — official pricing page rendered the plan table but dollar prices are JS-injected and never appeared in the page text.
- **Elai.io** — official pricing page showed only the $2/extra-minute top-up rate; plan prices did not render.
- **Fliki** — official page confirmed a free-forever plan but rendered paid plan prices as "…" placeholders.
- **VEED** — official pricing page rendered no pricing content at all (JS-only page).
- **Soundraw** — the pricing URL redirected to the marketing homepage with no pricing information.
- **Beatoven.ai** — pricing page failed to load.
- **Consensus (consensus.app, academic search)** — third-party figures conflicted ($10/mo, $11.99/mo, $19.99/mo) and no official page could be fetched this run; skipped rather than guessed.
- **D-ID** — official pricing pages (d-id.com/pricing, /pricing/api/, /pricing/studio/) render plan cards via JavaScript; no dollar price visible in fetched text.
- **Komo AI** — komo.ai/pricing requires sign-in and shows no plan prices; no paid price verifiable from the official source.
- **TTSMaker** — official homepage confirms a free tier (20,000 characters/week) and a "TTSMaker Pro" upgrade, but the official pricing page could not be fetched and no paid price appears anywhere on the official site text.
- **Voiceflow** — official pricing page shows plan descriptions ("free trial", "usage-based billing") but no dollar prices in the fetched text.
- **Boomy** — official pricing page could not be fetched this run; the $9.99/$29.99 tiers were only confirmed by third-party sources, which the task rules out.
- **Soundful** — official pricing page fetched, but prices render via JavaScript; no dollar amounts visible.
- **DreamStudio (dreamstudio.ai)** — official site failed to load in the fetch tool; no official pricing verifiable.
- **Microsoft Designer** — no official pricing/product page could be fetched this run.
- **Flowise** — considered then excluded: a search snapshot suggested a product sunset/EOL on 2026-08-31, needing official confirmation we did not have time to get.

## Pricing-clarity caveats

- **Scite**: plan cards are JS-rendered and did not render in the direct fetch; the $20/month (billed yearly) Basic price was read from the search engine's cached copy of the official scite.ai/pricing page. Single-source, official-domain.
- **Relevance AI**: dollar amounts sit in collapsed accordions that didn't render in the page fetch; $19/month (billed annually) Pro confirmed from the same official page's search-crawl content plus Relevance AI's own public docs repo (updated 2 days before this run). Single-source-confirmed.
- **Resemble AI** has pivoted from voice cloning to deepfake detection; the entry reflects the site's current offering honestly under ["voice"].
- **Tabnine** price is the annual-billed per-user price as written; no free individual tier is listed on the pricing page. **ChatSonic** is now folded into Writesonic. **AIVA / Mubert / Elicit / Scite** were verified by the assembler directly from official pages this run after a worker's tooling failed mid-run.
- **Pictory**'s plan-card prices did not render, but the official page title states "Pictory Pricing | From $25 per Month" — used for price_from; free_tier is false (14-day trial only, no ongoing free plan).

Nothing in this batch touches build.py, templates, CSS, pages, or deployment. The lead merges providers-016a.json into data/providers.json.

## Lead review + REVISE applied (2026-09-20, before merge)
An independent Opus 5 reviewer re-fetched 14 of the 30 prices from the official pages.
14 of 14 matched. Five things did not hold, and were fixed here — **30 shipped, 27 merged**:

1. **lovo-ai DROPPED** — lovo.ai returns HTTP 402 "Deployment Paused"; the whole site is down
   (verified twice by the lead with two user agents). A card cannot point at a dead site, and
   the $24/month could not be confirmed anywhere.
2. **resemble-ai DROPPED** — its `watch_out` claimed the company "pivoted from voice cloning to
   deepfake detection, so do not expect voice-generation features". False: their own pricing page
   still links live Resemble TTS, Voice Creation and STS products. The card was also a $350/month
   enterprise detection plan filed under "voice" — the priciest card in the batch, wrong for a
   beginners' guide.
3. **monica DROPPED** — the claimed US$8.3/month is not readable from monica.im/pricing. The raw
   HTML carries only coupon copy and an unfilled `$$var_price` template; plan prices load
   client-side. $8.3 was an inference, and the brief says drop what you cannot verify.
4. **synthesia watch_out FIXED** — it said the $29 Starter plan "only includes 10 minutes of video
   per month". The 10 minutes belongs to the FREE Basic plan (1,200 credits/mo). Starter is
   14,500 credits/year = up to 120 minutes of video per year (verified on the official page).
5. **Three links repointed to their real destinations** (each redirect confirmed by the lead):
   playground.com/pricing -> playgroundai.com/design/pricing;
   wellsaidlabs.com/pricing/ -> www.wellsaid.io/ai-voice-pricing;
   www.typebot.io/pricing -> typebot.com/pricing.

## Open finding for the NEXT batch (016b)
The reviewer spot-checked two "pricing page is JavaScript-only" drop reasons and **one was wrong**:
copy.ai/pricing plainly shows Chat $29/mo (annual $24/mo, billed $288/yr) in the page text. The
drop bar was too low. Before those stay dropped, retry with a browser-style fetch:
D-ID, Vidnoz, Fliki, Soundful, Voiceflow, Recraft, Getimg.ai — plus Copy.ai itself.
