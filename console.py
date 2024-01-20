#!/usr/bin/python3
"""CMD console for AirBnB clone"""

import cmd
import os
from models import base_model as BaseModel
import re
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def default(self, line: str):
        """Catch commands"""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search("^({.*})$", attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict
            )
            if match_attr_and_value:
                attr_and_value = (
                    (match_attr_and_value.group(1) or "")
                    + " "
                    + (match_attr_and_value.group(2) or "")
                )
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, dict_str):
        """Update() with a dictionary"""
        stri = stri_dict.replace("'", '"')
        dic = json.loads(stri)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif not uid:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in dic.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_create(self, line):
        """Creates a new instance of BaseModel,"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = storage.classes()[line]()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints __str__ rep"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if line != "":
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            else:
                all = [
                    str(obj)
                    for key, obj in storage.all().items()
                    if type(obj).__name__ == args[0]
                ]
                print(all)
        else:
            new = [str(obj) for key, obj in storage.all().items()]
            print(new)

    def do_update(self, line):
        """Updating an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        searcher = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        matching = re.search(searcher, line)
        classname = matching.group(1)
        uid = matching.group(2)
        attribute = matching.group(3)
        value = matching.group(4)
        if not matching:
            print("** class name missing **")
            return
        elif classname not in storage.classes():
            print("** class doesn't exist **")
            return
        elif uid is None:
            print("** instance id missing **")
            return
        else:
            k = "{}.{}".format(classname, uid)
            if k not in storage.all():
                print("** no instance found **")
                return
            elif attribute is None:
                print("** attribute name missing **")
                return
            elif value is None:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if "." in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', "")
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        # Let it remain a string
                        pass
                setattr(storage.all()[k], attribute, value)
                storage.all()[k].save()

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        args = line.split(" ")
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            all = [
                str(obj)
                for key, obj in storage.all().items()
                if type(obj).__name__ == args[0]
            ]
            print(len(all))

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
