# Re-check 019q (2026-11-20)

Patch file: data/providers-019q.json (19 verified cards as they should read after the merge; soundful is NOT in it, see unreachable). All 19 get last_checked "2026-11-20". No link changed. Every page returned 200 (or rendered in real Chrome). Pages checked were the cards' own watch_out_source pages. No card is open_weights or runs_on_your_computer; none changed.

## Changed fields
- copy-ai | price_from | "$24/month (billed annually)" -> "$29/month ($24/month billed annually)" | https://www.copy.ai/prices | Chat: "$29/mo Billed monthly" and "$24/mo Billed $288/yr". Reorder only (monthly first).
- fireflies-ai | price_from | "$10/month (billed annually)" -> "$18/month ($10/month billed annually)" | https://fireflies.ai/pricing | Pro: "$18 / $10 per seat / month, billed annually" (Monthly / Annual toggle). Reorder only.
- fathom-ai | price_from | "$16/month (billed annually)" -> "$20/month ($16/month billed annually)" | https://www.fathom.ai/pricing | Premium "$20 / $16 /month / per user" (Monthly / Annually). Reorder only.
- soundful | NOT patched (lead decides) | https://soundful.com/pricing/ now 301-redirects to https://soundful.com/, which says "Soundful is changing ... We're now taking Soundful in a new direction, and as part of that change, Soundful Studio will no longer be available to the public." No pricing page, no sign-up. The $9.99/month and free-plan facts cannot be verified. Recommendation: remove the card or mark it closed. Keeps last_checked 2026-11-07.

Reorder rule applied to those three; every other card was already monthly-first (or monthly-only).

## Verified, no change (price_from, free_tier and watch_out facts matched the page)
- narakeet: "The 6 USD package gives you 30 minutes ... top-up purchase"; free accounts: commercial use No; 20 conversions.
- wisecut: Starter (editing only) $19 monthly / $189 yearly (under "Explore plans without Autopilot"); Free 480p, exports up to 3 min; Starter+ $29, 300 credits, "1 credit = 1 processed minute". Promos seen, not published: Black Friday 30% off annual (wisecut30), 15% off first month.
- getimg-ai: Entry $15/month billed monthly, 8,000 credits, "Plan credits do not roll over", API credits not included in plans.
- augment-code: Standard $20/month, "flat 40% fee on LLM usage", top-ups pay as you go.
- gumloop: Pro $37/month, 20k credits, 8% orchestration fee, no rollover, overage $0.005/credit (14-day free trial only).
- dzine-ai: Beginner $8.99/month ($7 annual; $4.49 first-month promo not published); "Free and Beginner users cannot purchase Top-up Credits"; "New free users receive 100 Credits ... daily reset ... no longer available". Black Friday "40% Off Annual Plans" banner seen, not published.
- cartesia: Pro $5/mo, 100K credits; overages off by default, "$65 per 1M credits"; "new requests are blocked once your credits run out".
- relevance-ai: Pro $19 annual / $29 monthly, 2,500 Actions, $20 vendor credits; Free plan retired.
- kagi: Starter $5/mo, 300 searches; Professional $10 unlimited; trial 100 searches (free_tier stays false).
- kits-ai: Starter $10 monthly, 2 voice slots; Free $0 plan. link https://kits.ai/pricing redirects to https://www.kits.ai/pricing (200), left as is.
- listnr: $19/month, 20,000 credits (~2 hours); Free 1,000 credits.
- ltx-studio: Lite $15/month ($12 annual, $144/year), 8,000 credits; Free 800 credits one time. (Cyber Monday not seen.)
- krisp: Core $16 monthly / $8 annual; Free Trial 7 days only. Black Friday "55% off Annual Plans (KRISPBF2026)" seen, not published.
- reclaim-ai: Starter $12 monthly / $10 yearly per seat; Lite free forever.
- jasper-ai: "Pro: $59/month billed yearly or $69/month billed monthly"; 7-day free trial. Note for lead (no edit): the watch_out clause "built for teams rather than casual use" is not on the pricing page (page says Pro "Includes 1 seat"); it also matches the ai-for-writing-marketing-copy intro, so I left both alone.
- rytr: Lite $9 monthly / $7.50 yearly ("billed annually"); Free 10,000 characters/month.

unchanged: narakeet, wisecut, getimg-ai, augment-code, gumloop, dzine-ai, cartesia, relevance-ai, kagi, kits-ai, listnr, ltx-studio, krisp, reclaim-ai, jasper-ai, rytr
changed: copy-ai, fireflies-ai, fathom-ai (price_from order only)
unreachable: soundful (service closing to the public; keeps last_checked 2026-11-07)
checked: 19/20 verified (soundful checked but unverifiable)

## Question-page ripples
- No sentence is made wrong by the three price_from reorders (same numbers, new order); questions.json names Copy.ai only in ai-for-writing-marketing-copy (intro and meta_description) with no price.
- ONLY if the lead removes or flags soundful:
  - free-ai-music-maker | intro | "Mubert and Soundful make background music for videos, streams, and podcasts. Every tool here has a free tier..." | Soundful Studio is no longer available to the public | "Mubert makes background music for videos, streams, and podcasts." (name only providers already on the page; check Mubert is listed)
  - ai-background-music-for-my-videos | intro | "Mubert and Soundful make royalty-free background music for videos." | same reason | "Mubert makes royalty-free background music for videos."
  - ai-background-music-for-my-videos | meta_description | "...Mubert, Soundful, Soundraw and more..." | same reason | "...Mubert, Soundraw and more..."
