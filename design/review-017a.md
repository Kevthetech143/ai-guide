# Review 017a — question pages batch 4 (28 new)

Reviewer: Fable 5.1, independent, fresh context. 2026-10-11.
Verdict: **REVISE** — ship the 13 kept/fixed pages from /tmp/ag017a/questions.reviewed.json (36 old + 13 new = 49). Cut 15.

Method: for every page I matched the filter against providers.json myself, read every card's good_for / watch_out, checked each intro claim against the cards, and asked "does a non-technical person type this, and do the cards answer it?" Built the reviewed list in a temp copy (/tmp/ag017a/site-copy): build.py exit 0, linkcheck 0 broken, 49 question pages, each new page 1 h1 and >= 3 cards. Verified, not from memory.

Score 1-10. Under 7 = cut unless a small wording fix lifts it.

## Keep (10)

| slug | score | note |
|---|---|---|
| free-ai-music-maker | 8 | Real search. 21 cards. Intro claims (Suno, Udio, Mubert, Soundful, all free tier) match. A few cards are vocal removers, not makers, but all are music tools. |
| ai-music-generator-on-my-computer | 7 | Niche but real ("offline AI music generator"). All 10 cards fit. Intro honest about setup. |
| easiest-ai-image-generator | 7 | Real search. 22 easy image tools; intro names only on-page cards and flags the photo-editor ones (Remove.bg, Photoroom). |
| ai-image-generator-on-my-computer | 8 | Real search ("stable diffusion on my computer"). All 15 fit. Intro accurate (DiffusionBee, Draw Things, Fooocus claims match good_for). |
| ai-chatbot-on-my-computer | 8 | Real search ("offline AI chatbot"). 14 cards fit; intro (LM Studio, GPT4All, Jan, Ollama, AnythingLLM) accurate. |
| ai-coding-helper-on-my-computer | 7 | Borderline developer topic, but all 16 cards fit, jargon glossed (editor, terminal), claims match. |
| completely-free-ai-tools | 7 | Real search. 35 cards, all genuinely "Free". Intro honestly says "listed with a price of Free". Note: exact-string filter misses "Free (donations welcome)" etc.; acceptable since the page never claims completeness. |
| ai-that-takes-vocals-out-of-a-song | 7 | High-intent search ("ai vocal remover"). UVR and StemRoller are the right answer; Basic Pitch is a misfit the intro discloses. Filter is a proxy (music+local+easy): LALAL.AI, Vocal Remover, Spleeter are not on the page. Leftover: a "vocal-remover" tag in providers would make this page proper. |
| ai-that-types-what-i-say | 7 | Real search ("dictation app"). Handy, Buzz, Vibe fit; Fish Audio is a disclosed misfit. Same proxy-filter caveat. |
| ai-video-maker-on-my-computer | 7 | See Fixed — kept after intro fix. |

## Fixed (3)

| slug | score | fix |
|---|---|---|
| ai-text-to-speech-on-my-computer | 6 -> 7 | 4 of 10 cards (Whisper, Buzz, Vibe, Handy) do the opposite of the title. Retitled "Which AI voice tools run on my own computer?"; seo_title and meta updated to say both directions. Slug and intro unchanged (intro already covers both). |
| ai-video-maker-on-my-computer | 6 -> 7 | Intro called SwarmUI / SD.Next "a simple screen"; both are rated hard. Reworded to "give those models a web page you can click through. All of these are rated medium or hard to set up". |
| paid-ai-video-generator | 6 -> 7 | "Which … have no free plan?" is a question nobody types; "paid ai video generator" is. Retitled "Which AI video makers are paid only?", intro ends "expect to pay from day one". 9 cards incl. Veo, Luma; Replicate (developer, pay-per-run) is a weak fit but disclosed by its own card. |
| paid-ai-image-generator | 6 -> 7 | Same retitle: "Which AI picture makers are paid only?". 10 cards incl. Midjourney, Photoshop, Topaz. Magnific "bundles image, video, music, voice" matches its good_for. |

## Cut (15)

| slug | score | why |
|---|---|---|
| ai-tools-for-5-dollars-a-month | 4 | Exact string match on price_from. Unrelated tools (ElevenLabs, Kagi, Cartesia, a browser). Nobody types "AI tools $5 a month". |
| ai-tools-for-9-99-a-month | 4 | Same. Misses "$9.99/month (with Photoshop)", "Free (Pro $9.99/month)". Random 5. |
| ai-tools-for-10-dollars-a-month | 4 | Same. Midjourney + Suno + Copilot + Reclaim is a lookup table, not an answer. Misses 6 other "$10/month (…)" strings. |
| ai-tools-for-15-dollars-a-month | 4 | Same. 4 cards. |
| ai-tools-for-19-99-a-month | 3 | 3 cards. "Which AI tools start at $19.99 a month" has no search intent. |
| ai-tools-for-20-dollars-a-month | 4 | The one price people do compare ($20 plans), but the exact match excludes ChatGPT, Claude, Veo/Google AI Pro, Ollama — the tools a $20 searcher wants. Fails the real question. |
| ai-free-to-run-yourself | 3 | Data-string artifact (price_from == "Free to run yourself"). Excludes MusicGen "Free", ACE-Step "Free to download and run yourself". Duplicates open-source-ai-you-can-download. |
| ai-chat-tools-with-no-free-plan | 3 | Lead's concern confirmed. 3 cards: two marketing writers (Copy.ai, Jasper) and a screen-memory app (Pieces). No one asks this; "Paid" badge already answers it per card. |
| paid-ai-music-maker | 4 | 3 obscure cards (Stable Audio, ACE Studio, Jammable). No intent. |
| paid-ai-voice-generator | 4 | 4 cards, one with price "Check site"; mixes TTS, transcription, singing. No intent. |
| paid-ai-agents | 5 | "Helpers that do tasks for me" but 3 of 6 are coding tools (Codex, Qodo, Zencoder). Old ai-that-does-tasks-for-me covers the intent. |
| paid-ai-coding-tools | 5 | Developer topic (task said avoid); Qodo/Zencoder are team tools. No fix via filter. |
| ai-agent-on-my-computer | 6 | 7 of 17 cards are coding tools, 2 are automation builders at $24-$39; title promises "do tasks for me". Intro admits it. No filter fix (agents+local+easy gives Cursor/Typebot/AnythingLLM/LobeHub/Fellou — worse). OpenClaw/Hermes/goose deserve a page once data can tag "personal assistant". |
| ai-search-that-runs-on-my-computer | 5 | Every card needs Docker or a command line (Vane is rated hard). Not a page a non-technical person types or can act on. |
| easy-ai-picture-maker-to-install | 5 | 4 cards, 2 are upscalers; a strict subset of ai-image-generator-on-my-computer, whose intro already names DiffusionBee and Fooocus. Redundant. |

## Pattern notes for the lead

- The filter schema has only exact match on price_from, so any price-keyed page is an arbitrary subset. Do not ship price pages until the schema supports a numeric "price_under" rule (or providers carry a clean numeric field).
- "No free plan" is a badge, not a question. The "Paid" chip on every card already carries it.
- "On my own computer" pages work when the category's local tools are what people mean (chat, image, music, voice); they fail when the category is dominated by developer tools (agents, search).
- The worker's notes file (questions-batch4-notes.md) lists card counts that match my recount for all 28.

Unverified: I did not run the live site or deploy; search-intent judgments are reasoning, not measured search volume (no search-volume tool in this session).
