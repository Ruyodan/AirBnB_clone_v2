#!/usr/bin/python3

"""
Defines the BaseModel class.

The BaseModel class serves as the base class for all other classes in the
project. It defines the common attributes and methods that all other classes
should inherit.

Attributes:
id (sqlalchemy.Column): The unique identifier for the object.
created_at (sqlalchemy.Column): The datetime at which the object was created.
updated_at (sqlalchemy.Column): Datetime at which the object was last updated.

Methods:
__init__(self, *args, **kwargs): Initializes a new instance of the class.
__str__(self): Returns a string representation of the object.
__repr__(self): Returns a string representation of the object.
save(self): Updates the updated_at attribute with the current datetime.
to_dict(self): Returns a dictionary representation of the object.
delete(self): Deletes the object from the storage.
"""

import models
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
    The base class for all other classes in the project.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args (tuple): Unused positional arguments.
            **kwargs (dict): Key-value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def __repr__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in obj_dict:
            del obj_dict["_sa_instance_state"]
        return obj_dict

    def delete(self):
        """
        Deletes the object from the storage.
        """
        models.storage.delete(self)
