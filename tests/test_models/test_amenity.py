#!/usr/bin/python3
"""
Unittest module for the class Amenity():
"""

import unittest
import os
import json
import re
import time
from datetime import datetime
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """tests cases for the class Amenity():"""

    def setUp(self):
        """sets up test data."""
        pass

    def tearDown(self):
        """resets Filestorage data to original state."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """tests instantiation of the class Amenity():"""
        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_8_attributes(self):
        """tests the attributes of the class Amenity():"""
        attributes = storage.attributes()["Amenity"]
        newamen = Amenity()
        for m, t in attributes.items():
            self.assertTrue(hasattr(newamen, m))
            self.assertEqual(type(getattr(newamen, m, None)), t)

if __name__ == "__main__":
    unittest.main()
