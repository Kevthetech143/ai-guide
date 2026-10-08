# breadth-016k notes (worker: Sonnet 5.5, local fallback after Muse timeouts)

Date: 2026-10-08. Shipped: 23 cards in data/providers-016k.json. Nothing was tested by us; all facts read from provider pages (browser User-Agent, Playwright for JS pricing, Monthly toggles clicked where one existed).

## Shipped (23) and what was read
- stability-matrix: lykos.ai/membership (Monthly toggle: Supporter $5/mo; Basic Free); company from lykos.ai/legal/terms ("Lykos, LLC").
- dyad: dyad.sh/pro plan table (Free / Pro $20/month / Max $79); footer "Dyad Tech, Inc." (ToS only says "Dyad").
- clipdrop: clipdrop.co/pricing (Free, Pro $15 per month, no toggle). Company "InitML" is the footer copyright; the Terms/Legal/Privacy pages render blank (even in a browser), so legal entity NOT confirmed from terms.
- pixlr: pixlr.com/pricing monthly view (Plus $2.49). No Free plan in the table (home says free) so free_tier=false per rule 21. Entity "Pixlr Pte. Ltd." from terms and privacy.
- domoai: domoai.app/pricing, toggle clicked to Monthly: Basic $13 billed monthly ($9 billed annually). No Free column so free_tier=false. Entity: footer "DOMOAI PTE. LTD." (ToS only says "DomoAI").
- magnific: magnific.com/pricing (Premium $20 monthly, $14.50 billed annually, "Save $66" matches). Entity from terms-of-use. Homepage magnific.com returns a 403 "security filter" page to curl and Playwright, so the link is the pricing URL, which loads.
- viggle: viggle.ai/pricing, Monthly clicked: Free, Pro $9.99, Live $19.99. Entity from terms-of-use.
- d-id: d-id.com/pricing/studio, Monthly clicked: Lite $5.9 (credit slider at lowest, 40 credits). 14-day trial is not a free plan, so free_tier=false. Entity from privacy policy; the Terms page content does not render.
- researchrabbit: researchrabbit.ai/pricing (Free; RR+ $12.50 on Monthly plan, $10 annual, price has an asterisk for country discount codes). Entity from Termly terms iframe ("Litmap Limited").
- wan-2-2: GitHub README (80GB / 24GB quotes are from the README). Hosted wan.video pricing (create.wan.video/pricing): Free; Pro $10 billed monthly ($5 billed yearly) read from screenshot. The hosted site runs newer models (Wan3.0) than the open weights; the card links the open repo.
- ltx-2: README of Lightricks/LTX-2 (LTX-Video README says LTX-2 is the primary home). Hosted LTX Studio Lite $15 (yearly $12) from ltx.io/studio/pricing. Repo license shows NOASSERTION on GitHub; card makes no license claim.
- local-deep-research: README only. Company is the GitHub org name; README names no company.
- stockimg-ai: stockimg.ai/pricing on Monthly: Starter $12. Footer "Stockimg AI, Inc."; Terms text says only "Stockimg AI". No Free plan in table.
- mage-space: mage.space/membership: Basic $10/month. Terms: "Ollano Inc." No Free plan in the membership table (home page says free to start) so free_tier=false.
- magenta-realtime: README and magenta.withgoogle.com/mrt2 (Apple Silicon requirement and file sizes quoted from the page). Entity: Google Terms of Service ("Google LLC"). The site shows no price anywhere; "Free" means no paid tier exists on the site.
- bolt-diy: README + LICENSE ("StackBlitz, Inc. and bolt.diy contributors").
- sd-next: README. Maker not named in README; company = repo owner handle.
- wangp: README + wangp.ai (free locally, license summary).
- klangio: klang.io/transcription-studio (Annual billing shown: Pro $8.33; struck-through $19.99 not used). Entity from imprint ("Klangio GmbH").
- google-flow: flow.google.com/about plan table (Free; Google AI Plus $4.99, "prices may vary by market"). Entity from Google Terms.
- scenario: scenario.com/pricing, Monthly default confirmed (Annual click showed $10). Entity from terms ("Scenario Inc.").
- base44: base44.com/pricing, Monthly clicked: Free, Starter $20. Entity from ToS ("Wix.com Ltd.").
- screenpipe: screenpipe.com/onboarding pricing, monthly clicked: Basic $25. Entity from terms ("Negentropy Labs, Inc. d/b/a screenpipe").

## Dropped candidates and reasons
- Felo: monthly and yearly prices shown as "was $20.99 / $14.99" promo prices.
- Vizard: prices carry "50% OFF" banners on both views; no standing list price confirmed.
- Soundverse: no plan figures in the pricing page, and a "limited time offer" timer banner.
- OpenArt: per-seat prices with many promo banners ("until Oct 14"); unclear.
- ImagineArt: "Biggest Sale Ever" 50% off banner.
- Fotor: price digits animate; yearly figure shown; unclear.
- Trae: "One-Month" tab with $0/$3 intro pricing; standing monthly price not confirmed.
- Bing Image Creator: no price or free statement on the page; Microsoft Copilot already has a card.
- Gemini CLI: geminicli.com banner says it was replaced by Antigravity CLI for unpaid and Google One users (June 18, 2026).
- Qwen Code: docs say the free Qwen OAuth is discontinued; price depends on separate Alibaba plans.
- Khoj: app.khoj.dev says "Khoj Cloud Has Been Sunset" (April 15, 2026).
- Roo Code and Demucs and Void: GitHub repos archived.
- Jules: pricing page shows no price figures (paid plans via a Google AI plan), no explicit "free".
- Asta (Ai2), STORM (Stanford): no price or free statement on the site.
- Moises: pricing page is behind login.
- AnswerThis: pricing tabs (Academia/Industry) conflict; unclear.
- Hotpot: pay-once credits and a 2-payment minimum on monthly, no free plan shown; not shipped.
- FlexClip: a video editor with AI add-ons, not clearly an AI product by its own page.
- BandLab: music studio, AI is a side feature.
- LANDR, Klangio-adjacent LANDR mastering: no prices on the page; Samplab: site certificate error; RipX: domain does not resolve; Neutone: plugin host, entity and price unclear.
- Blocked by Cloudflare/CloudFront for every fetch (could not verify, so not shipped): Phind, Genspark, NightCafe, Tensor.Art, Pollo AI, Craiyon, SciSpace, Presearch, Scholarcy, Sider.
- Lexica, SeaArt, Dreamina: no readable price page.
- Blackbox AI (per-token), CodeRabbit (team code review, per developer), Bito (contact-sales): not beginner apps.
- Local-only candidates not shipped for staleness: Farfalle (last push 2024), MindSearch (July 2025), FramePack (Oct 2025), HiDream-I1 (July 2025), Forge (July 2025).
- Mochi 1, Open Interpreter, Pinokio: not read deeply enough to ship.

## Pricing pages that were unclear
- Clipdrop: no Monthly/Yearly toggle visible; only "per month".
- Klangio: only the annual-billing view was read (toggle not found); monthly list price not used.
- Magnific, Wan hosted, Viggle, DomoAI, Pixlr: show a crossed-out price next to the discounted annual one; the monthly figure was cross-checked against the toggle or the "Save $X" line.
- Mage: no Free plan in the membership table but the home page says free to start.
- ResearchRabbit: price has an asterisk for country discounts.
