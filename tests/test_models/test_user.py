#!/usr/bin/python3
"""Unittests for the User model class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """A unit test class for the User class."""

    def setUp(self):
        self.test_user_model = User()

    def test_string_representation_of_instance(self):
        """Tests the string representation of the User instance."""
        class_name = self.test_user_model.__class__.__name__
        id = self.test_user_model.id
        dict_rep = self.test_user_model.__dict__

        expected_value = f"[{class_name}] ({id}) {dict_rep}"
        self.assertEqual(str(self.test_user_model), expected_value)


if __name__ == "__main__":
    unittest.main()
