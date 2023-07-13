#!/usr/bin/python3
"""FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        __file_path (str): name of file to save objects to.
        __objects (dict): a dict of objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """St in __objects: obj with key <obj_class_name>.id"""
        nam = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(nam, obj.id)] = obj

    def save(self):
        """Srlz __objects to JSON file __file_path"""
        jct = FileStorage.__objects
        bjdict = {obj: jct[obj].to_dict() for obj in jct.keys()}
        with open(FileStorage.__file_path, "w") as y:
            json.dump(bjdict, y)

    def reload(self):
        """Dsrlz the JSON file __file_path to __objects if it exists"""
        try:
            with open(FileStorage.__file_path) as y:
                bjdict = json.load(y)
                for b in bjdict.values():
                    cls_name = b["__class__"]
                    del b["__class__"]
                    self.new(eval(cls_name)(**b))
        except FileNotFoundError:
            return
