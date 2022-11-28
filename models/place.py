#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship

from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all,delete", backref="users")
    amenities = relationship("Amenity", secondary='place_amenity', viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """
        Return a list of all
        Review objects that have a place_id attribute equal to the id attribute of the
        current Place object.
        """
        from models import storage

        reviews = []
        for review in storage.all(Review):
            if self.id == review.place_id:
                reviews.append(reviews)
        return reviews

    @property
    def amenities(self):
        """
        It returns a list of all the amenities that are associated with the place.
        """
        from models.amenity import Amenity
        from models.__init__ import storage

        amenities = []
        for amenity in storage.all(Amenity):
            if amenity.id in self.amenity_ids:
                amenities.append(amenity)
        return amenities

    @amenities.setter
    def amenities(self, obj):
        from models.amenity import Amenity

        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)