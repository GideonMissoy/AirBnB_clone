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
