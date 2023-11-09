#!/usr/bin/python3

""" Console module """

import cmd
from models import storage
from models.base_model import BaseModel


def checker(cls_name=None, cls_id=None, cls_attr=None, cls_value=None):
    """checker for commands"""
    if cls_name == "":
        print("** class name missing **")
        return False
    if cls_name != "BaseModel":
        print("** class doesn't exist **")
        return False
    if cls_id == "":
        print("** instance id missing **")
        return False
    if f"{cls_name}.{cls_id}" not in storage.all():
        print("** no instance found **")
        return False
    if cls_attr == "":
        print("** attribute name missing **")
        return False
    if cls_value == "":
        print("** value missing **")
        return False
    return True


class HBNBCommand(cmd.Cmd):
    """ command interpreter """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        return

    def do_create(self, cls_name):
        """create a new instanve of BaseModel and saves it to JSON file"""
        if checker(cls_name):
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        cls_arr = line.split()
        if len(cls_arr) == 2 and checker(cls_arr[0], cls_arr[1]):
            my_dict = storage.all()[f"{cls_arr[0]}.{cls_arr[1]}"]
            my_model = BaseModel(**my_dict)
            my_model.__str__()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        cls_arr = line.split()
        if len(cls_arr) == 2 and checker(cls_arr[0], cls_arr[1]):
            storage._FileStorage__objects.pop(f"{cls_arr[0]}.{cls_arr[1]}")
            sotrage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        all_list = []
        for obj in storage.all().values():
            my_model = BaseModel(**obj)
            all_list.append(my_model.__str__())
        print(all_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        cls_arr = line.split()
        if len(cls_arr) >= 4:
            if checker(cls_arr[0], cls_arr[1], cls_arr[2], cls_arr[3]):
                my_type = type(storage._FileStorage__objects[cls_arr[2]])
                storage._FileStorage__objects[cls_arr[2]] = my_type(cls_arr[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
