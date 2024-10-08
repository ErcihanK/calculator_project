import pytest
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    command = AddCommand()
    assert command.execute(2, 3) == 5
    assert command.execute(-1, -1) == -2

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(5, 3) == 2
    assert command.execute(3, 5) == -2

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(2, 3) == 6
    assert command.execute(0, 10) == 0

def test_divide_command():
    command = DivideCommand()
    assert command.execute(10, 2) == 5
    assert command.execute(9, 3) == 3

def test_divide_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        command.execute(10, 0)
