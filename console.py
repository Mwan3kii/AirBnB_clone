#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) ' 

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
