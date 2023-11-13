"""
City - The module which implements
the blue print for instantiating
city objects
"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class for creating cities"""

    state_id: str = ""
    name: str = ""
