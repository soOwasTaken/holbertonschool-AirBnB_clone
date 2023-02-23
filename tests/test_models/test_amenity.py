import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    def test_amenity(self):
        self.assertEqual(Amenity.name, "")
