#!/usr/bin/python3

"""Review class for AirBnB clone"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for AirBnB clone"""

    place_id = ""
    user_id = ""
    text = ""
