#!/usr/bin/python3
"""Defines the TestFileStorage class for unit testing the FileStorage class.
"""
import json
import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


classes = {"BaseModel": BaseModel, "User": User}


class TestFileStorage(unittest.TestCase):
    """A class used to test the FileStorage class.

    Attributes:
        prev_file_name (str): The previous file name of the FileStorage
        instance.
        prev_objects (dict): A copy of the previous objects of the FileStorage
        instance.
    """

    def setUp(self) -> None:
        """Set up the test environment before each test."""
        self.prev_file_name = storage._FileStorage__file_path
        self.prev_objects = storage.all()

        storage._FileStorage__file_path = "test_file.json"
        storage._FileStorage__objects = {}

    def tearDown(self) -> None:
        """Clean up after each test."""
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")
        storage._FileStorage__file_path = self.prev_file_name
        storage._FileStorage__objects = self.prev_objects

    def test_all(self):
        """Test the all method."""
        # Write a test for the all method
        self.assertDictEqual(storage.all(), {})

        obj1 = BaseModel()
        obj2 = BaseModel()

        expected = {
            f"{obj1.__class__.__name__}.{obj1.id}": obj1,
            f"{obj2.__class__.__name__}.{obj2.id}": obj2,
        }

        self.assertDictEqual(storage.all(), expected)

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        expected_key = f"{obj.__class__.__name__}.{obj.id}"

        storage.new(obj)
        self.assertIn(expected_key, storage.all())

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        key = f"{obj.__class__.__name__}.{obj.id}"
        storage.save()

        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

        with open("test_file.json", "r") as file:
            json_obj = json.load(file)
            class_name = json_obj[key]["__class__"]

            obj_from_storage = classes[class_name](**json_obj[key])
            self.assertEqual(obj_from_storage.id, obj.id)
            self.assertEqual(obj_from_storage.created_at, obj.created_at)
            self.assertEqual(obj_from_storage.updated_at, obj.updated_at)

    def test_reload(self):
        """Test the reload method."""
        obj = BaseModel()
        key = f"{obj.__class__.__name__}.{obj.id}"
        storage.save()

        storage._FileStorage__objects = {}
        self.assertNotIn(key, storage.all())

        storage.reload()
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
