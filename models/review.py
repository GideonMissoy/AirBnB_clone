#!/usr/bin/python3
"""Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """
        place_id (str): Is the Place id.
        user_id (str): User id.
        text (str): Is the text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
