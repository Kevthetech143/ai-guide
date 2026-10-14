# Review 017d — intro audit (Part 1) + question pages batch 6 (9 new, "ids" filter)

Reviewer: Fable 5.1, independent, fresh context. 2026-10-14.
Verdict: **REVISE** — ship /tmp/ag017d/questions.reviewed.json (67 old incl. the 3 Part-1 intro fixes + 9 new = 76). 6 kept as-is, 3 kept after a small intro fix, 0 cut.

Method (same as review-017a / 017c): for every new page I pulled each card's good_for / watch_out from providers.json myself and checked it really does the task in the title; checked every intro claim against those cards; asked "does a non-technical person type this, and do the cards answer it?"; computed shared-id overlap against all 67 existing pages (not eyeballed); and grepped providers.json for honest matches the worker left off. Re-ran the worker's /tmp/ag017d/intro_check.py myself (0 hits / 76) and a stricter span-aware version of the same check (0 hits; it also catches the "ChatGPT" on-page / "ChatGPT agent" off-page case the blanking method can miss). Diffed the live file against questions.json.bak-20261014-batch6: only the 3 named intros changed in the first 67, nothing else; first 67 slugs identical. Built the reviewed list in a temp copy (/tmp/ag017d/site-copy): build.py exit 0, test_question_filter.py 4 tests OK, linkcheck 353 pages / 8689 links / 0 broken, 76 question pages, each new page exactly 1 h1 and 3-8 cards, every new seo_title < 60 and ends " - AI Guide", every meta < 155, every new intro 2-3 sentences. Verified, not from memory.

Score 1-10. Under 7 = cut unless a small wording or ids fix lifts it.

## Part 1 — intro audit (3 rewrites)

| slug | result | note |
|---|---|---|
| ai-that-does-tasks-for-me | OK | New intro names ChatGPT agent, Fellou, Zapier AI, Lindy; all four are matched by {agents, easy}. Claims match: Fellou "comparing prices", Zapier "saving email attachments", Lindy "calendar". Manus gone. |
| best-paid-ai-worth-the-money | OK | Midjourney "no free plan", ChatGPT agent "fills out forms", Claude Code "read your whole project, make changes" all match. "$17 to $20 a month" = Claude Code $17 annual / $20 monthly, ChatGPT agent $20. ChatGPT and Sora (both free_tier true, so off-page) gone. |
| ai-that-browses-websites-for-me | OK | Only change: "a paid ChatGPT plan" -> "a paid plan". ChatGPT itself is not on the page, so this is right. Rest is the 017c-reviewed text. |

No filters changed (verified by diff). The worker's note that 5 raw checker hits were substring false positives (Claude in Claude Code, Perplexity in Perplexity Comet, Vocal Remover in Ultimate Vocal Remover) is correct; my span-aware check agrees.

## Part 2 — Keep (6)

| slug | score | note |
|---|---|---|
| ai-that-reads-text-out-loud | 8 | Real search ("ai that reads text aloud"). All 5 cards say read aloud / text-to-speech in their own text. Intro claims (Speechify robotic free voices + $29, Typecast paste-and-pick, ElevenLabs natural audio, Kokoro and Piper technical) match. Kokoro/Piper are hard; disclosed. Optional later ids add: PlayAI ("turns your written text into realistic spoken audio") and Fish Audio ("text-to-speech") qualify on the same basis as ElevenLabs; not needed. 5/5 cards also sit on the voice category pages, but "read this to me" is its own question. |
| ai-voiceover-for-my-videos | 8 | Real search. Murf, WellSaid, Listnr, Narakeet, ElevenLabs, Kapwing all say voiceover / spoken audio; Fliki says "video with a realistic AI voice" and the intro describes it that way. Murf no-download-on-free and Narakeet no-commercial-on-free claims match. Optional later ids add: InVideo ("AI voiceover"). |
| ai-that-summarizes-a-web-page | 7 | Real search ("ai to summarize an article"). Brave Leo (page/document/PDF), Comet (pages), Qwant (one-click page summary with free account), iAsk (instant summarizer), Claude (long documents) all say it. Intro carries Leo's Brave-only and Comet's ad-tracking watch_outs. Closest old page is ai-that-reads-documents-for-me (68 cards, generic search+voice filter); different question, 3/5 shared. ChatGPT absent because its card text never says summarize; correct under the hard rule. |
| one-app-for-many-ai-chatbots | 8 | Real search ("all ai chatbots in one app"). Poe, DDG AI Chat, Chatbox, LobeHub say many models / switch models; Msty and Open WebUI say local or online models in one app. Intro says those two take more setup (medium / hard) and that stronger models cost extra; both match. 6/6 are a subset of best-free-ai-chatbot by filter; different question. |
| ai-that-removes-objects-from-photos | 7 | Very high-intent search ("remove object from photo ai"). Only 3 cards (the minimum) but all three say erase / remove objects. Intro carries Clipdrop's 20-per-day cap and Photoshop's paid-plan-plus-practice watch_out. Worker correctly left off Krita / Mage / Automatic1111 (their text says "inpainting", not removal, and they are hard). Shares 2 cards with ai-that-removes-photo-backgrounds; different question. |
| ai-i-can-use-in-whatsapp | 7 | Real search ("ai in whatsapp"). Meta AI, OpenClaw, Hermes Agent, Botpress all name WhatsApp in their own text; no other provider does. Intro carries Meta AI's training-data opt-out, the two agents' setup, and Botpress being for businesses. Weak for the audience (3 of 4 are medium) but the one plain answer is first and the rest is disclosed. |

## Fixed (3)

| slug | score | fix (intro only; ids, title, seo, meta unchanged) |
|---|---|---|
| ai-that-adds-subtitles-to-videos | 7 -> 8 | All 8 cards say captions / subtitles. Intro said "Free plans have limits" as if every card had one; Submagic ($19/month) and Sonix ($25/month) have no free plan (free_tier false). Added "Submagic and Sonix have no free plan, and the free plans elsewhere have limits". Kapwing watermark and Wisecut 360p claims match. |
| ai-that-sings-in-another-voice | 7 -> 8 | All 4 cards say sing / cover / singing voice. Intro disclosed Jammable's no-free-plan but not ACE Studio's (free_tier false, $20.73/month, medium). Changed to "Jammable and ACE Studio have no free plan, and many of Jammable's voices imitate real singers". |
| ai-video-maker-with-sound | 7 -> 7 | Sora, Veo, LTX-2 all say matching / synchronized sound; no other video card does (Wondercraft "sound tools" and Mureka "music videos" correctly left off). Intro used "GiB", which is jargon for this audience; changed to "GB". Sora daily limit, Veo $20 + per-second, LTX-2 command-line claims match. |

## Cut (0)

None. Every card on every new page is justified by its own good_for / watch_out (I re-read all 45 card texts). The worker's notes file card counts match my recount for all 9, and every quoted justification is a real substring of that card's text. Skips (cover letter, medical bill, workouts, budgeting, room design, interview, translation at 2 cards, memes at 1, YouTube summary, teachers, kids, logo animation) are right: I grepped providers.json for each and found nothing the worker missed. The four "duplicate" skips (birthday song / lyrics, voice memo, app builder) are correctly covered by existing pages.

## Pattern notes for the lead

- Same gap as 017c, smaller this time: 2 of 3 fixes were "the intro implies a free plan where a card has none". Next brief: when the intro mentions free plans, name every card on the page with free_tier false.
- The intro checker (/tmp/ag017d/intro_check.py) is worth keeping as a repo-level check; it would have caught the Manus bug a batch earlier. Its blanking approach misses one case (an on-page name that is a prefix of an off-page name, e.g. ChatGPT on-page with ChatGPT agent off-page); a span-aware match fixes that. Not a hit today.
- Pre-existing, not this batch: ai-that-reads-documents-for-me's intro says Perplexity and Google AI Mode "can summarize long articles and web pages", but neither card's text says summarize. Same class of bug as Manus (intro claim not backed by card text), just not an off-page name, so the checker does not catch it. Worth a one-line intro fix in a later batch.
- The batch is small (9 of up to 18) because the data honestly runs out; the useful remaining searches (translation, medical letter, workouts, budgeting, teachers, YouTube summary) need providers.json entries, not question-page work. Translation needs just one more honest card.
- Three pages sit at the 3-4 card minimum (remove objects, video with sound, WhatsApp). They are honest and high-intent, but a data pass adding e.g. Kling / Hailuo "with sound" (if true) or a ChatGPT-on-WhatsApp note would lift them.

Unverified: search-intent judgments are reasoning, not measured search volume (no search tool in this session). I did not run the live site or deploy. The live site folder was not edited; all fixes live only in /tmp/ag017d/site-copy and /tmp/ag017d/questions.reviewed.json.
