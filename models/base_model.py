#!/usr/bin/python3
"""BaseModel class"""
from datetime import datetime
from uuid import uuid4

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
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates updated_at with current time"""
        
