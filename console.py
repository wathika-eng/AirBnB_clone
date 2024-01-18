#!/usr/bin/python3
"""A shell made using python"""

import cmd


class HBNBCommand(cmd.Cmd):
    """A shell made using python"""

    prompt = "(hbnb) "

    def __init__(self):
        """Init method"""
        super().__init__()
        self.users = {}

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit.isdigit():
                self.users[digit] = name
                print(f"{name} created as user {digit}")
            else:
                print("Only integers allowed\n Create <int> <str>")
        elif len(args) > 2:
            print("** too many arguments **")
        # else:
        #     print("** class name missing **")
        # if line:
        #     if line in self.users:
        #         print("** class already exists **")
        #     else:
        #         self.users[line] = []
        else:
            print("** class name missing **")

    def do_read(self, line):
        """Reads the string representation of an instance"""
        print("\t\tUsers available are: ")
        for digit, name in self.users.items():
            print(f"User ID: {digit}   \t username: {name}")

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

    def do_delete(self, line):
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
