# review-019l (batch 24) — Fable review, 2026-11-13

Verdict: FIX (applied by reviewer) -> SHIP after one question-page ripple. Score 7/10.
Patch backup: data/providers-019l.json.bak-2026-11-13-review

## Findings (one line each)
- taskade | WRONG, reverted | The "Yearly" label on each plan card is a toggle. Clicked in real Chrome: Pro shows "$20 /mo, billed monthly, Save $120". FAQ on the same page: "Choose annual billing to save 50% compared with monthly billing on Pro, Business, Max, and Enterprise." Starter stays $6 / $72 billed yearly (yearly only). price_from and watch_out restored to the live values; taskade is now date-only.
- viggle | FIXED good_for | "5 videos a day" is not on viggle.ai/pricing. The Free column of "Daily free credits" reads "Refreshes daily"; the "5 credits" cells are Pro/Live/Max. FAQ: features use different numbers of credits. New last sentence: "The free plan gives free credits that refresh every day." Pro monthly $9.99 and Live $19.99 confirmed with the Monthly toggle.
- ecosia | FIXED watch_out | "try AI Chat without signing in" is not on ecosia.org/pricing (Free card says "Create an account"). The claim itself is true: signed out at ecosia.org/ai-chat I sent a message and got an answer. First sentence now: "The free plan asks you to create an Ecosia account and has daily limits on file uploads and Think longer mode."
- adobe-firefly | KEEP | Standard US$9.99/mo, 2,000 credits, free daily generations all on plans.html; source move is right. Promo (ends Dec 6) only touches Pro / Pro Plus; cheapest paid plan unaffected.
- capcut-ai | KEEP | Teams is USD 12.49 per seat with a 2-seat minimum (about $24.98/month), so Pro $19.99 is still the cheapest paid plan. 1200 credits and 1 TB on page.
- wangp | OK | "LTX 2.5", "Wan 2.1 / 2.2", "Qwen Image / 2.1", "Flux 3 Klein", "ACE-Step", 6 GB VRAM, Community License, no paid hosting: all on wangp.ai.
- screenpipe | OK | Monthly toggle: Basic "$25 / month or $250/yr annually"; Free "search recent work".
- brave-search | OK | Help page: ads, Premium ad-free, Brave browser only. Checkout page: $3.00/month, $2.50/month ($29.99/year).
- chatgpt | OK | Go $8/month "may include ads", Plus $20 (real Chrome).
- claude / claude-code | OK | Pro $17 annual, "$20 if billed monthly"; Claude Code row Free = No.
- diff | OK | 20 cards, same keys as live. Non-date diffs after review: wangp good_for, adobe-firefly watch_out_source, viggle good_for, ecosia watch_out. All last_checked 2026-11-13.
- not re-fetched by me (worker's check stands, unverified by reviewer): mage-space, magenta-realtime, researchrabbit, scenario, sd-next, stockimg-ai, wan-2-2, anara, fellou.
- notes file | recheck-019l.md still says taskade changed and last_checked 2026-11-12; both are out of date.

## Ripples
- ai-that-puts-a-character-in-a-video | intro | "...to make memes and short social videos, with 5 free videos a day." | not on Viggle's pricing page | "...to make memes and short social videos, with free credits that refresh every day."
- ai-you-can-use-without-an-account | intro | "Ecosia lets you try its AI Chat without signing in, but its full free features need a free account." | no change: verified true by a live signed-out test.
- taskade: none (card back to live values).
