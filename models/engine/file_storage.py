#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent a file storage engine.

    Attributes:
    __file_path(str): Path to the JSON file.
    __objects(dict): To store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Serialize __object obj with key <obj_class_name>.id"""
        i = obj.__class__.name__
        FileStorage.__objects["{}.{}".format(i, obj.id)] = obj

    def save(self):
        """Serialize __objects to the Json file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for j in objdict.values():
                    cls_name = j["__class__"]
                    del j["__class__"]
                    self.new(eval(cls_name)(**j))
        except FileNotFoundError:
            return
