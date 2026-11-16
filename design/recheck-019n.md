# recheck-019n (2026-11-16)

Changed fields (price numbers are the same; only the order or a source URL changed):
- pika | price_from | "$8/month (billed annually; $10 monthly)" -> "$10/month ($8 billed annually)" | https://pika.art/pricing "Starter $10/mo, $8/mo ($96/year)"
- canva-ai | price_from | "$12/month (billed annually; $18 monthly)" -> "$18/month ($12 billed annually)" | https://www.canva.com/pricing/ Monthly toggle: Pro "US$ 18 /month"; Yearly: "US$ 144 /year"
- bolt-new | price_from | "$18/month (billed annually; $25 monthly)" -> "$25/month ($18 billed annually)" | https://bolt.new/pricing Pro "$25 /month Billed monthly"; Yearly toggle "$18 /month ... Billed annually"
- descript | price_from | "$16/month (billed annually; $24 monthly)" -> "$24/month ($16 billed annually)" | https://www.descript.com/pricing Hobbyist "$16 | $24 per person / month" (Annual | Monthly)
- ideogram | price_from | "$15/month (billed annually; $20 monthly)" -> "$20/month ($15 billed annually)" | https://ideogram.ai/pricing Plus "$20 per month, $180 billed annually"
- codex | watch_out_source | https://developers.openai.com/codex/pricing -> https://learn.chatgpt.com/docs/pricing | old URL gives 308 redirect to the new one; page: "Free ... quick coding tasks", "Go $8/month ... lightweight coding tasks", "Plus $20/month ... Codex on the web, in the CLI, in the IDE extension"
- last_checked -> 2026-11-16 on all 20 cards.

Verified, no change (prices, free_tier, open_weights, runs_on_your_computer, watch_out all match official pages):
- cursor (Free $0; Plus $8 Grok models only; Premium $30 third-party billed extra), devin (Free light quota; Pro $20; extra at API pricing), github-copilot (Free 2,000 completions/mo; Pro $10), character-ai (lite "starts at $4.99/mo ... varies by region"; free "unlimited messaging", lite "significantly reduces the ads"), veo/Flow (50 daily credits free; Google AI Plus $4.99/mo*), kling (Standard $10, 12% off yearly-monthly shows $8.8, 30% off first month, 6.99 first month: promo noted, list price kept), hailuo (Standard $14.99 list, 30% off = $10.50 monthly, 44% off = $8.40 yearly; free = one-time trial credits; page header says "From $9.99/mo" and a "H3 Image 50% off" banner: promos, not published), heygen (Free 3 videos/mo watermarked; Creator $29), amazon-q-developer (Pro $19; "Billing starts when you use agentic coding, transformation agents or code completions"; no end-of-sale notice on page), google-ai-mode (support page: "AI responses may include mistakes"; history needed to resume), deepseek (privacy policy: "store your Personal Data in People's Republic of China"; chat.deepseek.com redirects to sign_in, free).
- canva-ai free AI: "Limited access to Standard and Premium AI" still holds.

Open-source / local tools (not downloaded):
- whisper: github.com/openai/whisper, MIT, latest release v20250625 (2025-06-26), repo last push 2026-08-31, not archived; README: pip install + ffmpeg. Upkeep slow (FYI).
- aider: github.com/Aider-AI/aider, Apache-2.0, latest release v0.86.0 (2025-08-09), PyPI 0.86.2 (2026-02-12), repo last push 2026-05-22. Upkeep slow (watch item, FYI).
- codex: github.com/openai/codex, Apache-2.0, latest rust-v0.169.0 (2026-11-13), pushed 2026-11-16. Card keeps open_weights false (models are not open), runs_on_your_computer false (as before; CLI is open source, lead may want to review this flag, FYI).
- gemma: Hugging Face google/gemma-4-* (E2B/E4B/12B, updated 2026-10-30 to 2026-11-03), license apache-2.0, not gated (12B-it checked). gemma.ai/get-started returns 200 ("Quickstart - Gemma 4", by Google DeepMind). Unchanged.
- deepseek: HF deepseek-ai newest DeepSeek-V4.1-Flash-1017 (2026-11-10); license not re-read this round; open_weights true unchanged.
- ideogram open_weights true unchanged (past note: HF ideogram-ai non-commercial gated; not re-read).

Unverified items (left as they were): ideogram watch_out "public by default / weekly credits" is on docs.ideogram.ai (Plans and Credits, via web search summary), the pricing page itself only shows "Private generation" on Plus/Pro. descript "60 media minutes" free seen via WebFetch of the pricing page (not in the browser text).

unchanged: cursor, character-ai, deepseek, devin, gemma, github-copilot, kling, veo, whisper, aider, amazon-q-developer, google-ai-mode, hailuo, heygen (card facts); pika, canva-ai, bolt-new, descript, ideogram, codex had format/source edits only.
unreachable: none
checked: 20/20

## Question-page ripples
No free_tier, price_from amount, watch_out or good_for fact changed, only the order of the same prices, so no sentence is made wrong. Pages that name the five reordered providers (lead may skim for annual-first wording like "$8 a month if you pay yearly"): best-ai-for-making-videos, paid-ai-video-generator, ai-that-turns-a-photo-into-a-video, ai-that-is-fun-to-play-with (Pika); free-ai-image-generator, ai-for-making-logos, easiest-ai-image-generator, ai-for-designing-a-flyer-or-poster (Canva, Ideogram); ai-for-editing-photos, ai-for-making-a-presentation (Canva); ai-for-making-a-podcast, ai-for-meeting-notes, ai-for-editing-videos (Descript). Not checked sentence by sentence because no amount changed.
