#!/usr/bin/env python3
"""Tests for the "ids" question filter rule in build.py. Stdlib only."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import check_rule_ids, question_matches

PROVIDERS = [
    {"id": "a", "categories": ["chat"]},
    {"id": "b", "categories": ["image"]},
]


def matched(rule):
    return [p["id"] for p in PROVIDERS if question_matches(p, rule)]


class IdsFilter(unittest.TestCase):
    def test_ids_match(self):
        self.assertEqual(matched({"ids": ["a"]}), ["a"])

    def test_ids_miss(self):
        self.assertEqual(matched({"ids": ["zzz"]}), [])

    def test_ids_and_categories(self):
        self.assertEqual(matched({"ids": ["a", "b"], "categories": ["image"]}), ["b"])
        self.assertEqual(matched({"ids": ["a"], "categories": ["image"]}), [])

    def test_unknown_id_raises(self):
        check_rule_ids(PROVIDERS, {"ids": ["a", "b"]})
        with self.assertRaises(ValueError) as cm:
            check_rule_ids(PROVIDERS, {"ids": ["a", "nope"]})
        self.assertIn("nope", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
