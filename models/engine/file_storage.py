import json


class FileStorage:
    """Class for managing file storage and retrieval"""

    __file_path: str = "file.json"  # Path to the json file
    __objects: dict = {}   # Will store all objects by <class name>.id

    def all(self):
        """Returns the dictionary <__objects>"""
        return self.__objects

    def new(self, obj):
        """Sets in <__objects> the obj with key <obj class name>.id"""
        # self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Saves the dictionary <__objects> to the file <__file_path>"""
        with open(self.__file_path, "w") as f:
            json.dump({
                key: value.to_dict() for key, value in self.__objects.items()
            }, f)

    def reload(self):
        """Loads the dictionary <__objects> from the file <__file_path>"""

        # Try opening the file and read it
        # if an error occurred, do nothing
        try:
            with open(self.__file_path, "r") as f:
                # Get all the objects from the file <__file_path>
                objects = json.loads(f.read())
                # For each object in objects
                for obj in objects.values():
                    print(f"obj => {obj}")
                    # Get the class name of the object
                    class_name = obj["__class__"]
                    # Reincarnate the class / blueprint
                    cls = eval(class_name)
                    # Create a new instance
                    new_obj = cls(**obj)
                    # Make the object available to the user
                    self.new(new_obj)
        except Exception as e:   # Unable to open the file
            pass
