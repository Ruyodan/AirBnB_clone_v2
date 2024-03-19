#!/usr/bin/python3
"""
Defines the Amenity class.

The Amenity class represents an amenity for a place (e.g., WiFi, pool, etc.).
It inherits from the BaseModel class and the SQLAlchemy Base class, and it
is mapped to the 'amenities' table in the database.

Attributes:
    __tablename__ (str): The name of the MySQL table to store Amenities.
    name (sqlalchemy.Column): The amenity name.
    place_amenities (sqlalchemy.orm.relationship): The relationship between
        Amenities and Places, represented by the 'place_amenity' association
        table.
"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """
    Represents an Amenity for a place.
    """

    __tablename__ = "amenities"

    # Attributes for the Amenity class
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities",
                                       viewonly=False)
    else:
        name = ""
