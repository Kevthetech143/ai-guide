#!/usr/bin/env python3
"""Static-site builder for the plain-language AI-provider guide.

Reads data/providers.json + templates/, writes dist/.
STDLIB ONLY - no pip needed.

Usage: python3 build.py
"""
import html
import json
import os
import shutil
from datetime import date
from string import Template

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "providers.json")
TEMPLATES = os.path.join(ROOT, "templates")
STATIC = os.path.join(ROOT, "static")
DIST = os.path.join(ROOT, "dist")
BASE_URL = "https://kevthetech143.github.io/ai-guide/"
UPDATED = date.today().isoformat()

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
    "code": "Code", "search": "Search", "music": "Music", "agents": "Agents",
}

# Home-page tile order: (category, 3-6 word plain hint).
TILE_ORDER = [
    ("chat", "ask questions, write things"),
    ("image", "make pictures from words"),
    ("video", "make videos from words"),
    ("voice", "turn text into speech"),
    ("music", "make songs from words"),
    ("code", "help writing computer code"),
    ("search", "answers by looking things up"),
    ("agents", "does multi-step jobs alone"),
]


def esc(s):
    return html.escape(str(s), quote=True)


def load_providers():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def tmpl(name):
    with open(os.path.join(TEMPLATES, name), encoding="utf-8") as f:
        return Template(f.read())


def page(title, meta_description, body, style_prefix, home_href,
         show_back_link=True):
    topnav = ""
    if show_back_link:
        topnav = ('<nav class="topnav"><a href="%s">&larr; All AIs</a></nav>'
                  % esc(home_href))
    return tmpl("base.html").substitute(
        title=esc(title),
        meta_description=esc(meta_description),
        body=body,
        style_prefix=style_prefix,
        home_href=home_href,
        topnav=topnav,
        updated=UPDATED,
    )


def card(provider, href_prefix):
    """Render a provider card. href_prefix: path prefix to dist/p/ from the page."""
    p = provider
    free_badge = "Free" if p["free_tier"] else "Paid"
    skill_badge = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}[p["skill_level"]]
    open_badge = "Open" if p["open_weights"] else "Closed"
    local_badge = ' <span class="badge">Runs on your computer</span>' if p["runs_on_your_computer"] else ""
    card_href = "%s%s.html" % (href_prefix, p["id"])
    return tmpl("card.html").substitute(
        card_href=card_href,
        name=esc(p["name"]),
        free_badge=free_badge,
        skill_badge=skill_badge,
        open_badge=open_badge,
        local_badge=local_badge,
        good_for=esc(p["good_for"]),
        price_from=esc(p["price_from"]),
        watch_out=esc(p["watch_out"]),
        link=esc(p["link"]),
        last_checked=esc(p["last_checked"]),
    )


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def filtered_page(providers, title, meta_description, intro_html,
                  href_prefix, style_prefix, home_href):
    """A filtered provider list page (used by the start-here picker)."""
    cards = "\n".join(card(p, href_prefix) for p in providers)
    body = intro_html + "\n" + cards
    return page(title, meta_description, body, style_prefix, home_href,
                show_back_link=True)


def build():
    providers = load_providers()
    categories = sorted({c for p in providers for c in p["categories"]})

    # fresh dist
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(STATIC, os.path.join(DIST, "static"))

    # home page: tiles in fixed order with plain hints; no back link to self
    tiles = "\n".join(
        '<a class="tile" href="%s/index.html">'
        '<span class="tile-name">%s</span>'
        '<span class="tile-hint">%s</span></a>' % (
            c, esc(CATEGORY_NAMES.get(c, c.title())), esc(hint))
        for c, hint in TILE_ORDER if c in categories
    )
    cards = "\n".join(card(p, "p/") for p in providers)
    body = tmpl("home.html").substitute(tiles=tiles, cards=cards)
    write(os.path.join(DIST, "index.html"),
          page("Which AI should I use? - AI Guide",
               "A plain-language guide to picking an AI: what it costs, how hard it is, and where to get it.",
               body, ".", "index.html", show_back_link=False))

    # category pages
    for c in categories:
        cards = "\n".join(card(p, "../p/") for p in providers if c in p["categories"])
        body = tmpl("category.html").substitute(
            category_name=esc(CATEGORY_NAMES.get(c, c.title())),
            category_blurb=esc(CATEGORY_BLURBS.get(c, "")),
            cards=cards,
        )
        write(os.path.join(DIST, c, "index.html"),
              page("%s AIs - AI Guide" % CATEGORY_NAMES.get(c, c.title()),
                   "Plain-language %s AI picks: costs, difficulty, and official links." % c,
                   body, "..", "../index.html"))

    # provider pages
    for p in providers:
        free_badge = "Free" if p["free_tier"] else "Paid"
        skill_badge = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}[p["skill_level"]]
        open_badge = "Open" if p["open_weights"] else "Closed"
        local_badge = ' <span class="badge">Runs on your computer</span>' if p["runs_on_your_computer"] else ""
        body = tmpl("provider.html").substitute(
            name=esc(p["name"]),
            company=esc(p["company"]),
            free_badge=free_badge,
            skill_badge=skill_badge,
            open_badge=open_badge,
            local_badge=local_badge,
            good_for=esc(p["good_for"]),
            price_from=esc(p["price_from"]),
            watch_out=esc(p["watch_out"]),
            categories_text=esc(", ".join(CATEGORY_NAMES.get(c, c.title()) for c in p["categories"])),
            link=esc(p["link"]),
            last_checked=esc(p["last_checked"]),
        )
        write(os.path.join(DIST, "p", "%s.html" % p["id"]),
              page("%s - AI Guide" % p["name"],
                   "%s by %s: %s" % (p["name"], p["company"], p["good_for"]),
                   body, "..", "../index.html"))

    # start-here picker (no JavaScript required: plain links to built lists)
    start_urls = []

    def start_write(rel, title, meta_description, intro_html, plist,
                    href_prefix, style_prefix, home_href):
        html_out = filtered_page(plist, title, meta_description, intro_html,
                                 href_prefix, style_prefix, home_href)
        write(os.path.join(DIST, "start", rel), html_out)
        start_urls.append(BASE_URL + "start/" + rel)

    cat_links = "\n".join(
        '<a class="biglink" href="%s/">%s AIs<span class="hint">%s</span></a>' % (
            c, esc(CATEGORY_NAMES.get(c, c.title())), esc(hint))
        for c, hint in TILE_ORDER if c in categories
    )
    picker_body = (
        "<h1>Start here</h1>\n"
        '<p class="subtitle">Three quick questions. Tap an answer to see a short list.</p>\n'
        "<h2>1. What do you want to make?</h2>\n" + cat_links + "\n"
        "<h2>2. Free or paid?</h2>\n"
        '<a class="biglink" href="free/">Free ones<span class="hint">costs nothing to try</span></a>\n'
        '<a class="biglink" href="paid/">Paid ones<span class="hint">needs a subscription</span></a>\n'
        "<h2>3. Runs on my computer?</h2>\n"
        '<a class="biglink" href="local/">Runs on my computer<span class="hint">private, nothing sent to the cloud</span></a>\n'
    )
    write(os.path.join(DIST, "start", "index.html"),
          page("Start here - AI Guide",
               "Answer three quick questions and get a short plain-language list of AIs that fit.",
               picker_body, "..", "../index.html", show_back_link=True))
    start_urls.append(BASE_URL + "start/index.html")

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
        cname = CATEGORY_NAMES.get(c, c.title())
        cat_ps = [p for p in providers if c in p["categories"]]
        free_c = [p for p in cat_ps if p["free_tier"]]
        paid_c = [p for p in cat_ps if not p["free_tier"]]
        intro = ("<h1>%s AIs</h1>\n" % esc(cname)
                 + '<p class="subtitle">%s</p>\n' % esc(CATEGORY_BLURBS.get(c, ""))
                 + '<p><a class="biglink" href="../%s-free/">Free %s AIs</a></p>\n'
                 % (c, esc(cname))
                 + '<p><a class="biglink" href="../%s-paid/">Paid %s AIs</a></p>\n'
                 % (c, esc(cname)))
        start_write("%s/index.html" % c, "%s AIs - start here - AI Guide" % cname,
                    "Plain-language %s AI picks, filtered for you." % c,
                    intro, cat_ps, "../../p/", "../..", "../../index.html")
        start_write("%s-free/index.html" % c, "Free %s AIs - AI Guide" % cname,
                    "Plain-language list of free %s AIs." % c,
                    "<h1>Free %s AIs</h1>\n" % esc(cname),
                    free_c, "../../p/", "../..", "../../index.html")
        start_write("%s-paid/index.html" % c, "Paid %s AIs - AI Guide" % cname,
                    "Plain-language list of paid %s AIs." % c,
                    "<h1>Paid %s AIs</h1>\n" % esc(cname),
                    paid_c, "../../p/", "../..", "../../index.html")

    # sitemap.xml
    urls = [BASE_URL, BASE_URL + "index.html"]
    urls += [BASE_URL + c + "/" for c in categories]
    urls += [BASE_URL + "p/%s.html" % p["id"] for p in providers]
    urls += start_urls
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "".join("  <url><loc>%s</loc></url>\n" % u for u in urls)
               + "</urlset>\n")
    write(os.path.join(DIST, "sitemap.xml"), sitemap)

    # robots.txt
    write(os.path.join(DIST, "robots.txt"), "User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE_URL)

    print("Built %d providers, %d categories, %d start pages -> %s"
          % (len(providers), len(categories), len(start_urls), DIST))


if __name__ == "__main__":
    build()
