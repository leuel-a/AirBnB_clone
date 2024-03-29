#!/usr/bin/python3
"""Console for the AirBnB clone project"""
import cmd

from models import storage
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd.
    It provides a command line interface for the AirBnB clone project.
    """

    prompt = "(hbnb) "

    def do_EOF(self, line: str) -> bool:
        """Handles the EOF (End Of File) command which exits the program."""
        return True

    def do_quit(self, line: str) -> bool:
        """Handles the quit command which exits the program."""
        return True

    def emptyline(self) -> bool:
        """Handles the case when an empty line is entered in response
        to the prompt."""
        return False

    def do_create(self, line: str) -> bool:
        """Creates a new instance"""
        input_class = line.split(" ")[0] if len(line) != 0 else None
        if input_class is None:
            print("** class name missing **")
            return False

        if input_class not in classes:
            print("** class doesn't exist **")
            return False

        new_obj = classes[input_class]()
        storage.save()
        print(new_obj.id)

    def do_show(self, line: str) -> bool:
        """Shows the string representation of an instance"""
        key = HBNBCommand.checkValidInput(line)
        if key == "":
            return False

        if key not in storage.all():
            print("** no instance found **")
            return False

        print(storage.all()[key])

    def do_destroy(self, line: str) -> bool:
        """Deletes an instance based on the class name and id"""
        key = HBNBCommand.checkValidInput(line)
        if key == "":
            return False

        del storage.all()[key]
        storage.save()

    def do_all(self, line: str) -> bool:
        """Gets all instances from storage"""
        items = [str(item) for item in storage.all().values()]

        input_class_name = line.split(" ")[0] if line else ""
        if input_class_name != "":
            if input_class_name not in classes:
                print("** class doesn't exist **")
                return False
            items = []
            for key, value in storage.all().items():
                class_name, _ = key.split(".")
                if class_name == input_class_name:
                    items.append(str(value))
        print(items)

    def do_update(self, line: str) -> bool:
        key = HBNBCommand.checkValidInput(line)
        if key == "":
            return False

        input_list = line.split(" ")[2:]
        if len(input_list) == 0:
            print("** attribute name missing **")
            return False

        if len(input_list) == 1:
            print("** value missing **")
            return False

        name, value = input_list[:2]

        value = value[1:-1]  # Remove the quotes
        if "." in value:
            value = float(value)
        elif value.isdigit():
            value = int(value)

        setattr(storage.all()[key], name, value)
        storage.save()

    @staticmethod
    def checkValidInput(line: str) -> str:
        input_list = line.split(" ") if len(line) != 0 else None

        if input_list is None:
            print("** class name missing **")
            return ""

        if input_list[0] not in classes:
            print("** class doesn't exist **")
            return ""

        if len(input_list) == 1:
            print("** insance id missing **")
            return ""

        input_class, input_instance_id = input_list[:2]
        key = f"{input_class}.{input_instance_id}"

        if key not in storage.all():
            print("** no instance found **")
            return ""
        return key


if __name__ == "__main__":
    HBNBCommand().cmdloop()
