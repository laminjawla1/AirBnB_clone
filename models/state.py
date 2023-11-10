"""
state module - Implements a blueprint for
instantiating state objects
"""
from models.base_model import BaseModel


class State(BaseModel):
    """The user class"""

    name: str = ""
