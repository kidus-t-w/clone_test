#!/usr/bin/python3
"""Place class definition."""
from base_model import BaseModel


class Place(BaseModel):
    """A class to represent a place.

    Attributes:
        city_id (str): Identifier for the city.
        user_id (str): Identifier for the user.
        name (str): Name of the place.
        description (str): Description of the place.
        number_rooms (int): Count of rooms in the place.
        number_bathrooms (int): Count of bathrooms in the place.
        max_guest (int): Maximum guest capacity of the place.
        price_by_night (int): Nightly price for the place.
        latitude (float): Latitude coordinate of the place.
        longitude (float): Longitude coordinate of the place.
        amenity_ids (list): List of associated Amenity ids.
    """

    class_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0 
    amenity_ids = []
