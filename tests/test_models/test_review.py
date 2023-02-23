import unittest
from models.review import Review


class test_review(unittest.TestCase):
    def test_review(self):
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
