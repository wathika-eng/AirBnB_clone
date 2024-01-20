#!/usr/bin/python3
"""BaseModel class for AirBnB clone"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Main class for AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class
        Args:
            - *args: arguments
            - **kwargs: arguments
            - self: self
        Return:
            A new ID for each new instance
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], format)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], format)
            del kwargs["__class__"]
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns the string representation of BaseModel to a JSON"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict = {}
        dict.update(self.__dict__)
        dict.update({"__class__": (str(type(self)).split(".")[-1].split("'")[0])})
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
