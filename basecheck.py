#!/usr/bin/python3
from models import storage
class_name = "BaseModel"
if class_name in storage.all().keys():
    print("BaseModel exists")
else:
    print("BaseModel does not exist")

