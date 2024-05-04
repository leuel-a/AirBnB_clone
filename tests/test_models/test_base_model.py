#!/usr/bin/python3
"""Defines the TestBaseModel class"""
import json
import unittest
from datetime import datetime

from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A unit test class for the BaseModel class.

    Attributes:
        test_base_model (BaseModel): An instance of the BaseModel
        class for testing.
    """

    def setUp(self) -> None:
        """Sets up the test environment before each test method
        is run."""
        self.test_base_model = BaseModel()

    def test_string_representation_of_instance(self):
        """Tests the string representation of the BaseModel
        instance."""
        class_name = self.test_base_model.__class__.__name__
        id = self.test_base_model.id
        dict_rep = self.test_base_model.__dict__

        expected_value = f"[{class_name}] ({id}) {dict_rep}"
        self.assertEqual(str(self.test_base_model), expected_value)

    def test_to_dict_method(self):
        """Test the to_dict method of the BaseModel class."""
        dict_s = self.test_base_model.to_dict()

        for key, value in self.test_base_model.__dict__.items():
            self.assertTrue(dict_s.get(key, None) is not None)

            if isinstance(value, datetime):
                self.assertEqual(dict_s[key], value.isoformat())

        self.assertTrue(dict_s.get("__class__", None) is not None)
        self.assertTrue(dict_s.get("__class__", None), "BaseModel")

    def test_new_base_model_added_to_storage(self):
        """Tests that a new BaseModel instance is added to
        the storage dictionary"""
        key = f"BaseModel.{self.test_base_model.id}"
        self.assertIn(key, storage.all())

    def test_save_base_model_to_storage(self):
        """Tests that a BaseModel instance is saved to storage
        when it is updated"""
        key = f"BaseModel.{self.test_base_model.id}"
        self.test_base_model.save()

        with open(storage._FileStorage__file_path, "r") as file:
            json_objects = json.load(file)
            self.assertTrue(json_objects.get(key, None) is not None)
            self.assertEqual(json_objects[key], self.test_base_model.to_dict())


if __name__ == "__main__":
    unittest.main()
