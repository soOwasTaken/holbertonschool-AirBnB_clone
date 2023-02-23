#!/usr/bin/python3
"""Unittest module for file storage"""
import json
import os
import tempfile
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for file storage"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()
        self.storage = FileStorage()

    def test_file_path(self):
        """Test that the file path is correct"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """Test that the storage object is a dictionary"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_new(self):
        """Test that an object is added to __objects"""
        self.storage.new(self.model)
        key = type(self.model).__name__ + "." + self.model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that __objects is saved to a file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "file.json")
            self.storage._FileStorage__file_path = path
            self.storage.new(self.model)
            self.storage.save()
            with open(path, "r") as f:
                data = json.load(f)
                key = type(self.model).__name__ + "." + self.model.id
                self.assertIn(key, data)

if __name__ == "__main__":
    unittest.main()
