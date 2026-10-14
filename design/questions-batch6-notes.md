# Questions batch 6 notes (ai-guide-017d)

## Part 1: intro audit (all 67 existing pages)

Check: /tmp/ag017d/intro_check.py (run from site/). For every question it lists provider names in the intro that the page filter (build.py question_matches) does not match. On-page names are blanked first, so "Claude" inside "Claude Code" and "Perplexity" inside "Perplexity Comet" are not counted. Raw first run found 9 hits; 5 were substring false positives (Vocal Remover inside Ultimate Vocal Remover x2, Claude inside Claude Code x2, Perplexity inside Perplexity Comet), 4 were real (Manus; ChatGPT and Sora on best-paid; ChatGPT on ai-that-browses-websites-for-me). Fixed all 4 real ones (intro text only; no filter changed).

- ai-that-does-tasks-for-me
  - before: AI agents go beyond chatting: ChatGPT, Claude, and Manus can browse the web, fill in forms, and complete multi-step jobs for you. You describe the outcome you want, and the agent works through the steps on its own.
  - after: AI agents go beyond chatting: ChatGPT agent and Fellou can browse the web and carry out online chores like comparing prices. Zapier AI and Lindy take care of routine jobs such as saving email attachments or handling your calendar. You describe the outcome you want, and the agent works through the steps on its own.

- best-paid-ai-worth-the-money
  - before: If you make images every day, Midjourney's image quality is the reason professionals pay for it. ChatGPT Plus unlocks the ChatGPT agent and Sora video, and Claude Code pays for itself if coding is part of your job.
  - after: If you make pictures every day, Midjourney turns a short description into beautiful art, though it has no free plan. ChatGPT agent handles online chores like filling out forms, and Claude Code can read your whole coding project and make changes. Those two start around $17 to $20 a month.

- ai-that-browses-websites-for-me
  - before: ChatGPT agent browses the web, fills out forms, and compares prices for you, but it needs a paid ChatGPT plan. Fellou and Perplexity Comet are web browsers with an AI assistant built in that does online jobs for you, though Comet collects your browsing history to target ads. Hermes Agent is one you install yourself, and with any of them, check the work before they book or buy anything.
  - after: ChatGPT agent browses the web, fills out forms, and compares prices for you, but it needs a paid plan. Fellou and Perplexity Comet are web browsers with an AI assistant built in that does online jobs for you, though Comet collects your browsing history to target ads. Hermes Agent is one you install yourself, and with any of them, check the work before they book or buy anything.

Kept sentences matched to cards: ChatGPT agent and Fellou "browse the web"/"carries out online jobs"; Zapier AI "saving email attachments"; Lindy "email, calendar, meetings"; Midjourney "no free plan"; Claude Code "read your whole project, make changes"; "around $17 to $20 a month" from Claude Code ($17 annual/$20 monthly) and ChatGPT agent ($20/month).

On ai-that-browses-websites-for-me the fix was: "a paid ChatGPT plan" became "a paid plan" (ChatGPT itself is not on that page; the card text says ChatGPT plan).

## Part 2: 9 new pages (67 -> 76)

Format: slug | search phrase | card count | id: "quote from good_for/watch_out"

- ai-that-reads-text-out-loud | ai that reads text out loud | 5 | speechify: "articles, documents, and books read aloud"; elevenlabs: "natural-sounding spoken audio"; typecast: "pick an AI voice to read it aloud"; kokoro-tts: "reads text aloud in a natural voice"; piper-tts: "Good for reading text aloud"
- ai-voiceover-for-my-videos | ai voiceover for my video | 7 | murf: "natural-sounding voiceovers for videos"; wellsaid-labs: "studio-quality voiceovers for videos"; listnr: "natural voiceovers for videos and podcasts"; narakeet: "spoken voiceover or narrated video"; elevenlabs: "great for videos, podcasts"; kapwing: "AI tools for subtitles, voiceovers"; fliki: "realistic AI voice, stock footage"
- ai-that-adds-subtitles-to-videos | ai subtitles for video | 8 | submagic: "adds captions automatically"; capcut-ai: "AI captions, background removal"; kapwing: "AI tools for subtitles"; veed: "web video editor with AI subtitles"; wisecut: "adds subtitles and background music"; sonix: "translation, and subtitle exports"; vibe: "with subtitles export"; whisper: "transcribing meetings, lectures, or video subtitles"
- ai-that-summarizes-a-web-page | ai summarize web page | 5 | brave-leo: "summarize the web page, document or PDF"; perplexity-comet: "can summarize pages"; qwant: "condenses a web page in one click"; iask-ai: "instant summarizer"; claude: "summarizing long documents"
- one-app-for-many-ai-chatbots | use multiple ai chatbots in one app | 6 | poe: "trying many different AI models in one app"; duckduckgo-ai-chat: "you can switch between models"; chatbox: "One app on desktop, mobile and the web"; lobehub: "Chat with many AI models"; msty: "chatting with AI models, either ones"; open-webui: "works with AI models on your own computer"
- ai-that-removes-objects-from-photos | remove object from photo ai | 3 | clipdrop: "erase unwanted objects"; pixelcut: "Remove backgrounds, erase objects"; photoshop-generative-fill: "add or remove anything in a photo"
- ai-that-sings-in-another-voice | ai cover song different voice | 4 | jammable: "Make AI cover songs"; audimee: "different singing voice"; kits-ai: "Training AI voices to sing"; ace-studio: "AI singing voices from your melody"
- ai-i-can-use-in-whatsapp | ai in whatsapp | 4 | meta-ai: "already lives inside WhatsApp"; openclaw: "message from WhatsApp, Telegram"; hermes-agent: "talk to from Telegram, Discord, Slack, WhatsApp"; botpress: "website, WhatsApp, or Slack"
- ai-video-maker-with-sound | ai video with sound | 3 | sora: "even with matching sound"; veo: "even with matching sound"; ltx-2: "video with synchronized sound"

### Candidates skipped (data cannot honestly support them, or already covered)
- cover letter, medical bill/letter, workouts, budgeting, room design, interview practice, teachers, kids/parents, photo-to-cartoon, old-photo fixing: no provider's good_for/watch_out mentions them.
- translation: only Sonix and Buzz mention it (2, need 3). YouTube summaries: none. Memes: only Viggle.
- birthday song / song lyrics: duplicate of ai-that-writes-a-song-with-lyrics. Voice memo to notes: covered by ai-that-transcribes-an-audio-file and ai-for-meeting-notes. Logo animation: nothing in the data. App builders: duplicate of ai-that-builds-websites (same 11 cards). Dyslexia: no card says it; the read-aloud page claims only reading aloud.
- Summarizing long emails: no card says it (Lindy only "handles your email").

### Notes for the reviewer
- ai-that-removes-objects-from-photos has the 3-card minimum; the only other possible matches (Krita AI inpainting, Mage inpainting) do not say "remove".
- ai-video-maker-with-sound is 3 cards; Wondercraft mentions "sound tools" only, so it was left off.
- ai-i-can-use-in-whatsapp: Botpress is a business chatbot builder; the intro says so. Meta AI's training-data caution is carried in the intro (biggest watch_out).
- Pages are filter-subsets of category pages by design (see review-017c).
- No existing filter was changed.

