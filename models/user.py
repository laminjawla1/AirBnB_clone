#!/user/bin/python3
"""
user module - Implements a blueprint for
instantiating user objects
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The user class - Implements a blueprint
    for creating user instances

    Attr:
        email: str
        password: str
        first_name: str
        last_name: str
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
