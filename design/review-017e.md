# Review 017e — guidecheck E-offpage check (Part A) + question pages batch 7 (9 new, "ids" filter)

Reviewer: Fable 5.1, independent, fresh context. 2026-10-15.
Verdict: **REVISE** — ship /tmp/ag017e/questions.reviewed.json (76 old unchanged + 9 new = 85). 2 kept as-is, 7 kept after a small fix (6 intro-only, 1 intro + ids + meta), 0 cut. Part A check is correct and ships as-is; one gap noted below with a tested 4-line patch the lead can take or leave.

Method (same as review-017c / 017d): for every new page I pulled each card's good_for / watch_out from providers.json myself and checked it really does the task in the title; checked every intro claim against those cards; asked "does a non-technical person type this, and do the cards answer it?"; computed shared-id overlap against all 76 existing pages (not eyeballed); grepped providers.json for honest matches the worker left off; and checked the company field for the three company pages. Diffed live questions.json against questions.json.bak-20261015-batch7: first 76 entries identical, 9 appended. Diffed guidecheck.py against guidecheck.py.bak-20261015-offpage: only the import and the E-offpage block added; A-D and the old E unchanged. Built the reviewed list in a temp copy (/tmp/ag017e/site-copy): build.py exit 0, test_question_filter.py 4 tests OK, linkcheck 362 pages / 8844 links / 0 broken, guidecheck 0 issues exit 0, 85 question pages under dist/best/, each new page exactly 1 h1 and 3-9 cards, every new seo_title < 60 and ends " - AI Guide", every new meta < 155, every new intro 3 sentences. Verified, not from memory.

Score 1-10. Under 7 = cut unless a small wording or ids fix lifts it.

## Part A — guidecheck.py "E-offpage"

Ran it myself. Live data: 0 issues, exit 0. Negative cases in a scratch copy (/tmp/ag017e/neg-review, never the live folder):

| case | expected | result |
|---|---|---|
| "Manus" appended to ai-that-does-tasks-for-me meta_description (the original bug) | flag | flagged: `E-offpage: ai-that-does-tasks-for-me meta_description names Manus (not on page)`, exit 1 |
| "ChatGPT agent" in best-free-ai-chatbot intro (ChatGPT on page, agent off page: the prefix case 017d warned about) | flag "ChatGPT agent" | flagged correctly |
| "Lindy" in how_picked; "Claude" in a title | flag both | both flagged (proves all five fields are read) |
| "Perplexity Comet" named on a page that has Comet but not Perplexity | no flag | no flag (longest-name-wins works) |
| "Perplexity AI" (the company) in text | n/a | flags "Perplexity". Conservative, not wrong; the fix is to not write the company name in copy. |
| "PlayAI" and "Brave Search" named on ai-tools-from-meta (both off page) | flag | **not flagged** — see gap |

Gap: four provider names carry a parenthesised suffix ("PlayAI (formerly PlayHT)", "Brave Search (Ask Brave)", "Canva AI (Magic Studio)", "Photoshop (generative fill)") and copy always writes the short form, so an off-page "PlayAI" / "Brave Search" / "Canva AI" / "Photoshop" can never be caught. Tested a 4-line patch that also counts the part before " (" as an alias, both for matching and for the on-page set: 0 issues on the reviewed data, and the same negative run goes 5 -> 7 issues (adds PlayAI and Brave Search). Patched file: /tmp/ag017e/guidecheck-alias-patch.py (whole-file drop-in for guidecheck.py; diff is the `_aliases` helper + the `on_page` line). Not applied to the live file; the lead's call. Also checked: `from build import question_matches` is side-effect free (build.py has a `__main__` guard), and the regex escapes dotted names (You.com, Remove.bg) correctly.

Part A verdict: correct, stdlib only, A-D untouched, exits non-zero, prints slug + field + name. Ship as-is; alias patch optional.

## Part B — Keep (2)

| slug | score | note |
|---|---|---|
| ai-built-into-my-web-browser | 7 | Real search ("ai browser"). Brave Leo "built into the Brave browser"; Comet and Fellou both "a web browser with an AI assistant/agent built in". Intro carries Comet's ad-tracking watch_out. Only 3 cards but no other provider's text says it is a browser (Microsoft Copilot's text never mentions Edge, so leaving it off is right). Shares 2 cards with ai-that-browses-websites-for-me and 2 with ai-that-summarizes-a-web-page; "is there an AI in my browser" is its own question. |
| ai-tools-from-meta | 7 | Real search ("meta ai tools"). All 3 cards have company = Meta; no fourth exists. Intro claims (WhatsApp/Instagram/Messenger, opt-out training, Llama download or Meta's apps, MusicGen needs coding + non-commercial license) all match. Thin (2 of 3 are medium/hard) but the plain answer is first and the rest is disclosed. |

## Fixed (7)

| slug | score | fix |
|---|---|---|
| ai-search-that-shows-its-sources | 6 -> 8 | **ids + intro + meta.** The worker's 7 cards are all justified, but the page left off the two mainstream answers to this exact question: Perplexity ("answers that show exactly which websites the facts came from") and You.com (same phrase). A non-technical person asking this expects Perplexity first. Added both (9 cards), named them first in the intro, kept every original claim, and added the biggest watch_out on the page (Scira's free plan allows only 3 searches a day). Meta now 147 chars. how_picked unchanged. Google AI Mode ("full AI answers with links") is a borderline optional add; left off. |
| ai-for-editing-videos | 7 -> 7 | Intro only: 4 sentences -> 3 (brief says 2-3; 017c fixed the same). All 6 cards say edit / captions / cut silences / edit by transcript. Claims (Kapwing watermark, Submagic no free plan) match. 5/6 cards also sit on ai-that-adds-subtitles-to-videos, but "help me edit a video" is the broader question people type; subtitles is one job inside it. InVideo and HeyGen say "without editing", correctly left off. |
| ai-that-automates-work-between-my-apps | 6 -> 7 | Intro only. Dropped "n8n is the most powerful of the five" (a comparison no card text backs; n8n's own text says "powerful step-by-step automations across hundreds of apps", now quoted instead). Intro mentioned Zapier's free plan but not that Gumloop has none (free_tier false, $37/month); added. 4 -> 3 sentences. 3/5 cards overlap ai-that-does-tasks-for-me (16 cards); different question. |
| ai-that-runs-jobs-on-a-schedule | 6 -> 7 | Intro only. All 4 cards say "schedule" in their own text (Reclaim.ai also does, but that is calendar scheduling; correctly left off). Intro mentioned Fellou's free plan but not that Gumloop has none, and disclosed Hermes' setup but not AutoGPT's (free version "needs Docker setup and your own AI model keys"); added both. Niche but real ("ai that runs tasks automatically"). |
| ai-voices-in-many-languages | 6 -> 7 | Intro only. PlayAI 600 voices / 142 languages, Narakeet "hundreds of voices and languages", Fish Audio 30+, Synthesia 160 all match; Synthesia being video is disclosed. Intro mentioned free Narakeet / Fish Audio limits but not that PlayAI has no free plan (free_tier false); added. 4 -> 3 sentences. Kokoro and Orpheus mention languages only to say "check the page" / "English only", correctly left off. |
| ai-tools-from-google | 6 -> 7 | Intro only. All 7 cards have company Google / Google LLC (checked); Gemma and Antigravity left off as developer tools, and how_picked says so. Every per-card claim matches. Missing the two biggest watch_outs: Veo has no free plan ($20/month, pay per second) and Magenta RealTime 2 needs an Apple Silicon Mac; added both in plain words. 4 -> 3 sentences. |
| ai-tools-from-openai | 7 -> 7 | Intro only. All 5 cards have company OpenAI (the complete set). Claims match (agent needs paid plan, Whisper self-install, Codex for programmers). Added that Codex also needs a paid plan (its watch_out says so). 4 -> 3 sentences. |

## Cut (0)

None. I re-read all 44 original card texts (46 after the two adds); every card is justified by its own good_for / watch_out or, on the three company pages, by its company field. The worker's notes card counts match my recount for all 9, and every quoted justification is a real substring of that card's text. Skips (translation, sheet music, noise removal, game art, companion, Slack/Telegram, Mac image apps, sales leads at under 3 cards; teachers, kids, real estate, YouTube summary, spreadsheets, essays, health, legal, interior design with no card text; royalty-free music, blog-to-video, customer chatbots, no-code apps as duplicates) are right: I grepped for each topic and found nothing the worker missed. Anthropic / Perplexity AI / Stability AI company pages at 2 cards each, correctly skipped.

On the three company-keyed pages (the worker flagged them for judgment): keep. They are real searches ("google ai tools", "openai products"), they are keyed on a data field (company), not on memory, and how_picked honestly says "the tools in our guide made by X" rather than claiming a complete list. They do not hit the 017a ban list. Two notes, neither score-affecting: (1) these are the first pages that are not task questions, so they will not find new entries automatically (same as every ids page); (2) the Google page drops its developer tools but the OpenAI page keeps Codex (medium skill, labelled "for programmers"); consistent enough since Gemma is a raw model (hard) while Codex is an app, but the lead may prefer one rule.

## Pattern notes for the lead

- Same gap as 017d, now the dominant one: 4 of 7 fixes were "the intro mentions free plans or setup but skips a card with free_tier false or a technical install" (Gumloop twice, PlayAI, Veo, AutoGPT). It is mechanical: when a page has any free_tier false card and the intro says "free" anywhere, name that card. Worth a one-line rule in the next brief, or a small check in guidecheck (intro contains "free" and a free_tier-false card on the page is not named in the same sentence as "no free plan" is harder to check; the brief rule is enough).
- Sentence count slipped: 5 of 9 new intros were 4 sentences against a 2-3 rule that 75 of the 76 old pages follow. Cheap to check in guidecheck (count sentence enders in intro, fail on > 3) if it keeps happening.
- The sources page is the first batch-7 miss of the "grep providers.json for the title's words" kind: the worker searched for "sources" / "cite" but Perplexity and You.com say "which websites the facts came from". Next brief: for each page, grep synonyms, not just the title word.
- Part A closes the loop from 017c/017d (the Manus bug can no longer ship). The alias gap is small (4 names) but real; the patch is tested and sits at /tmp/ag017e/guidecheck-alias-patch.py.
- Pre-existing, still open from 017d: ai-that-reads-documents-for-me's intro claims Perplexity and Google AI Mode "summarize", which neither card says. Not touched here.

Unverified: search-intent judgments are reasoning, not measured search volume (no search tool in this session). I did not run the live site or deploy. The live site folder was not edited; all fixes live only in /tmp/ag017e/site-copy and /tmp/ag017e/questions.reviewed.json.
