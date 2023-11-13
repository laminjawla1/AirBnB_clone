#!/usr/bin/python3
"""
This module implements and an abstract form of
saving objects
"""
import json
from models.user import User
from models.city import City
from datetime import datetime
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine import custom_exceptions


class FileStorage:
    """Class for managing file storage and retrieval"""

    __file_path: str = "file.json"  # Path to the json file
    __objects: dict = {}  # Will store all objects by <class name>.id
    models = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]

    def all(self):
        """Returns the dictionary <__objects>"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in <__objects> the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the dictionary <__objects> to the file <__file_path>"""
        with open(FileStorage.__file_path, "w") as f:
            obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            f.write(json.dumps(obj))

    def reload(self):
        """Loads the dictionary <__objects> from the file <__file_path>"""
        # Try opening the file and read it
        # if an error occurred, do nothing
        try:
            with open(FileStorage.__file_path, "r") as f:
                # Get all the objects from the file <__file_path>
                objects = json.loads(f.read())

                FileStorage.__objects = {
                    k: eval(o["__class__"])(**o) for k, o in objects.items()
                }
        except Exception as e:  # Unable to open the file
            pass

    def get(self, model, id):
        """Gets an element by ID"""
        if model not in FileStorage.models:
            raise custom_exceptions.GetClassException(model)

        key = f"{model}.{id}"
        try:
            return FileStorage.__objects[key]
        except KeyError:
            raise custom_exceptions.GetInstanceException(id, model)

    def delete(self, model, id):
        """Deletes an element by ID"""
        if model not in FileStorage.models:
            raise custom_exceptions.GetClassException(model)

        key = f"{model}.{id}"
        try:
            del FileStorage.__objects[key]
            FileStorage.save(self)
        except KeyError:
            raise custom_exceptions.GetInstanceException(id, model)

    def print_all(self, model=None):
        """Prints all elements"""
        items = []
        if model:
            if model not in FileStorage.models:
                raise custom_exceptions.GetClassException(model)
            for key, value in FileStorage.__objects.items():
                if key.split(".")[0] == model:
                    items.append(value.__str__())
            return items
        else:
            for key, value in FileStorage.__objects.items():
                items.append(value.__str__())
            return items

    def count(self, model=None):
        """Prints all elements"""
        cnt = 0
        if model:
            if model not in FileStorage.models:
                raise custom_exceptions.GetClassException(model)
            for key, value in FileStorage.__objects.items():
                if key.split(".")[0] == model:
                    cnt += 1
            return cnt
        else:
            for key, value in FileStorage.__objects.items():
                cnt += 1
            return cnt

    def update(self, model, id, attr_name, attr_value):
        """Updates an element by ID"""
        if model not in FileStorage.models:
            raise custom_exceptions.GetClassException(model)

        key = f"{model}.{id}"
        try:
            obj = FileStorage.__objects[key]
            setattr(obj, attr_name, attr_value)
            FileStorage.__objects[key] = obj
            FileStorage.save(self)
        except KeyError:
            raise custom_exceptions.GetInstanceException(id, model)
