# breadth-016j notes (worker: Sonnet 5.5, 2026-10-07)

Verified and shipped: 13 of 30 (fewer than 30 on purpose, no padding).
Shipped: msty, open-webui, brave-leo, lumo, antigravity, morphic, audimee, submagic, vidu, basic-pitch, crush, musicgpt, autogpt.
Categories added: search 1, music 3, video 2, code 2, agents 3 (antigravity, crush, autogpt), chat 4.

## Method
curl with browser User-Agent for static pages; Playwright (session ag016j) for JS pricing, clicking Monthly toggles. Company names read from Terms or Privacy legal-entity lines. Sunset keywords grepped on every shipped homepage (clean; AutoGPT hits were testimonials only).

## Dropped candidates and reasons
- Phind, Genspark, Wondera, Ecosia AI, Perplexity (already listed): Cloudflare or firewall challenge page in both curl and a real browser, cannot verify anything.
- Felo: monthly $14.99 shown next to struck-through "was $20.99"; looks like a promo, list price unclear (rules 10, 14).
- Khoj: app.khoj.dev says Khoj Cloud was sunset April 15, 2026 (rule 11).
- Pipali (Khoj team): "Free to try", billing after signup credits, no price anywhere on site.
- Roo Code: roocode.com redirects to roomote.dev, a different product; no standing Roo Code page.
- LibreChat: homepage banner says it is joining ClickHouse (rule 11 caution).
- Gemini CLI: geminicli.com says it was replaced by Antigravity CLI for the unpaid tier on June 18, 2026. Antigravity shipped instead.
- Trae: Lite/Pro prices shown with first-month and crossed-out figures, no free plan; plan table unclear (rule 10).
- Moises: pricing page requires login (redirects to auth).
- Soundverse: plan table has no figures, plus a "limited time offer" banner.
- LANDR: pricing page shows no figures; only "Starting at $8.25/month" on home, billing period not stated.
- BandLab: general music maker, not an AI product by its own page; membership price not shown.
- Hooktheory: AI is only an add-on (Aria AI); not an AI product by its own page (rule 12).
- AnswerThis: pricing page contradicts itself (Pro $35 vs a comparison table showing Pro $14, Max $100, with an Academia/Industry split).
- Gling: Terms and Privacy pages render empty in browser and curl, legal entity unverifiable (rule 18).
- Vizard: plan cards show "50% OFF" struck prices on both billing views, list price unclear.
- Dify: monthly price rendered as a rolling digit animation, could not read it; also developer-leaning.
- Asta (Ai2): site never states a price or "free".
- ThinkAny: Pro $20/month seen only in a sign-in popup, no plan table, no legal entity found.
- Agent Zero: site is built around a token/wallet/staking system, not a plain product.
- Pinokio: a launcher for third-party scripts, not an AI product by its own page; company unclear.
- Qwen Code: README does not name the company or any price.
- Wan2.2, LTX-2, HunyuanVideo, CogVideo, Mochi (open video models): skipped for time and because several need very large GPUs; company attribution for Wan not stated on README.
- Klang.io, Samplab, SynthesizerV (Dreamtonics 403), Sonauto (redirects to another domain), Neutone: no readable price or blocked.
- Audimee, Msty kept even though pages have toggles; both read at Monthly.

## Unclear pricing pages (shipped, but flag for the reviewer)
- Vidu: pricing page carries a banner "Plans will be upgraded on October 6" and add-on promos "until October 6". Prices were read from the plan table with Monthly Billing selected (Standard $10, Yearly view shows $8 billed yearly). Free plan details are mostly check-marks that do not survive text extraction, so the card only quotes 10 references/month (free) and 800 credits (Standard). Company comes from the Privacy Policy (Terms say only "Vidu Team").
- Brave Leo: free tier comes from the Leo page sentence "Brave Leo is free to use"; the Premium prices ($14.99/month, $149.99/year) come from brave.com/premium. Legal entity from the Terms of Use.
- Antigravity: only the $0 Individual plan has a price on the page; paid Google AI Pro/Ultra prices not shown, so none quoted. Company from Google Terms of Service (Google LLC).
- Msty: Aurum $149/year is billed yearly (no monthly price shown); lifetime $349. Free-plan "Limited" labels come from the feature matrix.
- Morphic: link is the GitHub repo. morphic.sh returns 403 in a real browser, so no hosted demo is mentioned. Maker "miurla" is the GitHub account; the README names no company.
- Crush: "Charm" from the README line "Part of Charm". Hyper pricing from hyper.charm.land.
- AutoGPT: pricing page default view is Monthly ($50.00 billed monthly, 7-day trial, card required). Company Determinist Ltd (trading as AutoGPT) from the platform Terms. The open-source self-host option is shown as a column on the pricing page.
- Basic Pitch: demo page loads in a real browser (basicpitch.io 301s to basicpitch.spotify.com). open_weights true because the model files ship in the repo (basic_pitch/saved_models, Apache-2.0).
- Lumo: Plus read after clicking Monthly ($12.99/month); Yearly view shows $9.99 billed $119.88 yearly.
- MusicGPT: Plus read after clicking Monthly ($11.99); default Yearly view shows $9.99 billed annually.
- Audimee: Starter read after clicking Monthly ($12); Yearly view shows $9 billed yearly. Company Audimee AB from Terms of Use.
- Submagic: Monthly view, "$19 /member/mo" for Starter; no seat minimum seen on the page. No free plan in the table (trial only), so free_tier false.

Nothing was tested by us.
