#!/usr/bin/python3
"""State class definition."""
from .base_model import BaseModel

class State(BaseModel):
    """A class to represent a state.

    Attributes:
        name (str): Name of the state.
    """
    name = ""
