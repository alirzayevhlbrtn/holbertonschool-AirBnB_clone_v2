#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
    
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def places():
            from models import storage
            objects = storage.all(Place)
            places = []
            for i in objects:
                if City.id == objects[i].city_id:
                    places.append(objects[i])
            return places
