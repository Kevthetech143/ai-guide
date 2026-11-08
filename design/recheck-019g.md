# ai-guide-019g recheck (2026-11-08), batch 19: the 20 oldest cards

Patch file: data/providers-019g.json (20 verified cards as they should read after the merge). All 20 get last_checked "2026-11-08". No link changed (vocalremover.org returns 403 to curl but renders in real Chrome; the other 19 return 200). Existing watch_out_source values kept. Rung: Sonnet 5.5 (routine page checks).

## Changed fields
- qodo | price_from | "$30/month (Pro Team; extra credit packs $0.012/credit)" -> "$30/month (Pro Team; extra credits $0.015/credit)" | https://www.qodo.ai/pricing/ | "$0.015/credit, pooled across the team"; overage "at the same per-credit rate as your base plan"
- qodo | watch_out | "$30/month buys 2,500 credits (about 18 reviews a month); about 36 reviews costs $60/month. 14-day free trial; free only for open-source projects" -> "$30/month buys 2,000 credits (about 14 reviews a month); about 29 reviews costs $60/month. 14-day free trial, no card needed; free only for open-source projects" | https://www.qodo.ai/pricing/ | plan picker: "~14 Reviews/Mo 2,000 credits" = $30, "~29 Reviews/Mo 4,000 credits" = $60, "~114 Reviews/Mo 16,000 credits" = $240; "Free 14 Day Trial NO CREDIT CARD"; FAQ "We don't offer a permanent free tier"; "Qualified open source projects can apply ... for free access". Free_tier false holds.
- warp-dev | price_from | "$20/month (Build)" -> "$20/month (Build; $18/month billed annually)" | https://www.warp.dev/pricing | Build Monthly "$20 /month", Annual toggle "$18 /month Annual plan". Shape change only; watch_out unchanged (still "$20 of agent usage included each month at API rates", "$20 (1,500 credits)").
- consensus | price_from | "Pro from $20/month" -> "$20/month (Pro; $12/month billed annually)" | https://consensus.app/pricing/ | Monthly toggle Pro "$20/mo"; Annual "$12/mo $144 annually". Shape change only; watch_out unchanged and still true (Free "10 Pro messages per month", "Up to 3 Deep reviews per month"; Pro "15 Deep reviews per month").
- v0 | price_from | "$30/user/month (Plus)" -> "$30/user/month (Plus; the page shows $90 crossed out)" | https://v0.app/pricing | Plus card: "$30" with a struck-through "$90 /user/month" (HTML <del>). This is the watch-item promo. I could not tell from the page whether $90 is the normal list price or only a reference price (no promo text, FAQ silent), so the charged price $30 stays and the note is added. Lead may prefer to revert to "$30/user/month (Plus)" or to price it at $90 if Vercel confirms $90 is list. Rest unchanged: Free "7 message/day limit", Plus "$30 of included monthly credits per user", Business $100. New on Free: "$5 in one-time credits for new users" (not added to the card).

## Verified, no field changed (last_checked only)
- diffusionbee | https://diffusionbee.com/ | "Download for macOS", "macOS 13.1 or higher. Machines with Apple silicon are recommended", Intel works but "very slow"; "runs 100% offline". GitHub divamgupta/diffusionbee-stable-diffusion-ui: AGPL-3.0, latest release 2.5.3 (2024-08-14), last push 2024-10-30, not archived. Quiet repo (no commits in a year) but the app and download link are live; weights are Stable Diffusion models under the CreativeML Open RAIL-M license. Not downloaded.
- vocal-remover | https://vocalremover.org/next/pricing | Free 10 min/day, 8 min file, 100Mb; Month US$12.95; Year US$99. "New version with better algorithms - currently available for subscribers only" is on the home page https://vocalremover.org/ (not the pricing page the card cites).
- tavily | https://www.tavily.com/pricing | Researcher "Free", "1,000 API credits / month", "No credit card required"; Pay As You Go "$0.008 / credit"; Project "$30 / month", "4,000 API credits / month". No monthly/yearly switch.
- goose | https://goose-docs.ai | "Open Source - Apache 2.0 - Agentic AI Foundation"; "Works with 15+ providers ... Use API keys or your existing Claude, ChatGPT, or Gemini subscriptions". GitHub moved to aaif-goose/goose (block/goose redirects): Apache-2.0, latest release v1.57.0 (2026-10-28), pushed today. The "model costs are separate" half of watch_out is a plain reading, not a quoted line.
- pieces | https://pieces.app/pricing | Pro "$18.99 per user / month - billed monthly", "Save 25% yearly"; Enterprise $22.99; "Is Pieces free to use? No."; "7-day free trial", "Card required to start". The "every 2 seconds ... Captured by default" fact is on the home page https://pieces.app (not the pricing page the card cites), same page says "Saved on-device by default".
- replicate | https://replicate.com/pricing and /docs/topics/billing | flux-dev $0.025/image, flux-1.1-pro $0.04/image unchanged; billing page "You can run select models on Replicate for free, but after a bit you'll be asked to set up billing." Banner: "Minimax H3 Lite and Highspeed are 50% until end of year" (not a card fact).
- mureka-ai | https://www.mureka.ai/subscribe | Monthly: Pro "$10.00 /month", "5,000 Gold/month", "Up to 500 songs"; Yearly "$8.00 /month Billed $96 yearly"; Premier $30 monthly / $24 yearly; Free "4 songs, daily"; Pro "Unlimited MP3 downloads", Premier "Unlimited downloads: WAV, Stems, MIDI".
- loudly | https://www.loudly.com/music/pricing | Monthly: Personal "$10 / month Billed monthly", "2,500 credits"; Annual "$8 / month Billed annually ($96/year)"; Free "1 download per day", "Non-commercial use".
- boomy | https://boomy.com/pricing | Creator "33% off $14.99/mo" now "$9.99 /mo" (card keeps list price with the discount note); Free "25 song saves", "No downloads", "No commercial use"; Creator "25 WAV downloads per month".
- stable-audio | https://stableaudio.com/pricing | Solo "$12/mo", "660 credits/mo"; Free "50 credits a month", "About 12 full-mix generations"; FAQ "No, your unused credits don't roll over." Note: Free now lists "Commercial license" (card does not say otherwise).
- iask-ai | https://iask.ai/ | home still says "free question AI search engine"; /pricing and /plans both still land on the home page, no Pro plan or price anywhere on the page, so the card's "we could not confirm what the Pro plan costs" is still right.
- recraft-ai | https://www.recraft.ai/pricing | Pay monthly: Basic "$12 billed monthly", "1,000 credits per month"; annual "$10 per month billed annually $120"; Pro $16 annual; Free "All images are public", "No commercial use".
- zed-editor | https://zed.dev/pricing | Pro "Free Trial $10 per month", "$5 of tokens included", "Usage-based billing beyond $5"; FAQ "Zed Pro bills at API list price +10%". Personal $0, Business $30/seat.
- vane | https://github.com/ItzCrazyKns/Vane | MIT, latest release v1.12.2 (2026-04-10), last push 2026-09-01, not archived; README "runs entirely on your own hardware", "local LLMs (Ollama) and cloud providers (OpenAI, Claude, Groq)", "Using Docker is highly recommended".
- andi | https://andiai.com/legal/terms-of-service "AI-generated content may have errors"; https://andiai.com/api "Outcome-Based Pricing", "<1c Per query"; consumer site andisearch.com loads (v0.8.38) with "No ads, spam or tracking".
- semantic-scholar | https://www.semanticscholar.org/ | "A free, AI-powered research tool for scientific literature"; "Search 241,005,679 papers".

## Notes for the lead (no card field changed)
- v0: decision needed on the $90 crossed-out price (see above).
- Two watch_out facts live on a different page than the cited watch_out_source: vocal-remover (new-version-for-members is on the home page) and pieces (2-second capture is on the home page). Kept as before; trim or re-source if a reviewer objects.
- stable-audio open_weights stays false (the web app is closed; Stability's separate Stable Audio Open model is not the app).
- Browser: session ag019g closed; `pgrep -f pw-aiguide-recheck` printed nothing.

unchanged: diffusionbee, vocal-remover, tavily, goose, pieces, replicate, mureka-ai, loudly, boomy, stable-audio, iask-ai, recraft-ai, zed-editor, vane, andi, semantic-scholar (last_checked only)
changed: qodo (price_from, watch_out), warp-dev (price_from shape), consensus (price_from shape), v0 (price_from note)
unreachable: none
checked: 20/20

## Question-page ripples
Searched data/questions.json (94 questions; intro, meta_description, title) for qodo, warp, consensus, v0, Zed-free names. Only match: ai-for-finding-scientific-papers (intro and meta_description name Consensus).
- ai-for-finding-scientific-papers | intro | "Consensus answers from peer-reviewed papers, and Elicit builds evidence tables..." | still true; consensus facts changed only in the shape of price_from, no price. No edit needed. Listed only because the card changed.
- No page names Qodo, Warp or v0 in intro, meta_description or title. Ripples: 0.
