#!/usr/bin/python3
"""Defines the TestFileStorage class for unit testing the FileStorage class.
"""
import json
import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """A class used to test the FileStorage class.

    Attributes:
        prev_file_name (str): The previous file name of the FileStorage instance.
        prev_objects (dict): A copy of the previous objects of the FileStorage instance.
    """

    def setUp(self) -> None:
        """Set up the test environment before each test."""
        self.prev_file_name: str = FileStorage._FileStorage__file_path
        self.prev_objects: dict = FileStorage._FileStorage__objects.copy()
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self) -> None:
        """Clean up after each test."""
        FileStorage._FileStorage__file_path = self.prev_file_name
        FileStorage._FileStorage__objects = self.prev_objects.copy()

        if os.path.isfile("test.json"):
            os.remove("test.json")

    def test_all(self) -> None:
        """Test the all method of the FileStorage class."""
        # Check if the dictionary is empty before any new object is added
        self.assertDictEqual({}, storage.all())

        # Check if a new object creation is added to the _FileStorage__objects
        # dictionary
        test_model = BaseModel()
        key = f"BaseModel.{test_model.id}"
        self.assertTrue(storage.all().get(key, None) is not None)

    def test_new_object_creation_added_to_the_storage(self) -> None:
        """Test if a new object creation is added to the storage."""
        new_object = BaseModel()

        key = new_object.__class__.__name__ + "." + new_object.id
        expected_dict = {key: new_object}
        self.assertDictEqual(expected_dict, storage.all())

    def test_reload_method(self):
        """Test the reload method of the FileStorage class."""
        # Add a new object from storage
        storage.new(BaseModel())

        # Store the objects to the storage
        storage.save()
        prev_objects = storage.all()

        # Clear the _FileStorage__objects dictionary
        storage.all().clear()

        # Reload objects from the storage
        storage.reload()
        self.assertDictEqual(prev_objects, storage.all())


if __name__ == "__main__":
    unittest.main()
