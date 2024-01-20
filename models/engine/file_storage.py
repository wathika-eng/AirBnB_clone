#!/usr/bin/python3

"""File storage class for AirBnB clone"""
import datetime
import json
import models
import os


class FileStorage:
    """File storage class for AirBnB clone"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dump = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dump, f)

    def classes(self):
        """Returns a dictionary of valid classes"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {
                k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()
            }
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns a dictionary of valid attributes"""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime,
            },
        }
