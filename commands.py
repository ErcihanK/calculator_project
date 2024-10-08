# commands.py

class Command:
    """Base class for commands."""
    def execute(self, x, y):
        raise NotImplementedError("You should implement this method in subclasses")


class AddCommand(Command):
    def execute(self, x, y):
        return x + y


class SubtractCommand(Command):
    def execute(self, x, y):
        return x - y


class MultiplyCommand(Command):
    def execute(self, x, y):
        return x * y


class DivideCommand(Command):
    def execute(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y


class MenuCommand:
    """Displays the available commands."""
    def execute(self, commands):
        print("Available commands:")
        for command in commands:
            print(command)
