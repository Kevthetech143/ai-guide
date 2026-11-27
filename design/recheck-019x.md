# Recheck 019x (2026-11-27)

## Changed fields
- researchrabbit | watch_out | "Free allows up to 50 seed articles. Up to 300 seed articles, advanced search controls and multiple projects need ResearchRabbit+ at $12.50/month ($10/month on the annual plan)." -> "Free allows up to 50 seed articles. Even more seeds, filters, projects, alerts and Zotero sync need ResearchRabbit+ at $12.50/month ($10/month on the annual plan)." | https://www.researchrabbit.ai/pricing | "Start with even more Seeds"; "Filter"; "Projects"; "Alerts"; "Sync with Zotero"; FAQ "up to 50 seed articles" (the "300" figure is no longer on the page)
- all 20 | last_checked | -> 2026-11-27

unchanged: viggle, wan-2-2, stockimg-ai, mage-space, sd-next, wangp, scenario, screenpipe, taskade, gemini, grok, perplexity, llama, mistral, qwen, midjourney, stable-diffusion, flux, elevenlabs
unreachable: none
checked: 20/20

## Notes (no change made)
- Promos seen, not published: ElevenLabs Starter "$1 first month" on monthly billing (list $6/month confirmed) and Black Friday up to 55% off yearly (ends Dec 1); Scenario Black Friday up to 60% off yearly (to Nov 29); Screenpipe BF 20% off first year (list Basic $25/month, $250/yr); Grok Premium "$30 / 2 months" BF deal (list $30/month); Viggle yearly shows crossed-out list prices (Pro list $9.99/month monthly, $7.99 yearly).
- No promo or sale price appears in any existing watch_out.
- stockimg-ai: FAQ on the official pricing page says "Stockimg AI offers a free account option with limited features" and "$19 to $29 per month" (stale; plan cards show $12/$24/$48). Plan cards show no free plan; free_tier left false. Lead may decide.
- mage-space: header shows "Get 300 free Gems" for new accounts; plans start at $10 Basic. free_tier left false (sign-up bonus, no free plan).
- perplexity: pricing page shows only "$17/month when billed annually"; no monthly price shown, kept as is.
- taskade: Starter is yearly-only ($72/yr); Pro $20 monthly / $10 yearly confirmed via the card toggle.
- Open source: wan-2-2 (Apache-2.0, last push 2026-09-21, not archived, README 80GB / 24GB lines confirmed); sd-next (Apache-2.0, pushed 2026-11-26, All-in-One Windows launcher confirmed); wangp (repo deepbeepmeep/WanGP, Community License 2.0, pushed 2026-11-26; site: free locally, paid hosting needs permission, from 6 GB VRAM); screenpipe (repo moved to screenpipe/screenpipe, pushed 2026-11-27; not archived).
- Model families: llama (Meta page still lists Llama 4 with HF/Kaggle downloads; HF meta-llama last Llama 4 update 2025-05; Meta's new "Muse" models are listed, so Llama is going quiet, note only); mistral (HF mistralai updated 2026-11-24, open weights still published); qwen (HF Qwen3.6-27B etc, Apache-2.0, updated 2026-11-20); stable-diffusion (SD 3.5 community license page 200, HF stabilityai still active, newest uploads 2026-11); flux (FLUX 3 Image Klein open weights released 2026-10 under FLUX Kommunity License, gated; FLUX.2 klein 4B still Apache-2.0 and cited as source).
- Hosted Wan: wan.video/pricing Pro $10/month monthly ($5 yearly), confirmed.
- Hand-checked: all card links and watch_out_source URLs returned 200 or rendered in real Chrome (x.ai, midjourney docs, perplexity block curl). Browser session closed; pgrep -f pw-aiguide-recheck prints nothing (needed a kill of my own ag019x daemon, PID 85505).

## Question-page ripples
None. Only researchrabbit's watch_out changed; searched data/questions.json (title, meta_description, intro) for "ResearchRabbit" / "Research Rabbit": no matches.
