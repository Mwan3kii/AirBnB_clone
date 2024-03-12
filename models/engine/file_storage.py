#!/usr/bin/python3

import json
import os
import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        objcname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcname, obj.id)] = obj

    def save(self):
        obdict = FileStorage.__objects
        ser_objs = {obj: obdict[obj].to_dict() for obj in obdict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(ser_objs, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                ser_objs = json.load(file)
                for ob in ser_objs.values():
                    class_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_name)(**ob))
        except FileNotFoundError:
            return
