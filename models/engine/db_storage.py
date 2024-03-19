#!/usr/bin/python3

"""
Define class DatabaseStorage

This class is responsible for managing the database storage engine
for the AirBnB application. It provides methods to interact with
the database, such as creating, reading, updating, and deleting
objects.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base

class DBStorage:
    """
    Create SQLalchemy database

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize a new DBStorage instance.

        This method creates the engine and links it to the MySQL database
        specified by the environment variables (HBNB_MYSQL_USER,
        HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB).

        If the environment variable HBNB_ENV is set to 'test', it drops
        all existing tables in the database.
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query the current database session for all objects of the given class.

        Args:
            cls (class, optional): The class of objects to query. If None,
                queries all types of objects.

        Returns:
            dict: A dictionary of queried objects in the format
                <class name>.<obj id> = obj.
        """
        db_dict = {}

        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__, obj.id)
                            db_dict[key] = obj

        return db_dict

    def new(self, obj):
        """
        Add the given object to the current database session.

        Args:
            obj (object): The object to be added to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete the given object from the current database session.

        Args:
            obj (object, optional): The object to be deleted from the session.
                If None, no action is taken.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and initialize a new session.
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """
        Close the working SQLAlchemy session.
        """
        self.__session.close()
