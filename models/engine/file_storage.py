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
    """Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path(str): Path to the JSON file
        __objects(dict): An empty dictionary that will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Serialize __object obj with key <obj_class_name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the Json file __file_path."""
        json_objects = {}
        for key in FileStorage.__objects:
            json_objects[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the Json file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
            for key in objdict.values():
                class_name = key["__class__"]
                del key["__class__"]
                self.new(eval(class_name)(**key))
        except FileNotFoundError:
            return
