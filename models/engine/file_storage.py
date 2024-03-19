#!/usr/bin/python3

"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The path to the file for saving objects.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return a dictionary of instantiated objects.

        If a class is specified, returns objects of that type only.
        Otherwise, returns all objects.
        """
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the __objects dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file specified by __file_path."""
        obj_dict = {
            key: value.to_dict()
            for key, value in self.__objects.items()
        }
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete an object from __objects, if it exists.

        Args:
            obj (BaseModel): The object to be deleted.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Call the reload method to deserialize JSON file."""
        self.reload()
