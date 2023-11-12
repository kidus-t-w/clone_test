#!/usr/bin/python3
"""Review class definition."""
from base_model import BaseModel


class Review(BaseModel):
    """A class to encapsulate a review.

    Attributes:
        place_id (str): Identifier for the place.
        user_id (str): Identifier for the user.
        text (str): Content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
