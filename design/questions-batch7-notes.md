# Questions batch 7 notes (ai-guide-017e)

Part A: guidecheck.py now has check "E-offpage" (the old heading-order check keeps its "E:" label). It reads data/questions.json + data/providers.json, uses build.py question_matches, and flags any provider name in intro/title/seo_title/meta_description/how_picked that is not on the page. Longest provider name wins at each spot, so "Perplexity" inside "Perplexity Comet" is not flagged. Output: slug + field + name; exit 1.

Part B: 9 new pages (76 -> 85). Format: slug | search phrase | card count | id: "quote from good_for/watch_out"

- ai-for-editing-videos | ai for editing videos | 6 | capcut-ai: "A free video editor"; veed: "A web video editor with AI"; kapwing: "Edits videos in a web browser"; descript: "editing podcasts and videos"; wisecut: "Automatically cuts silences, adds subtitles"; submagic: "lets you cut the video"
- ai-that-automates-work-between-my-apps | ai to automate tasks between apps | 5 | zapier-ai: "connects your apps and does boring tasks"; gumloop: "no-code AI automations"; taskade: "automated workflow in one workspace"; relevance-ai: "multi-step work across apps"; n8n: "automations across hundreds of apps"
- ai-that-runs-jobs-on-a-schedule | ai scheduled tasks | 4 | gumloop: "run on a schedule"; autogpt: "They can run on a schedule"; fellou: "can run scheduled tasks"; hermes-agent: "runs scheduled tasks"
- ai-built-into-my-web-browser | ai browser | 3 | brave-leo: "built into the Brave browser"; perplexity-comet: "web browser with an AI assistant built in"; fellou: "web browser with an AI agent built in"
- ai-voices-in-many-languages | ai text to speech other languages | 4 | playht: "600 voices in 142 languages"; narakeet: "hundreds of voices and languages"; fish-audio: "in 30+ languages"; synthesia: "in over 160 languages"
- ai-search-that-shows-its-sources | ai search with sources | 7 | scira: "answers with sources from the web"; morphic: "complete answer with its sources"; liner: "writes answers with sources"; komo: "AI answers with links to the sources"; brave-search: "AI answers that cite their sources"; qwant: "shows a short Flash Answer with source links"; andi: "check the sources it shows"
- ai-tools-from-google | google ai tools | 7 | gemini: "help inside Google apps like Gmail"; google-ai-mode: "built into Google Search"; veo: "Google's top video maker"; google-flow: "Google's AI studio for making videos"; notebooklm and flow-music and magenta-realtime: no Google quote in text, picked by the company field ("Google" / "Google LLC")
- ai-tools-from-openai | openai tools | 5 | openai-agent: "paid ChatGPT plan"; codex: "paid ChatGPT plan to use it"; chatgpt, sora, whisper: picked by company field "OpenAI" (whisper text: "turns spoken audio into written text")
- ai-tools-from-meta | meta ai tools | 3 | meta-ai: "WhatsApp, Instagram, and Messenger"; llama: "through Meta's own apps"; musicgen: "Meta's open music-generation model"

### For the reviewer
- The three company pages (google, openai, meta) are keyed on the providers.json "company" field, not on a task. Cards whose own text does not say the company are listed above. Anthropic (2), Perplexity AI (2), Stability AI (2) were skipped as under 3.
- Google page leaves out Gemma and Google Antigravity (both for developers). OpenAI page keeps OpenAI Codex and says it is for programmers.
- ai-voices-in-many-languages: Synthesia is a video presenter, not audio; the intro says so.
- ai-search-that-shows-its-sources is a subset of ai-search-engine (same pattern as other ids pages). Self-install search tools (Vane, Local Deep Research, GPT Researcher) and developer APIs (Tavily, Exa) were left out.
- ai-that-automates-work-between-my-apps overlaps ai-that-does-tasks-for-me (Zapier AI, Gumloop, Taskade); n8n and Relevance AI are not on that page.
- No existing filter or page text was changed.

### Candidates skipped
- Under 3 honest cards: translation (Sonix, Buzz), sheet music (Klangio, Basic Pitch), background-noise removal (Krisp, LALAL.AI), game art (Leonardo, Scenario), AI friend/companion (Character.AI, Pi), Slack/Telegram chat (same cards as the WhatsApp page), Mac/iPhone image apps (Draw Things, DiffusionBee), sales leads (Relevance AI, AutoGPT).
- No card text at all: teachers, kids and parents, real estate, YouTube summaries, spreadsheets, essays, health, legal, interior design.
- Near-duplicates: royalty-free/commercial music (background-music page), blog to video, customer chatbots, apps without code.
