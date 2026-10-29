import unittest

from src.sponsor_match.matching import Event, Sponsor, normalize, rank_events


class MatchingTests(unittest.TestCase):
    def setUp(self):
        self.sponsor = Sponsor(
            "Northstar Audio",
            frozenset({"Music"}),
            frozenset({"Creators"}),
            frozenset({"Southeast"}),
            10000,
        )

    def test_normalize_handles_punctuation_and_case(self):
        self.assertEqual(normalize("  Creator-Focused  "), "creator focused")

    def test_rank_is_explainable_and_deterministic(self):
        events = [
            Event("Arts Night", frozenset({"arts"}), frozenset({"creators"}), frozenset({"southeast"}), 5000),
            Event("Music Summit", frozenset({"music"}), frozenset({"creators"}), frozenset({"southeast"}), 5000),
        ]
        ranked = rank_events(self.sponsor, events)
        self.assertEqual(ranked[0].event.name, "Music Summit")
        self.assertEqual(ranked[0].confidence, "high")
        self.assertTrue(any("industry overlap" in reason for reason in ranked[0].reasons))

    def test_budget_shortfall_is_visible(self):
        event = Event("Small Showcase", frozenset({"music"}), frozenset(), frozenset(), 20000)
        match = rank_events(self.sponsor, [event])[0]
        self.assertIn("budget below sponsorship minimum", match.reasons)


if __name__ == "__main__":
    unittest.main()
