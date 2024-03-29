#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime

import models


class BaseModel:
    """A base model class.

    Attributes:
        id (str): A unique identifier for each instance, generated using uuid.
        created_at (datetime): The time the instance was created.
        updated_at (datetime): The time the instance was last updated.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initializes a new instance of the BaseModel class."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            # add the objects to storage
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ["created_at", "updated_at"]:
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)

    def __str__(self) -> str:
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts the instance's attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the instance's attributes.
        """
        dict_s = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_s[key] = value.isoformat()
            else:
                dict_s[key] = value

        dict_s["__class__"] = self.__class__.__name__
        return dict_s
