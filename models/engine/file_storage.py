import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                objects_dict = json.load(f)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    obj_dict = value
                    obj_dict['__class__'] = class_name
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
