VERDICT: FIX (3 small edits in the patch, plus soundful removal ripples for the lead). Prices in the patch are all right.

# review 019q (batch 29), 2026-11-20, Opus reviewer

How I checked: curl with a Chrome UA on 11 of the 19 cards (all 200), plus real Chrome (playwright-cli -s=ag019qr, profile ~/.config/pw-aiguide-recheck, no sign-in) for the rytr Yearly toggle. Page texts in /tmp/ag019qr/. Sample: copy-ai, fireflies-ai, fathom-ai, jasper-ai, kagi, kits-ai, krisp, getimg-ai, listnr, rytr, cartesia.

1. copy-ai OK. https://www.copy.ai/prices: "Chat ... $29/mo Billed monthly" and "$24 ... $288/yr". No free plan on the page, so free_tier false is right. The watch_out is on the page.
2. fireflies-ai OK. https://fireflies.ai/pricing: "Pro ... $18 $10 per seat / month, billed annually", "8,000 mins of storage/seat 20 AI credits", Free "$0 Free forever".
3. fathom-ai OK. https://www.fathom.ai/pricing: "Premium $ 20 $ 16 ... /month / per user", "Team $ 19 $15 ... (2 user min)", "Free forever". Team at $19 a month is lower than Premium's $20, but it needs 2 users ($38 at least), so Premium is the cheapest plan one person can buy. The watch_out explains this. Keep.
4. jasper-ai FIX. Price OK: "Pro: $59/month billed yearly or $69/month billed monthly", "Start Free 7-Day Trial". "Built for teams rather than casual use" is NOT on https://www.jasper.ai/pricing. The page says Pro "Includes 1 seat", "$ 59 month/ seat", and "built for marketers". Exact edit:
   - watch_out: "The $59/month Pro price needs yearly billing; month-to-month is $69, and it is priced per seat."
   - Ripple, ai-for-writing-marketing-copy intro: "Jasper writes on-brand marketing content but is built for teams rather than casual use." -> "Jasper writes on-brand marketing content and is priced per seat, with a 7-day free trial."
5. kits-ai FIX. https://kits.ai/pricing redirects to https://www.kits.ai/pricing (200). The link must match the final URL, so: link -> "https://www.kits.ai/pricing". The watch_out_source already uses www. Price "Starter ... $10", "voice slot" limits and Free "$0 per month" are all OK.
6. rytr OK. In Chrome, clicking Yearly shows "Lite $7.50 /mo billed annually". Monthly is "$9 /mo". Free is "10,000 characters per month". The "$90 up front" is just $7.50 x 12. Note: the page's "Save 20%" would give $7.20, but the toggle shows $7.50, so keep $7.50.
7. getimg-ai OK. The page says "Entry $ 15 /month $180 billed yearly". The page data also says "8,000 product credits per month, billed monthly","price":15. So the price is the same either way. FAQ: "Plan credits do not roll over" and "API credits are not included in the subscription plans".
8. kagi OK: "Starter 300 searches $5 /mo". krisp OK: "Free for 7 days", "Core ... $16 /mo/user $8 /mo/user". cartesia OK: "Pro $5 /mo ... 100K credits / month", FAQ "Pro: $65 per 1M credits ... With overages off, new requests are blocked once your credits run out." listnr OK: "Individual $19 per month Billed $190 annually 20,000 credits/month ~2 hours", Free "1,000 credits". (The $190/year option is optional to add later, not an error.)
9. No promo price was published on any sampled card.

10. soundful: CONFIRMED shut to the public. https://soundful.com/pricing/ ends at https://soundful.com/ (200). The page says: "Soundful is changing ... We're now taking Soundful in a new direction, and as part of that change, Soundful Studio will no longer be available to the public." There is no pricing and no sign-up. Remove the card (as with hume-ai).
11. Soundful ripples. Mubert (music, free, easy) matches the free-ai-music-maker filter. Mubert and Soundraw are both in the ai-background-music-for-my-videos filter ids, so all the names below are allowed.
   - MISSED by worker, will break the build: ai-background-music-for-my-videos filter.ids lists "soundful". build.py check_rule_ids raises an error on an unknown id. Remove "soundful" from that ids list.
   - free-ai-music-maker intro: "Mubert and Soundful make background music for videos, streams, and podcasts." -> "Mubert makes background music for videos, podcasts, and apps." (This matches Mubert's card good_for. The worker's "streams" is not on Mubert's card.)
   - ai-background-music-for-my-videos intro: "Mubert and Soundful make royalty-free background music for videos." -> "Mubert makes royalty-free background music for videos." Worker's text is true. Keep it.
   - ai-background-music-for-my-videos meta_description: "Mubert, Soundful, Soundraw and more" -> "Mubert, Soundraw and more". Worker's text is true. Keep it.
   - No other question page names Soundful (I searched all 94 pages).

Browser: playwright-cli close said "not open" but left its daemon running (PID 65546, my own ag019qr). I killed only that one. `pgrep -f pw-aiguide-recheck` now prints nothing (exit 1).
