#!/usr/bin/python3

import json
from models import storage
from models.base_model import BaseModel
from os.path import exists

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ser_objs = {}
        for key, obj in self.__objects.items():
            ser_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(ser_objs, file)

    def reload(self):
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj_data in json.load(f).values():
                    class_name = obj_data["__class__"]
                    obj_class = globals()[class_name]
                    self.new(obj_class(**obj_data))
        except FileNotFoundError:
            return
