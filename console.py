#!/usr/bin/env python3
""" Console module """

# Importing the necessary module
import cmd
from shlex import split
from models import storage
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine import custom_exceptions


# Define a custom command-line interface class named HBNBCommand
# that inherits from cmd.Cmd
class HBNBCommand(cmd.Cmd):
    """
    HBNB command line interface - This will be used as the
    frontend of the project where users can interact with the program
    """

    # Set a custom prompt for the command-line interface
    prompt = "(hbnb) "

    # Error messages
    ERROR_MESSAGES = [
        "** class name missing **",  # 0
        "** class doesn't exist **",  # 1
        "** instance id missing **",  # 2
        "** no instance found **",  # 3
        "** attribute name missing **",  # 4
        "** value missing **",  # 5
    ]

    # Define a command to quit the program
    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    # Define a command to handle the End-of-File (EOF) input,
    # also quitting the program
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
                print(HBNBCommand.ERROR_MESSAGES[0])
            case 1:
                try:
                    cls = eval(args[0])
                    instance = cls()
                    print(instance.id)
                    instance.save()
                except NameError:
                    print(HBNBCommand.ERROR_MESSAGES[1])
            case _:
                pass

    # Show command
    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args, args_len = arg_parse(line)
        match args_len:
            case 0:
                print(HBNBCommand.ERROR_MESSAGES[0])
            case 1:
                print(HBNBCommand.ERROR_MESSAGES[2])
            case 2:
                try:
                    instance = storage.get(*args)
                    print(instance)
                except custom_exceptions.GetClassException:
                    print(HBNBCommand.ERROR_MESSAGES[1])
                except custom_exceptions.GetInstanceException:
                    print(HBNBCommand.ERROR_MESSAGES[3])
            case _:
                pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args, args_len = arg_parse(line)
        match args_len:
            case 0:
                print(HBNBCommand.ERROR_MESSAGES[0])
            case 1:
                print(HBNBCommand.ERROR_MESSAGES[2])
            case 2:
                try:
                    storage.delete(*args)
                except custom_exceptions.GetClassException:
                    print(HBNBCommand.ERROR_MESSAGES[3])
                except custom_exceptions.GetInstanceException:
                    print(HBNBCommand.ERROR_MESSAGES[4])
            case _:
                pass

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args, args_len = arg_parse(line)
        if args_len < 2:
            try:
                print(storage.print_all(*args))
            except custom_exceptions.GetClassException:
                print(HBNBCommand.ERROR_MESSAGES[1])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args, args_len = arg_parse(line)
        match args_len:
            case 0:  # update
                print(HBNBCommand.ERROR_MESSAGES[0])
            case 1:  # update BaseModel
                print(HBNBCommand.ERROR_MESSAGES[2])
            case 2:  # update BaseModel id
                print(HBNBCommand.ERROR_MESSAGES[4])
            case 3:  # update BaseModel id attribute_name
                print(HBNBCommand.ERROR_MESSAGES[5])
            case 4:  # update BaseModel id attribute_name attribute_value
                try:
                    storage.update(*args)
                except custom_exceptions.GetClassException:
                    print(HBNBCommand.ERROR_MESSAGES[1])
                except custom_exceptions.GetInstanceException:
                    print(HBNBCommand.ERROR_MESSAGES[3])
            case _:
                pass


def arg_parse(line):
    """Splits the argument by a space"""
    tokens = split(line)
    return tokens, len(tokens)


# Check if this script is the main entry point for execution
if __name__ == "__main__":
    # Create an instance of the HBNBCommand class and start the command loop
    HBNBCommand().cmdloop()
