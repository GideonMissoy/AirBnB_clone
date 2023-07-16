#!/usr/bin/python3
"""
Unittest module for the class User():
"""

import os
import unittest
import json
import re
import time
from datetime import datetime
from models.user import User
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """tests cases for the class User():"""

    def setUp(self):
        """sets up test data."""
        pass

    def tearDown(self):
        """resets FileStorage data to original state."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FIleStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """tests instantiation of the class User."""
        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")
        self.assertIsInstance(u, User)
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_8_attributes(self):
        """tests the attributes of the class User():"""
        attributes = storage.attibutes()["User"]
        newuser = User()
        for m, t in attributes.items():
            self.assertTrue(hasattr(newuser, t))
            self.assertEquall(type(getattr(newuser, t, None)), t

if __name__ == "__main__":
    unittest.main()
