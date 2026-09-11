#!/usr/bin/env python3
"""Link checker for the ai-guide static dist/. Stdlib only.
Checks every internal href in every dist HTML page resolves to a file
in dist/. Exit 0 = all good. Usage: python3 linkcheck.py
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("a", "link") and d.get("href"):
            self.links.append(("href", d["href"]))
        if tag in ("img", "script") and d.get("src"):
            self.links.append(("src", d["src"]))

def resolve(url, from_dir):
    url = url.split("#")[0].split("?")[0]
    if not url:
        return None
    if re.match(r"^(https?:|mailto:|tel:|data:|//)", url):
        return None
    return os.path.normpath(os.path.join(from_dir, url))

def main():
    pages = []
    for dirpath, _dirs, files in os.walk(DIST):
        for f in files:
            if f.endswith(".html"):
                pages.append(os.path.join(dirpath, f))
    broken = []
    checked = 0
    for page in pages:
        with open(page, encoding="utf-8") as fh:
            finder = LinkFinder()
            finder.feed(fh.read())
        from_dir = os.path.dirname(page)
        for kind, url in finder.links:
            fs = resolve(url, from_dir)
            if fs is None:
                continue
            checked += 1
            if os.path.isdir(fs):
                fs = os.path.join(fs, "index.html")
            if not os.path.isfile(fs):
                broken.append((os.path.relpath(page, DIST), kind, url))
    print("pages: %d, internal links checked: %d, broken: %d" % (len(pages), checked, len(broken)))
    for page, kind, url in sorted(broken):
        print("BROKEN %s %s -> %s" % (page, kind, url))
    return 1 if broken else 0

if __name__ == "__main__":
    sys.exit(main())
