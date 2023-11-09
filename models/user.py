"""
user module - Implements a blueprint for
instantiating user objects
"""
from models.base_model import BaseModel


class User(BaseModel):
    """The user class"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
