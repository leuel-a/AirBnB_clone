#!/usr/bin/python3
"""Console for the AirBnB clone project"""
import cmd
from typing import List, Dict, Union

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
        tokens = HBNBCommand.parse_tokens(line)

        cls_name, *_ = tokens
        if not cls_name:
            print("** class name missing **")
            return False

        if cls_name not in classes:
            print("** class doesn't exist **")
            return False

        new_obj = classes[cls_name]()
        storage.save()
        print(new_obj.id)

    def do_show(self, line: str) -> bool:
        """Shows the string representation of an instance"""
        cls_name, ins_id, *_ = HBNBCommand.parse_tokens(line)

        if not cls_name:
            print("** class name missing **")
            return False

        if cls_name not in classes:
            print("** class doesn't exist **")
            return False

        if not ins_id:
            print("** instance id missing **")
            return False

        key = f"{cls_name}.{ins_id}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        print(storage.all()[key])

    def do_destroy(self, line: str) -> bool:
        """Deletes an instance based on the class name and id"""
        cls_name, ins_id, *_ = HBNBCommand.parse_tokens(line)

        if not cls_name:
            print("** class name missing **")
            return False

        if cls_name not in classes:
            print("** class doesn't exist **")
            return False

        if not ins_id:
            print("** instance id missing **")
            return False

        key = f"{cls_name}.{ins_id}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        del storage.all()[key]
        storage.save()

    def do_all(self, line: str) -> bool:
        """Gets all instances from storage"""
        cls_name, *_ = HBNBCommand.parse_tokens(line)
        if cls_name is not None and cls_name not in classes:
            print("** class doesn't exist **")
            return False

        items = []
        for key, value in storage.all().items():
            obj_class, _ = key.split(".")

            if cls_name is not None and cls_name != obj_class:
                continue

            items.append(str(value))
        print(items)

    def do_update(self, line: str) -> bool:
        cls_name, ins_id, attr_name, attr_value = HBNBCommand.parse_tokens(line)

        if not cls_name:
            print("** class name missing **")
            return False

        if cls_name not in classes:
            print("** class doesn't exist **")
            return False

        if not ins_id:
            print("** instance id missing **")
            return False

        key = f"{cls_name}.{ins_id}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        if not attr_name:
            print("** attribute name missing **")
            return False

        if not attr_value:
            print("** value missing **")
            return False

        if "." in attr_value:
            attr_value = float(attr_value)
        elif attr_value.isdigit():
            attr_value = int(attr_value)

        setattr(storage.all()[key], attr_name, attr_value)
        storage.save()

    @staticmethod
    def parse_tokens(input: str) -> List[Union[str, None]]:
        tokens = [None for _ in range(4)]
        token_idx = 0

        i = j = 0
        while i < len(input) and token_idx != 4:
            j = i + 1

            if input[i] == " ":
                i += 1
                continue

            if input[i] == '"':
                while j < len(input) and input[j] != '"':
                    j += 1

                if (j + 1 < len(input) and input[j + 1] == " ") or j == len(input) - 1:
                    tokens[token_idx] = input[i + 1 : j]
            else:
                while j < len(input) and input[j] != " ":
                    j += 1
                tokens[token_idx] = input[i:j]

            token_idx += 1
            i = j + 1
        return tokens


if __name__ == "__main__":
    HBNBCommand().cmdloop()
