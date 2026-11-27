# Review 019x (2026-11-27), reviewer ag019x-review (Opus 5.5)

## Verdict: SHIP, 9/10

The patch is clean and accurate. Only optional polish below; nothing blocks the merge.

## Structure check (verified by script)
- providers-019x.json parses as a JSON list of 20 cards, same 20 ids as the task.
- Every card has the same field set as its current card in providers.json (no added or removed fields).
- Only diffs vs providers.json: researchrabbit watch_out, plus last_checked "2026-11-27" on all 20.
- File ends with "}\n]\n" (indent=2 + trailing newline).

## researchrabbit change: CONFIRMED
https://www.researchrabbit.ai/pricing (curl 200): plan card "ResearchRabbit+ $10* per month $12.5* per month Annual plan Monthly plan"; features "Sync with Zotero", "Start with even more Seeds", "Filter your results", "Projects", "Alerts"; FAQ "the option to use up to 50 seed articles". The old "300 seed articles" figure is gone from the page. New watch_out is correct.
(Side note: the FAQ also says "default pricing ... is USD$10 per month" and "monthly payments". This conflicts with the plan card; the plan card was kept, which is right.)

## Spot-checks of "unchanged" cards (14 of 19), all on the maker's own page
- elevenlabs: https://elevenlabs.io/pricing "Free $0 /mo"; "Starter Billed yearly, $60 a year regular price $6 , now $5 /mo 2 months free Billed monthly $1 first month Then $6 per month". $6/month ($5 annual) correct. "$1 first month" and "Black Friday Up to 55% off ... Ends December 1" seen, not published, not in watch_out.
- grok: https://x.ai/pricing (real Chrome) "Free $0/month", "Plus $8/month", "Premium $30/month", "Limited Chat requests". Card correct. No Black Friday banner seen on this page today.
- gemini: https://gemini.google/subscriptions/ "Free $0 / month", "Google AI Plus ... $4.99 / month". Correct.
- perplexity: https://www.perplexity.ai/hub/pricing (real Chrome) "$0 /month Good for limited daily usage"; "$17 /month when billed annually". No monthly price on the page, so the annual-only wording stays.
- midjourney: docs page (real Chrome) "Monthly Price $10 $30 $60 $120", "Annual Price $96 ($8 / month)", "Stealth Mode, which keeps your images and videos private, is only available on the Pro and Mega Plans." No free plan listed. Correct (optional format edit below).
- scenario: https://www.scenario.com/pricing "Starter ... $15 /mo", "Pro ... $45 /mo ... Priority queue + unlimited relaxed generations ✓ Train custom models", FAQ "There's a free tier with 50 credits". Banner "Black Friday: up to 60% off yearly plans, until Nov 29" not published. Correct.
- taskade: https://www.taskade.com/pricing; Starter "$6 /mo Yearly $72 billed today for 1 year" (no monthly switch); Pro switched to monthly in real Chrome: "$20 /mo ... billed monthly"; table People "2 3 10", Agents "1 3 ∞", "Free keeps up to 3" apps, Pro "Unlimited automations". Correct.
- viggle: https://viggle.ai/pricing "Free $0.00 /month ... 1 video generation at a time ... 7-day asset & generation storage"; "Pro Was $9.99 ... 80 credits/month ... Permanent asset storage No watermark ... All models except Seedance"; "Live Was $19.99 ... Access to all models". Correct.
- stockimg-ai: https://stockimg.ai/pricing (real Chrome) "Starter Plan $12 /mo monthly billing 300 Credits per Month", "Premium Plan $24", "Ultra Plan $48 /mo ... Unlimited Credits per Month". Correct.
- mage-space: https://www.mage.space/membership "Basic $10 /month ... 500 Monthly Gems", "Pro ... $30 /month ... Unlimited Video Generation ... ControlNet", base models include "Flux 2". Correct.
- mistral: https://mistral.ai/pricing/ (real Chrome) Free "Limited messages and web searches"; Pro "$14.99 /mo" is the default (non-student) view. Correct.
- screenpipe: https://screenpipe.com/pricing, monthly toggle in real Chrome: "Basic Full personal history $25 / month or $250/yr annually"; Free "search recent work across apps and conversations". Default annual view shows Black Friday "$200 for the first year · renews at $250/year", not published. Correct.
- flux: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B "License: apache-2.0", "runs on consumer hardware, with as little as 13GB VRAM", "consumer GPUs like the RTX 3090/4070". watch_out still true. bfl.ai lists "FLUX 3 Image Klein ... open weights". The card's general "open weights" claim and the Apache-2.0 source stay correct; no card text is wrong.
- llama: https://dev.meta.ai/llama/ 200, still lists Llama 4/3/2 with Hugging Face and Kaggle download docs. Card is still true (see note below).

Open-source repos (GitHub API): Wan-Video/Wan2.2 Apache-2.0, not archived, pushed 2026-09-21; vladmandic/sdnext Apache-2.0, pushed 2026-11-26; deepbeepmeep/WanGP pushed 2026-11-26 (the old Wan2GP name redirects); wangp.ai: "Select models start at 6 GB of VRAM", "Paid hosting, SaaS, white-labeling ... require separate permission". All match the cards.

## Open calls: both decided, both stay free_tier false
- stockimg-ai: keep false. The plan table on https://stockimg.ai/pricing shows only Starter $12, Premium $24, Ultra $48 and Enterprise, with no free plan. The FAQ line "Stockimg AI offers a free account option with limited features" sits next to "$19 to $29 per month", which is out of date against the plan cards. No free allowance is stated anywhere, so it is not a real ongoing free plan.
- mage-space: keep false. The homepage says "Sign up and get 300 Gems to try any model". The membership FAQ says "Logged-in free users can use signup or purchased Gems", and also "$10 gets you 10,000 Gems". So it is a one-time sign-up bonus of about 30 cents of Gems that never refills, not a free plan.

## Screenpipe repo move
github.com/mediar-ai/screenpipe now 301s to github.com/screenpipe/screenpipe (not archived, pushed 2026-11-27). The card's link (https://screenpipe.com/) and watch_out_source (https://screenpipe.com/pricing) do not point at GitHub, so nothing on the card needs to change.

## Exact edits
Required: none.

Optional (format rule "monthly-first with the annual rate in brackets"; safe to apply):
- midjourney | price_from | $10/month ($8/month billed annually) | https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans | "Monthly Price $10 ... Annual Price $96 ($8 / month)"

## Question-page ripples
None. The researchrabbit watch_out and the optional midjourney price_from make no sentence in questions.json wrong. I searched title, meta_description and intro: ResearchRabbit has no matches, and the Midjourney sentences ("has no free plan", "makes beautiful art") are still true. The Viggle sentence "free credits that refresh every day" matches the page's "Free credits refresh daily".

## Notes for the lead (no edit)
- llama: Meta's dev site now leads with "Muse" models, including "Muse Spark Open", which it calls "the most capable open-weight model from a US lab", while Llama's last Hugging Face update was 2025-05. Llama is going quiet. The llama good_for clause "or through Meta's own apps" may be stale if the Meta AI app now runs Muse. Unverified: Meta's own pages I could reach do not say which model the app uses, and meta.ai returned 403. Muse Spark Open might also deserve its own card later.
- wangp watch_out ("not sell WanGP itself or offer it as a paid hosted service") is slightly stronger than the site's "require separate permission". It is acceptable as written.
- The worker reported a Grok "$30 / 2 months" Black Friday deal. I did not see it on x.ai/pricing today. It changes nothing, since list prices are already on the card.

## Process
Pages: curl, plus real Chrome via `playwright-cli -s=ag019xr` (profile ~/.config/pw-aiguide-review, no sign-in) for x.ai, midjourney, stockimg, mistral, perplexity, taskade and screenpipe. The session is closed, and `pgrep -f pw-aiguide-review` printed nothing (exit 1). providers.json, questions.json and the patch were not edited.
