import unittest
from models.state import State


class test_state(unittest.TestCase):
    def test_state(self):
        self.assertEqual(State.name, "")