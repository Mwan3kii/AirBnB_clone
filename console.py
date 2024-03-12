#!/usr/bin/env python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def help_quit(self):
        """Help message when quit command it executed"""
        print("Quit command to exit the program\n")
        return

    def emptyline(self):
        """Doesnt execute anything when entered"""
        pass

    def do_create(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.all():
            print("** class doesn't exist **")
            return
        object = storage.all()[class_name]()
        object.save()
        print(object.id)

    def do_show(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        args = line.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        class_name = args[0]
        if class_name not in [cls.__name__ for cls in storage.all().values()]:
            print("** class doesn't exist **")
            return
        for obj in storage.all().values():
            if class_name == obj.__class__.__name__:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
