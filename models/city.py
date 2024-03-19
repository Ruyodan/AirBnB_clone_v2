#!/usr/bin/python3
"""
Defines the City class.

The City class represents a city in a specific state. It inherits from the
BaseModel class and the SQLAlchemy Base class, and it is mapped to the
'cities' table in the database.

Attributes:
    __tablename__ (str): The name of the MySQL table to store Cities.
    name (sqlalchemy.Column): The name of the City.
    state_id (sqlalchemy.Column): The ID of the State the City belongs to.
    places (sqlalchemy.orm.relationship): The relationship between Cities
        and Places, representing the places located in the City.
"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import State


class City(BaseModel, Base):
    """
    Represents a City in a specific State.
    """

    __tablename__ = "cities"

    # Attributes for the City class
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")

    else:
        name = ""
        state_id = ""

    # Relationship with the State class
    state = relationship("State", back_populates="cities")
