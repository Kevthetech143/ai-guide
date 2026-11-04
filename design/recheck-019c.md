# Re-check 019c (batch 15), 2026-11-04

Field changes: none. All 20 cards verified; only last_checked moves to 2026-11-04 (patch: data/providers-019c.json). No watch_out or watch_out_source edits.

Verified (no field change), with the official page seen:
- google-ai-mode: https://www.google.com/aimode loads signed out (redirects to google.com/search?udm=50). https://support.google.com/websearch/answer/16011537 still says "AI responses may include mistakes" and "enable history ... can't pick up where you left off".
- hailuo: https://hailuoai.video/subscribe (plan modal): Free "One-time free trial credits"; Standard $14.99/month list. NOTE promo: Standard currently shown 30% off ($10.50 billed monthly, $8.40 yearly), and the header says "From $9.99/mo"; list price kept at $14.99 (temporary discount rule).
- heygen: https://www.heygen.com/pricing Free "3 videos a month, watermarked"; Creator "$29 / mo"; FAQ "Creator plan costs $29/month (or $24/month if you pay annually)".
- ideogram: https://ideogram.ai/pricing Plus "$20 per month, $180 billed annually" (comparison table "$15/mo"); FAQ "Ideogram Plus and Pro subscribers can generate unpublished images"; "Eligible free accounts receive weekly credits ... the amount may vary".
- leonardo: https://leonardo.ai/pricing/ Free "150 / day", "Creations access Public"; Essential $12/month on Pay Monthly ($10 on Pay Yearly); paid plans "Private".
- luma: https://lumalabs.ai/pricing Plus "$30/month" (Pro $90, Ultra $300); no Free plan listed; cost table shows "20 credits/5 sec" and "60 credits/10 sec" (supports the 5 to 10 second clip line).
- manus: https://manus.im/pricing $20 / month (4,000 credits), $40, $200 (price shown by screenshot; page uses animated digits). Free plan still exists: https://help.manus.im/en/articles/11711097-what-are-the-rules-for-credits-consumption-and-how-can-i-obtain-them "monthly consumption limit for daily refresh credits for free users is set to 1,500 credits". watch_out left, still not sourced ("always double-check its work" is not on the page).
- meta-ai: https://www.meta.ai/ renders, no subscription shown. https://www.facebook.com/privacy/genai/ "Information shared on Meta Products ... and your interactions with features that are part of AI at Meta" is used for training.
- microsoft-copilot: https://www.microsoft.com/en-us/copilot/solutions/individuals Personal "$9.99 /month", Family $12.99, Premium "$19.99 /month"; "chat with higher usage than free".
- murf: https://murf.ai/pricing (Studio tab) Creator "$19 / month" billed yearly, "$29 / month" on the monthly switch; Free "No Commercial Rights", "(No Downloads)".
- n8n: https://n8n.io/pricing/ Starter "$20 /mo, billed annually", "$24 /mo, billed monthly" on the Monthly switch (USD); "Community Edition ... self-hosted version of n8n is available on GitHub". watch_out left, not sourced ("technical users / hard setup" is not on the page).
- ollama: https://ollama.com/pricing Pro "$20 / mo or $200/yr"; Pay as you go $0 "Run models locally". GitHub ollama/ollama MIT, not archived, latest release v0.40.14 (2026-11-03). watch_out left, not sourced.
- replit: https://replit.com/pricing Core "$20 ... $18 / month, billed annually"; no free card on the page, but https://docs.replit.com/billing/plans/starter-plan still says Starter is free: "daily credits for Agent ... up to a monthly cap", "Lite build". watch_out_source unchanged.
- udio: https://www.udio.com/pricing Free "10 credits per day and 100 credits per month", "Limit of 3 full length ... per day"; Standard "$10 / $8/month, $96 billed annually".
- zapier-ai: https://zapier.com/pricing Free "100 tasks per month", "Two-step Zaps"; Professional "Starting from $29.99/month" on Pay monthly, "$19.99" on Pay yearly.
- aider: https://aider.chat/ 200. GitHub Aider-AI/aider Apache-2.0, not archived; latest GitHub release v0.86.0 (2025-08-09), PyPI aider-chat 0.86.2; last push 2026-05-22 (FYI: slow upkeep). Free; the provider key cost is on https://aider.chat/docs/faq.html (unchanged source).
- amazon-q-developer: https://aws.amazon.com/q/developer/pricing/ "Free Tier ... zero cost", "Pro Tier: ... $19/mo. per user"; FAQ "activates the subscription ... billed the monthly fee".
- bolt-new: https://bolt.new/pricing Free "$0", Pro "$25 /month Billed monthly", "$18" on Yearly switch; "300K tokens daily limit, 1M tokens per month".
- codex: https://developers.openai.com/codex/pricing Free "quick coding tasks", Go "$8/month ... lightweight coding tasks", Plus "$20/month" with "Codex on the web, in the CLI, in the IDE extension"; Pro now "From $100/month". Link https://openai.com/codex renders (403 to curl, 200 in Chrome; lands on /codex/).
- descript: https://www.descript.com/pricing Hobbyist "$16" annual / "$24" monthly; Free "60 minutes (1 hr) / month" of media (paid plans now quoted in media hours).

Links: every card link returned 200 (curl with browser User-Agent) or rendered in Chrome (ideogram.ai, leonardo.ai/pricing, meta.ai, openai.com/codex return 403 to plain curl but render).
open_weights / runs_on_your_computer: no change on any card. Ideogram true stays: https://huggingface.co/ideogram-ai lists ideogram-4-fp8 / -nf4 (gated, auto-approve, license "ideogram-4-non-commercial"), FYI only.

Lead decisions / FYI (nothing changed in the patch):
1. hailuo open_weights: MiniMax published the weights of its current model MiniMax H3 on https://huggingface.co/MiniMaxAI/MiniMax-H3 (not gated, "MiniMax H3 Community License"), and the Hailuo app runs H3. But the license's "Excluded Territories" are "the European Union, the United Kingdom, the Republic of Korea and the United States of America". I left false because an "Open source" badge for US readers would mislead. Your call.
2. luma free_tier: pricing page lists only paid plans, so false kept, but the Luma home page and /dream-machine show a "Try for free" button; I could not tell without signing up whether it gives free credits (unverified).
3. hailuo shows a temporary discount (see above); no action.

unchanged: google-ai-mode, hailuo, heygen, ideogram, leonardo, luma, manus, meta-ai, microsoft-copilot, murf, n8n, ollama, replit, udio, zapier-ai, aider, amazon-q-developer, bolt-new, codex, descript
unreachable: none
checked: 20/20

## Question-page ripples

None. No card's free_tier, price_from, watch_out or good_for changed, so no questions.json sentence went stale from this batch.
