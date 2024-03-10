#!/usr/bin/python3

import json
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
