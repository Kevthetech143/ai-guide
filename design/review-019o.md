# review-019o (batch 27) — Opus review, 2026-11-17

Verdict: FIX. Score 8/10. Facts are right on every changed card; the price format needs "/month" in the brackets (same fix as 019n), and chatsonic has a published monthly price ($99) the worker missed.
Reviewer: Opus 5.5, read only. I did not edit providers-019o.json, providers.json, build.py or questions.json.

## Patch shape
- 20 cards, same ids, same key order as providers.json, file format exact (json.dumps indent=2 + newline). All last_checked 2026-11-17.
- Non-date diffs are exactly the 11 listed in recheck-019o.md. No unlisted change.

## Changed fields, checked on the provider's own page
- udio | OK, format FIX | https://www.udio.com/pricing (JS page, real Chrome): Standard "$10" then "$8 /month", "$96 billed annually".
- murf | OK, format FIX | https://murf.ai/pricing (Chrome, Studio tab): yearly "Creator ... $19 / month $228 Billed Annually"; after switching to monthly "Creator ... $29 / month".
- n8n | OK, format FIX | https://n8n.io/pricing/ (Chrome, USD): Annually "Starter ... $20 /mo, billed annually"; Monthly "Starter ... $24 /mo, billed monthly". (curl gets the EUR version "20€ /mo".)
- replit | OK, format FIX | https://replit.com/pricing (curl 200): "Core $20 $18 / month, billed annually".
- zapier-ai | OK, format FIX | https://zapier.com/pricing (Chrome): "Pay yearly (Save 33%)" default shows "Professional Starting from $19.99 /month"; after "Pay monthly": "Professional Starting from $29.99 /month".
- ollama | watch_out_source OK | https://ollama.com/pricing (curl 200): "Pay as you go $0 ... Run models locally"; "Pro ... $20 / mo. or $200/yr".
- chatsonic | see section below.

## chatsonic (the big one)
Page https://writesonic.com/pricing (curl 200 + Chrome): title "Pricing | Writesonic AI Search Visibility Platform". Annual (default): "Starter $ 79 Save $240/year per month, billed annually"; Basic $199; Growth $399. I denied the cookie banner and flipped the switch to Monthly: "Starter $99 per month", Basic "$249 per month", Growth "$499 per month". FAQ: "Annual billing saves 20%". So the monthly price IS on the page; the worker's "$99 not published" is wrong.
- free_tier false: KEEP. Every plan says "Start free trial"; FAQ "No. Sign up and explore Writesonic with full access. No credit card."; https://writesonic.com/chat says "Start 7-Day Free Trial". No free plan anywhere. Same ruling as scite (018s), krisp (018t), submagic (018y): a trial is not a free plan.
- price_from: FIX to monthly-first "$99/month ($79/month billed annually)".
- good_for: KEEP worker text. Page: "Track your brand across ChatGPT, Gemini, and Google AI Overviews. Includes AI articles and site audits to fix visibility gaps."
- watch_out: FIX (price sentence). "marketing teams" is on the page ("Trusted by leading marketing teams and agencies"); "Start free trial" is on the page.
- watch_out_source https://writesonic.com/pricing: KEEP. link https://writesonic.com/chat: 200, reads "Chatsonic: Your AI Agent for AI Search Visibility ... Chatsonic helps you show up in AI answers"; keep.
- categories ["chat"]: it is no longer a general chatbot (it is a chat-style agent over your SEO and AI-visibility data).
- RECOMMENDATION: FLAG TO LEAD FOR REMOVAL. It is now a $99-a-month business tool for SEO and brand-tracking teams with no free plan, so it doesn't fit "chat" or this site's readers. With free_tier false it also joins best-paid-ai-worth-the-money, a page for everyday readers. If the lead keeps it, apply the edits below. The worker's ai-for-writing-marketing-copy intro line is fine, but the cleaner choice is to drop chatsonic from that page's ids list and its meta_description.

## Spot-check of 3 "unchanged" cards (curl 200)
- elicit | OK | https://elicit.com/pricing: "Basic ... Free Limited usage for Research Agent and Research Reports"; "Plus ... $11 Save 42% Per user/month, billed as $132 annually"; Industry tab "Pro ... $49 Save 35% Per user/month, billed as $588 annually".
- kapwing | OK | https://www.kapwing.com/pricing: "Free ... 10 credits $ 0 ... Unlimited exports with a watermark Export videos up to 4 minutes long 720p video quality"; "Pro ... $ 16".
- luma | OK | https://lumalabs.ai/pricing: "Plus $30 /month $300 billed yearly"; no Free plan card; clips priced "20 credits/5 sec 60 credits/10 sec".
- Not re-fetched by me (worker's check stands, unverified by reviewer): leonardo, manus, meta-ai, microsoft-copilot, botpress, aiva, colossyan, duckduckgo-ai-chat, huggingchat, invideo.

## watch_out sentences
- Each changed card's watch_out is on its cited page except chatsonic's old price sentence (fixed below). Nothing to cut.

## Ripples
- ai-for-writing-marketing-copy intro: the worker's replacement "and ChatSonic is Writesonic's tool for tracking how AI answers mention your brand, with some article writing." names only ChatSonic/Writesonic, which are already on the page. OK for guidecheck.
- The worker missed this, but it's harmless: free_tier false takes chatsonic off best-free-ai-chatbot, ai-for-students, ai-for-homework-help, ai-for-writing-emails, ai-for-job-hunting-and-resumes and ai-for-older-adults, and adds it to best-paid-ai-worth-the-money. None of those intros name ChatSonic, so no sentence goes stale. The 5 reorders change no page membership.

## Lead's cloud-line fix (build.py legend, /start/ hint, /start/local/ subtitle, questions.json how_picked)
- True, plain and short: yes. "These run on your own device. Some, like coding helpers, still send what you type to an online AI." is true for claude-code, cursor, github-copilot and codex, and "Some" also covers the agents in the list (n8n, openclaw, hermes-agent, autogpt, gpt-researcher). The start hint "runs on your own device" is fine. build.py parses and questions.json is valid JSON. I did not run build.py, because it rebuilds dist.
- One optional leftover: questions.json ai-that-runs-on-my-own-computer meta_description "Llama, Stable Diffusion and more keep your data private." The "and more" now overclaims. Suggested: "Which AIs run on your own computer? Llama, Stable Diffusion and more, with plain-English notes on what stays private." The intro is already hedged ("as long as you stick to models on your own machine"), so it can stay.

## Exact field edits for providers-019o.json (if chatsonic is kept)
- udio | price_from | "$10/month ($8/month billed annually)" | https://www.udio.com/pricing
- murf | price_from | "$29/month ($19/month billed annually)" | https://murf.ai/pricing
- n8n | price_from | "$24/month ($20/month billed annually)" | https://n8n.io/pricing/
- replit | price_from | "$20/month ($18/month billed annually)" | https://replit.com/pricing
- zapier-ai | price_from | "$29.99/month ($19.99/month billed annually)" | https://zapier.com/pricing
- chatsonic | price_from | "$99/month ($79/month billed annually)" | https://writesonic.com/pricing (Monthly switch "$99 per month"; Annual "$79 ... per month, billed annually")
- chatsonic | watch_out | "It is now built for marketing teams that track how AI answers mention their brand, not for everyday chatting, and it costs $99 a month, or $79 a month if you pay for a year, after a free trial." | https://writesonic.com/pricing
- Keep as the worker wrote: chatsonic free_tier false, good_for, watch_out_source; ollama watch_out_source.
Why "/month" in brackets: a beginner can read "($8 billed annually)" as "$8 a year". This matches the 019n review and the cards already live.

## Browser
- Session ag019o-rev, profile ~/.config/pw-aiguide-review, no sign-in. Closed ("Browser 'ag019o-rev' closed"). After that, `pgrep -fl pw-aiguide-review` printed nothing (exit 1).
