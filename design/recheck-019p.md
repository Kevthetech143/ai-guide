# recheck 019p (batch 28), 2026-11-18

Changes (patch: data/providers-019p.json, 19 cards, last_checked 2026-11-18):
- lovable | price_from | "$21/month (billed annually; $25 monthly)" -> "$25/month ($21/month billed annually)" | https://lovable.dev/pricing (Pro "$25 ... Originally $25 per month"; Yearly toggle "$21 / month, billed annually")
- otter | price_from | "$8.33/month (billed annually; $16.99 monthly)" -> "$16.99/month ($8.33/month billed annually)" | https://otter.ai/pricing (Pro "$16.99 /user/month"; Annual toggle in browser "$8.33 /user/month")
- playground-ai | price_from | "$12/month (billed annually; $15 monthly)" -> "$15/month ($12/month billed annually)" | https://playgroundai.com/design/pricing (Pro "$15 ... $12 /mo ... $144 will be charged in total annually")
- pictory | price_from | "$25/month (billed annually)" -> "$29/month ($25/month billed annually)" | https://pictory.ai/pricing (Starter "Was $29"; page title "From $25 per Month"). Annual $25 is seen only in the page title because of the Black Friday banner (annual shows $12.50, monthly $14.50): reviewer please confirm.
- synthesia | price_from | "$14/month (billed yearly)" -> "$19/month ($14/month billed yearly)" | https://www.synthesia.io/pricing (Starter "$19 /month"; yearly "$14 /month, $168 billed yearly")
- mubert | price_from | "$11.69/month (billed annually)" -> "$14/month" | https://mubert.com/render/pricing (Monthly toggle: Creator "$14 / month"). The annual list rate is hidden by Black Friday (annual shows $8.17 first year, "Billed $98 for the first year"), so I could not verify $11.69 and dropped the bracket. Lead may restore after BF (ends in ~9 days).
- scite | price_from | "$12/month (billed yearly)" -> "$20/month ($12/month billed yearly)" | https://scite.ai/pricing (Basic "$12 / month Billed yearly"; unchecking the "Billed yearly" box in the browser shows "$20 / month")
- photoshop-generative-fill | watch_out | "...includes 25 generative credits a month, while unlimited Generative Fill comes with Creative Cloud Pro at $69.99 a month." -> "You need a paid plan: Photoshop costs $22.99 a month (annual plan, billed monthly) and comes with generative credits for AI features. Creative Cloud Pro, which bundles more apps and AI tools, costs $69.99 a month at its regular price." | https://www.adobe.com/products/photoshop.html ("US$22.99/mo Annual, billed monthly"; "Generative credits for AI features in Photoshop"; CC Pro "Regularly at US$69.99/mo"). Reason: the "25 credits" and "unlimited Generative Fill" claims are no longer on the cited page, so cut.
- All 19: last_checked -> 2026-11-18.

Notes (no change made):
- perplexity-comet: Pro "$17 /month when billed annually" on https://www.perplexity.ai/pro; no monthly rate appears on any official page I could open, so the card stays annual-only as written (price not guessed). Free plan "Browser Agent (Comet Assistant) Queries: No" still true (help center plan table).
- lindy: curl returned an A/B variant showing Team $49.99 (5,000 credits); the real browser shows $29.99 (3,000 credits). Kept $29.99, verified in Chrome.
- lm-studio: pricing now "Bionic" (Free $0, Bionic+ $20/month, Pro $100), card still right. Newest build Bionic 1.2.1 (changelog dated Nov 16, 2026); download page live. Memory text 16GB confirmed at https://lmstudio.ai/docs/app/system-requirements. The app itself is free, closed-source; open_weights refers to the open models it runs.
- typebot: still self-hostable; latest GitHub release v3.19.1 (2026-10-20); license FSL-1.1-Apache-2.0 (source-available, not OSI open source); not archived, last push 2026-11-07. Starter $39, Free 200 chats unchanged.
- windsurf: link https://devin.ai/desktop 200; Free/Pro $20/Max $200 unchanged.
- notebooklm: notebook.google.com redirects to /trynow (renders); free plan exists; paid tiers only via Google AI Plus/Pro/Ultra, prices not on the page, so price_from stays "Free".
- Promos seen, NOT published: Pictory Black Friday (Starter $12.50 annual / $14.50 monthly), Mubert Black Friday (Creator $8.17 first-year annual), Adobe CC Pro $29.99 first year (ends Nov 27), Synthesia Starter $9 first month.

unchanged (only last_checked bumped): lm-studio, poe, windsurf, notebooklm, perplexity-comet, lindy, pi-ai, speechify, opus-clip, vapi, typebot
unreachable: wellsaid-labs (kept last_checked 2026-11-06, NOT in the patch). https://www.wellsaid.io/ai-voice-pricing now redirects to the homepage; no public prices anywhere. Homepage FAQ: "Plans are scoped with our team based on how much voiceover you produce" and only "Get a demo" buttons. So "$10/month (billed annually)" and free_tier true cannot be verified; the lead should decide (likely sales-only, free_tier false, price "Contact sales").
checked: 19/20

## Question-page ripples
None. All 8 changed cards are only price ordering/wording or the Photoshop credit detail; every question-page sentence naming Lovable, Otter, Mubert, Pictory, Photoshop, Synthesia (ai-that-builds-websites, ai-for-meeting-notes, free-ai-music-maker, paid-ai-video-generator, paid-ai-image-generator, ai-talking-avatar-video-maker, ai-background-music-for-my-videos, ai-that-turns-a-blog-post-into-a-video, ai-that-removes-objects-from-photos, ai-voices-in-many-languages) has no price or credit claim and stays true. If the lead edits wellsaid-labs, search questions.json for WellSaid first.
