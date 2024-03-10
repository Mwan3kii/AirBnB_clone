#!/usr/bin/python3
"""Creates the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Define class Review that inherits from Basemodel"""

    place_id = ""
    user_id = ""
    text = ""
