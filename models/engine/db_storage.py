#!/usr/bin/python3
"""
    It creates an engine that connects to the database,
    and creates a session object that can be used to query the database.
"""


from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review

class DBStorage:
    """ DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """
        The __init__ function creates an engine that connects to the database.
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                           .format(getenv('HBNB_MYSQL_USER'),
                                   getenv('HBNB_MYSQL_PWD'),
                                   getenv('HBNB_MYSQL_HOST'),
                                   getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        It returns a dictionary of all the objects in the database.
        
        :param cls: the class name
        :return: A dictionary of all the objects in the database.
        """
        from console import HBNBCommand

        result = {}

        if cls in HBNBCommand.classes:
            response = self.__session.query(HBNBCommand.classes[cls]).all()
            for row in response:
                result[f"{cls}.{row.id}"] = row
        else:
            for c in HBNBCommand.classes.values():
                if c.__name__ != 'BaseModel':
                    response = self.__session.query(c).all()
                    for row in response:
                        result[f"{c.__class__.__name__}.{row.id}"] = row.to_dict()
        return result

    def new(self, obj):
        """
        Add the object to the current database session 
        """
        self.__session.add(obj)
    
    def save(self):
        """
        It commits the changes made to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        It deletes the object from the database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        It creates a new session object and assigns it to the variable self.__session
        """
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(new_session)
