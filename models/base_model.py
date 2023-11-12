#!/usr/bin/python3
"""Base model for all common attributes/methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """Symbolizes the foundational model for the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Construct a new instance of BaseModel.

        Args:
            *args (any): Not utilized.
            **kwargs (dict): Dictionary of attribute key/value pairs.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    
    def __str__(self):
        """Generate the printable/string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """Refresh updated_at to the current datetime."""
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """Provide the BaseModel instance's dictionary.

        Contains the key/value pair __class__ indicating
        the object's class name.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
