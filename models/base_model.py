"""
BaseModel Module - The Base for all other classes
"""
import uuid
import models
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

    DATE_TIME_FORMAT = r"%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Constructor - Normally creates an instance
        if kwargs is not passed else
        it uses the key/value pair
        in kwargs
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        # If the kwargs is not None or is not empty
        if kwargs and len(kwargs):
            # If the id is not provided
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    F = self.DATE_TIME_FORMAT
                    self.__dict__[key] = datetime.strptime(value, F)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Saves an instance to the database
        and update the updated_at time
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a key value pair of the current instance's attributes
        and also append the __class__.__name__ attribute
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """An official string representation of the current object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
