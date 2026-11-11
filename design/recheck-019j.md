# ai-guide-019j recheck (2026-11-11), batch 22: the 20 oldest cards

Patch file: data/providers-019j.json (20 verified cards as they should read after the merge). All 20 get last_checked "2026-11-11". Every card link and every watch_out_source returned HTTP 200 (curl, 2026-11-11); clipdrop and the toggle pages were read in real Chrome (session ag019j, closed; `pgrep -f pw-aiguide-recheck` printed nothing).

## Changed fields
- wispr-flow | watch_out | "The free plan is capped at 2,000 words a week on a computer and has limited weekly use on a phone. Pro removes the cap." -> "The free plan is capped at 2,000 words a week. Pro removes the cap." | https://wisprflow.ai/ (home FAQ) | "Is Flow free? ... Flow's is free, with no trial countdown or credit card required, for 2,000 words per week. If you want unlimited dictation, upgrade to Flow Pro." The pricing page https://wisprflow.ai/pricing now only says "Word limit: Limited words per week" (Free) vs "No limits" (Pro), and no Wispr page says the cap differs between computer and phone, so that half was cut.
- wispr-flow | watch_out_source | https://wisprflow.ai/pricing -> https://wisprflow.ai/ | the 2,000 number is only on the home page.

No price_from, free_tier, open_weights, runs_on_your_computer or good_for change on any of the 20.

## Verified, no field changed (last_checked set to 2026-11-11)
- liner | https://liner.com/pricing | Pro "$17.99" monthly, "$14.99 /month, billed annually" (Annual toggle "Save 17%"); Free "$0", "1 file upload/day", "Answers with ads"; FAQ "a free account offers limited credits which may run out quickly with just a few tasks".
- pixelcut | https://www.pixelcut.ai/pricing | Pro "$10 $8 per month, billed yearly", "600 AI Credits Monthly"; Free "Limited Background Removal", "Limited Upscale"; FAQ "Credits are ... used ... with certain advanced AI models".
- typecast | https://typecast.ai/pricing/ | Free "$0 /month", "3,000 credits (~5 mins)", "Attribution is required for all content downloaded on the Free plan"; Basic "$5 /month $54 billed yearly", "30,000 credits (~35 mins)". Monthly $5 (yearly = 10% off).
- undermind | https://www.undermind.ai/ (#pricing, read in Chrome) | Academic: Monthly "$20 per month", Annual "$16 per month, billed annually"; Industry Monthly "$75 per month"; Pro "10x higher usage limits"; Free "Standard rate limits on chats and searches".
- antigravity | https://antigravity.google/pricing | "Generally Available", Individual "$0/month", "Basic weekly rate limits"; Google AI Pro "More rate limits", Ultra "Even more rate limits". Not a preview any more, still free at the Individual level.
- audimee | https://audimee.com/pricing (Monthly toggle clicked in Chrome) | Starter "$12 /mo" monthly ("Was $12, $9 /mo, $108 billed yearly" in the Yearly view); Free "15 min conversion time", "No harmony maker", "Personal use only", compare table "Save conversions Not included", "Audio quality MP3"; Starter "1 hr conversion time".
- autogpt | https://agpt.co/pricing/ | Pro "$50.00 / month billed monthly", "7 days free, then $50/mo", "Card required; no subscription charge today"; Yearly view saves 15% ($42.50). Max $320/month. "Scheduled workflow runs use your credit wallet, with a spending cap you can set for each Expert." GitHub README (https://github.com/Significant-Gravitas/AutoGPT): self-host "You provide model credentials", Docker image `significantgravitas/autogpt`; latest release autogpt-platform-beta-v0.11.1 (2026-11-06), pushed 2026-11-11, not archived, license shown as NOASSERTION.
- brave-leo | https://brave.com/leo/ and https://brave.com/premium/ | Premium page: "Leo AI premium $14.99 /month $149.99 /year", "Higher rate limits", "7-day free trial". Leo page: "Brave Leo is free to use. Or it's available as a premium experience, with access to more models"; "available in the Brave browser for desktop ... and mobile". The price is on /premium/, not on the cited /leo/ page.
- clipdrop | https://clipdrop.co/pricing (Chrome; static HTML shows "- - per month" until the script loads) | Pro "15 US$ per month"; Free: Background Removal 20/24h, Image Upscaler x2 20/24h, Cleanup 20/24h, Relight 20/24h, Text Remover 50/24h; Text to image, Uncrop, Replace Background have no free quota; Pro lists "High Resolution ... Image Upscaler x16", 1000/24h.
- domoai | https://www.domoai.app/pricing (Monthly toggle read in JS, the click does not work, so the page was flipped by the switch input) | Monthly view: Basic "$13 per month, billed monthly", "600 Monthly credits ... (~150 images or ~85 videos)"; Standard "$42 per month, billed monthly", "Unlimited Relax generations". Yearly view: Basic $9, Standard $29. No free plan on the page.
- dyad | https://www.dyad.sh/pro | Free "No sign-up required", "Basic Agent 20 messages/day"; Pro "$20 /month", "200 AI credits/month"; Max "$79 /month". App v1.23.0 released 2026-11-09, GitHub dyad-sh/dyad not archived, license NOASSERTION, 12 release files.
- crush | https://hyper.charm.land/ + /faq (Chrome) | Plans "$10 per month", "$20", "$50", "$100", "$200"; FAQ "We've retired the monthly free Hypercredit allowance. ... purchasing prepaid credits ... for as little as five bucks." GitHub charmbracelet/crush: latest v0.100.0 (2026-11-05), pushed 2026-11-11; README lists Anthropic, OpenAI, Gemini API keys and "Hyper model" as the quickest start. The old https://hyper.charm.land/pricing is now a 404; the FAQ link in watch_out_source still works.
- krita-ai-diffusion | GitHub Acly/krita-ai-diffusion (GPL-3.0, latest v1.53.0 2026-08-22, pushed 2026-11-06, zip release file present) + https://www.interstice.cloud/service | README "at least 6 GB VRAM (NVIDIA) is recommended. Otherwise generating images will take very long or may fail"; cloud page "Start exploring with a limited number of free tokens", "One-time payment 10 € 5 000 tokens", "28 € 15 000 tokens".
- piper-tts | GitHub OHF-Voice/piper1-gpl (GPL-3.0, latest v1.8.0 2026-09-04, pushed 2026-11-09, wheels attached) | README "pip install piper-tts", "Looking for Maintainers".
- spleeter | GitHub deezer/spleeter (MIT, latest release v2.3.0 2021-09-03, pushed 2026-10-28, PyPI spleeter 2.4.2) | README "2 stems / 4 stems / 5 stems", command-line use `spleeter separate`.
- stemroller | https://www.stemroller.com/ + GitHub stemrollerapp/stemroller (latest 3.1.1 2026-06-30, not archived; license shown NOASSERTION) | Home: "totally free and open-source", "Donations are always appreciated"; README "You'll need to wait several minutes for splitting to complete". Downloads are on Hugging Face (stemrollerapp/stemroller: 3.1.1 mac zip and Windows .exe, HTTP 200; the Windows file is about 2.5 GB). Not downloaded.
- swarmui | GitHub mcmonkeyprojects/SwarmUI (MIT, latest 0.9.8-Beta 2026-02-06, pushed 2026-11-11) | README "any models used have their own licenses".
- vibe | GitHub thewh1teagle/vibe (MIT, latest v3.3.0 2026-10-29, 17 release files) | README "Summarize transcripts ... using the Claude API", "Ollama support", "Speaker diarization", "Optimized for GPU".
- basic-pitch | https://basicpitch.spotify.com/ + GitHub spotify/basic-pitch (Apache-2.0, latest v0.4.0 2024-08-16, last push 2025-11-13, PyPI basic-pitch 0.4.0) | Site "Try Basic Pitch, a free audio-to-MIDI converter", "sing a ditty into your computer. Or drop a recording of any single instrument". Upkeep note: no release since 2024-08 and no push since 2025-11-13, still not archived.

## Notes for the lead (no field changed)
- basic-pitch: the card's "version for programmers that you install with pip" sentence is on the GitHub README ("`pip install`-able"), not on the cited site page. The cited page only links to GitHub. Left as is; trim the sentence or switch the source if the reviewer wants one URL per fact.
- autogpt: the "free version needs Docker setup and your own AI model keys" half is on the GitHub README (self-host section), not on the cited pricing page (which only has a feature comparison for "what comes with self-hosting").
- krita-ai-diffusion: the "free tokens run out" half is on https://www.interstice.cloud/service, the cited GitHub README only says "Cloud generation is also available".
- brave-leo: price is on https://brave.com/premium/ (not cited).
- stemroller / swarmui / vibe / krita: card says open_weights false; left as is (unchanged policy).
- spleeter upkeep: last release v2.3.0 is from 2021 (repo still receives pushes, latest 2026-10-28).
- Watch items seen: none of the listed ones are in this batch.

## Question-page ripples
None. The only changed card is wispr-flow (watch_out). Searched data/questions.json for "wispr" (any case): 0 matches anywhere, and no "2,000 words" text either.

unchanged: krita-ai-diffusion, liner, piper-tts, pixelcut, spleeter, stemroller, swarmui, typecast, undermind, vibe, antigravity, audimee, autogpt, basic-pitch, brave-leo, clipdrop, crush, domoai, dyad (last_checked + nothing else)
changed: wispr-flow (watch_out, watch_out_source)
unreachable: none
checked: 20/20
- Lead at merge (2026-11-11): the 3 source gaps (basic-pitch, autogpt, krita-ai-diffusion) were closed by the review (review-019j.md); brave-leo needed no change. Optional autogpt ripple applied to ai-for-building-my-own-ai-helper intro.
