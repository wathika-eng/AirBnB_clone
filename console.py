#!/usr/bin/python3
"""CMD console for AirBnB clone"""

import cmd
from models import base_model as BaseModel
import re
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        pass

    def do_show(self, line):
        pass

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

    def do_count(self, line):
        pass

    def default(self, line: str) -> None:
        return super().default(line)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_exit(self, line):
        """Exit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
