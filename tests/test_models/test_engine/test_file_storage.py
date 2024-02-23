#!/usr/bin/python3
"""Defines the TestFileStorage class for unit testing the FileStorage class.
"""
import unittest

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class.

    This class defines several test methods to ensure the correct behavior of
    FileStorage functionalities, particularly the `all()` method.

    Attributes:
        mock_storage (FileStorage): A mock instance of FileStorage for testing.
        prev_file_name (str): The original file path of FileStorage before testing.
    """

    def setUp(self) -> None:
        """Sets up the test environment.

        Creates a mock instance of FileStorage and temporarily changes the
        _FileStorage__file_path attribute to "test.json" for testing purposes.
        """
        self.mock_storage = FileStorage()
        self.prev_file_name = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "test.json"

    def tearDown(self) -> None:
        """Restores the original test environment.

        Reverts the _FileStorage__file_path attribute back to its original value.
        """
        FileStorage._FileStorage__file_path = self.prev_file_name

    def test_all(self) -> None:
        """Tests the all() method of FileStorage.

        Verifies that the `all()` method of the FileStorage class returns
        the same dictionary as its internal `_FileStorage__objects` attribute.

        Raises:
            AssertionError: If the dictionaries returned by `all()` and
                `_FileStorage__objects` are not equal.
        """
        self.assertDictEqual(
            self.mock_storage._FileStorage__objects, self.mock_storage.all()
        )


if __name__ == "__main__":
    unittest.main()
