import unittest
import os.path
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage



class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        model = BaseModel()
        model.save()
        self.assertEquals(FileStorage._FileStorage__file_path, "file.json")
        os.remove("file.json")

    def test_all(self):
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        FileStorage.new(FileStorage, model)
        self.assertNotEquals(objects[f"{model.__class__.__name__}.{model.id}"], None)

    def test_objects(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        model.save()
        self.assertEqual(type(objects), dict)
        os.remove("file.json")

    def test_reload(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        obj = objects.copy()
        model = BaseModel()
        FileStorage.reload(FileStorage)
        self.assertNotEqual(obj, objects)
        """ os.remove("file.json") """

    def test_save_storage(self):
        self.assertEqual(os.path.isfile("file.json"), False)
        model = BaseModel()
        FileStorage.save(FileStorage)
        self.assertEqual(os.path.isfile("file.json"), True)
        os.remove("file.json")