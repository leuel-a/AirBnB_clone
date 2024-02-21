#!/usr/bin/python3
"""Defines the FileStorage class"""
import json

from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{str(type(obj))}.id"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dict_objects = {}

        for key, value in self.__objects.items():
            dict_objects[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(dict_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        with open(self.__file_path, "r") as file:
            dict_objects = json.load(file)

        for key, value in dict_objects.items():
            obj_class = value["__class__"]
            self.__objects[key] = classes[obj_class](value)
