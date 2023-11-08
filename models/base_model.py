import uuid
from datetime import datetime
from models import storage


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

        # If the kwargs is not None or is not empty
        if kwargs and len(kwargs):
            # Get the key/value from the dictionary passed
            for key, value in kwargs.items():
                # If key is created_at or updated_at
                # Convert the string to a datetime
                # object with the format specified
                # by the DATE_TIME_FORMAT constant
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                                            value, self.DATE_TIME_FORMAT
                                        )
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def save(self):
        """Saves an instance to the database"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        Returns a key value pair of the current instance's attributes
        and also append the __class__.__name__ attribute
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """An official string representation of the current object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"
