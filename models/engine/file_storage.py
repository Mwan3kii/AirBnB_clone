#!/usr/bin/python3

import json
import os
import datetime

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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, instance_id = key.split('.')
                    cls = globals().get(class_name, None)
                    if cls:
                        obj = cls(**obj_data)
                        self.__objects[key] = obj
