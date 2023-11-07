import uuid
from datetime import datetime


class BaseModel:
    """
    Base model for all other models

    Attributes:
        id (str): Unique identifier of the instance
        created_at (datetime): Timestamp when the instance was created
        updated_at (datetime): Timestamp when the instance was last updated

    Methods:
        save(): Saves an instance to the database
        to_dict(): Returns a key value pairs of the current instance's
        attributes
        __str__(): An official string representation of the current object
    """
    def __init__(self):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Saves an instance to the database"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Returns a key value pair of the current instance's attributes
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """An official string representation of the current object"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
