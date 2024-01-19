#!/usr/bin/python3
"""A shell made using python"""

import sys
import os

from models.base_model import BaseModel
import models
import cmd


class HBNBCommand(cmd.Cmd):
    """A shell made using python"""

    prompt = "(hbnb) "

    def __init__(self):
        """Init method"""
        super().__init__()
        self.users = {}

    # creating a new user
    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in models.storage.classes:
            print("** class doesn't exist **")
        else:
            new = models.storage.classes()[line]()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Reads the string representation of an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in models.storage.classes:
            print("** class doesn't exist **")
        elif line.split()[0] == "":
            print("** instance id missing **")
        elif line.split()[0] not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[line.split()[0]])

    def do_update(self, line):
        """Update Users"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit in self.users:
                self.users[digit] = name
                print(f"User updated to {digit} {name}")
            else:
                print(f"No user found with the ID {digit}")
        else:
            print(f"Invalid, use the create command")

    def do_destroy(self, line):
        """Delete a User"""
        if line in self.users:
            del self.users[line]
            print(f"Deleted user at ID {line}")
        else:
            print(f"No user found at ID {line}")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    # def default(self, line):
    #     """If unknown command is called"""
    #     print("** class name missing **")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_help(self, line):
        """Help command to show the help message"""
        cmd.Cmd.do_help(self, line)

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
