#!/usr/bin/env python3
"""Static-site builder for the plain-language AI-provider guide.

Reads data/providers.json + data/questions.json + templates/, writes dist/.
STDLIB ONLY - no pip needed.

Usage: python3 build.py
"""
import html
import json
import os
import re
import shutil
from datetime import date
from string import Template

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "providers.json")
QUESTIONS = os.path.join(ROOT, "data", "questions.json")
TEMPLATES = os.path.join(ROOT, "templates")
STATIC = os.path.join(ROOT, "static")
DIST = os.path.join(ROOT, "dist")
BASE_URL = "https://kevthetech143.github.io/ai-guide/"
UPDATED = date.today().isoformat()

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def freshness_line():
    """Page-level freshness microcopy, e.g. 'Prices and plans checked September 2026.'"""
    y, m, _d = UPDATED.split("-")
    return "Prices and plans checked %s %s." % (MONTHS[int(m) - 1], y)


CATEGORY_BLURBS = {
    "chat": "AIs you talk to. Ask questions, get writing help, brainstorm.",
    "image": "AIs that make pictures from your words.",
    "voice": "AIs that turn text into speech, or work with your voice.",
    "video": "AIs that make or edit video.",
    "code": "AIs that help you write computer code.",
    "search": "AIs that answer questions by looking things up.",
    "music": "AIs that make songs from your words.",
    "agents": "AIs that do multi-step jobs for you on their own.",
}

CATEGORY_NAMES = {
    "chat": "Chat", "image": "Image", "voice": "Voice", "video": "Video",
    "code": "Code", "search": "Search", "music": "Music", "agents": "Task helpers",
}

# Labels used in the start-here picker flow (plain words, not category jargon).
# One plain name for every category on every surface (round-4 fix:
# home tiles, picker, category h1s/titles, /all/ headings — no "X AIs").
def start_label(c):
    return CATEGORY_NAMES.get(c, c.title())


# One-line chip legend shown above the first card on every list page
# (round-2 fix: "Open source"/"Company-made" must be explained where chips appear).
LEGEND_HTML = ('<p class="legend">Badges, in plain words: '
               '<strong>Open source</strong> &mdash; anyone can download and inspect how it works. '
               '<strong>Company-made</strong> &mdash; a company runs it for you. '
               '<strong>Free</strong> &mdash; you can use the main features without paying. '
               '<strong>Paid</strong> &mdash; you need to pay, usually a monthly plan. '
               '<strong>Runs on your computer</strong> &mdash; it runs on your own device, nothing sent to the cloud. '
               '<strong>Easy / Medium / Hard</strong> &mdash; how tricky it is to set up and use.</p>')


# Home-page tile order: (category, 3-6 word plain hint).
TILE_ORDER = [
    ("chat", "ask questions, write things"),
    ("image", "make pictures from words"),
    ("video", "make videos from words"),
    ("voice", "turn text into speech"),
    ("music", "make songs from words"),
    ("code", "help writing computer code"),
    ("search", "answers by looking things up"),
    ("agents", "do multi-step jobs for you"),
]


def esc(s):
    return html.escape(str(s), quote=True)


# Build date baked into sitemap <lastmod> (brief: YYYY-MM-DD).
BUILD_DATE = "2026-09-16"


def ld_block(schema_obj):
    """One <script type="application/ld+json"> block. json.dumps does all
    escaping, so a quote or unicode char in a blurb cannot break the page."""
    return ('<script type="application/ld+json">\n%s\n</script>'
            % json.dumps(schema_obj, ensure_ascii=False, indent=2))


def offer_from_price(price_from):
    """Offer from a provider's price_from, or None when there is no real
    dollar amount (\"Free\", \"Check site\", open-weights-only, etc.).
    Never invents a price; the regex only reads what data/ provides."""
    if "free" == price_from.strip().lower():
        return None
    m = re.search(r"\$(\d+(?:\.\d{1,2})?)", price_from)
    if not m:
        return None
    return {"@type": "Offer", "price": m.group(1), "priceCurrency": "USD"}


def software_app_schema(p):
    """SoftwareApplication for a provider page: real fields only. No rating,
    review count, or author — we have no such data and fake schema risks a
    penalty. Offers omitted unless price_from is a real dollar amount."""
    schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": p["name"],
        "applicationCategory": CATEGORY_NAMES.get(p["categories"][0], p["categories"][0].title()),
        "description": p["good_for"],
    }
    offer = offer_from_price(p["price_from"])
    if offer is not None:
        schema["offers"] = offer
    return schema


def faq_page_schema(question, matched, matched_urls):
    """FAQPage (one Question, acceptedAnswer = the page's intro text) plus an
    ItemList of the matched provider cards in display order. @graph keeps both
    schema types in the single ld+json block each page gets."""
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "FAQPage",
                "mainEntity": [{
                    "@type": "Question",
                    "name": question["title"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": question["intro"],
                    },
                }],
            },
            {
                "@type": "ItemList",
                "name": question["title"],
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "name": p["name"],
                        "url": matched_urls[i],
                    }
                    for i, p in enumerate(matched)
                ],
            },
        ],
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "AI Guide",
        "url": BASE_URL,
    }


def load_providers():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def load_questions():
    with open(QUESTIONS, encoding="utf-8") as f:
        return json.load(f)


def question_matches(provider, rule):
    """A provider matches a filter rule if every condition holds.

    Rule keys: "categories" (list; provider matches if any listed category
    is in the provider's categories), or a provider field name compared
    for exact equality (e.g. "free_tier": true).
    """
    for key, want in rule.items():
        if key == "categories":
            if not any(c in provider.get("categories", []) for c in want):
                return False
        elif provider.get(key) != want:
            return False
    return True


def tmpl(name):
    with open(os.path.join(TEMPLATES, name), encoding="utf-8") as f:
        return Template(f.read())



def seo_meta_desc(name, company, good_for):
    """Meta description for a provider page, always under 155 chars
    measured after HTML escaping (as it appears in the <meta> tag)."""
    base = "%s by %s: " % (name, company)
    gf = good_for
    budget = 154 - len(esc(base)) - len(esc("\u2026"))
    while len(esc(gf)) > budget and gf:
        gf = gf[:-1]
    gf = gf.rstrip()
    return base + gf + ("\u2026" if gf != good_for else "")


def page(title, meta_description, body, style_prefix, home_href,
         show_back_link=True, canonical=None, is_start_page=False,
         is_about_page=False, json_ld=None):
    # Breadcrumb now points at the real /all/ everything page (round-2 fix:
    # the old "All AIs" crumb pointed at a home page with no list).
    all_href = home_href.replace("index.html", "all/index.html")
    if show_back_link:
        topnav = ('<div class="crumbwrap"><div class="sitehead-inner">'
                  '<nav class="topnav"><a href="%s">&larr; All AIs</a></nav>'
                  '</div></div>' % esc(all_href))
    else:
        topnav = ""
    start_href = home_href.replace("index.html", "start/index.html")
    about_href = home_href.replace("index.html", "about/index.html")
    start_current = ' aria-current="page"' if is_start_page else ""
    # The about page must not link to itself in the footer (round-2 cut).
    about_link = ("How this guide works" if is_about_page
                  else '<a href="%s">How this guide works</a>' % esc(about_href))
    return tmpl("base.html").substitute(
        title=esc(title),
        meta_description=esc(meta_description),
        body=body,
        style_prefix=style_prefix,
        home_href=home_href,
        start_href=start_href,
        start_current=start_current,
        about_link=about_link,
        topnav=topnav,
        updated=UPDATED,
        canonical=esc(canonical or BASE_URL),
        og_title=esc(title),
        og_description=esc(meta_description),
        json_ld=ld_block(json_ld) if json_ld is not None else "",
    )


def badges(p):
    """Badge spans with semantic classes for the redesigned templates."""
    free_txt = "Free" if p["free_tier"] else "Paid"
    free_cls = "badge-free" if p["free_tier"] else "badge-paid"
    skill_txt = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}[p["skill_level"]]
    # Plain words, not jargon: "Open source"/"Company-made" (round-1 fix).
    open_txt = "Open source" if p["open_weights"] else "Company-made"
    open_cls = "badge badge-open" if p["open_weights"] else "badge"
    local = ' <span class="badge">Runs on your computer</span>' if p["runs_on_your_computer"] else ""
    return ('<span class="badge %s">%s</span> <span class="badge">%s</span> '
            '<span class="%s">%s</span>%s' % (free_cls, free_txt, skill_txt, open_cls, open_txt, local))


def price_line(p):
    """Facts-row price text that never contradicts the Free/Paid badge.

    A free-tier provider whose price_from is a paid-plan figure reads
    "Free tier available; paid plans from $X" instead of a bare "$X".
    Unknown prices ("Check site") get their own plain branch (round-2 fix).
    """
    pf = p["price_from"]
    if "check site" in pf.lower():
        if p["free_tier"]:
            return "Free to try; check the provider's site for paid plans"
        return "No monthly price listed \u2014 check the provider's site"
    # Round-5 fix: scrub developer jargon out of price rows ("open weights",
    # "usage-based API pricing") — plain words, same facts, never data/.
    pf = (pf.replace("(open weights)", "")
            .replace("usage-based API pricing", "pay-per-use options"))
    pf = " ".join(pf.split()).replace(" ;", ";")
    if p["free_tier"] and "free" not in pf.lower():
        return "Free tier available; paid plans from " + esc(pf)
    return esc(pf)


def card(provider, href_prefix):
    """Render a provider card. href_prefix: path prefix to dist/p/ from the page."""
    p = provider
    card_href = "%s%s.html" % (href_prefix, p["id"])
    return tmpl("card.html").substitute(
        card_href=card_href,
        name=esc(p["name"]),
        badges=badges(p),
        skill_badge={"easy": "Easy", "medium": "Medium", "hard": "Hard"}[p["skill_level"]],
        good_for=esc(p["good_for"]),
        price_from=price_line(p),
        watch_out=esc(p["watch_out"]),
        link=esc(p["link"]),
        last_checked=esc(p["last_checked"]),
    )


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def filtered_page(providers, title, meta_description, intro_html,
                  href_prefix, style_prefix, home_href, canonical):
    """A filtered provider list page (used by the start-here picker)."""
    cards = "\n".join(card(p, href_prefix) for p in providers)
    body = intro_html + "\n" + LEGEND_HTML + "\n" + cards
    return page(title, meta_description, body, style_prefix, home_href,
                show_back_link=True, canonical=canonical)


def build():
    providers = load_providers()
    questions = load_questions()
    categories = sorted({c for p in providers for c in p["categories"]})

    # fresh dist
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(STATIC, os.path.join(DIST, "static"))

    # home page: tiles in fixed order with plain hints; no back link to self.
    # Round-1 cut: the "All providers" card stack is gone from home; the
    # home ends at "Popular questions" and cards live on category pages.
    tiles = "\n".join(
        '<a class="tile" href="%s/index.html">'
        '<span class="tile-name">%s</span>'
        '<span class="tile-hint">%s</span></a>' % (
            c, esc(CATEGORY_NAMES.get(c, c.title())), esc(hint))
        for c, hint in TILE_ORDER if c in categories
    )
    question_links = "\n".join(
        '<a class="biglink" href="best/%s/"><span class="biglink-label">%s</span></a>' % (q["slug"], esc(q["title"]))
        for q in questions
    )
    body = tmpl("home.html").substitute(tiles=tiles, questions=question_links)
    write(os.path.join(DIST, "index.html"),
          page("Which AI should I use? - AI Guide",
               "A plain-language guide to picking an AI: what it costs, how hard it is, and where to get it.",
               body, ".", "index.html", show_back_link=False,
               canonical=BASE_URL, json_ld=website_schema()))

    # category pages (round-2 fix: the "Agents" category wears the
    # "Task helpers" name on every surface via start_label).
    for c in categories:
        label = start_label(c)
        # Round-5 fix: free-first order on category pages — a 60-year-old
        # hunting for free should not scroll past the paid ones.
        cat_ps = sorted((p for p in providers if c in p["categories"]),
                       key=lambda p: (not p["free_tier"], p["name"]))
        cards = "\n".join(card(p, "../p/") for p in cat_ps)
        body = tmpl("category.html").substitute(
            category_kicker="Category",
            category_name=esc(label),
            freshness=esc(freshness_line()),
            category_blurb=esc(CATEGORY_BLURBS.get(c, "")),
            cards=LEGEND_HTML + "\n" + cards,
        )
        write(os.path.join(DIST, c, "index.html"),
              page("%s - AI Guide" % label,
                   "Plain-language %s picks: costs, difficulty, and official links." % label.lower(),
                   body, "..", "../index.html",
                   canonical=BASE_URL + c + "/"))

    # provider pages
    for p in providers:
        body = tmpl("provider.html").substitute(
            name=esc(p["name"]),
            company=esc(p["company"]),
            badges=badges(p),
            skill_badge={"easy": "Easy", "medium": "Medium", "hard": "Hard"}[p["skill_level"]],
            good_for=esc(p["good_for"]),
            price_from=price_line(p),
            watch_out=esc(p["watch_out"]),
            categories_text=esc(", ".join(CATEGORY_NAMES.get(c, c.title()) for c in p["categories"])),
            link=esc(p["link"]),
            last_checked=esc(p["last_checked"]),
        )
        meta_desc = seo_meta_desc(p["name"], p["company"], p["good_for"])
        write(os.path.join(DIST, "p", "%s.html" % p["id"]),
              page("%s - AI Guide" % p["name"],
                   meta_desc,
                   body, "..", "../index.html",
                   canonical=BASE_URL + "p/%s.html" % p["id"],
                   json_ld=software_app_schema(p)))

    # start-here picker (no JavaScript required: plain links to built lists)
    start_urls = []

    def start_write(rel, title, meta_description, intro_html, plist,
                    href_prefix, style_prefix, home_href):
        # SEO fix (2026-09-16): canonical uses the trailing-slash page URL,
        # not the /index.html file URL — the /index.html form is duplicate
        # content and must not appear in the sitemap either.
        canonical = (BASE_URL + "start/" + rel).replace("/index.html", "/")
        html_out = filtered_page(plist, title, meta_description, intro_html,
                                 href_prefix, style_prefix, home_href,
                                 canonical=canonical)
        write(os.path.join(DIST, "start", rel), html_out)
        start_urls.append(canonical)

    cat_links = "\n".join(
        '<a class="biglink" href="%s/"><span class="biglink-label">%s<span class="hint">%s</span></span></a>' % (
            c, esc(start_label(c)), esc(hint))
        for c, hint in TILE_ORDER if c in categories
    )
    picker_body = (
        "<h1>Start here</h1>\n"
        '<p class="subtitle">Tap what you want to do first &mdash; then narrow by free or paid.</p>\n'
        "<h2>1. What do you want to do?</h2>\n" + cat_links + "\n"
        "<h2>2. Free or paid?</h2>\n"
        '<a class="biglink" href="free/"><span class="biglink-label">Free ones<span class="hint">costs nothing to try</span></span></a>\n'
        '<a class="biglink" href="paid/"><span class="biglink-label">Paid ones<span class="hint">need a subscription</span></span></a>\n'
        '<a class="biglink" href="../all/"><span class="biglink-label">No preference &mdash; show everything<span class="hint">the full list, free and paid</span></span></a>\n'
        "<h2>3. Runs on my computer?</h2>\n"
        '<a class="biglink" href="local/"><span class="biglink-label">Runs on my computer<span class="hint">private, nothing sent to the cloud</span></span></a>\n'
        '<a class="biglink" href="../all/"><span class="biglink-label">Either is fine &mdash; show everything<span class="hint">the full list</span></span></a>\n'
    )
    write(os.path.join(DIST, "start", "index.html"),
          page("Start here - AI Guide",
               "Pick what you want to do, then narrow by free or paid \u2014 a short plain-language list of AIs that fit.",
               picker_body, "..", "../index.html", show_back_link=True,
               canonical=BASE_URL + "start/", is_start_page=True))
    start_urls.append(BASE_URL + "start/")

    free_ps = [p for p in providers if p["free_tier"]]
    paid_ps = [p for p in providers if not p["free_tier"]]
    local_ps = [p for p in providers if p["runs_on_your_computer"]]
    start_write("free/index.html", "Free AIs - AI Guide",
                "Plain-language list of AIs you can try for free.",
                "<h1>Free AIs</h1>\n", free_ps, "../../p/", "../..", "../../index.html")
    start_write("paid/index.html", "Paid AIs - AI Guide",
                "Plain-language list of AIs that need a paid plan.",
                "<h1>Paid AIs</h1>\n", paid_ps, "../../p/", "../..", "../../index.html")
    start_write("local/index.html", "AIs that run on your computer - AI Guide",
                "Plain-language list of AIs that run on your own computer.",
                "<h1>Runs on your computer</h1>\n"
                '<p class="subtitle">Private: nothing you type is sent to the cloud.</p>\n',
                local_ps, "../../p/", "../..", "../../index.html")

    for c in categories:
        label = start_label(c)
        cat_ps = [p for p in providers if c in p["categories"]]
        free_c = [p for p in cat_ps if p["free_tier"]]
        paid_c = [p for p in cat_ps if not p["free_tier"]]
        intro = ("<h1>%s</h1>\n" % esc(label)
                 + '<p class="subtitle">%s</p>\n' % esc(CATEGORY_BLURBS.get(c, ""))
                 + '<a class="biglink" href="../%s-free/"><span class="biglink-label">Free %s</span></a>\n'
                 % (c, esc(label))
                 + '<a class="biglink" href="../%s-paid/"><span class="biglink-label">Paid %s</span></a>\n'
                 % (c, esc(label)))
        start_write("%s/index.html" % c, "%s - start here - AI Guide" % label,
                    "Plain-language %s picks, filtered for you." % label.lower(),
                    intro, cat_ps, "../../p/", "../..", "../../index.html")
        start_write("%s-free/index.html" % c, "Free %s - AI Guide" % label,
                    "Plain-language list of free %s." % label.lower(),
                    "<h1>Free %s</h1>\n" % esc(label),
                    free_c, "../../p/", "../..", "../../index.html")
        start_write("%s-paid/index.html" % c, "Paid %s - AI Guide" % label,
                    "Plain-language list of paid %s." % label.lower(),
                    "<h1>Paid %s</h1>\n" % esc(label),
                    paid_c, "../../p/", "../..", "../../index.html")

    # About page: who makes this guide and how (trust for a non-technical audience).
    about_body = tmpl("about.html").substitute()
    write(os.path.join(DIST, "about", "index.html"),
          page("How this guide works - AI Guide",
               "Who writes this plain-language AI guide, how providers get checked, and why there are no ads or affiliate links.",
               about_body, "..", "../index.html",
               canonical=BASE_URL + "about/", is_about_page=True))
    start_urls.append(BASE_URL + "about/")

    # The real "everything" destination (round-2 fix): the escape hatches and
    # every "All AIs" breadcrumb point here, so the promise is true.
    # Round-3 fix: grouped under category headings with a jump list and a
    # back-to-top link, so the 60-card page is navigable.
    all_sections = []
    jump_links = []
    for c in categories:
        cat_ps = [p for p in providers if c in p["categories"]]
        cards_html = "\n".join(card(p, "../p/") for p in cat_ps)
        all_sections.append('<h2 id="%s">%s</h2>\n%s' % (c, esc(start_label(c)), cards_html))
        jump_links.append('<a href="#%s">%s</a>' % (c, esc(start_label(c))))
    all_body = ("<h1>All AIs</h1>\n"
                '<p class="subtitle">Every provider in this guide, in one list.</p>\n'
                '<nav class="jump" aria-label="Jump to a category">%s</nav>\n'
                % " &middot; ".join(jump_links)
                + LEGEND_HTML + "\n" + "\n".join(all_sections)
                + '\n<p class="top"><a href="#">Back to top</a></p>\n')
    write(os.path.join(DIST, "all", "index.html"),
          page("All AIs - AI Guide",
               "The complete plain-language list of every AI provider in this guide: costs, difficulty, and official links.",
               all_body, "..", "../index.html", show_back_link=False,
               canonical=BASE_URL + "all/"))
    start_urls.append(BASE_URL + "all/")

    # SEO question pages: data-driven from data/questions.json
    best_urls = []
    for q in questions:
        slug = q["slug"]
        matched = [p for p in providers if question_matches(p, q["filter"])]
        cards = "\n".join(card(p, "../../p/") for p in matched)
        body = ("<h1>%s</h1>\n" % esc(q["title"])
                + '<p class="subtitle">%s</p>\n' % esc(q["intro"])
                + LEGEND_HTML + "\n"
                + cards + "\n"
                + '<p class="method">How we picked: %s</p>\n' % esc(q["how_picked"])
                + '<p class="checked">Last checked %s</p>\n' % UPDATED)
        canonical = BASE_URL + "best/%s/" % slug
        write(os.path.join(DIST, "best", slug, "index.html"),
              page(q["seo_title"], q["meta_description"], body, "../..",
                   "../../index.html", canonical=canonical,
                   json_ld=faq_page_schema(
                       q, matched,
                       [BASE_URL + "p/%s.html" % p["id"] for p in matched])))
        best_urls.append(canonical)
    print("Built %d SEO question pages" % len(best_urls))

    # sitemap.xml (2026-09-16 SEO fix: each page exactly once, using the
    # canonical URL form from the <link rel="canonical"> tag — the old
    # BASE_URL+"index.html" twin is gone — and a <lastmod> on every entry).
    urls = [BASE_URL]
    urls += [BASE_URL + c + "/" for c in categories]
    urls += [BASE_URL + "p/%s.html" % p["id"] for p in providers]
    urls += start_urls
    urls += best_urls
    assert len(urls) == len(set(urls)), "sitemap would contain duplicate <loc>"
    assert not any(u.endswith("/index.html") for u in urls), \
        "sitemap would contain an /index.html twin"
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "".join("  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n"
                         % (u, BUILD_DATE) for u in urls)
               + "</urlset>\n")
    write(os.path.join(DIST, "sitemap.xml"), sitemap)

    # robots.txt
    write(os.path.join(DIST, "robots.txt"), "User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE_URL)

    print("Built %d providers, %d categories, %d start pages, %d question pages -> %s"
          % (len(providers), len(categories), len(start_urls), len(best_urls), DIST))


if __name__ == "__main__":
    build()
