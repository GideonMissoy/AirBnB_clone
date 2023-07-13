#!/usr/bin/python3
"""
Tests the FileStorage(): class
"""

import unittest
import os.path
import json
from time import sleep
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class test_FileStorage(unittest.TestCase):
    """tests the class FileStorage():"""
    def test_file_path(self):
        """tests file path"""
        bm = BaseModel()
        bm.save()
        self.assertEquals(file, "file.json")
        os.remove("file.json")

    def test_objects(self):
        """tests objects."""
        FileStorage._FileStorage__object = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        model.save()
        self.assertEqual(type(objects), dict)
        os.remove("file.json")

    def test_all(self):
        """tests all"""
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        model.save()
        all_objs = storage.all()
        os.remove("file.json")

    def test_new(self):
        """tests for new file"""
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        FileStorage.new(FileStorage, model)
        self.assertNotEquals(objectts[f"{model.__class__.__name__}.{model.id}"], None)

    def test_reload(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        obj = objects.copy()
        model = BaseModel()
        FileStorage.reload(FileStorage)
        self.assertNotEqual(obj, objects)

    def test_save(self):
        """test save"""
        self.assertEqual(os.path.isfile("file.json"), False)
        model = BaseModel()
        FileStorage.save(FileStorage)
        self.assertEqual(os.path.isfile("file.json"), True)
        os.remove("file.json")
