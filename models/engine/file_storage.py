#!/usr/bin/python3
"""
Defines the FileStorage class.

The FileStorage class is an abstracted storage engine that provides methods
to store and retrieve objects in a JSON file. It serves as a persistent
storage solution for the application's data.
"""
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
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary of instantiated objects.

    Methods:
    all(cls=None): Retrieves all objects or objects of a specific class.
    new(obj): Adds a new object to the __objects dictionary.
    save(): Serializes the __objects dictionary to the JSON file.
    reload(): Deserializes objects from the JSON file to the objects dictionary
    delete(obj=None): Deletes an object from the __objects dictionary.
    close(): Calls the reload method to update the __objects dictionary.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return a dictionary of instantiated objects in __objects.

        Args:
            cls (class, optional):returns only objects of this class.

        Returns:
            dict: A dictionary of objects, filtered by class if specified.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            return {
                key: value for key, value in self.__objects.items()
                if isinstance(value, cls)
            }
        return self.__objects

    def new(self, obj):
        """
        Set a new object in the __objects dictionary.

        Args:
            obj (object): The object to be added to the __objects dictionary.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the __objects dictionary to the JSON file.
        """
        obj_dict = {
            key: value.to_dict() for key, value in self.__objects.items()
        }
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize objects from the JSON file to the __objects dictionary.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
            for obj in obj_dict.values():
                cls_name = obj["__class__"]
                del obj["__class__"]
                self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete an object from the __objects dictionary.

        Args:
            obj (object, optional): To be deleted from the objects dictionary.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """
        Call the reload method to update the __objects dictionary.
        """
        self.reload()
