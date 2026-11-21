# Recheck 019r (2026-11-21), batch 30

## Changes
- vocal-remover | watch_out | "...a membership raises that to 300 minutes a day and 25-minute files" -> "...a membership raises that to 300 minutes a day (500 on the yearly plan) and 25-minute files" | https://vocalremover.org/next/pricing (seen in real Chrome) | "Month US$12.95 300 minutes 25 minutes; Year US$99 500 minutes 25 minutes"
- goose | watch_out | "You connect your own AI model (an API key or an existing Claude, ChatGPT or Gemini subscription), and that model's costs are separate" -> "You connect your own AI model - a local model on your computer, an API key, or an existing Claude or ChatGPT subscription - and that model's costs are separate from goose" | https://goose-docs.ai/docs/getting-started/providers | "ChatGPT Codex ... Requires a ChatGPT Plus/Pro subscription"; "Claude Code subscription"; "Atomic Chat Run local models"; home page: "Load and run local models directly inside goose". (Old text named a Gemini subscription; the page only shows Google Gemini "provides a free tier", so it was dropped.)
- goose | watch_out_source | https://goose-docs.ai -> https://goose-docs.ai/docs/getting-started/providers | the old home page does not show the API key / subscription facts.

## Notes (no field changed)
- tabby: NOT verified. https://www.tabbyml.com/pricing (the card's link, and /pricing/) now returns 404 and tabbyml.com home is now a consulting page ("Turn failure patterns into measurable improvements"), with no plans or prices. $19/seat Team and 5-user Community cannot be re-seen anywhere official. Product itself still exists: github.com/TabbyML/tabby not archived, v0.32.0 (2026-01-25), last push 2026-06-30, Apache 2.0 outside ee/ (see LICENSE), docs at tabby.tabbyml.com load. Old card kept with old date (2026-11-07). Lead decision: keep, drop the price, or point link to https://github.com/TabbyML/tabby.
- diffusionbee: still downloadable, page matches; but newest GitHub release is 2.5.3 (2024-08-14), last push 2024-10-30. Not a card fact change.
- gpt4all: page still has downloads; newest GitHub release v3.10.0 (2025-02-25), last push 2025-05-27. nomic.ai banner "Nomic Individual Plans start at $20/month" is for Nomic's own product, not GPT4All; card unchanged.
- Open-model checks: musicgen (HF, cc-by-nc-4.0, public), jan v0.8.8 (2026-10-28), anythingllm v1.20.0 (MIT), comfyui v0.46.0 (GPL-3.0), goose v1.60.2 (Apache-2.0).
- Promos seen, not published: lalal.ai "40% OFF" on Top-Ups; replicate "Minimax H3 Lite and Highspeed are 50% until end of year"; boomy Creator shows 33% off (card already keeps list $14.99); loudly/lalal/flow/soundraw pages open on the yearly view (card already monthly-first).
- Verified unchanged prices: soundraw $16.99 ($11.04 yr), lalal $9.99 ($7.50 yr, monthly seen after clicking Monthly), flow $8 ($6 yr), exa from $4/1k, comfy cloud $20 ($16 yr), anythingllm $50, tavily $30 / $0.008 credit, qodo $30, pieces $18.99, replicate per-model, mureka $10 ($8 yr) / Premier $30, loudly $10 ($8 yr), boomy $14.99 list.

unchanged: soundraw, lalal-ai, flow-music, musicgen, exa, gpt4all, jan, anythingllm, comfyui, diffusionbee, tavily, qodo, pieces, replicate, mureka-ai, loudly, boomy (all re-dated 2026-11-21)
unreachable: tabby (pricing page 404, company site changed)
checked: 19/20

## Question-page ripples
None. The only name hits in data/questions.json are "Ultimate Vocal Remover" (a different tool from vocalremover.org) on ai-music-generator-on-my-computer, ai-that-takes-vocals-out-of-a-song, ai-that-splits-a-song-into-instruments; no question page names goose or Vocal Remover (vocalremover.org). No ripple from changed watch_out text.
