#!/usr/bin/python3
'''
    Implementation of the Amenity class
    The Amenity class represents an amenity for a place (e.g., WiFi, pool.)
    It inherits from the BaseModel class and the SQLAlchemy Base class, and it
    is mapped to the 'amenities' table in the database.
'''
from os import getenv
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
