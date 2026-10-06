# breadth-016i notes (worker: Sonnet 5.5, 2026-10-06)

Shipped: 20 verified cards in data/providers-016i.json. Dropped: see below. No card is padded.
Method: curl with browser User-Agent for homepages, READMEs and terms pages; Playwright (rendered text, toggles clicked) for every price. GitHub API used for repo owner, archived flag, licence, last push.

## Shipped (price source and toggle state)
- yue (YuE2), diffrhythm-2, kokoro-tts, piper-tts, f5-tts, dia2, buzz, vibe, handy, stemroller, swarmui, easy-diffusion, krita-ai-diffusion: free open-source, no plan table. Prices stated as "Free" / "Free to run yourself".
- wispr-flow: pricing page opens on Annual. Clicked Monthly: Pro $15/user/mo (annual $12). Free plan word caps read from the compare table (2,000/week desktop, 1,000/week mobile). Company from Terms: Wispr AI, Inc.
- liner: Clicked Monthly: Pro $17.99 (annual $14.99). Company "Liner Corp." comes from the Privacy Policy (Terms name only "Liner").
- undermind: two tables. Academic tab (default): Pro $16 billed annually, $20 monthly. Industry tab: $75 monthly. Both recorded. Terms: Undermind AI, Inc.
- pixelcut: opens on Yearly. Clicked Monthly: Pro $10. Terms: Pixelcut Inc.
- typecast: opens on Monthly: Basic $5, free plan 3,000 lifetime credits (~5 min). Terms: Neosapience, Inc.
- jammable: Basic $8.99/mo list price; first-month $1.99 promo ignored. No free plan on the plan table. Terms: Jammable Limited.
- draw-things: Free edition + free community account + Draw Things+ $8.99/mo. Footer and privacy policy: Draw Things, Inc.

## Newer-version swaps (rule 22)
- Dia README says Dia2 released: carded Dia2 (nari-labs/dia2), not dia.
- DiffRhythm README lists DiffRhythm 2 with its own repo: carded ASLP-lab/DiffRhythm2.
- YuE repo is now YuE2 (original kept on YuE-v1 branch): carded YuE2. Weights CC BY-NC 4.0 with creator permission; companies need a licence.

## Dropped (with reason)
- Moises: pricing only behind sign-in (studio.moises.ai/billing/pricing redirects to login); /pricing redirects home. Price unverifiable.
- Soundverse: plan table has no figures, only a "30% off, limited time" banner.
- Felo: prices shown with "was" strikethrough discounts; list price unclear.
- OpenArt: promo banners, per-seat pricing, plan names/prices unclear.
- Fotor: "30% off / special offer" promo pricing on the plan table.
- LANDR: plan table did not render any figures; mostly a distribution/mastering service.
- Mage Space: plan table shows paid tiers only; not pursued further.
- Civitai: community model-sharing site, membership sells perks only; not a fit for beginners.
- Clipdrop: Terms and legal-notice pages render empty, so the legal entity cannot be read (rule 18). Footer says InitML; site banner says it is part of Jasper. Price was clear (Free / Pro $15).
- Morphic: site states no price or free-use terms; operator is "Shironel" (Tokyo corporation) per Terms.
- Khoj: pricing not found on its site.
- Forge (lllyasviel): no maker named in README, last push 2025-07-31.
- Producer.ai: redirects to flowmusic.app, already carded as flow-music.
- Podcastle: redirects to async.com (different brand/domain).
- Cloudflare blocked both curl and the browser (cannot verify, not bypassed): Craiyon, NightCafe, Phind, Genspark, Sider, Tensor.art, TTSMaker, TurboScribe, Freepik, Magnific.
- Samplab: no response. Hika: pricing 404. Lexica: pricing page empty. Superwhisper: /pricing 404. NaturalReader: pricing 404. Voicemod: pricing redirects to home. MacWhisper: price not on the store page (Gumroad, promo text). VoiceInk: no figures, "50% off" banner.
- Fetched but not pursued for time: SciSpace, Voice.ai, Notta, Aqua Voice, SeaArt, PixAI.

## Least sure of
1. krita-ai-diffusion: company is the repo owner handle (Acly); optional interstice.cloud service pricing sits behind sign-in so it is described without a price.
2. undermind: two audience-specific prices; reviewer should confirm the Academic/Industry tab behaviour.
3. Open-source cards whose "company" is a handle, not a legal entity (stemroller, easy-diffusion, vibe, handy, buzz): READMEs name no company.
