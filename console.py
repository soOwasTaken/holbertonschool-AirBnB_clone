#!/usr/bin/python3
"""This module contains a command line interpreter for HBNB project"""
import cmd
import shlex
import models

class HBNBCommand(cmd.Cmd):
    """Class for HBNB console"""

    prompt = '(hbnb) '
    classes = ['BaseModel']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file command to exit the program"""
        print('')
        return True

    def emptyline(self):
        """Do nothing when user input is empty"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            class_name = args[0]
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == class_name])

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            class_name = args[0]
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == class_name])

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        arg_list = shlex.split(line)
        class_name = arg_list[0]
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_key = class_name + "." + arg_list[1]
        all_objs = models.storage.all()
        if obj_key not in all_objs:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        instance = all_objs[obj_key]
        setattr(instance, arg_list[2], arg_list[3])
        instance.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        args = shlex.split(line)
        class_name = args[0]
        method = args[1] + "_" + class_name
        if method in self.methods:
            self.methods[method](args[1])
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in models.storage.all().values():
            if obj.__class__.__name__ == args[0]:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()