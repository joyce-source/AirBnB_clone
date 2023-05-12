#!/usr/bin/python3
"""Defines a Module for the HBNBCommand"""

import cmd
import importlib
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    __class_names = ["BaseModel"]

    def default(self, line):
        print("defualt(%s)" % line)
        return cmd.Cmd.default(self, line)

    def do_greet(self, line):
        '''Pints a greet message
        '''
        print("Hello")

    def do_quit(self, line):
        """Quit: command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF: end-of-file mark the exits the program
        """
        "Exit"
        return True

    def emptyline(self):
        """Deals with the empty lines
        """
        pass

    def parseline(self, line):
        print('parseline(%s) =>' % line)
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (JSON file) & prints id
        Usage: create <class name>
        Ex: $ create BaseModel
        """
        args = line.split()
        
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.__class_names:
                print("** class doesn't exist **")
                print(class_name)
                print(self.__class_names)
            else:
                try:
                    module_name = BaseModel.__module__
                    module = importlib.import_module(module_name)
                    cls = getattr(module, class_name)
                except AttributeError:
                    print("** class doesn't exist **")
                    return

                new_obj = cls()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string rep. of an instance based on the class name & id.
        Usage: show <class name> <id>
        Ex: $ show BaseModel 1234-1234-1234.
        """
        pass

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: destroy <class name> <id>
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        pass

    def do_all(self, line):
        """
        Prints all string rep. of all instances based or not on the class name
        Usage: all <class name>
        Ex: $ all BaseModel or $ all.
        """
        pass

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
