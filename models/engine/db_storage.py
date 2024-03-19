#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects of the class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        classes = {
            'State': State,
            'City': City,
            'User': User,
            'Place': Place,
            'Review': Review,
            'Amenity': Amenity
        }

        db_dict = {}

        if cls is None:
            for class_name, cls in classes.items():
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(class_name, obj.id)
                    db_dict[key] = obj
        else:
            if type(cls) == str:
                cls = classes.get(cls)
            if cls is not None:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(cls.__name__, obj.id)
                    db_dict[key] = obj

        return db_dict

    def new(self, obj):
        """Add object to current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session."""
        self.__session.close()
