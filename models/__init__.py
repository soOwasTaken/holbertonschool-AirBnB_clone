#!/usr/bin/python3
"""Create a unique FileStorage instance"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


storage = FileStorage()
storage.reload()
__class__ = ['BaseModel', 'User', 'City', 'Place',
             'Amenity', 'Review', 'State']
