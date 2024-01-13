#!/usr/bin/python3
"""BaseModel class"""
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """
        Constructor of BaseModel class
        Args:
            *args: Unused
            **kwargs: Key/value pairs of attributes
        Raises:
            TypeError: If kwargs are not given in correct format
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """The string representation of BaseModel"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
