#!/usr/bin/python3
""" BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Rep the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Int BaseModel
            *args: Unused
            **kwargs(dict): Key/value pairs of attrb
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for c, v in kwargs.items():
                if c == "created_at" or c == "updated_at":
                    self.__dict__[c] = datetime.strptime(v, tform)
                else:
                    self.__dict__[c] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dict of BaseModel instance
        Includes key/value pair __class__
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """rtn the print/str rep of BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
