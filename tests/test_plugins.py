import pytest
from plugins.cube import CubeCommand
from plugins.sqrt import SqrtCommand
from plugins.square import SquareCommand

def test_cube_command():
    command = CubeCommand()
    assert command.execute(2) == 8
    assert command.execute(-3) == -27

def test_sqrt_command():
    command = SqrtCommand()
    assert command.execute(4) == 2
    assert command.execute(9) == 3

def test_sqrt_negative():
    command = SqrtCommand()
    result = command.execute(-4)
    assert result == 2j

def test_square_command():
    command = SquareCommand()
    assert command.execute(2) == 4
    assert command.execute(5) == 25
