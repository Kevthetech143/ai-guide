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


def esc(s):
    return html.escape(str(s), quote=True)


def load_providers():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def tmpl(name):
    with open(os.path.join(TEMPLATES, name), encoding="utf-8") as f:
        return Template(f.read())


def page(title, meta_description, body, style_prefix, home_href):
    return tmpl("base.html").substitute(
        title=esc(title),
        meta_description=esc(meta_description),
        body=body,
        style_prefix=style_prefix,
        home_href=home_href,
        updated=UPDATED,
    )


def card(provider, style_depth):
    """Render a provider card. style_depth: 0 on home, 1 on category page."""
    p = provider
    free_badge = "Free" if p["free_tier"] else "Paid"
    skill_badge = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}[p["skill_level"]]
    open_badge = "Open" if p["open_weights"] else "Closed"
    local_badge = ' <span class="badge">Runs on your computer</span>' if p["runs_on_your_computer"] else ""
    card_href = ("p/%s.html" % p["id"]) if style_depth == 0 else ("../p/%s.html" % p["id"])
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


def build():
    providers = load_providers()
    categories = sorted({c for p in providers for c in p["categories"]})

    # fresh dist
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(STATIC, os.path.join(DIST, "static"))

    # home page
    tiles = "\n".join(
        '<a class="tile" href="%s/index.html">%s</a>' % (c, esc(CATEGORY_NAMES.get(c, c.title())))
        for c in categories
    )
    cards = "\n".join(card(p, 0) for p in providers)
    body = tmpl("home.html").substitute(tiles=tiles, cards=cards)
    write(os.path.join(DIST, "index.html"),
          page("Which AI should I use? - AI Guide",
               "A plain-language guide to picking an AI: what it costs, how hard it is, and where to get it.",
               body, ".", "index.html"))

    # category pages
    for c in categories:
        cards = "\n".join(card(p, 1) for p in providers if c in p["categories"])
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

    # sitemap.xml
    urls = [BASE_URL, BASE_URL + "index.html"]
    urls += [BASE_URL + c + "/" for c in categories]
    urls += [BASE_URL + "p/%s.html" % p["id"] for p in providers]
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "".join("  <url><loc>%s</loc></url>\n" % u for u in urls)
               + "</urlset>\n")
    write(os.path.join(DIST, "sitemap.xml"), sitemap)

    # robots.txt
    write(os.path.join(DIST, "robots.txt"), "User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE_URL)

    print("Built %d providers, %d categories -> %s" % (len(providers), len(categories), DIST))


if __name__ == "__main__":
    build()
