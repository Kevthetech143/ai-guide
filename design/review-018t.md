REVISE
Reviewer: Fable 5.1 (independent, fresh context). Date 2026-10-25. Read + verify only; no site file edited besides this one.
Why REVISE: all 7 changed cards and all 13 unchanged cards match the provider's own page today (every one re-opened). One field still needs a fix before shipping: rytr good_for says "marketing copy", and the words "marketing" and "copy" are no longer anywhere on rytr.me/pricing (the product is now sold as a follow-up assistant with writing as one feature), so under the never-guess rule the card and the one intro sentence that repeats it should be reworded. Krisp free_tier false and relevance-ai free_tier false both hold. No card should be removed; no service is shut down or business-only. The ripple list is right; I found no missed sentence in title, seo_title, meta_description, intro or how_picked for the 20 names.

How I checked: curl with a Chrome UA for all 20 pricing pages (all 200) plus relevanceai.com/pricing and krisp.ai home; real Chrome (playwright-cli session ag018tr, headed, shared profile ~/.config/pw-aiguide-recheck, no sign-in anywhere) for soundful (Monthly + Annual), getimg (Monthly + Yearly, FAQ opened), rytr (Yearly + Monthly), krisp pricing + help center (search "free plan", "How Krisp subscription works?", "AI Meeting Assistant overview"). Session closed; `pgrep -f pw-aiguide-recheck` printed nothing. Page texts under /tmp/ag018tr/pg/. Progress log /tmp/ag018tr/progress.log.

## Per-card lines (id | verdict | quote + URL)

relevance-ai | OK | "Note : The Free plan is retired for new signups and existing accounts. If your Organization was on Free, upgrade to Pro or Team to keep using it."; "Pro — $19 / month annual, $29 / month monthly"; "30,000 Actions / year (or 2,500 / month)"; "$240 Vendor Credits / year (or $20 / month)" https://relevanceai.com/docs/get-started/pricing. relevanceai.com/pricing shows only "Enterprise ... Talk to sales", so keeping the docs link is right. The old "takes genuine setup effort" is on neither page; right to cut.

copy-ai | OK | "Chat For small teams ... $29/mo Billed monthly"; "$24/mo Billed $288/yr" https://www.copy.ai/prices. Only "Try for free" (trial), no free plan shown.

soundful | OK | Chrome, Monthly: "Plus $9.99 Per user/month, billed monthly ... 100 MP3 & WAV downloads/month"; Annual: "Plus $4.99 Per user/month, billed monthly"; Free "1 MP3 download/month"; FAQ "Available Downloads/STEMs will reset every month" https://soundful.com/pricing/. Note for the lead: the page opens on the Annual toggle (button shows [pressed]), so a reader sees $4.99 first; the card's $9.99 monthly price follows the batch convention and the watch_out explains the $4.99, so fine.

getimg-ai | OK | Chrome, Monthly: "Entry $15 /month billed monthly, excl. tax"; Yearly (curl default): "Entry $ 15 /month $180 billed yearly, excl. tax"; "8 000 credits /month ... Access to selected models"; FAQ "Plan credits do not roll over to the next month."; "No, the API credits are not included in the subscription plans." https://getimg.ai/pricing. $15 is the cheapest paid plan on both toggles (Core is $35/$26); the old $8 yearly price is gone, so the price_from change is right.

augment-code | OK | "STANDARD $20 /month flat, no per-seat charge ... $20/mo of usage across LLM, Context Engine & compute ... Top-ups, pay as you go" https://www.augmentcode.com/pricing. "heavy coding sessions can burn through it" is a soft reading of "usage included + top-ups"; pre-existing, acceptable.

gumloop | OK | "Pro Starts at $37 / month Start 14 -day free trial"; "Included Credits 20k per month"; FAQ "What happens if I spend more than 20k credits mid-month?" https://www.gumloop.com/pricing. No free plan (trial only).

kagi | OK | "Starter 300 searches $5 /mo (+ Sales Tax)"; "Trial 100 searches Free" https://kagi.com/pricing. Entry price is the real cheapest paid plan.

kits-ai | OK | "Free ... $0 per month"; "Starter ... $10 per month ... 60 conversion minutes 2 voice slots 15 download minutes" https://www.kits.ai/pricing (kits.ai/pricing redirects here, 200).

listnr | OK | "Free ... $0 per month ... 1,000 credits to start"; "Individual ... $19 per month Billed $190 annually 20,000 credits/month ~2 hours of voice generation" https://listnr.ai/pricing.

ltx-studio | OK | "Free $0 Forever No billing 800 credits (one time)"; "Lite special offer $15 $12 /month Billed yearly $144 8,000 credits/month ... Exclusive limited time offer" https://ltx.io/studio/pricing.

dzine-ai | OK | Beginner "$ 8.99 /mo Billed monthly ... 1000 Credits / mo" (Annual: "$ 7 /mo $84 billed annually"); "Beginner: No rollover; Creator: up to 3 months"; "Top-up Credits are available for Creator plans and above ... Free and Beginner users cannot purchase Top-up Credits."; "New free users receive 100 Credits after sign-up, valid for 12 months. The previous daily reset to 32 Credits is no longer available." https://www.dzine.ai/pricing/. Only the Creator column carries "Credit Rollover ... Up to 3 Months"; the Beginner column has none, so the sentence holds. Note: the page also shows a "$ 4.49 / first month Then $8.99 /mo" promo on Beginner; the card's $8.99 regular price is the right one to show.

cartesia | OK | "Free $0 /mo ... 20K credits / month"; "Pro $5 /mo ... 100K credits / month"; FAQ "Paid users can turn on overages ... At pro tier, it's $65 per 1M credits." https://www.cartesia.ai/pricing (cartesia.ai/pricing redirects here, 200).

fireflies-ai | OK | "Pro ... $18 $10 per seat / month, billed annually ... Unlimited transcription Unlimited AI summaries 8,000 mins of storage/seat 20 AI credits"; Free "$0 Free forever ... Unlimited transcription* ... 400 mins of storage/team" https://fireflies.ai/pricing. The old "set number of transcription minutes" is not on the page; right to cut.

krisp | OK | Pricing page, curl and Chrome: "Free Trial Explore Krisp on your own. $0 Try it Free Test all premium features risk-free No credit card required Free for 7 days"; "Core Best for individuals and small teams $16 /mo/user $8 /mo/user" https://krisp.ai/pricing/. Settling the free-plan question: the pricing FAQ has no free-plan entry; help center search "free plan" returns 151 loose hits and none about a free plan, an exact-phrase search returns "Try searching another keyword."; "How Krisp subscription works?" talks only about paid monthly/yearly cycles https://help.krisp.ai/hc/en-us/articles/5626527210908-How-Krisp-subscription-works; "AI Meeting Assistant overview" names no plan. Home page says only "Get Krisp for free" (the trial button). No official page says an ongoing free plan exists, so free_tier false holds under the never-guess rule (unverified whether a signed-in account keeps working after day 7; I did not sign up). Krisp leaves any "free" filter pages; see ripples: none name it.

reclaim-ai | OK | Yearly view "Starter For small teams. $10 per seat/month"; Monthly view "Starter ... $12 per seat/month"; "Lite For calendar basics. Free Free forever" https://reclaim.ai/pricing.

jasper-ai | OK | "Pro: $59/month billed yearly or $69/month billed monthly (cancel anytime)." https://www.jasper.ai/pricing. "built for teams rather than casual use" is pre-existing; the page says "designed to meet marketers where they work" and sells seats, so it is a soft reading, not a new claim. Acceptable as is.

rytr | FIX: good_for -> "Writing emails and short posts in your own voice on a tight budget." (price_from, free_tier and the new watch_out stay) | Chrome, Yearly: "Lite Unlimited content creation $7.50 /mo billed annually"; Monthly: "Lite ... $9 /mo"; Free "10,000 characters per month ... 40+ writing use cases"; nav "Engage Relationships and follow-through / Create Writing in your voice"; headline "Know who needs you, and follow through" https://rytr.me/pricing. The words "marketing" and "copy" appear nowhere on the page, so the card cannot keep "marketing copy". It still writes emails and posts, so it can stay on ai-for-writing-marketing-copy with the reworded sentence below; cutting it from the page is also defensible, lead's call.

fathom-ai | OK | "FOR INDIVIDUALS Premium $ 20 $ 16 $ 20 /month / per user"; "FOR TEAMS Team $ 19 $15 $19 /month / per user (2 user min)"; "Free plan ... Sign up. Free forever." https://www.fathom.ai/pricing.

soundraw | OK | "Creator ... $16.99/mo $11.04/mo ... Download as mp3"; "Artist Starter ... $29.99/mo $19.49/mo ... Download as mp3"; "Artist Pro ... $35.99/mo $23.39/mo ... Download as mp3, wav, stems"; "Try it for free" https://soundraw.io/#pricing-section.

lalal-ai | OK | "Starter Always free Lite $7.5 /mo $90 billed annually Pro $15 /mo $180 billed annually Minutes in Relaxed Queue 10 Minutes Unlimited Unlimited Minutes in Fast Queue – 90 minutes/mo 250 minutes/mo"; "The VST plugin is available on the Pro plan only."; "Pro is the better choice if you need ... local processing in the desktop app" https://www.lalal.ai/pricing/.

Spot-check for "entry price is really a higher tier" (the lindy error): none found. Every price_from above is the cheapest individual paid plan on its page.

Plain words: all 7 new watch_out sentences read at 8th-grade level and stay inside their cited page. "Actions" and "vendor credits" (relevance-ai) and "AI credits" (fireflies) are the pages' own words; fine.

## Ripples (questions.json)

CONFIRMED | ai-for-building-my-own-ai-helper | intro | "Relevance AI builds no-code agents for multi-step work, though its builder still takes real setup effort." is wrong (claim not on the cited page, cut from the card). Replacement is good and names only Relevance AI, already on the page: "Relevance AI builds no-code agents for multi-step work, and its free plan is gone, so it starts at $19 a month on a yearly plan."
CONFIRMED | ai-that-automates-work-between-my-apps | intro | no change needed; the sentence does not claim a free plan. ("Gumloop has no free plan" also still true: 14-day trial only.)
CONFIRMED | ai-background-music-for-my-videos | intro | no change needed; Soundful free plan still exists.
CONFIRMED | free-ai-music-maker | intro | "Every tool here has a free tier" still true for Soundful ("Free ... 1 MP3 download/month").
WRONG (needs the edit, not a lead option) | ai-for-writing-marketing-copy | intro | "Rytr is a budget pick for short marketing copy and emails" repeats a claim the official page no longer makes. Replace with: "Rytr is a budget pick for writing emails and short posts in your own voice". Names only Rytr, already on the page. meta_description for this page ("Copy.ai, Jasper, Rytr and ChatSonic") needs no change.
MISSED | none. Grepped title, seo_title, meta_description, intro, how_picked and filter ids for all 20 names (relevance, copy.ai, soundful, getimg, augment, gumloop, kagi, kits, listnr, ltx, dzine, cartesia, fireflies, krisp, reclaim, jasper, rytr, fathom, soundraw, lalal). Other hits (gumloop x2, kits-ai, listnr, reclaim-ai, lalal-ai, copy-ai, jasper-ai) state facts that still match their pages. The "ltx" hits are about the LTX-2 model on run-on-your-computer pages, not LTX Studio.
