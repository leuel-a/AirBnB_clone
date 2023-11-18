#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class definition"""
    def __init__(self):
        """__init__ constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns the string representation of an object"""
        cls_name = self.__class__.__name__
        return f'[{cls_name}] ({self.id}) {self.__dict__}'

    def save(self) -> None:
        """Saves changes of the current object to storage"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of an object"""
        result = {}
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                result[key] = val.isoformat()
            else:
                result[key] = val
        class_name = self.__class__.__name__
        result['__class__'] = class_name
        return result
