#!/usr/bin/python3
"""
Unittest module for the class Review():
"""

import unittest
import os
import re
import json
import time
from datetime import datetime
from models.review import Review
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """test cases for the class Review():"""

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
        """tests instantiation of the class Review():"""
        r = Review()
        self.assertEqual(str(type(r)), "<class 'models.review.Review'>")
        self.assertIsInstance(r, Review)
        self.assertTrue(issubclass(type(r), BaseModel))

    def test_8_attributes(self):
        """tests the attributes of the class Review():"""
        attributes = storage.attributes()["Review"]
        rev = Review()
        for m, t in attributes.items():
            self.assertTrue(hasattr(rev, m))
            self.assertEqual(type(getattr(rev, m, None)), t)

if __name__ == "__main__":
    unittest.main()
