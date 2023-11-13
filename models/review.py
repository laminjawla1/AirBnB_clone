"""
review - The module which implements
the blue print for instantiating
review objects
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class for creating reviews"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
