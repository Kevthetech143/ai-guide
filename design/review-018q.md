REVISE
Reviewer: Fable 5.1 (independent, fresh context). Date 2026-10-22. Read + verify only; no site file edited besides this one.
Why REVISE: every price, free_tier, link and runs_on_your_computer change in data/providers-018q.json matches the provider's own page (all re-opened today). Two small watch_out wording fixes (leonardo, n8n). Four question-page sentences need the ripple edits below. Nothing else blocks.

How I checked: curl for the open pages; real Chrome (playwright-cli session ag018qr, headed, own throwaway profile /tmp/ag018q/pw-profile because the shared ~/.config/pw-aiguide-recheck profile was held by another session, pid 9157; session closed when done) for the JS/Cloudflare pages: udio.com x2, ideogram.ai (FAQ expanded), leonardo.ai, hailuoai.video (plan pop-up, Yearly and Monthly), murf.ai (Studio tab, Billed Monthly switch), facebook.com/privacy/genai (accordion), meta.com/meta-one-plans (FAQ), n8n.io (Monthly), zapier.com (Pay monthly), replit.com (Monthly), ai.google.dev old Gemma page, google.com/aimode signed out, you.com. Page texts saved under /tmp/ag018q/. Progress log /tmp/ag018q/review-progress.log.

## Per-card lines (id | verdict | quote + URL)

udio | OK | Standard "$10 $8/month $96 billed annually"; Free "10 credits per day and 100 credits per month (no rollovers)", "Limit of 3 full length (2:10s) song generations per day". No "public" or "commercial" wording anywhere on the pricing page, so dropping the old claim was right. https://www.udio.com/pricing (JS, Chrome). Terms: "you may use Output solely for your personal and non-commercial purposes" with no plan carve-out that I could find. https://www.udio.com/terms-of-service

manus | OK | date only. Help page: "[Free Plan Price: $0/month] ... Daily Refresh Credits: 300 credits provided daily". https://help.manus.im/en/articles/11711111-what-is-the-current-membership-pricing-for-manus (200). manus.im/pricing is JS and I did not re-render it (worker's Pro "$20 / month" quote unverified by me; card unchanged anyway).

devin | OK | Free "$0 ... Light quota to code with agents"; Pro "$20 per month ... Increased quotas"; "Purchase extra usage at API pricing"; FAQ "you can purchase extra usage which is consumed at API pricing". No "computer time"/ACU wording on the page. https://devin.ai/pricing (200).

github-copilot | OK | "Free $0", "Pro $10 per month", "Free plan Limited chat and agent usage", FAQ "GitHub Copilot Free users are limited to 2,000 completions". https://github.com/features/copilot/plans (200).

replit | OK | Yearly: Core "$20 $18 / month, billed annually"; Monthly toggle: Core "$20 / month". No Free card on the pricing page. https://replit.com/pricing (200). Docs: "Create apps and publish your first project — all at no cost"; "Starter plan users receive daily credits for Agent usage, up to a monthly cap"; "Full build ... Starter plan builders can only use Lite build". https://docs.replit.com/billing/plans/starter-plan (200). free_tier true from docs is sound.

google-ai-mode | OK | "Without this setting enabled, you can still access AI Mode but can't pick up where you left off with previous searches"; "Tip: AI responses may include mistakes." https://support.google.com/websearch/answer/16011537 (200). Live check in a fresh signed-out Chrome profile: google.com/aimode loaded the AI Mode prompt box with only a "Sign in" link (I did not submit a question). Old sign-in claim was wrong.

ollama | OK | date only. Free "$0 ... Run models locally"; "Pro ... $20 / mo. or $200/yr billed annually". https://ollama.com/pricing (200).

deepseek | OK | "we directly collect, process and store your Personal Data in People's Republic of China." https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html (200).

ideogram | OK | Plus "$20 per month, $180 billed annually"; yearly table "Plus plan $15/mo"; "Pay as you go 1¢/credit"; FAQ "By default, all images on Ideogram are published ... Ideogram Plus and Pro subscribers can generate unpublished images"; "Eligible free accounts receive weekly credits when signing in with Google, Apple, or Microsoft; the amount may vary." https://ideogram.ai/pricing (curl 403, renders in Chrome; FAQ items must be clicked open).

leonardo | FIX: watch_out -> "It uses tokens instead of a simple price, so free users only get 150 tokens a day, and keeping pictures private needs a paid plan." | "150 a day" names no unit; a non-technical reader cannot tell 150 what. Page: Free "Fast Tokens 150 / day", "Creations access Public"; Essential "$12 /month", "Creations access Private". https://leonardo.ai/pricing/ (curl 403, renders in Chrome). Price unchanged, OK.

heygen | OK | Free "3 videos a month, watermarked"; Creator "Everything in Free, plus: 600 credits ... Remove HeyGen branding". https://www.heygen.com/pricing (200).

luma | OK | Plus "$30 /month $300 billed yearly"; no free plan listed; "20 credits/5 sec 60 credits/10 sec". https://lumalabs.ai/pricing (200). Old link 200-redirects to /pricing.

hailuo | OK (note) | Free "$ 0.00 /month ... 0 credits monthly ... One-time free trial credits"; Standard list price "$14.99" is struck through in both views: Yearly "44% OFF $ 8.40 /month $100.80 billed yearly", Monthly "30% OFF $ 10.50 /month $10.50 billed monthly". No end date shown for the discount. Same situation as kling in 018p (list price kept), so $14.99 is defensible, but today's page charges $10.50 monthly; lead may prefer price_from "$10.50/month" + watch_out "...the cheapest paid plan (Standard) is listed at $14.99 a month but was on sale for $10.50 when we checked." Header "From $9.99 /mo" untraceable, same as worker. Watermark row could not be read per plan (column layout), so dropping it was right. https://hailuoai.video/subscribe (pop-up over home page, Chrome).

murf | OK | Studio tab, Billed Yearly: Creator "$19 / month $228 Billed Annually"; Billed Monthly switch: Creator "$29 / month"; Free "10 minutes of Voice Generation", "(No Downloads) No Commercial Rights". Note: the pricing page opens on the API tab; the Studio tab must be clicked to see these. https://murf.ai/pricing (JS, Chrome).

microsoft-copilot | OK | "Microsoft 365 Personal $9.99 /month" with "Advanced Copilot chat with higher usage than free"; "Microsoft 365 Family $12.99 /month"; "Microsoft 365 Premium $19.99 /month" with "Advanced Copilot chat with extensive usage". https://www.microsoft.com/en-us/copilot/solutions/individuals (curl 200 for me with a browser UA). Old link now lands on https://www.microsoft.com/en-us/microsoft-365/copilot-learning-center (no prices). $19.99 -> $9.99 and new watch_out confirmed; "Copilot Pro discontinued" is not on the page, dropping it was right.

meta-ai | OK | Accordion "Where does Meta get training information?": "Information shared on Meta Products including things like posts or photos and their captions, and your interactions with features that are part of AI at Meta"; same panel also says "We do not use the content of your private messages with friends and family". No "opt out" wording. https://www.facebook.com/privacy/genai/ (curl 400, renders in Chrome). price_from Free holds: FAQ "Is Meta AI still free? Yes. Meta AI is free for everyone." https://www.meta.com/meta-one-plans/ (curl 400, renders in Chrome).

zapier-ai | OK | Pay yearly: Professional "Starting from $19.99 /month"; Pay monthly: "Starting from $29.99 /month"; Free "$0 /month ... (100 tasks per month)", "Two-step Zaps". https://zapier.com/pricing (200).

n8n | FIX: watch_out -> "It's built for technical users, so the first setup can feel hard if you've never made a workflow before; the cloud plan costs $24 a month, or $20 a month if you pay for a year, or you can run it on your own computer for free." | price_from now leads with $20 but the watch_out still only says "$24 a month"; both numbers are on the page: Annually "Starter ... $20 /mo, billed annually"; Monthly "$24 /mo, billed monthly". https://n8n.io/pricing/ (200). Note: plain curl from here showed "20€ /mo" (currency is geo-based); US Chrome shows dollars.

gemma | OK | "Intended Platform: E4B Mobile devices and laptops; 12B Laptops, desktop computers and small servers"; Run paths "Ollama, llama.cpp, LM Studio, MLX". https://gemma.ai/get-started/ (200). Old page banner: "This documentation is deprecated. Please visit the new documentation at gemma.ai." (renders in Chrome; plain curl 302s to a Google sign-in). runs_on_your_computer true is correct; watch_out ("raw model ... technical tools") still fits.

## watch_out_source URL check
All official domains. curl 200: udio, devin, github, replit docs, support.google, heygen, lumalabs, hailuoai.video, murf, microsoft, zapier, gemma.ai, cdn.deepseek. curl blocked but render in Chrome: ideogram (403), leonardo (403), facebook.com/privacy/genai (400). None dead.

## Ripples (data/questions.json; exact replacement text)
Confirmed:
1. ai-that-writes-a-song-with-lyrics | intro | last sentence "Songs made on the free plans of Suno and Udio cannot be used for business." -> "Songs made on Suno's free plan cannot be used for business, and Udio's terms say its songs are for personal use only, not business." (Suno Free "No commercial rights" per 018p; Udio terms quote above, not plan-specific.)
2. ai-i-can-use-in-whatsapp | intro | first sentence -> "Meta AI is free and already lives inside WhatsApp, but Meta says your chats with its AI can be used to train its AI, so avoid sharing private details." ("unless you opt out" is not on Meta's page.)
3. ai-tools-from-meta | intro | first sentence -> "Meta AI is free and lives inside WhatsApp, Instagram and Messenger, but Meta says your chats with its AI can be used to train its AI, so avoid sharing private details."
4. ai-that-keeps-one-art-style | intro | "though free users get only 150 credits a day" -> "though free users get only 150 tokens a day".
Not needed (soft, worker right to flag only): free-ai-image-generator intro and ai-for-making-logos meta still fine (Ideogram FAQ keeps a free weekly-credit account; free_tier stays true). ai-that-runs-on-my-own-computer and ai-chatbot-on-my-computer: intros do not name Gemma; Gemma joining the list is fine.
Missed by worker: none in this batch. FYI outside this batch: ai-that-is-fun-to-play-with intro says Grok "need[s] an X account to sign in"; 018p review found no X-account wording on x.ai/pricing.

## You.com finding
you.com public site is API-only today. Home: "The Leading Web Search APIs for AI". Pricing headline: "Web Search APIs, priced per call" (Free tier "No API key, no account, no credit card", Standard "$5 /1k calls"); no Pro/Max consumer plan anywhere. https://you.com/search?q=test redirects to https://you.com/signin?redirectUrl=%2Fsearch%3Fq%3Dtest, so a consumer chat/search still exists behind sign-in, but its price is not published. No official shutdown notice found; third-party reviews conflict (one says consumer subscriptions retired, others say the chat app still runs with unpublished pricing). Verdict: the card's "$15/month (billed annually; $20 monthly)" and the daily-limit watch_out cannot be verified from any official page. Lead decides; if kept, suggested watch_out: "You now have to sign in to use it, and You.com no longer shows a price for the chat and search app on its website; its public pages only sell search tools for software developers." and price_from "Free (paid plan price not published)". The two question pages (ai-search-engine, ai-search-that-shows-its-sources) say You.com is free with sources; safest is to drop You.com from those sentences if the card is removed.

## Ship list
Ship as patched: udio, manus, devin, github-copilot, replit, google-ai-mode, ollama, deepseek, ideogram, heygen, luma, hailuo (note), murf, microsoft-copilot, meta-ai, zapier-ai, gemma.
Apply the two FIX watch_out strings above: leonardo, n8n.
Apply ripples 1-4.
