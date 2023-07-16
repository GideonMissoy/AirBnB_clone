#!/usr/bin/python3
"""
Unittest module for the class State():
"""

import unittest
import os
import json
import re
import time
from datetime import datetime
from models import storage
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """test cases for the classs State():"""

    def setUp(self):
        """sets up test data."""
        pass

    def tearDown(self):
        """resets FileStorage data to original state."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """tests instantiation of the class State():"""
        attributes = storage.attributes()["State"]
        sta = State()
        for m, t in attributes.items():
            self.assertTrue(hasattr(sta, m))
            self.assertEqual(type(getattr(sta, m, None)), t)

if __name__ == "__main__":
    unittest.main()
