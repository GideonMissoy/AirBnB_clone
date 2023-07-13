#!/usr/bin/python3
"""BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Rep BaseModel of the HBnB proj"""

    def __init__(self, *args, **kwargs):
        """Init a  BaseModel.
           *args: Any unused.
           **kwargs: Key or value pairs of attrib (dict).
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for c, n in kwargs.items():
                if c == "created_at" or c == "updated_at":
                    self.__dict__[c] = datetime.strptime(n, tform)
                else:
                    self.__dict__[c] = n
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Rtn the dict of the BaseModel instance."""
        rtndict = self.__dict__.copy()
        rtndict["created_at"] = self.created_at.isoformat()
        rtndict["updated_at"] = self.updated_at.isoformat()
        rtndict["__class__"] = self.__class__.__name__
        return rtndict

    def __str__(self):
        """Rtn the print/str rep of the BaseModel"""
        clasname = self.__class__.__name__
        return "[{}] ({}) {}".format(clasname, self.id, self.__dict__)
