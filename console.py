#!/usr/bin/env python3
"""
Contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the console on EOF (Ctrl-D).
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line + ENTER.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()