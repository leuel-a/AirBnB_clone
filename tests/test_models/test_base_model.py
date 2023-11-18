#!/usr/bin/python3
"""Tests for the BaseModel class"""
import unittest
from datetime import datetime

# project import statements
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines the unittests for the BaseModel class"""
    def setUp(self):
        """Setup method"""
        self.test_base = BaseModel()

    def test_id_is_string(self):
        """tests the id of an instance is actually a string type
        """
        self.assertIsInstance(self.test_base.id, str)

    def test_created_at_is_datetime(self):
        """Tests if the created_at is a datetime object when new object
        is created
        """
        self.assertIsInstance(self.test_base.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Tests if the updated_at is a datetime object when new object
        is created
        """
        self.assertIsInstance(self.test_base.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Tests if the save method updates the updated_at instance attribute
        """
        before = self.test_base.updated_at
        self.test_base.save()
        after = self.test_base.updated_at

        self.assertNotEqual(before, after)

    def test_to_dict_method(self):
        """Tests the to_dict method does what is intended"""
        dict_s = {}
        for key, val in self.test_base.__dict__.items():
            if isinstance(val, datetime):
                dict_s[key] = val.isoformat()
            else:
                dict_s[key] = val

        dict_s['__class__'] = 'BaseModel'
        self.assertDictEqual(dict_s, self.test_base.to_dict())


if __name__ == '__main__':
    unittest.main()
