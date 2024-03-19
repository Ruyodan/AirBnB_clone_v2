#!/usr/bin/python3
"""
Package initializer for the models module.

This module is responsible for creating an instance of the appropriate
storage engine (either DBStorage or FileStorage) based on the value of
the HBNB_TYPE_STORAGE environment variable.

If HBNB_TYPE_STORAGE is set to 'db', a DBStorage instance is created,
which means data will be stored in a database. Otherwise, a FileStorage
instance is created, which means data will be stored in a JSON file.

The created storage instance is assigned to the 'storage' variable, and
the 'reload' method is called to load the existing data from the
respective storage medium.

Additionally, a dictionary 'classes' is defined, mapping class names
to their corresponding class objects. This dictionary is used by the
storage engines to manage instances of different classes.
"""

import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Dictionary mapping class names to their corresponding class objects
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

# Check the value of the HBNB_TYPE_STORAGE environment variable
storage_type = os.getenv("HBNB_TYPE_STORAGE", "fs")

# Import and instantiate the appropriate storage engine
if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Load existing data from the storage medium
storage.reload()
