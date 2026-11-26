# Review 019w (2026-11-26) — reviewer ag019w-review (Opus 5.5)

## Verdict: FIX 7.5/10

The patch is accurate on prices and free plans for all 20 cards. No promo price is published anywhere. Three small fixes, plus the date:
- LobeHub's regular yearly price IS on its own page, so it should be restored, not dropped.
- Magnific's "aimed at Relax mode" uses the page's slogan without saying what Relax mode is.
- bolt.diy's Mac installer only works on Apple Silicon Macs.
- last_checked should be today's date.

Apply the edits below, then it ships.

I compared providers-019w.json with data/providers.json (HEAD 7d58798) field by field. The only differences are the 6 changed fields the worker listed (magnific watch_out; lobehub price_from, good_for, watch_out; bolt-diy watch_out; claude watch_out) plus last_checked on all 20. No hidden edits, and all 20 cards are present.

## 1. Changed fields

- **magnific watch_out**: facts OK, wording needs a fix. Source: https://www.magnific.com/pricing (real Chrome, Monthly tab).
  - What the page says: Premium "$20 /month billed monthly, 20K credits per month". Plus "For individuals who want Relax mode generations and full AI access", "$45 /month billed monthly", "45K credits per month". Pro "$110". The Annual tab shows Plus "$45 $33.75 /month Billed annually".
  - Premium+ is gone. The plans are now Premium, Plus and Pro.
  - Relax mode FAQ: "Relax mode lets you generate without using credits on selected models. It's included in Plus, Business, and Pro plans ... although speed may vary."
  - Compare table: Kling 2.5 720p RELAX MODE shows Premium "142 videos" and a check mark for Plus and Pro.
  - The problem: "aimed at Relax mode generations" copies the slogan but never says what Relax mode is. Readers at an 8th-grade level will not know. Say it in plain words (edit 1).
  - The Black Friday deal (annual only, "Premium $7.25 ... $87 the first year then $174/year", ends Dec 1) is not on the card. OK.
- **lobehub price_from**: FIX. Source: https://lobehub.com/pricing (real Chrome).
  - The plan comparison table on the same page shows the regular prices: "Plus $20.0 Month / $216.0 Year". The Black Friday card says the same: "$216 / 2 years, then $216 yearly".
  - $216 a year is $18 a month, so the old "$18/month billed yearly" was right and can be verified. Restore it (edit 2).
- **lobehub good_for and watch_out**: OK. Same page. Free plan: "Standard models", "One-time trial credits", "About 50 agent tasks", "15 MB file storage". The table says "Trial credits — Granted once — About 50 agent tasks".
- **bolt-diy watch_out**: OK, with one detail to add.
  - Release v1.0.3 (2026-11-15), via the GitHub API, has these files: bolt-1.0.3-win-x64-setup.exe, bolt-1.0.3-linux-x86_64.AppImage, bolt-1.0.3-linux-amd64.deb, Bolt.Local-1.0.3-arm64.dmg. The only Mac build is arm64, so it is for Apple Silicon Macs only (edit 3).
  - README (https://github.com/stackblitz-labs/bolt.diy): "no new features are planned"; "WebContainers API, which has specific commercial licensing terms for enterprise deployment"; "Grab pre-built installers from Latest Releases".
- **claude watch_out**: OK. Source: https://claude.com/pricing. Free: "Limited usage every 5 hours and every week". Pro: "$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." No promo on the page.

## 2. The 13 paid cards (providers' own pages, list prices)

All 13 are OK. No promo appears in any price_from, good_for or watch_out.
- **base44**: https://base44.com/pricing. Monthly: Starter "$20 /mo", "100 message credits", "Connect a domain". Free: "$0", "25 message credits /mo", "Up to 5 apps". Annual: "$16 /mo Billed annually". No sale.
- **d-id**: https://www.d-id.com/pricing/studio/.
  - Monthly: Lite "$5.9/month", Pro "$29/month". Annual: Lite "$4.7/month", Pro "$16/month".
  - Lite "D-ID watermark". Pro "Commercial use license". Trial "$0 14-day trial", "3 minutes".
  - The "Unlimited videos for your first month!" promo is not on the card. Correct.
- **google-flow**: https://flow.google.com/about. "Free of Charge ... 50 daily Google Flow credits". "Google AI Plus $4.99/mo*", "720 & 1080p video upscaling", "Higher image generation limits". "* Prices may vary by market". "18+".
- **klangio**: https://klang.io/transcription-studio/. The page shows "Black Friday Sale 70% OFF".
  - Monthly list prices (crossed out): Pro "$19.99" (sale $6.00), Ultimate "$29.99" (sale $9.00).
  - Annual list prices: Pro "$8.33" (sale $2.50), Ultimate "$12.50".
  - Free "Transcribe up to 30 seconds". Pro "50 transcriptions/month", "up to 15 minutes".
  - The card uses the list prices. Correct.
- **magnific**: price_from "$20/month (Premium; $14.50/month billed annually)". The annual price comes from "then $174/year" (174 / 12 = 14.50). OK. free_tier false: no free plan on the page.
- **adobe-firefly**: https://www.adobe.com/products/firefly/plans.html. Banner: "Black Friday ends soon. Save up to 60% ... Ends Dec 6".
  - The sale applies only to Pro ("Regularly at US$19.99/mo") and Pro Plus. Firefly Standard is "US$9.99/mo" with no sale, so $9.99 is the list price.
  - Free: "Limited free daily generations". Standard: "2,000 monthly generative credits".
- **anara**: https://anara.com/pricing. FAQ: "Plus is $10, Pro is $20, Max 5x is $100 ... Billed yearly, they are $8, $16, $80". Free: "20MB or 120 pages per upload". Max: "Deep Search for multi-step, complex research tasks". No sale.
- **brave-search**:
  - Checkout page https://account.brave.com/?intent=checkout&product=search: "Monthly payment $3.00 /month", "Annual payment ... $2.50 /month. $29.99 /year", "Search Premium is available exclusively in the Brave browser."
  - Help page https://search.brave.com/help/premium: "Brave Search results include paid ads".
- **capcut-ai**: https://www.capcut.com/pricing. Monthly: "Pro USD 19.99 /month", "1200 monthly AI credits", "All premium templates", "1 TB of space storage". Free: "Basic editing tools". The "(first month)" Seedance per-second prices are not on the card. Correct.
- **chatgpt**: https://chatgpt.com/pricing (real Chrome). Free "$0", "Unlimited text chats", "Limited messages with uploads", "Limited image creation", "Limited voice chats". Go "$8 / month", "This plan may include ads." The Business 2x-usage promo is Business only and not on the card.
- **claude**: see section 1.
- **claude-code**: https://claude.com/pricing compare table: "Claude Code No Yes Yes Yes" (Free / Pro / Max / Ultra). Pro is $20 a month, or $17 a month billed annually. OK.
- **ecosia**: https://www.ecosia.org/pricing (real Chrome). Free "$0.00", "Create an account", "File uploads (daily limit)", "Think longer mode (daily limit)". Starter "$7.99 / month", "Unlimited AI Chat messages". Pro "$14.99 / month". No sale.

## 3. Open-source / local cards: 7 of 7 checked (GitHub API and cited pages; nothing downloaded)

None of the repos is archived.
- **bolt-diy**: MIT. Last push 2026-11-21. Release v1.0.3 on 2026-11-15. See section 1.
- **ltx-2**: Apache-2.0. Release v1.6.3 on 2026-11-24.
  - README: "hf download Lightricks/LTX-2.5 ... That is roughly 66 GiB."
  - README: "If you get a 401/403, accept the model terms on Hugging Face".
  - OK.
- **local-deep-research**: MIT. Release v2.0.4 on 2026-11-24. Pushed today. OK.
- **magenta-realtime**: Apache-2.0. Release v2.0.3 on 2026-07-30. Last push 2026-10-02.
  - https://magenta.withgoogle.com/mrt2: "~2.5GB for base, 450MB for small"; "The Base model requires an M3 Pro / M2 Max or higher. The Small model will run on any Apple Silicon MacBook, including MacBook Air."
  - OK.
- **chatbox**: GPL-3.0. Release v1.24.4 on 2026-11-12.
  - https://chatboxai.app/en/pricing: Lite "$3.99 / Month" (annual "$3.50"), Pro "$19.99", Free "10,000 Daily reset", "Work Mode ... Trial only".
  - OK.
- **lobehub**: Release v2.3.6 on 2026-11-24. License shows NOASSERTION. Pushed today. OK apart from edit 2.
- **fellou**: https://fellou.ai/pricing: "1000 Sparks (New User Bonus) - Approximately 4 Tasks", "2 Scheduled Tasks", Plus "$19.0 /month", "$192 ($16/Monthly)", "2000 Sparks/month - Approximately 8 Tasks". OK.

## 4. Question-page ripple

I searched questions.json (title, intro, meta_description) for LobeHub, Magnific, bolt.diy and Claude.
- No sentence makes a claim about LobeHub's credits or price, Magnific's Premium+ or "unlimited", bolt.diy's installers, or Claude's free-plan limits.
- paid-ai-image-generator and ai-site-with-many-picture-and-video-models say Magnific "has no free plan". That is still true.
- one-app-for-many-ai-chatbots says "the stronger models in most of these cost extra". That is still true.

No change needed.

## Edit list for the lead (apply on top of providers-019w.json)

1. magnific | watch_out | Monthly Premium includes 20,000 credits a month. Plus at $45/month ($33.75/month billed annually) gives 45,000 credits a month and adds Relax mode, which makes pictures and videos on selected models without using credits, though it can be slower. Prices exclude VAT and local taxes.
2. lobehub | price_from | Free (Plus plan $20/month, or $18/month billed yearly)
3. bolt-diy | watch_out | You add your own AI provider keys (paid access codes from AI companies) or a local model. Ready-made desktop installers for Windows, Mac (Apple Silicon only) and Linux are on the releases page; otherwise it is a developer setup with Node.js and pnpm or Docker. One part it relies on (WebContainers) has separate commercial terms for large business use. The makers say they now only do bug fixes and upkeep, with no new features planned.
4. all 20 ids (chatgpt, claude, claude-code, adobe-firefly, capcut-ai, magnific, d-id, ltx-2, local-deep-research, magenta-realtime, bolt-diy, klangio, google-flow, base44, chatbox, lobehub, fellou, anara, brave-search, ecosia) | last_checked | 2026-11-26. I re-verified every card today.

Everything else in providers-019w.json ships as written. No questions.json edits.

## Housekeeping

- **Browser:** my own session ag019w-review, profile ~/.config/pw-aiguide-recheck. My first `close` was run from the wrong folder and reported "not open". I ran it again from /tmp/ag019w-review. After that, `pgrep -f pw-aiguide-recheck` printed nothing (exit 1).
- **Read-only:** I wrote only this file. I did not touch providers*.json, questions.json, any page, or /tmp/ai-wrapper/. No downloads. No commit.
- **Scratch:** pages and a screenshot are in /tmp/ag019w-review/.
- **Rung:** Opus 5.5. An independent final review of published facts fits the Opus tier.
