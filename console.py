#!/usr/bin/env python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
import re
from shlex import split


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [j.strip(",") for j in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for j in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [j.strip(",") for j in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

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

    def default(self, arg):
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        argline = parse(arg)
        if len(argline) == 0:
            print("** class name missing **")
        elif argline[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argline[0])().id)
            storage.save()

    def do_show(self, arg):
        argline = parse(arg)
        ser_objs = storage.all()
        if len(argline) == 0:
            print("** class name missing **")
        elif argline[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argline) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argline[0], argline[1]) not in ser_objs:
            print("** no instance found **")
        else:
            print(ser_objs["{}.{}".format(argline[0], argline[1])])

    def do_destroy(self, arg):
        argline = parse(arg)
        ser_objs = storage.all()
        if len(argline) == 0:
            print("** class name missing **")
        elif argline[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argline) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argline[0], argline[1]) not in ser_objs.keys():
            print("** no instance found **")
        else:
            del ser_objs["{}.{}".format(argline[0], argline[1])]
            storage.save()

    def do_all(self, arg):
        argline = parse(arg)
        if len(argline) > 0 and argline[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obl = []
            for ob in storage.all().values():
                if len(argline) > 0 and argline[0] == ob.__class__.__name__:
                    obl.append(ob.__str__())
                elif len(argline) == 0:
                    obl.append(ob.__str__())
            print(obl)

    def do_count(self, arg):
        argline = parse(arg)
        count = 0
        for ob in storage.all().values():
            if argline[0] == ob.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        argline = parse(arg)
        ser_objs = storage.all()
        if len(argline) == 0:
            print("** class name missing **")
            return False
        if argline[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argline) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argline[0], argline[1]) not in ser_objs.keys():
            print("** no instance found **")
            return False
        if len(argline) == 2:
            print("** attribute name missing **")
            return False
        if len(argline) == 3:
            try:
                type(eval(argline[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argline) == 4:
            ob = ser_objs["{}.{}".format(argline[0], argline[1])]
            if argline[2] in ob.__class__.__dict__.keys():
                valtype = type(ob.__class__.__dict__[argline[2]])
                ob.__dict__[argline[2]] = valtype(argline[3])
            else:
                ob.__dict__[argline[2]] = argline[3]
        elif type(eval(argline[2])) == dict:
            ob = ser_objs["{}.{}".format(argline[0], argline[1])]
            for key, value in eval(argline[2]).items():
                if (key in ob.__class__.__dict__.keys() and
                        type(ob.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(ob.__class__.__dict__[key])
                    ob.__dict__[key] = valtype(value)
                else:
                    ob.__dict__[key] = value
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
