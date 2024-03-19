#!/usr/bin/python3
"""Console for the AirBnB clone project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd.
    It provides a command line interface for the AirBnB clone project.

    Attributes:
        prompt (str): The prompt string which is displayed before each command.
    """

    prompt = "(hbnb) "

    def do_EOF(self, line: str) -> bool:
        """
        Handles the EOF (End Of File) command which exits the program.

        Args:
            line (str): Not used in this method.

        Returns:
            bool: True indicating the program should exit.
        """
        return True

    def do_quit(self, line: str) -> bool:
        """
        Handles the quit command which exits the program.

        Args:
            line (str): Not used in this method.

        Returns:
            bool: True indicating the program should exit.
        """
        return True

    def emptyline(self) -> bool:
        """
        Handles the case when an empty line is entered in response to the prompt.

        Returns:
            bool: False indicating the program should not take any action on an empty input line.
        """
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
