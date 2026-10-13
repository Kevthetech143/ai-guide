# Review 017c — question pages batch 5 (18 new, first batch using the "ids" filter)

Reviewer: Fable 5.1, independent, fresh context. 2026-10-13.
Verdict: **REVISE** — ship /tmp/ag017c/questions.reviewed.json (49 old + 18 new = 67). 14 kept as-is, 4 kept after a small intro fix, 0 cut.

Method (same as review-017a): for every new page I pulled each card's good_for / watch_out from providers.json myself and checked it really does the task in the title; checked every intro claim against those cards; asked "does a non-technical person type this, and do the cards answer it?"; checked for near-duplicates against all 49 existing slugs (shared-id overlap computed, not eyeballed); and grepped providers.json for honest matches the worker left off. Built the reviewed list in a temp copy (/tmp/ag017c/site-copy): build.py exit 0, test_question_filter.py 4 tests OK, linkcheck 344 pages / 8536 links / 0 broken, 67 question pages, each new page exactly 1 h1 and 3-10 cards. seo_title < 60 and ends " - AI Guide", meta < 155, intros name only on-page providers (word-boundary check over all 237 names). Verified, not from memory.

Score 1-10. Under 7 = cut unless a small wording or ids fix lifts it.

## Keep (14)

| slug | score | note |
|---|---|---|
| ai-talking-avatar-video-maker | 8 | Real search ("ai avatar video"). All 5 cards say talking person / presenter / avatar. Intro claims (Synthesia lifelike presenter, HeyGen no camera or actors, D-ID from a photo, Colossyan training videos) match. Veed, DomoAI, Wondercraft also mention avatars in passing; not needed. |
| ai-for-short-videos-tiktok-reels | 8 | Real search. All 6 fit (clips, captions, "short social video"). Intro claims match. Distinct from ai-for-social-media-posts (103 cards, generic). |
| ai-that-removes-photo-backgrounds | 8 | High-intent search. All 5 say background removal. Clipdrop "20 uses per 24 hours" and Remove.bg "one click" claims match. Stockimg AI is a generator whose Starter plan includes removal; weak but honest and paid-badged. |
| ai-that-turns-a-photo-into-a-video | 8 | Real search ("image to video ai"). All 8 say "words or photos" / "from a photo". "About 10 seconds" (Luma 5-10s, Hailuo 6-10s) and "some free plans add a watermark" (Pika, Hailuo) match. |
| ai-that-keeps-what-i-type-private | 7 | Real search ("private ai chat", "ai that does not train on my data"). All 10 say private / no tracking / stays on your machine. Mixes chat and search but the title says "AI tools" and both are what the searcher means. You.com rides on the single word "private" in its own text; acceptable. |
| ai-that-writes-a-song-with-lyrics | 7 | See Fixed. |
| ai-that-transcribes-an-audio-file | 7 | Real search. 4 cards, all say audio -> text. Buzz and Vibe also sit on ai-that-types-what-i-say, but "transcribe a file" and "dictation" are different questions and this is the proper home for the first. Descript / Fireflies / Fathom were left off; they are meeting recorders by their own text, so leaving them off is right. |
| ai-for-finding-scientific-papers | 8 | Real search ("ai for research papers"). All 8 say scientific / academic / peer-reviewed. Intro claims (Semantic Scholar free + one-line summaries, Elicit 138M, Consensus peer-reviewed, "academic only") match. By filter it is a subset of ai-search-engine (33 cards), but that page answers a different question; this one is the direct answer students type. |
| ai-that-makes-a-small-photo-bigger | 8 | Real search ("ai photo upscaler"). All 4 say upscale / sharpen. Upscayl's Vulkan graphics-card warning is correctly surfaced. DiffusionBee and Stockimg also mention upscaling; optional. |
| ai-background-music-for-my-videos | 8 | Real search. All 7 say background / royalty-free music. Mubert watermark + attribution and Ecrett preview-only claims match. Distinct from free-ai-music-maker (intent is "music I can put under a video"). |
| ai-that-copies-a-voice | 7 | Very high-intent search ("ai voice cloning"). All 6 mention cloning in their own text. Weak for the audience: 2 are hard (Python), Hume is "mainly for people building apps", ACE Studio is a singing tool, PlayAI only mentions cloning in its watch_out. Fish Audio is the one plain answer; the intro says so and discloses the Python ones. ElevenLabs is absent because its data never says "clone" — correct under the hard rule. |
| ai-that-manages-my-calendar | 7 | Real search. 3 cards (the minimum), all say calendar / scheduling. Intro claims match, including OpenClaw's "connect only accounts you are happy for it to use". No other provider's text mentions calendar. |
| ai-that-researches-a-topic-and-writes-a-report | 7 | Real search ("ai deep research"). 6 of 7 say deep research / report; Perplexity rides on "deep searches" in its watch_out, a stretch but it is the mainstream answer. Two hard cards (GPT Researcher, Local Deep Research) are disclosed in the intro. |
| ai-that-turns-a-blog-post-into-a-video | 8 | Real search ("blog to video ai"). Pictory, Fliki, Lumen5 say blog post; Narakeet says script; InVideo says "text prompt", which the intro states honestly. Pictory "no ongoing free plan" matches. |
| ai-for-writing-marketing-copy | 7 | Real search ("ai copywriting tool"). All 4 say marketing copy / content. Intro claims (brand voice, teams not casual, budget pick, folded into Writesonic) match. Distinct from ai-for-writing-emails and ai-for-social-media-posts. |

## Fixed (4)

| slug | score | fix (intro only; ids, title, seo, meta unchanged) |
|---|---|---|
| ai-that-browses-websites-for-me | 6 -> 7 | Intro skipped the two cards a non-technical person actually asks about (ChatGPT agent, Perplexity Comet) and hid Comet's "collects your browsing history to target ads". Rewrote to name all 4 cards, state ChatGPT agent needs a paid plan, and carry the Comet ad caveat. 3 of 4 cards also sit on ai-that-does-tasks-for-me (16 cards), but that page is a broad agents list; "can AI browse websites for me" is its own search. |
| ai-that-answers-my-customers | 6 -> 7 | 3 of 4 cards are rated medium, and Vapi / Retell both say the AI model and voice are billed on top of the headline price. The intro said none of that. Added: both phone tools charge extra for model and voice; only Typebot is rated easy. |
| ai-for-designing-a-flyer-or-poster | 6 -> 7 | Flux's own text says posters, but also "technical steps and a strong graphics card" on your own computer; the intro named Flux nowhere while the meta did. Added one sentence disclosing that. Kept rather than cut because dropping it leaves 3 cards and the disclosure is more useful to the reader. No other provider's text mentions flyer or poster. |
| ai-that-writes-a-song-with-lyrics | 7 -> 7 | Intro was 4 sentences (brief says 2-3). Merged two sentences; claims unchanged. ACE Studio sings your melody and lyrics rather than writing them; its own card says so. |

## Cut (0)

None. The worker followed the hard rule (every card justified by its own text; I re-read all 92 card texts and found no card that does not do the titled task), skipped the thin candidates (translation, teachers, YouTube summary, cartoon, book, kids, real estate) correctly, and avoided the 017a ban list (no price pages, no "no free plan" pages, no developer-only topics).

## Pattern notes for the lead

- The "ids" filter works. Every page is a focused answer to a task question, which is what category pages could not give. Expect every ids page to be a filter-subset of some category page; that is by design, not a near-duplicate. The near-duplicate test should be "same question" not "same cards".
- The worker's recurring gap is the intro, not the card list: three fixes were "the cards' own watch_out says something a buyer needs (medium setup, add-on charges, ad tracking, technical install) and the intro skipped it". Next brief: require the intro to carry the biggest watch_out on the page.
- Pre-existing bug, not this batch: the intro of the old page ai-that-does-tasks-for-me names Manus, but Manus (skill medium) is not matched by its filter (agents + easy), so the intro names an off-page provider. Worth a one-line fix in a later batch.
- Data gaps that block honest pages people do search for: "translate text / a conversation" (only Buzz and Sonix mention translation), "AI for teachers", "summarize a YouTube video", "photo to cartoon". These need providers.json entries, not question-page work.
- ElevenLabs' good_for / watch_out never says "clone", so the voice-cloning page cannot list the most-searched tool. A one-line data fix would lift that page.
- The worker's notes file (questions-batch5-notes.md) card counts match my recount for all 18, and every quoted justification is a real substring of that card's text.

Unverified: search-intent judgments are reasoning, not measured search volume (no search tool in this session). I did not run the live site or deploy.
