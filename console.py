#!/usr/bin/python3
"""
Console module - Implements a
command-line interface
"""

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
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # Define a command to handle the End-of-File (EOF) input,
    # also quitting the program
    def do_EOF(self, arg):
        """Exits the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when the user press only enter"""
        pass

    # Create Command
    def do_create(self, line):
        """Create a new instance"""

        args, args_len = arg_parse(line)
        if args_len == 0:
            print(HBNBCommand.ERROR_MESSAGES[0])
        elif args_len == 1:
            try:
                print(args[0])
                cls = eval(args[0])
                instance = cls()
                print(instance.id)
                instance.save()
            except Exception as e:
                print(HBNBCommand.ERROR_MESSAGES[1])
        else:
            pass

    # Show command
    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args, args_len = arg_parse(line)
        if args_len == 0:
            print(HBNBCommand.ERROR_MESSAGES[0])
        elif args_len == 1:
            print(HBNBCommand.ERROR_MESSAGES[2])
        elif args_len == 2:
            try:
                instance = storage.get(*args)
                print(instance)
            except custom_exceptions.GetClassException:
                print(HBNBCommand.ERROR_MESSAGES[1])
            except custom_exceptions.GetInstanceException:
                print(HBNBCommand.ERROR_MESSAGES[3])
        else:
            pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args, args_len = arg_parse(line)
        if args_len == 0:
            print(HBNBCommand.ERROR_MESSAGES[0])
        elif args_len == 1:
            print(HBNBCommand.ERROR_MESSAGES[2])
        elif args_len == 2:
            try:
                storage.delete(*args)
            except custom_exceptions.GetClassException:
                print(HBNBCommand.ERROR_MESSAGES[1])
            except custom_exceptions.GetInstanceException:
                print(HBNBCommand.ERROR_MESSAGES[3])
        else:
            pass

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args, args_len = arg_parse(line)
        if args_len < 2:
            try:
                print(storage.print_all(*args))
            except custom_exceptions.GetClassException:
                print(HBNBCommand.ERROR_MESSAGES[1])

    def do_count(self, line):
        """Counts all objects in a given class"""
        args, args_len = arg_parse(line)
        if args_len < 2:
            try:
                print(storage.count(*args))
            except custom_exceptions.GetClassException:
                print(HBNBCommand.ERROR_MESSAGES[1])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args, args_len = arg_parse(line)
        if args_len == 0:  # update
            print(HBNBCommand.ERROR_MESSAGES[0])
        elif args_len == 1:  # update BaseModel
            print(HBNBCommand.ERROR_MESSAGES[2])
        elif args_len == 2:  # update BaseModel id
            print(HBNBCommand.ERROR_MESSAGES[4])
        elif args_len == 3:  # update BaseModel id attribute_name
            print(HBNBCommand.ERROR_MESSAGES[5])
        elif args_len == 4:  # update M id attribute_name attribute_value
            try:
                storage.update(*args)
            except custom_exceptions.GetClassException:
                print(HBNBCommand.ERROR_MESSAGES[1])
            except custom_exceptions.GetInstanceException:
                print(HBNBCommand.ERROR_MESSAGES[3])
        else:
            pass

    def precmd(self, line):
        """Before the command is executed"""
        line = line.strip()
        if "." in line and line.endswith(")"):
            line = parse_final_cmd(line)
        return cmd.Cmd.precmd(self, line)


def parse_final_cmd(line):
    """
    Parsed the final command
    if in the form
    <class name>.cmd() ...
    """
    # Remove unnecessary characters
    line = replace_all(line, "\"'", "")
    line = line.split(".")
    try:
        if "show" in line[1] or "destroy" in line[1]:
            command = line[1].split("(")
            command[1] = command[1].replace(")", "")
            line = "{} {} {}".format(command[0], line[0], command[1])
        elif "update" in line[1]:
            line[1] = line[1].split("(")
            line = [line[0], line[1][0], line[1][1]]
            line[2] = line[2].split(",")
            line = [
                line[0],
                line[1],
                line[2][0],
                line[2][1].strip(),
                replace_all(line[2][2], ")", "").strip(),
            ]
        else:
            line[1] = replace_all(line[1], "()", "")
    except (IndexError, ValueError):
        pass

    if line[1] in ["all", "count", "create"]:
        line = "{} {}".format(line[1], line[0])
    elif line[1] == "update":
        line = "{} {} {} {} {}".format(
            line[1], line[0], line[2], line[3], line[4])
    return "".join(line)


def arg_parse(line):
    """Splits the argument by a space"""
    tokens = split(line)
    return tokens, len(tokens)


def replace_all(s, pattern, value):
    """
    Replace all occurrences of characters in the pattern
    with the specified value in the given string.

    Parameters:
    - s (str): The input string.
    - pattern (str): The set of characters to be replaced.
    - value (str): The value to replace the matching characters with.

    Returns:
    - str: The modified string.
    """
    # Using a dictionary to map each character in pattern
    # to the replacement value
    replacement_dict = {char: value for char in pattern}

    # Using str.translate to replace characters
    translation_table = str.maketrans(replacement_dict)

    # Applying the translation and returning the result
    result = s.translate(translation_table)
    return result


if __name__ == "__main__":
    HBNBCommand().cmdloop()
