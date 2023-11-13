"""
Amenity - The module which implements
the blue print for instantiating
amenity objects
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class for creating amenities"""

    name: str = ""
