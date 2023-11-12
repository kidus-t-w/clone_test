#!/usr/bin/python3
"""City class definition."""
from base_model import BaseModel


class City(BaseModel):
    """A class to represent a city.

    Attributes:
        state_id (str): Identifier for the state.
        name (str): Name of the city.
    """
    state_id = ""
    name = ""
