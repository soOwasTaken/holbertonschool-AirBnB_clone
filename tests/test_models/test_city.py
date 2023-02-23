import unittest
from models.city import City


class test_city(unittest.TestCase):
    def test_city(self):
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
