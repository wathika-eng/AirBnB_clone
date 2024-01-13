#!/usr/bin/python3
""" FileSys.py - File System Module"""
 import BaseModel from models.base_model

 class FileStorage:
     """ File Storage Class """
     __file_path = "file.json"
     __objects = {}

     def all(self):
         """ Returns the dictionary """
         return self.__objects

     def new(self, obj):
         """ Sets in __objects the obj with key <obj class name>.id """
         key = "{}.{}".format(obj.__class__.__name__, obj.id)
         self.__objects[key] = obj

     def save(self):
         """ Serializes __objects to the JSON file (path: __file_path) """
         with open(self.__file_path, mode='w', encoding='utf-8') as f:
             json.dump(self.__objects, f)

     def reload(self):
         """ Deserializes the JSON file to __objects """
         try:
             with open(self.__file_path, mode='r', encoding='utf-8') as f:
                 self.__objects = json.load(f)
         except FileNotFoundError:
             pass
