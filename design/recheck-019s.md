# Recheck 019s (2026-11-22), batch 31

## Changes
- warp-dev | watch_out | "Build: 1,500 credits ($20 of agent usage at API rates); you can add more usage as an add-on or with auto-reload" -> "Build: $20 of agent usage included each month at API rates; you can add more usage as an add-on or with auto-reload" | https://www.warp.dev/pricing (Warp Agent tab) | quote: "$20 of agent usage included each month at API rates"; "Add-on agent usage, auto-reload, and team-wide spend cap". The "1,500 credits" wording no longer appears on the page. price_from unchanged (Build $20/mo monthly, $18/mo annual).
- last_checked -> "2026-11-22" on all 20 cards.

## Verified unchanged (with notes)
- stable-audio: Free 50 credits, Solo $12/mo 660 credits; FAQ "No, your unused credits don't roll over."
- iask-ai: /pricing still redirects to the home page; no plans listed; home says "free question AI search engine". Old watch_out kept.
- recraft-ai: monthly toggle Basic $12 billed monthly (annual list $10/mo); Black Friday 40% off yearly ends Dec 1 (promo not published). Free images public, no commercial use.
- v0: Free $0 (7 message/day limit); Plus $30/user/month with $90 strikethrough still shown (list price recorded).
- zed-editor: Pro $10/mo, $5 tokens included, beyond at API list price +10%.
- vane: MIT, last release v1.12.2 (2026-04-10), last push 2026-09-01, Docker recommended, Ollama/OpenAI/Claude/Groq in README.
- andi: consumer search "Free forever. Andi Pro coming soon."; developer Search API has $5 free credit, prepaid credits, Team $49/mo; terms still say AI content may have errors.
- semantic-scholar: homepage 200 in browser (curl got no response); "free, AI-powered research tool for scientific literature".
- consensus: monthly toggle Pro $20/mo ($12/mo annual); 15 Deep reviews; Free 10 Pro messages, up to 3 Deep.
- gpt-researcher: Apache-2.0, v3.8.0 (2026-11-09), pushed 2026-11-12; README "~5 minutes per deep research", OpenAI+Tavily keys.
- ace-studio: Artist $20.73/mo billed yearly list, 20% holiday discount still shown ($16.58); 2500 credits/mo (holiday discount: list price kept).
- fish-audio: monthly toggle Plus $15/mo (50% off first month promo, not published); Free 8,000 credits; FAQ free plan personal non-commercial, unused credits do not roll over. fish-speech repo: Fish Audio Community License, S2-Pro weights on Hugging Face (Fish Audio Research License), latest GitHub release v1.5.1 (2025-05-31), pushed 2026-11-14. open_weights kept true (weights downloadable, with a custom license).
- retell-ai: pay-as-you-go $0.07-$0.31/min, $10 free credits; calculator voice infra $0.055/min, Retell voice $0.015/min.
- orpheus-tts: Apache-2.0, no GitHub releases, last push 2025-12-05; HF model canopylabs/orpheus-3b-0.1-ft still public (modified 2025-05-06). English models + multilingual research preview, pip install.
- sonix: Core $25/mo (5 hrs), +$25/seat; annual toggle shows no different Core price. NOTE for lead: page also lists Pay as you go $10/hr (no monthly fee) and a 30 min free trial; price_from kept at Core $25/month, free_tier false.
- upscayl: Cloud Pro $9.99/mo at 100 credits ($89.99/yr annual), $24.99 at 300; free trial 10 credits. Desktop app AGPL-3.0, last release v2.15.0 (2024-12-25), repo pushed 2026-11-20; README Vulkan/iGPU warning.
- automatic1111: AGPL-3.0, last release v1.10.1 (2025-02-09), last push 2026-03-02 (quiet, still downloadable). README "4GB video card support (also reports of 2GB working)", "must install python and git".
- fooocus: GPL-3.0, last release v2.5.5 (2024-08-12), last push 2025-12-01 (quiet). README Limited LTS bug fixes only; 4GB Nvidia, 8GB RAM, 40GB free.
- photoroom: Pro $12.99/mo monthly ($7.50/mo yearly); 8,000 credits, 1,000 exports; Video and 4K not in Pro. Free account confirmed in help center (free accounts personal use only): https://help.photoroom.com/en/articles/12523455-free-accounts-and-commercial-use

unchanged: stable-audio, iask-ai, recraft-ai, v0, zed-editor, vane, andi, semantic-scholar, consensus, gpt-researcher, ace-studio, fish-audio, retell-ai, orpheus-tts, sonix, upscayl, automatic1111, fooocus, photoroom
unreachable: none
checked: 20/20

## Question-page ripples
None. Searched data/questions.json (intro, meta_description, title) for "Warp"; no hits.
