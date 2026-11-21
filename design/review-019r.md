# Review 019r (2026-11-21) — reviewer ag019r-review (Opus 5.5)

## Verdict: SHIP (19-card patch as written) + 1 recommended lead edit for tabby (not in the patch)

The patch matches HEAD 755fc09 except the 3 declared field changes (vocal-remover watch_out; goose watch_out + watch_out_source) and last_checked. I checked this with a field-by-field diff of providers-019r.json against `git show 755fc09:data/providers.json`. No hidden edits.

## 1. Changed cards (checked against the providers' own pages)
- vocal-remover: verified in real Chrome at https://vocalremover.org/next/pricing (curl gets 403 from Cloudflare). The page says: "Free 10 minutes 8 minutes 100Mb ... Month US$12.95 ... 300 minutes 25 minutes ... Year US$99 ... 500 minutes 25 minutes". Every part of the new watch_out sentence and the price_from is on the page. OK.
- goose: https://goose-docs.ai/docs/getting-started/providers/ returns 200. It shows "Atomic Chat Run local models", "ChatGPT Codex ... Requires a ChatGPT Plus/Pro subscription" and "Claude ACP ... active Claude Code subscription", plus many API-key providers (ANTHROPIC_API_KEY, GOOGLE_API_KEY ...). That supports "a local model on your computer, an API key, or an existing Claude or ChatGPT subscription". Dropping Gemini from the subscription list is right: the page lists Gemini only as an API key. "costs are separate from goose" reads the same as the old text. The home page says "Open Source · Apache 2.0". OK.

## 2. Unchanged cards re-checked: 13 of 17
- soundraw: $16.99/mo, $11.04/mo yearly, cheapest paid plan is Creator. "Download as mp3" on Creator and Artist Starter; "mp3, wav, stems" on Artist Pro. OK.
- lalal-ai: in Chrome, after clicking the Monthly radio: "Lite $9.99 billed monthly / Pro $19.99 billed monthly". The yearly view shows "Lite $7.5/mo $90 billed annually". Fast queue "90 minutes/mo 250 minutes/mo". The Pro yearly price carries a "Black Friday Price 40% OFF" label. The card uses Lite, so it is not affected. OK.
- flow-music: "Starter ($8/mo billed monthly, or $6/mo billed yearly"; Free "Daily top-up credits 2 concurrent generations". OK.
- exa: "Search From $4 /1k requests"; "$10 credits every month plus a $10 onboarding bonus. No payment method required". OK.
- tavily: "Researcher Free ... 1,000 API credits / month"; "Pay As You Go $0.008 / credit"; "Project $30 / month". OK.
- qodo: "Pro Team $30 ... Free 14 Day Trial no credit card ... ~14 Reviews/Mo 2,000 credits ~29 Reviews/Mo 4,000 credits"; the $60 step is shown on the slider (data-plan-price="$60"); "We don't offer a permanent free tier"; "Free for open source projects". free_tier false is correct. OK.
- pieces: "$18.99 per user / month · billed monthly Save 25% yearly"; "Is Pieces free to use? No."; "Card required to start". OK.
- mureka-ai: in Chrome, Monthly view: "Pro Plan $10.00/month", "Premier Plan $30.00/month". Yearly view: "$8.00 ... Billed $96 yearly". Compare table: "4 songs, daily ... Free model (v7.5-all)"; Audio Download "MP3 / MP3, WAV". OK.
- loudly: in Chrome, Monthly: "Personal $10 / month Billed monthly ... 2,500 credits". Annual: "$8 / month Billed annually ($96/year)". Free: "1 download per day ... Non-commercial use". OK.
- boomy: in Chrome: "CREATOR 33% off$14.99/mo $9.99 /mo"; Free "25 song saves No downloads No commercial use"; Creator "25 WAV downloads per month". The card correctly keeps the $14.99 list price with a discount note. OK.
- comfyui: https://comfy.org/pricing shows "STANDARD $16 $20 /month $192 billed yearly". The cheapest paid plan is right, and free_tier/runs_on_your_computer stand because the app is open source. OK.
- anythingllm: https://anythingllm.com/cloud shows "Basic ... $50 /monthly". OK.
- replicate: billing docs say "You can run select models on Replicate for free, but after a bit you'll be asked to set up billing". https://replicate.com/pricing lists flux-dev "$0.025 / output image" and flux-1.1-pro "$0.04 / output image". OK.
- Links return 200 at their final URL: soundraw, lalal, flowmusic, exa, tavily, qodo, pieces, mureka, loudly, boomy, comfy.org, anythingllm.com, replicate.com, huggingface musicgen-small, nomic.ai/gpt4all, jan.ai, diffusionbee.com, github janhq/jan, goose-docs.ai. vocalremover.org is blocked for curl (403) and loads in Chrome.
- Not re-checked in depth (link 200 only): musicgen, gpt4all, jan, diffusionbee. Their prices are "Free" and the worker logged the GitHub/Hugging Face checks.
- No promo price was published. No price comes only from a meta tag. The lalal monthly price also appears in the page's JSON data, but I checked it on screen in Chrome.

## 3. tabby — recommendation: point the link to the GitHub repo and change the fields to what can be verified
My checks: https://www.tabbyml.com/pricing returns 404. https://www.tabbyml.com/ is now a consulting page ("Turn failure patterns into measurable improvements"). The $19/seat price and the 5-user Community plan appear nowhere official, and tabby.tabbyml.com/pricing is also 404. The product is still alive: https://github.com/TabbyML/tabby is not archived, the last push was 2026-06-30, and the latest release is v0.32.0 (2026-01-25). The LICENSE file says code outside "ee/" is "available under the 'Apache 2.0' license". The docs at https://tabby.tabbyml.com/docs/welcome/ return 200 and say "Tabby is an open-source, self-hosted AI coding assistant". The README says "Self-contained, with no need for a DBMS or cloud service" and "Supports consumer-grade GPUs".
Removing the card is not needed, because the software is still downloadable. Keeping it as it is would leave a dead link and a price no one can check.
- tabby | link | https://github.com/TabbyML/tabby | GitHub repo, 200
- tabby | price_from | Free (open source; you run it yourself) | LICENSE: "available under the 'Apache 2.0' license"
- tabby | free_tier | true (unchanged)
- tabby | watch_out | You install and run it yourself on your own computer or server, and it works best with a graphics card (it supports regular consumer GPUs). The newest release came out in January 2026. | README: "Supports consumer-grade GPUs"; releases: "v0.32.0" published 2026-01-25
- tabby | watch_out_source | https://github.com/TabbyML/tabby
- tabby | last_checked | 2026-11-21
- good_for, open_weights, runs_on_your_computer, company: unchanged.

## 4. Question-page ripples: none
I searched data/questions.json (94 pages, every field) for "vocal remover", "goose", "tabby" and "tabbyml". The only hits are "Ultimate Vocal Remover" (the separate ultimate-vocal-remover card) on ai-music-generator-on-my-computer, ai-that-takes-vocals-out-of-a-song and ai-that-splits-a-song-into-instruments. No page names goose or tabby. Tabby's price is not quoted on any page, so the tabby edit causes no ripple either. This matches the worker's report.

## Housekeeping
- Browser: my own session ag019r-rv (profile ~/.config/pw-aiguide-recheck). After `close` its daemon was still alive, so I stopped only my own daemon (pid 73377) and its Chrome (pid 73405). `pgrep -f pw-aiguide-recheck` then printed nothing (exit 1).
- Read-only apart from this file. I did not touch providers*.json, questions.json or /tmp/ai-wrapper/.
- Rung: Opus 5.5. An independent final review of published facts fits the Opus tier.
