#!/usr/bin/python3
"""
This program creates a simple command
line interpreter
"""
import cmd
import re
import shlex
from models.base_model3 import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    a simple command line processor
    """
    prompt = "(hbnb) "
    auth_class = ["BaseModel"]

    def do_create(self, arg):
        """
        creates an instance of BaseModel saved to JSON file.
        """
        command_line = shlex.split(arg)
        if len(command_line) == 0:
            print("** class name missing **")
        elif command_line[0] not in self.auth_class:
            print("** class dosent't exist **")
        else:
            auth_instance = BaseModel()
            auth_instance.save()
            print(auth_instance.id)

    def do_show(self, arg):
        """
            show string representation of the instance
            Usage: Show <class_name><id>
        """
        command_line = shlex.split(arg)
        if len(command_line) == 0:
            print("** class name missing **")
        elif command_line[0] not in self.auth_class:
            print("** class dosen't exist**")
        elif len(command_line) < 2:
            print("** instance id missing **")
        else:
            objt = storage.all()
            key = "{}.{}".format(command_line[0], command_line[1])
            if key in objt:
                print(objt[key])
            else:
                print("** no instance found **")
    
    def do_all(self, arg):
        """
            Print string representation of all instance
            Usage: all[class_name]
        """
        objt = storage.all()
        command_line = shlex.split(arg)
        if len(command_line) == 0:
            for key, value in objt.items():
                print(str(value))
        elif command_line[0] not in self.auth_class:
            print("** class doesn't exist **")
        else:
            for key, value in objt.items():
                if key.split('.')[0] == command_line[0]:
                    print(str(value))

    def do_destroy(self, arg):
        """
        Delete an instance
        Usage: destroy <class_name>
        """
        command_line = shlex.split(arg)

        if len(command_line) == 0:
            print("** class name missing **")
        elif command_line[0] not in self.auth_class:
            print("** class dosen't exist **")
        elif len(command_line) < 2:
            print("**instance id  missing **")
        else:
            objt = storage.all()
            key = "{}.{}".format(command_line[0], command_line[1]) 
            if key in objt:
                del objt[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """
             Updates an instance based on the class name and id by adding or updating attribute
             Usage: <class_name> <attribute_name> "<attribute_value>"
        """
        command_line = shlex.split(arg)
        if len(command_line) == 0:
            print(" **class name is missing **")
        elif command_line[0] not in self.auth_class:
            print("** class dosen't exit **")
        elif len(command_line) < 2:
            print("** instance id missing **")
        else:
            objt = storage.all()
            key = "{}.{}".format(command_line[0], command_line[1])
            if key not in objt:
                print("** no instance found **")
            elif len(command_line) < 3:
                print("** attribute name missing **")
            elif len(command_line) < 4:
                print("** value missing **")
            else:
                skip_braces = re.search(r"\{(.*?)\}", arg)
                objects =  objt[key]
                if skip_braces:
                    try:
                        data_string = skip_braces.group(1)
                        attribute_dict = ast.literal_eval("{" + data_string + "}")
                        att_names1 = list(attribute_dict.keys())
                        att_values1 = list(attribute_dict.values())
                        try:
                            at_name1 = att_names1[0]
                            at_values = att_values1[0]
                            setattr(objects, att_names1, att_values1)
                        except Exception:
                            pass
                        try:
                            at_name2 = att_names1[1]
                            at_value2 = att_values1[1]
                            setattr(object, at_name2, at_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:
                    at_name = command_line[2]
                    at_value = command_line[3]
                    try:
                        at_value = eval(at_value)
                    except Exception:
                        pass
                    setattr(objects, at_name, at_value)

                objects.save()

    def do_quit(self, arg):
        """
          method to quite the command line
        """
        return True

    def help_quit(self, arg):
        """
        prints an instruction to the user to quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        method when we reach end of line
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
