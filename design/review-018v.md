SHIP
Reviewer: Fable 5.1 (independent, fresh context). Date 2026-10-27. Read + verify only; no site file edited besides this one.
Why SHIP: all 19 patched cards match the provider's own page today (every page re-opened by me). The 7 wording changes (semantic-scholar good_for; andi, warp-dev, vane, gpt-researcher, automatic1111, fooocus watch_out) are each backed by text I saw on the cited page, and the 12 date-only cards hold on free_tier, price_from, open_weights, runs_on_your_computer, watch_out and link. One mechanical fix before merge: ace-studio price_from should carry the discount note the site already uses for boomy (list price + "the page currently shows a N% discount"), because today's page charges $16.58 and shows $20.73 struck through. Diff of providers-018v.json against providers.json: every changed field is listed in recheck-018v.md; no unlisted change. hume-ai: shutdown confirmed on Hume's own changelog; recommend REMOVE (same as 018r). Accuracy score: 9/10.

How I checked: curl with a Chrome UA for all pages (all 200; hume.ai/pricing 200 but lands on the home page) plus GitHub API (license, archived, pushed_at, latest release) and raw READMEs for the six open-source cards; real Chrome (playwright-cli session ag018vr, headed, profile ~/.config/pw-aiguide-recheck, no sign-in anywhere) for recraft (Monthly + Annual toggle), consensus (Monthly + Annual), acestudio.ai/pricing, artbreeder (Monthly + Yearly), upscayl (slider moved to 100 credits; One-Time tab), photoroom (Monthly + Yearly toggle), andisearch.com, andisearch.com/pricing and /settings. Session closed; `pgrep -f pw-aiguide-recheck` printed nothing (checked twice, after each session). Page texts under /tmp/ag018v/rv/. Progress log /tmp/ag018v/review-progress.log.

## Per-card lines (id | verdict | quote + URL)

recraft-ai | OK | Chrome, Monthly: Basic "$12 billed monthly ... 1,000 credits per month"; Annual: "$10 per month billed annually $120"; Free: "3 generations per style per day ... All images are public ... No commercial use"; Pro "$20 billed monthly" / "$16 per month billed annually"; model list shows "Flux", "GPT Image", "Nano Banana"; Pro adds "Video generation" https://www.recraft.ai/pricing. Basic is the cheapest paid plan.

v0 | OK | "Free $0 /month ... 7 message/day limit"; "Plus Popular $30 /user/month ... $30 of included monthly credits per user"; "Business $100 /user/month" https://v0.app/pricing. Note for the lead: the Plus price is rendered as "$30" with a struck-through "$90" beside it (a <del> tag), so $30 may be a promo figure; the page gives no end date and no other Plus price, so $30 is the right number to show. Lead may want to watch it next batch.

warp-dev | OK | "Build ... $20 /month"; "$20 of agent usage included each month at API rates"; "Add-on agent usage, auto-reload, and team-wide spend cap"; comparison table (in page data) "Included monthly usage ... Build: $20 (1,500 credits)"; Free column "Additional agent usage at pay-as-you-go rates" https://www.warp.dev/pricing. The new watch_out moves "pay-as-you-go" out of the Build sentence, which is right: that phrase sits under Free.

zed-editor | OK | "Personal $0 forever"; "Pro Free Trial $10 per month ... Unlimited edit predictions $5 of tokens included Usage-based billing beyond $5"; FAQ (worker quote, I saw the same page) "API list price +10%" https://zed.dev/pricing. GitHub latest release v1.25.3 published 2026-10-23.

vane | OK | README: "Vane is a privacy-focused AI answering engine that runs entirely on your own hardware ... support for local LLMs (Ollama) and cloud providers (OpenAI, Claude, Groq) ... cited sources"; "Using Docker is highly recommended"; "configure your settings (API keys, models, etc.)" https://github.com/ItzCrazyKns/Vane. GitHub API: MIT, not archived, pushed 2026-09-01, latest release v1.12.2 (2026-04-10). "Paid" is not on the page; cutting it was right.

andi | OK | ToS: "4.1 Search Results ... May include AI-generated summaries and explanations ... No guarantee of accuracy or completeness"; "9.1 Service Provided 'As Is' ... AI-generated content may have errors" https://andiai.com/legal/terms-of-service. API: "Outcome-Based Pricing ... <1¢ Per query" https://andiai.com/api; "Get an API key: free tier available" https://api.andiai.com/llms.txt, so cutting "the developer Search API is paid" was right. The ToS also says "5.1 Pricing: Current rates posted on andisearch.com/pricing" and "Paid Plans: Additional storage and features", so I opened https://andisearch.com/pricing in Chrome: it lands on the home page (URL becomes https://andisearch.com/), and /settings shows no plan or price; the search site itself shows no paid plan, so price_from "Free (a separate Search API for developers is paid per query)" holds. andisearch.com renders in Chrome with no sign-in (New Chat, About, Help, Settings).

semantic-scholar | OK | Home: "A free, AI-powered research tool for scientific literature. Search 239,806,569 papers from all fields of science" https://www.semanticscholar.org/. Product page: "TLDRs ... super-short summaries of the main objective and results of a paper ... available for nearly 60 million papers in computer science, biology, and medicine" https://www.semanticscholar.org/product. So "summaries of each paper" was wrong and "on many papers" is right. The watch_out ("Academic literature only — not a general web search engine") is a plain-words reading of "scientific literature"; pre-existing, acceptable.

consensus | OK | Chrome, Monthly: Pro "$20/mo ... Unlimited Pro messages ... 15 Deep reviews per month"; Annual: "$12/mo $144 annually"; Free "$0/mo ... 10 Pro messages per month ... Up to 3 Deep reviews per month" https://consensus.app/pricing/. Pro is the cheapest paid plan (next is $65/mo).

gpt-researcher | OK | README: "export OPENAI_API_KEY ... export TAVILY_API_KEY"; "Aggregate over 20 sources for objective conclusions"; "Takes ~5 minutes per deep research" https://github.com/assafelovic/gpt-researcher. GitHub API: Apache-2.0, not archived, pushed 2026-10-10, latest v3.7.0 (2026-09-26). "Paid" is not on the page; cutting it was right.

ace-studio | FIX (convention) | Chrome: "HOLIDAY DISCOUNT"; Artist "RENT-TO-OWN ... $16.58/mo. [struck] $20.73 Billed yearly"; "Credit-Based Features 2500 credits/mo: Music/SFX Generative Kits, Music Video, Video Composer, Stem Splitter"; Artist Pro "$22/mo. [struck] $27.5 Billed yearly"; no free plan on the page (free_tier false holds); no monthly billing option shown https://acestudio.ai/pricing/. The card keeps the $20.73 list price but says nothing about the discount; boomy on this site reads "$14.99/month (Creator list price; the page currently shows a 33% discount)". Apply the same shape (fix below). Link https://acestudio.ai/ returns 200.

fish-audio | OK | "Free Tier ... $0 mo No credit card needed ... 8,000 credits monthly"; in the Free column "Commercial use" is struck through (line-through class, X icon); "Plus ... $11 mo [struck] $15 $132 billed annually"; FAQ "Free plan users can only use generated content for personal, non-commercial projects"; "Unused minutes do not roll over to the next month" https://fish.audio/plan/. open_weights true: github.com/fishaudio/fish-speech exists, not archived, pushed 2026-10-14 (I did not open the weight files; the worker's reading).

retell-ai | OK | "Pay as you go ... $10 in free credits ... $0.07-$0.31 / min for AI Voice Agents"; "20 Free Concurrent Calls"; calculator "Retell Voice Infra $0.055 /min ... TTS Cost $0.015 /min" and component table "Retell Voice Infra $0.055/minute"; "No Charge for Sip Trunking/Custom Telephony" https://www.retellai.com/pricing.

orpheus-tts | OK | README: "We provide 2 English models"; "a family of multilingual models in a research preview"; "pip install orpheus-speech"; "Zero-Shot Voice Cloning"; Colab notebooks; emotion tags https://github.com/canopyai/Orpheus-TTS. GitHub API: Apache-2.0, not archived, pushed 2025-12-05, no GitHub releases (so "latest release still exists" is read as "repo and install command still there").

sonix | OK | "30 min free trial No credit card required"; "Pay As You Go ... $10/hr"; "Core ... $25/mo ... 5 hrs/mo ... transcription & translation ... 1 user included +$25/mo per extra seat"; "54+ languages"; "subtitles" https://sonix.ai/pricing. free_tier false holds (trial only). Core kept as the cheapest plan, same as before; Pay As You Go is per-hour, not a plan.

upscayl | OK | Chrome, slider at 100 credits, Monthly: "Pro Plan $9.99 100 credits / month"; at 300 credits "$24.99"; "Free Trial $0 10 credits included"; One-Time tab "50 Credits $9.99 One-time purchase" https://upscayl.org/pricing. README: "You'll need a Vulkan compatible GPU ... Many iGPUs (integrated graphics) do not work"; "Free and Open Source AI Image Upscaler" https://github.com/upscayl/upscayl. GitHub API: AGPL-3.0, pushed 2026-10-05, latest v2.15.0.

automatic1111 | OK | README: "One click install and run script (but you still must install python and git)"; "4GB video card support (also reports of 2GB working)" https://github.com/AUTOMATIC1111/stable-diffusion-webui. GitHub API: AGPL-3.0, not archived, pushed 2026-03-02, latest v1.10.1. New wording matches the page.

fooocus | OK | readme.md: "The software is offline, open source, and free"; "Project Status: Limited Long-Term Support (LTS) with Bug Fixes Only"; "the minimal requirement is 4GB Nvidia GPU memory (4GB VRAM) and 8GB system memory (8GB RAM)"; "make sure that you have at least 40GB free space on each drive if you still see 'RuntimeError: CPUAllocator'" https://github.com/lllyasviel/Fooocus. GitHub API: GPL-3.0, not archived, pushed 2025-12-01, latest v2.5.5. New wording matches: 40GB is the fix for an error, not a base requirement.

photoroom | OK (note) | Chrome, Monthly: Pro "$12.99 Per month ... 8,000 AI credits • 1,000 exports"; Yearly: "[struck] $12.99 $7.50 Per month, billed yearly"; Pro "Not included: Video Generator", "Not included: Adjustable AI Shadows", "Not included: 4K images + HD video"; every plan button says "Start free trial" https://www.photoroom.com/pricing. free_tier true rests on the official tool page: "Photoroom is available on mobile and desktop. You can get started for free to remove backgrounds, and when you're ready, upgrade to access more AI photo editing tools and high-resolution exports" https://www.photoroom.com/tools/background-remover. That is Photoroom's own page saying free use with upgrade optional, so true is defensible; the pricing page itself lists no Free plan. If the lead wants the stricter reading (krisp, 018t), set free_tier false; I would keep true.

artbreeder | OK | Chrome, Monthly: "starter 100 Credits / month $8.99 $0.09 / credit ~ 1000 SDXL images"; Yearly: "starter 1200 Credits / year $7.49 x 12"; FAQ "credits reset at the beginning of your billing period"; "Artbreeder is able to provide unlimited usage for free because of its (beloved) susbcribers" https://www.artbreeder.com/pricing.

Spot-check for "entry price is really a higher tier" (the lindy error): none found. Every price_from above is the cheapest individual paid plan on its page.

Plain words: the 7 new sentences read at 8th-grade level. "TLDRs" (semantic-scholar) is the page's own word and is explained as "short one-line summaries"; fine.

## Required fixes

1. id: ace-studio | field: price_from | new value: "$20.73/month (Artist list price, billed yearly; the page currently shows a 20% holiday discount)" | source quote: "HOLIDAY DISCOUNT ... Artist RENT-TO-OWN $16.58/mo. $20.73 Billed yearly" https://acestudio.ai/pricing/ (Chrome). Same shape as boomy's price_from in providers.json.

No other field needs a change. The 19 cards may merge as written apart from fix 1.

## hume-ai

Confirmed on Hume's own site: changelog entry "October 2, 2026 — TTS and EVI API sunset notice: Hume is sunsetting the TTS and EVI APIs. Access ends November 13, 2026 at 12:01 a.m. EST, and both APIs remain fully supported until then. Any data in your account is permanently deleted after November 13, 2026." https://dev.hume.ai/voice/changelog.md. https://www.hume.ai/pricing returns 200 but lands on https://www.hume.ai/ ("Infrastructure to improve voice AI. The bar is human." — an evaluation product; "Explore Expression APIs"); no price, no Starter plan, no TTS/EVI sign-up anywhere on it. The billing doc still points to the dead pricing page https://dev.hume.ai/voice/docs/resources/billing.md. The card's "$3/month (Starter)", "30 minutes of text-to-speech and 40 minutes of AI voice chat" cannot be seen on any Hume page today.

Recommendation: REMOVE the card (same rule as 018r: openai-agent, you-com, tabnine). Reasons: the product the card describes ends in 17 days, nothing a reader can sign up for today is priced on the site, and what Hume now sells (Expression APIs, evaluation) is business-only with no public price.

If the lead prefers keep-with-note until 2026-11-13, exact values:
- free_tier: false
- price_from: "Shutting down (text-to-speech and voice chat end November 13, 2026)"
- watch_out: "Hume is closing its text-to-speech and voice-chat services on November 13, 2026, and its pricing page is gone, so do not start anything new here."
- watch_out_source: "https://dev.hume.ai/voice/changelog.md"
- link: "https://www.hume.ai/" (the /pricing URL only redirects there)
- good_for: "AI voices that react to your tone; the service is shutting down on November 13, 2026."
- last_checked: "2026-10-27"
Then remove the card in the first batch after 2026-11-13.

## Ripples

Grepped title, seo_title, meta_description, intro, how_picked and filter ids in data/questions.json for all 20 names (recraft, v0, warp, zed, vane, andi, semantic scholar, consensus, gpt researcher, ace studio, fish audio, hume, retell, orpheus, sonix, upscayl, automatic1111, fooocus, photoroom, artbreeder). 30 sentence hits; all but the two below still match today's pages (checked: recraft "free-plan images are public with no commercial use"; retell "charge extra for the AI model and the voice"; sonix "no free plan"; upscayl "many laptop graphics chips do not work"; fish audio "not for business use" and "10 seconds"; ace studio "no free plan"; andi "its own terms say the AI can make mistakes"; fooocus "simple text-to-picture on your own machine"; gpt researcher "you set them up yourself"; orpheus "laughing or sighing").

CONFIRMED (needs the edit) | ai-for-finding-scientific-papers | intro | "Semantic Scholar is a free AI search across scientific papers, with a one-line summary of each." -> "Semantic Scholar is a free AI search across scientific papers, with a short one-line summary on many of them." Names only Semantic Scholar (in ids). Rest of the intro unchanged; meta_description unchanged.

CONFIRMED | ai-search-that-shows-its-sources | intro | no change: "Andi gives conversational answers, though its own terms say the AI can make mistakes" is still on the ToS page.

IF hume-ai IS REMOVED (recommended) | ai-that-copies-a-voice |
- filter.ids: drop "hume-ai" -> ["fish-audio", "ace-studio", "orpheus-tts", "f5-tts"]
- intro: "Fish Audio can copy a voice from as little as 10 seconds of audio. Hume AI also mentions voice cloning, while Orpheus TTS and F5-TTS run on your own computer and need Python, a programming tool. Only copy voices you have permission to use." -> "Fish Audio can copy a voice from as little as 10 seconds of audio, while Orpheus TTS and F5-TTS run on your own computer and need Python, a programming tool. Only copy voices you have permission to use."
- meta_description: "AI that copies a voice from a short sample: Fish Audio, Hume AI and more, with plain-English notes and links." -> "AI that copies a voice from a short sample: Fish Audio, Orpheus TTS, F5-TTS and more, with plain-English notes and links."
All named providers (fish-audio, orpheus-tts, f5-tts) are in that page's ids list (verified in questions.json). No other question page names Hume.

IF hume-ai IS KEPT with the note | ai-that-copies-a-voice | intro "Hume AI also mentions voice cloning" becomes misleading; use the same intro replacement above and keep the meta_description as is until removal.

MISSED by the worker: none. The worker's ripple list matches mine.
