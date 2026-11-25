# Review 019v (2026-11-25) — reviewer ag019v-review (Opus 5.5)

## Verdict: FIX 7.5/10 (patch is accurate on 18 cards; both of the worker's open questions resolve to "yes, there is a free version", so Submagic and Pixlr need free_tier true, and two question pages say "Submagic has no free plan"). Apply the edits below, then it ships.

The patch matches HEAD 5280de2 except audimee watch_out, antigravity watch_out and last_checked. I checked this with a field-by-field diff of providers-019v.json against data/providers.json. No hidden edits. All 20 cards are in the patch.

## 1. The two changed fields
- audimee — OK on facts, small wording fix. https://audimee.com/pricing (real Chrome, FAQ opened): compare table "Conversion time per month: 15 min, one-time | 1 hr"; "Audio exports per month: Listen in the app only | 15 min"; free card "Text to Vocals ... No downloads"; FAQ "Free includes 15 minutes in total, and it doesn't refill."; Starter card "15 min download time per month", "1 hr conversion time per month"; "Save conversions: Not included"; "Audio quality: MP3". So "15 minutes of voice conversion in total (one time)" is right, and "15 minutes of Text to Vocals downloads" on Starter is right. But "in total (one time)" says the same thing twice and the bracket reads awkwardly. Use the page's own plain wording ("does not refill") and split the long sentence (edit 1).
  Price: Monthly tab "Starter $12 /mo"; the Yearly tab (default) is all Black Friday ("Was $12 $8.50 /mo", "$102 billed for the first year"). price_from "Free (Starter $12/month)" is the list monthly price. OK. No promo in the watch_out.
- antigravity — OK. https://antigravity.google/pricing: "For Individuals $0/month ... Baseline agent quota refreshed weekly"; Pro "higher 5-hour refreshed quotas"; Ultra "our highest quotas". Dropping "heavy users will hit the cap" (not on the page) is right. The page gives no Google AI Pro price, so price_from with no paid dollar figure is fine.

## 2. Paid web apps (all on the providers' own pages, list prices)
- typecast — OK. https://typecast.ai/pricing: Free "Lifetime download credits 3,000 credits (~5 mins)", "Attribution is required for all content downloaded on the Free plan"; Basic "$5 /month", "30,000 credits (~35 mins)". No promo.
- brave-leo — OK. https://brave.com/leo/: "Brave Leo is free to use"; FAQ "You can subscribe to Brave Leo Premium to get higher usage limits", "available in the Brave browser for desktop ... and mobile". Checkout https://account.brave.com/?intent=checkout&product=leo: "Monthly payment $14.99 /month", "$149.99 /year", "Leo AI is available exclusively in the Brave browser", "7-day free trial" (not on the card, fine).
- clipdrop — OK. https://clipdrop.co/pricing (real Chrome): Free "Background Removal 20/24h ... Text Remover 50/24h", Text to image / Uncrop / Replace Background not in Free; "Pro 15 US$ per month", "High Resolution Image Upscaler x16". No promo.
- domoai — OK. https://www.domoai.app/pricing (real Chrome, both tabs). Black Friday banner "Save up to 37%". Monthly tab: "Basic $11.70 $13 per month, billed monthly ... $11.70 first month · then $13/mo"; "Standard $37.80 $42 ... then $42/mo". So $13 and $42 are the list monthly prices; the card does not publish the sale. "600 Monthly credits ... (~150 images or ~85 videos)"; Standard "Unlimited Relax generations on supported models". No free plan on the page. OK.
- lumo — OK. https://proton.me/lumo: "Lumo AI Plus $12.99 $9.99 /month", "Billed at $119.88 every 12 months"; Free "Limited Max model usage, Limited messages & chat history, Limited image generations, 1 Project". The 23% yearly saving is standing, not a sale.
- submagic — FIX (free_tier). See section 3.
- vidu — OK. https://www.vidu.com/pricing (real Chrome, both tabs): Monthly "Standard $10 / month, 800 credits monthly"; Yearly "$8.25 / month ... Billed yearly as $99"; compare "Generate up to 200 videos"; Free "10 references/month". The "Limited-time offer 100 credits = $1.03" is a top-up credit price; not on the card. OK.
- musicgpt — OK. https://musicgpt.com/pricing (real Chrome). Yearly tab default is Black Friday ("Plus $9.99 $4.99 / month Billed annually"). Monthly tab: "Plus $11.99 / month", "Pro $21.99 / month ... Unlock all: Remix, Edit". Compare table "Monthly credits 500 credits | 5K credits", "Download cost 50 credits | Unlimited free", Plus "Create 100 songs /month". Card uses list prices. OK.
- pixlr — FIX (free_tier). See section 3.
- antigravity, audimee — section 1.

## 3. The worker's two open questions
- submagic: a real free plan, not only a trial. Submagic's own help centre:
  - https://care.submagic.co/en/article/how-much-does-it-cost-to-use-submagic-1xm83pa/ (updated 15/11/2026): table row "Trial | Free | Free | 15, one time | Trying Submagic out"; "The free plan gives you 15 credits once when you sign up, not every month. It needs no credit card, and exported videos carry a Submagic watermark."
  - https://care.submagic.co/en/article/does-submagic-have-a-free-trial-7opyg3/ (also updated 15/11/2026): "Yes. Submagic has a free plan that gives you 15 credits a month, enough for 5 video uploads with captions. No credit card is needed to start. Videos exported on the free plan carry a Submagic watermark."; "Your 15 credits reset at the start of each month."
  Both pages call it a free plan, with no card and no end date. That matches how we treat Typecast (lifetime credits only, free_tier true). So free_tier becomes true. The two pages disagree on whether the 15 credits come once or every month, so the card should not state the number; it states only the watermark, which both pages agree on. The pricing page shows no Free column but says "Try For Free" and "No credit card required".
- pixlr: yes, a free version with ads. https://pixlr.com/ FAQ: "Is it free to use Pixlr? You can enjoy Pixlr's free version, which offers a robust set of features that many users find satisfying without requiring an account or any charges. However, for those seeking additional content, advanced features, AI-powered tools, and an ad-free editing experience, we provide premium and plus options". The editors https://pixlr.com/x/ and https://pixlr.com/e/ load with config "ads":true. The pricing page https://pixlr.com/pricing/ lists Plus "Ad-Free", "$2.49 per month" (yearly "+ SAVE 20%", homepage "Plans start at just $1.99/month"). So free_tier becomes true and price_from gets the "Free (...)" shape.

## 4. Open-source / local cards: 9 of 9 checked (GitHub API + cited pages)
None archived.
- crush: v0.102.0 (2026-11-19), pushed today. https://hyper.charm.land/faq: "Where's the free plan? We've retired the monthly free Hypercredit allowance. You can still use Hyper without a subscription by purchasing prepaid credits whenever you need them for as little as five bucks." Pricing "Shred Diet $10 per month". OK.
- autogpt: platform beta v0.12.0 (2026-11-19). https://agpt.co/pricing/: "Pro 7-day free trial $50.00 / month billed monthly", "Scheduled workflow runs use your credit wallet, with a spending cap you can set for each Expert." OK.
- dyad: v1.24.0 (2026-11-23). https://www.dyad.sh/pro: "Basic Agent 20 messages/day", "full Pro Agent mode Starting at $20/month!". OK.
- yue: Apache-2.0 code, yue2-v0.1.6 (2026-09-09). README: "Linux · Python 3.12 · NVIDIA GPU with BF16 support and 24 GB VRAM."; "Commercial use by companies | Contact us to discuss a commercial license for the model weights." OK.
- open-webui: v0.13.5 (2026-11-25). Quick start lists "Open WebUI as an App"/Desktop, pip, Docker; "Connect a Provider". OK.
- morphic: Apache-2.0, v1.10.0 (2026-11-09). README "Docker (Recommended)", "set at least one AI provider API key". OK.
- stability-matrix: AGPL-3.0, v2.17.0 (2026-11-24). https://lykos.ai/membership: "Supporter $5 4,000 credits/mo", "Early access to dev + preview builds", "Credits are used for Prompt Amplifier, Image Analyzer, and other cloud features." OK.
- basic-pitch: Apache-2.0, v0.4.0 (2024-08-16), last push 2025-11-13 — going quiet, as the worker noted. README "Basic pitch works best on one instrument at a time", "generate a MIDI file". OK.
- msty: https://msty.ai/pricing/: "Free $0 Forever", "Aurum $149 USD per user / year", "Aurum Lifetime $349 USD per user". The "NEXUS PRO $399 LIMITED-TIME LIFETIME OFFER ... through November 30" is a different product and is rightly not on the card. OK.

## 5. Question-page ripple
Searched questions.json (title, intro, meta_description) for Submagic, Pixlr, Audimee, Antigravity.
- ai-that-adds-subtitles-to-videos intro says "Submagic and Sonix have no free plan". Now wrong for Submagic. Replace the intro with:
  "Submagic, CapCut AI, Kapwing, VEED, and Wisecut are video tools that add captions or subtitles for you. Sonix and Vibe turn the speech in a video into text and export subtitles, and Whisper can too but needs command-line steps. Sonix has no free plan, and the free plans elsewhere have limits: Submagic's and Kapwing's free exports carry a watermark, and Wisecut's free plan only exports at 480p."
- ai-for-editing-videos intro ends "Kapwing's free exports carry a watermark, and Submagic has no free plan." Replace the intro with:
  "CapCut AI, VEED and Kapwing are video editors with AI helpers built in, like captions, subtitles, voices and background removal, and Descript lets you edit a podcast or video by editing its written transcript, like a document. Wisecut cuts silences and adds subtitles on its own, and Submagic adds captions automatically. Kapwing's and Submagic's free exports carry a watermark."
- ai-for-short-videos-tiktok-reels: names Submagic, no free-plan claim. No change.
- Audimee (ai-that-sings-in-another-voice, ai-that-splits-a-song-into-instruments): no free-plan or price claim. No change. Pixlr and Antigravity: not named. No change.

## Edit list for the lead (apply on top of providers-019v.json)
1. audimee | watch_out | The free plan gives 15 minutes of voice conversion in total, and it does not refill. It is MP3 quality and personal use only, with no harmony maker, and you cannot save your conversions. On the free plan, Text to Vocals can be played in the app but not downloaded. Starter includes 1 hour of conversions and 15 minutes of Text to Vocals downloads a month.
2. submagic | free_tier | true
3. submagic | price_from | Free (Starter $19/month, or $12/month billed yearly)
4. submagic | watch_out | Videos made on the free plan carry a Submagic watermark. The $19/month Starter plan includes 45 credits (about 15 videos) a month and videos up to 2 minutes long. Automatic removal of silences and bad takes needs Pro ($39/month).
5. pixlr | free_tier | true
6. pixlr | price_from | Free (Plus $2.49/month, or $1.99/month billed yearly)
7. pixlr | watch_out | The free version shows ads. Plus removes them and adds 80 monthly AI credits, which cover about 80 fast AI images or about 16 higher-quality ones. Unlimited fast image generations (fair use applies) need the Ultra plan, which starts at $24.99/month.
8. questions.json | ai-that-adds-subtitles-to-videos | intro | (text in section 5)
9. questions.json | ai-for-editing-videos | intro | (text in section 5)
Everything else in providers-019v.json ships as written. watch_out_source stays as is for submagic and pixlr (the pricing pages carry the paid-plan facts; the free-plan quotes are in this review). Non-blocking: if the lead prefers the source to hold the free-plan sentence, use https://care.submagic.co/en/article/how-much-does-it-cost-to-use-submagic-1xm83pa/ and https://pixlr.com/.

## Housekeeping
- Browser: my own session ag019v-review (profile ~/.config/pw-aiguide-recheck). After `close`, `pgrep -fl pw-aiguide-recheck` printed nothing (exit 1).
- Read-only apart from this file. I did not touch providers*.json, questions.json, any page, or /tmp/ai-wrapper/. No downloads. No commit. Scratch pages are in /tmp/ag019v-review/.
- Rung: Opus 5.5. An independent final review of published facts fits the Opus tier.
