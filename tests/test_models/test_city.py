#!/usr/bin/python3
"""
Unittest module for the class City():
"""

import unittest
import os
import json
import re
import time
from datetime import datetime
from models import storage
from models.city import City
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """test case for the class City():"""

    def setUp(self):
        """sets up test data."""
        pass

    def tearDown(self):
        """resets FileStorage data to original state."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """resets FIleStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """tests instantiation of the clas City():"""
        cit = City()
        self.assertEqual(str(type(cit)), "<class 'models.city.City'>")
        self.assertIsInstance(cit, City)
        self.assertTrue(issubclass(type(cit), BaseModel))

    def test_8_attributes(self):
        """tests the attributes of the class City():"""
        attributes = storage.attributes()["City"]
        ci = City()
        for m, t in attributes.items():
            self.assertTrue(hasattr(ci, m))
            self.assertEqual(type(getattr(ci, m, None)), t)

if __name__ == "__main__":
    unittest.main()
