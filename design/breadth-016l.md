# breadth-016l notes (worker: Sonnet 5.5; ran over the 25-minute budget; Haiku-tier fetch work done locally)

Date: 2026-10-09. Shipped: 9 verified cards in data/providers-016l.json (fewer than 27, no padding). Nothing was tested by us; every fact was read from the provider's own pages with a browser User-Agent and Playwright (Monthly toggles clicked where one existed).

## Shipped (9) and what was read
- taskade: taskade.com/pricing. Page opens on Yearly ($10 Pro); Monthly clicked: Pro $20/mo. Free column: 2 members, 3 apps, 1 AI agent (compare table). Entity "Taskcade Inc." is the exact spelling in the Terms of Service (not "Taskade").
- chatbox: chatboxai.app/en/pricing, Monthly clicked: Lite $3.99, Pro $19.99, Pro+ $39.99; Free $0 (10,000 compute points, daily reset). Entity: only the Terms footer "© 2026 Mediocre, LLC" (terms text does not name it in a sentence). Unclear: the Free column's "Work Mode: Trial only" wording, left out of the card.
- lobehub: lobehub.com/pricing, Monthly clicked: Starter $12.9 (Yearly $9.9). Entity "LobeHub LLC" in the Terms sentence; footer says "LobeHub, LLC". Whether the Mac app is a full client or a web shell was not checked, so runs_on_your_computer=false.
- mindstudio: mindstudio.ai/pricing, "Pay monthly" clicked: Free, Individual $20 + usage. Entity "GoMeta, Inc." from Terms of Use (footer: "MindStudio (GoMeta, Inc.)"). Homepage now leads with a new "Remy" product agent; card describes the agent platform per the pricing page only.
- fellou: fellou.ai/pricing, Monthly shown: Plus $19.0 (annual $16). Entity "ASI X Inc." from Platform Service Terms. The page marks "Unlimited Concurrent Tasks" as "Limited Time", so the card does not mention it.
- wondercraft: wondercraft.ai/pricing, Monthly view: Creator $25 (shows a "First month 50% off" promo, not used). Free 150 credits. Entity "Wondercraft, Inc." from the Terms of Service on support.wondercraft.ai. Home page now calls itself an "AI video studio"; categories video+voice.
- hermes-agent: hermes-agent.nousresearch.com plan strip: Free $0 (free models only), Plus $20 per month. No Monthly/Yearly toggle was visible. The page does not say "open source" so the card does not. Entity "Nous Research, Inc." from portal.nousresearch.com/terms. UNCLEAR: whether the $20 Plus price is monthly-only (page says "PER MONTH").
- rork: rork.com/pricing: Free $0 (35 credits/mo, max 5/day), Rork Pro $20/mo, Rork Max $200/mo. No toggle found on the page. Entity "Rork, Inc." from terms. The Free column's platform ticks were not readable in text, so the card does not say which platforms Free covers.
- openclaw: openclaw.ai (text: "No subscription. No hosted tier."; MIT; stewarded by the OpenClaw Foundation, footer "OpenClaw Foundation"). So bare "Free" is accurate. Terms page not opened; entity is the footer/foundation name.

## Dropped candidates and reasons
- Flowise: homepage banner "We're sunsetting Flowise."
- Khoj (Cloud app): app.khoj.dev says "Khoj Cloud Has Been Sunset".
- Sider: pricing page shows no plan table or prices in a loaded browser.
- Genspark: /pricing redirects to a login page; price not visible.
- Phind: site returns 404. Ecosia AI page: 404. OpenEvidence: 403 to the browser.
- SciSpace: Premium $20/mo monthly verified, but legal entity could not be established (terms page blank/404); no Free plan in table.
- AnswerThis: Free + Pro $35/mo seen, but terms name only "AnswerThis.io", no legal entity.
- Activepieces: Free + Plus $20/mo seen, but Terms/Privacy pages render blank and footer says only "Activepieces"; entity unconfirmed (rule 18).
- Qoder: Free + Pro $20 seen, but "limited-time" bonus banners and no terms page found (404); entity unconfirmed.
- Tunee: every price carries "% OFF" promo banners (rule 10).
- Staccato: $4.99 first-month intro price; list price $14.99 not checked further.
- Anything (createanything): Monthly $24 read, but no Free plan column visible in table and not enough time to confirm entity.
- Captions, Pollo AI, PixVerse, Moises, Kaiber, Argil, Higgsfield: not completed (pricing unread, JS-only or promo heavy; time).
- Browser Use: pay-as-you-go credits for agents/browsers; developer-oriented (rule 16).
- Dify, Langflow, LibreChat, Letta, Factory, Blackbox, Bito, Amp, Jules, Kortix/Suna, Agent Zero, OpenManus, Open Interpreter, Simular, Opera Neon, Hunyuan Video, CogVideo, Mochi, Asta, Hika, Voiceflow: fetched or skimmed but not carried through; most are developer-focused or need more reading than the time allowed. Not a verdict on quality.
- Cherry Studio: cherry-ai.com redirects to cherryai.com.cn (different domain).

## Unclear pricing pages
- Hermes Agent (no toggle visible), Rork (no toggle found), Chatbox (Work Mode wording), Fellou (page lists a "Limited Time" unlimited-tasks feature).
