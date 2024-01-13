#!/usr/bin/python3
"""A shell made using python"""

import cmd


class HBNBCommand(cmd.Cmd):
    """A shell made using python"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def default(self, line):
        """If unknown command is called"""
        print("** class name missing **")

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
