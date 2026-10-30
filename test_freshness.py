#!/usr/bin/env python3
"""Tests for the freshness rules in build.py (30-day overdue, stamp, sitemap lastmod).

Run: python3 test_freshness.py. Builds into a temp dir, never into dist/. Stdlib only.
"""
import importlib
import json
import os
import re
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build


def load_build(build_date):
    """Re-import build.py with AI_GUIDE_BUILD_DATE set."""
    os.environ["AI_GUIDE_BUILD_DATE"] = build_date
    return importlib.reload(build)


class Overdue(unittest.TestCase):
    def test_thirty_days_is_overdue_twenty_nine_is_not(self):
        b = load_build("2026-10-30")
        self.assertTrue(b.is_overdue({"last_checked": "2026-09-30"}))   # 30 days
        self.assertFalse(b.is_overdue({"last_checked": "2026-10-01"}))  # 29 days
        self.assertEqual(b.OVERDUE_DAYS, 30)

    def test_default_build_date_is_today(self):
        os.environ.pop("AI_GUIDE_BUILD_DATE", None)
        b = importlib.reload(build)
        self.assertEqual(b.BUILD_DATE, b.date.today().isoformat())


class Stamp(unittest.TestCase):
    def test_count_and_oldest(self):
        b = load_build("2026-10-30")
        ps = [{"last_checked": "2026-09-01"}, {"last_checked": "2026-09-30"},
              {"last_checked": "2026-10-01"}, {"last_checked": "2026-10-29"}]
        self.assertEqual(b.review_stamp_text(ps),
                         "2 of 4 listings checked in the last 30 days. Oldest check: September 1, 2026.")


class Sitemap(unittest.TestCase):
    def test_lastmod_from_real_dates(self):
        # build date must be one no real card can have, else it collides with real last_checked dates (hit 2026-10-30)
        b = load_build("2099-01-01")
        with tempfile.TemporaryDirectory() as tmp:
            b.DIST = tmp
            b.build()
            sm = open(os.path.join(tmp, "sitemap.xml"), encoding="utf-8").read()
            home = open(os.path.join(tmp, "index.html"), encoding="utf-8").read()
        mods = dict(re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", sm))
        with open(b.DATA, encoding="utf-8") as f:
            providers = json.load(f)
        p = providers[0]
        self.assertEqual(mods[b.BASE_URL + "p/%s.html" % p["id"]], p["last_checked"])
        self.assertEqual(mods[b.BASE_URL], max(x["last_checked"] for x in providers))
        self.assertNotIn("2099-01-01", mods.values())
        self.assertIn("listings checked in the last 30 days. Oldest check:", home)


if __name__ == "__main__":
    try:
        unittest.main()
    finally:
        os.environ.pop("AI_GUIDE_BUILD_DATE", None)
