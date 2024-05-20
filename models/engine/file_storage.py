#!/usr/bin/python3

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        """
        object_name = obj.__class__.__name__
        serialize_obj = obj.to_dict()
        key = f"{object_name}.{obj.id}"
        FileStorage.__objects[key] = serialize_obj

    def all(self):
        """
        """
        return FileStorage.__objects

    def save(self):
        """
            An empty dictionary to hold our objects
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f4:
            json.dump(FileStorage.__objects, f4)

    def reload(self):
        """
        """
        if os.path.isfile(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) > 0:
                with open(self.__file_path, "r", encoding="utf-8") as f2:
                    FileStorage.__objects = json.load(f2)
            else:
                FileStorage.__objects = {}
        else:
            open(self.__file_path, "r", encoding="utf-8").close()
            FileStorage.__objects = {}
