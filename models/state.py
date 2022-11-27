#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="states")

    @property
    def cities(self):
        """
        Return a list of all
        City objects that have a state_id attribute equal to the id attribute of the
        current State object.
        """
        cities = []
        for city in storage.all(City):
            if self.id == city.state_id:
                cities.append(city)
        return cities