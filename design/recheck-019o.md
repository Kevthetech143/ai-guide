# recheck 019o (batch 27, 20 oldest cards), 2026-11-17

Sonnet 5.5. All 20 cards opened on the provider's own page (curl or real Chrome profile pw-aiguide-recheck). Patch: data/providers-019o.json (all 20 cards, last_checked 2026-11-17).

## Changed fields
- udio | price_from | "$8/month (billed annually; $10 monthly)" -> "$10/month ($8 billed annually)" | https://www.udio.com/pricing | Standard "$10 / $8/month / $96 billed annually" (reorder only)
- murf | price_from | "$19/month (billed annually; $29 monthly)" -> "$29/month ($19 billed annually)" | https://murf.ai/pricing (Studio tab, toggled both ways) | Creator "$29 / month" monthly, "$19 / month, $228 Billed Annually" yearly (reorder only)
- n8n | price_from | "$20/month (billed annually; $24 monthly)" -> "$24/month ($20 billed annually)" | https://n8n.io/pricing/ | Starter "$24 /mo, billed monthly" / "$20 /mo, billed annually" (reorder only; page shows EUR by default in curl, USD in the browser)
- replit | price_from | "$18/month (billed annually; $20 monthly)" -> "$20/month ($18 billed annually)" | https://replit.com/pricing | Core "$20 ... $18 / month, billed annually" (reorder only)
- zapier-ai | price_from | "$19.99/month (billed annually; $29.99 monthly)" -> "$29.99/month ($19.99 billed annually)" | https://zapier.com/pricing | Professional "$29.99/month" on Pay monthly, "$19.99/month" on Pay yearly (reorder only)
- ollama | watch_out_source | null -> https://ollama.com/pricing | Pro "$20 / mo. or $200/yr", Pay as you go "$0 ... Run models locally" (text unchanged)
- chatsonic | free_tier | true -> false | https://writesonic.com/pricing | every plan button reads "Start free trial"; FAQ "No. Sign up and explore Writesonic with full access. No credit card." No free plan shown. JUDGMENT CALL: lead may veto and keep true if a free trial counts.
- chatsonic | price_from | "$16/month" -> "$79/month (billed annually)" | https://writesonic.com/pricing | Starter "$79 ... per month, billed annually"; Basic $199, Growth $399. Monthly price not shown on the page when toggled (toggle did not switch for me); "Save $240/year" and "Annual saves 20%" imply about $99 monthly, NOT published (unverified).
- chatsonic | good_for | "Drafting marketing content and pulling live web data inside one chat window." -> "Tracking how ChatGPT, Gemini, and Google AI Overviews talk about your brand, and drafting marketing articles." | https://writesonic.com/pricing | "Track your brand across ChatGPT, Gemini, and Google AI Overviews. Includes AI articles and site audits"
- chatsonic | watch_out | "It is built for marketing work rather than everyday chatting, and the $16/month price is billed annually." -> "It is now built for marketing teams that track how AI tools mention their brand, not for everyday chatting, and the $79/month price is billed annually." | https://writesonic.com/pricing | "Starter $79 per month, billed annually"
- chatsonic | watch_out_source | https://writesonic.com/chat -> https://writesonic.com/pricing | same page. Link https://writesonic.com/chat still 200 and reads "Chatsonic: Your AI Agent for AI Search Visibility" (kept). The lead may want to re-think the category "chat" for this card (it is now an AI-search-visibility/SEO tool, not a chatbot).

## Verified, no change (with notes)
- leonardo: Free $0 150 tokens/day, Essential $12 monthly ($10 yearly), private creations paid only. Page 403s curl, renders in Chrome.
- luma: Plus $30/month ($300 yearly), no free plan shown, clips 5 or 10 sec.
- manus: Standard $20/month (annual toggle saves 17%). Pricing page shows no Free card; free plan confirmed on help center https://help.manus.im/en/articles/11711111-what-is-the-current-membership-pricing-for-manus (Free $0, 300 daily credits). Daily free credits are Manus 2.0 Lite only, capped at 1,500/month (not published).
- meta-ai: still free, no paid plan on meta.ai; https://www.facebook.com/privacy/genai/ still lists "your interactions with features that are part of AI at Meta" as training info. Page 403s curl, renders in Chrome.
- microsoft-copilot: Personal $9.99, Premium $19.99 list. PROMO SEEN, NOT PUBLISHED: Personal "$6.99 first month", Premium "$13.99 first month" (limited time).
- botpress: Plus $150/mo billed annually, $189/mo billed monthly, 250 conversations, packs 100 for $65. (Left annual-first as before; monthly price is already in watch_out.)
- aiva: Standard EUR 11/month billed annually, EUR 15 monthly (checked with toggle); Pro EUR 33 / EUR 49. Card kept as is.
- colossyan: Professional $59/mo yearly (-34%), free plan, watermark removal is a Professional feature, minutes do not roll over.
- duckduckgo-ai-chat: "FROM $9.99/MONTH OR $99.99/YEAR", advanced models need subscription. New Pro tier exists above Plus (card price still right).
- elicit: Basic free; Plus $11/mo billed $132 annually; Pro $49 (tab for everyone else) billed $588. Same as card.
- huggingchat: HF PRO "$9/month"; docs "Free Users: None" monthly credits, PRO $2.00. Repo huggingface/chat-ui Apache-2.0, last push 2026-11-16, latest release v0.10.0 (2026-05-11), not archived (GitHub API; nothing downloaded). Chat page "Now with ML Intern!" shows 164 models.
- invideo: Starter $20 list, 50% off yearly ($10) still shown; credits do not roll over. Same as card.
- kapwing: Pro $16/month (annual, Save 33%), free = 10 credits, watermark, 4 min, 720p.
- ollama: Pro $20/mo ($16.67 annually), Max $100, Team $500; "Run models locally" under free. github.com/ollama/ollama MIT, latest release v0.40.16 (2026-11-09), pushed 2026-11-17.
- n8n (open/local check): github.com/n8n-io/n8n active (latest release n8n@2.48.4, 2026-11-13, pushed 2026-11-17, 210k stars, "Sustainable Use License", not archived). Pricing page lists "Community Edition ... self-hosted ... on GitHub". Card watch_out text already says $24/$20 and free self-host; unchanged.
- replit: Core $20 ($18 yearly); free Starter plan docs confirm daily credits up to a monthly cap, Lite build, Full build needs Core.

Watch items seen: none of the standing list; Microsoft first-month promo noted above.

unchanged: leonardo, luma, manus, meta-ai, microsoft-copilot, botpress, aiva, colossyan, duckduckgo-ai-chat, elicit, huggingchat, invideo, kapwing (verified, only last_checked bumped); ollama (source field added only)
unreachable: none
shut down: none
checked: 20/20

## Question-page ripples
(Checked questions.json intro, meta_description, title for every changed card: udio, murf, n8n, replit, zapier-ai, chatsonic. The five reorders changed only the price text and no page quotes those prices, so no ripple from them. Only chatsonic matters.)

- ai-for-writing-marketing-copy | intro | "and ChatSonic is Writesonic's marketing chat assistant." | ChatSonic is now an AI-search-visibility tool (tracks brand mentions in AI answers), no longer a marketing chat assistant; also how_picked says "tools whose own descriptions say they write marketing copy". | "and ChatSonic is Writesonic's tool for tracking how AI answers mention your brand, with some article writing." (names no new provider). Alternative: the lead removes chatsonic from this page's filter.
- ai-for-writing-marketing-copy | meta_description | "AI that writes marketing copy and emails: Copy.ai, Jasper, Rytr and ChatSonic, ..." | same reason (milder). | Optional: leave, or drop "and ChatSonic" if removed from the page.
