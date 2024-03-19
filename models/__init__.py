#!/usr/bin/python3
'''
    Package initializer
    This module is responsible for creating an instance of the appropriate
    storage engine (either DBStorage or FileStorage) based on the value of
    the HBNB_TYPE_STORAGE environment variable.
'''
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

storage.reload()
