#!/usr/bin/python3
"""
Unittest module for the class Place():
"""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Tests cases for the class Place."""

    def SetUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        self.resetStorage()
        pass

    def resetStorage(self):
        """resets storage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isFile(FileStorage._FileStorage__file_path):
            os.remove(FIleStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """tests instatiation of the class Place():"""

        p = Place()
        self.assertEqual(str(type(p)), "<class 'models.place.Place'>")
        self.assertIsInstance(p, Place)
        self.assertTrue(issubclass(type(p), BaseModel))

    def test_8_attributes(self):
        """tests the attributes of the class Place():"""
        attributes = storage.attributes()['Place']
        mtaa = Place()
        for m, t in attributes.items():
            self.assertTrue(hasattr(mtaa, m))
            self.assertEqual(type(getattr(mtaa, m, None)), t)

if __name__ == "__main__":
    unittest.main()
