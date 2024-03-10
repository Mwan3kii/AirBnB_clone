#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""

        print()
        return True

    def help_quit(self):
        """Help message when quit command it executed"""
        print("Quit command to exit the program\n")
        return

    def emptyline(self):
        """Doesnt execute anything when entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
