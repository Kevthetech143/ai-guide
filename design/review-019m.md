# review-019m (batch 25) — Fable review, 2026-11-14

Verdict: FIX (applied by reviewer) -> SHIP. Score 8/10. No question-page ripples.
Patch backup: data/providers-019m.json.bak-2026-11-14-review

## Findings (one line each)
- mindstudio | KEEP card, REWORDED watch_out | Not a rename or shutdown. Pricing page headline says "MindStudio is now Remy", but the home page (mindstudio.ai) labels Remy "New product. From the team at MindStudio" with its own site (goremy.ai) and still leads with "Build powerful AI agents ... Start Building Free". Pricing page: "Or continue with legacy MindStudio / Legacy MindStudio plans", Free $0 + usage ("Get Free"), Individual $20/month + usage, $16 billed yearly ("Get Started"). Name, link and price_from stay. Worker's sentence was true but "promotes" / "lists these plans as legacy" is hard for an 8th-grade reader; reworded (below). Watch item: if the legacy plans stop taking sign-ups, the card needs a real rewrite.
- elevenlabs | FIXED price_from | Monthly-first rule (as applied since 019e/019f/019g). Real Chrome: Monthly billing Starter "$1 first month, Then $6 per month" (promo "Until Dec 1"); Yearly billing Starter "$6 -> $5 /mo, 2 months free". "$5/month (billed annually; $6 monthly)" -> "$6/month ($5/month billed annually)". $1 promo not published: right.
- suno | FIXED price_from | suno.com/pricing: Pro "$10 / $8 / month, Billed $96/year"; Free "No commercial rights". "$8/month (billed annually; $10 monthly)" -> "$10/month ($8/month billed annually)".
- runway | FIXED price_from | runway.com/pricing: Standard "$15 / $12 /month, Billed annually. Save $36/year."; Free "125 one-time credits". "$12/month (billed annually; $15 monthly)" -> "$15/month ($12/month billed annually)".
- perplexity | OK, stays annual-only | perplexity.ai/hub/pricing and /pro (real Chrome): Pro "$17 /month when billed annually"; no monthly price and no billing toggle on either page, so no monthly figure can be published. Free "Good for limited daily usage".
- hermes-agent | OK | Table on hermes-agent.nousresearch.com: Free "$0, pay as you go", Models "Free models only", Hosted tools "—" for Free; "All paid tiers include ... access to 200+ cutting-edge models, built-in tool use"; Plus "$20 / month". FAQ: "free and open source under the MIT license". Old "$0 of monthly credits" wording is gone from the page; cut is right.
- gemini | OK | gemini.google/subscriptions: $0, Google AI Plus $4.99 / month, Pro $19.99.
- midjourney | OK | Real Chrome: Basic Monthly Price $10 (annual $96 = $8/month); "Stealth Mode ... is only available on the Pro and Mega Plans". Card price is monthly already.
- mistral | OK | mistral.ai/pricing: Free "Limited messages and web searches"; Pro $14.99 /mo.
- flux | KEEP, no FLUX 3 mention needed | bfl.ai headlines FLUX 3; "FLUX 3 Image Klein ... open weights". The card names no version in good_for or watch_out, so nothing on it is wrong. Cited page FLUX.2-klein-4B still up: Apache 2.0, "~13GB VRAM". Next re-check: consider moving watch_out_source to the flux-3-image-klein model page (Hugging Face org lists it, created 2026-10-13).
- llama | OK, nothing newer | dev.meta.ai/llama (llama.com redirects there) lists Llama 4, 3.x, 2 only. Hugging Face meta-llama newest uploads are Llama 4 / Llama Guard 4 / Prompt Guard 2 (April 2025). Unverified beyond those two places.
- wondercraft / openclaw | OK | Creator $25 / $21, "Up to 720p export resolution"; "No subscription. No hosted tier."
- diff | OK | 20 cards, same keys and key order as live, file format exact. Non-date diffs after review: mindstudio watch_out, hermes-agent watch_out, elevenlabs / suno / runway price_from. All last_checked 2026-11-14.
- not re-fetched by me (worker's check stands, unverified by reviewer): grok, kimi, rork, qwant, reddit-ai-search, qwen, stable-diffusion.
- notes file | recheck-019m.md says "No change to ... price_from"; out of date after this review (3 price_from reorders).
- browser | session ag019m-rev closed; pgrep -f pw-aiguide-recheck printed nothing.

## Changes made to providers-019m.json
- mindstudio | watch_out last sentence | "The pricing page now also promotes a newer product called Remy ($99/month after a 30-day free trial) and lists these plans as legacy MindStudio plans." -> "The pricing page now puts a newer product called Remy first ($99/month after a 30-day free trial) and calls the plans above its older \"legacy MindStudio plans\"."
- elevenlabs | price_from | "$5/month (billed annually; $6 monthly)" -> "$6/month ($5/month billed annually)"
- suno | price_from | "$8/month (billed annually; $10 monthly)" -> "$10/month ($8/month billed annually)"
- runway | price_from | "$12/month (billed annually; $15 monthly)" -> "$15/month ($12/month billed annually)"

## Ripples
- None. Searched questions.json title / meta_description / intro for ElevenLabs, Suno, Runway, MindStudio, Hermes: no sentence quotes a price, credit count or plan name for any of them (Suno "free plan cannot be used for business" still true).
- Merge note: build.py offer_from_price reads the first dollar figure, so the structured-data offer for elevenlabs / suno / runway becomes 6 / 10 / 15 (same behaviour as every other monthly-first card).
