""" Console module """
#!/usr/bin/env python3

# Importing the necessary module
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.engine.custom_exceptions import (GetInstanceException, GetClassException)


# Define a custom command-line interface class named HBNBCommand that inherits from cmd.Cmd
class HBNBCommand(cmd.Cmd):
    """
    HBNB command line interface - This will be used as the
    frontend of the project where users can interact with the program
    """

    # Set a custom prompt for the command-line interface
    prompt = "(hbnb) "

    # Define a command to quit the program
    def do_quit(self, _):
        """Quit command to exit the program"""
        return True
    
    # Define a command to handle the End-of-File (EOF) input, also quitting the program
    def do_EOF(self, _):
        """Exits the program"""
        return True
    
    def emptyline(self):
        """Do nothing when the user press only enter"""
        pass

    # Create Command
    def do_create(self, line):
        """Create a new instance"""

        args, args_len = arg_parse(line)
        match args_len:
            case 0:
                print("** class name missing **")
            case 1:
                try:
                    cls = eval(args[0])
                    instance = cls()
                    print(instance.id)
                    instance.save()
                except NameError:
                    print("** class doesn't exist **")
            case _:
                print(
                    "** too many arguments passed: Usage: create <model> **"
                )
    
    # Show command
    def do_show(self, line):
        """Prints the string representation of an instance
based on the class name and id
        """
        args, args_len = arg_parse(line)
        match args_len:
            case 0:
                print("** class name missing **")
            case 1:
                print("** instance id missing **")
            case 2:
                instance = storage.get(*args)
                try:
                    print(instance)
                except GetClassException:
                    print("** class doesn't exist **")
                except GetInstanceException:
                    print("** no instance found **")

            case _:
                print(
                    "** too many arguments passed: Usage: create <model> **"
                )
        
      
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


def arg_parse(line):
    """Splits the argument by a space"""
    tokens = split(line)
    return tokens, len(tokens)

# Check if this script is the main entry point for execution
if __name__ == "__main__":
    # Create an instance of the HBNBCommand class and start the command loop
    HBNBCommand().cmdloop()
