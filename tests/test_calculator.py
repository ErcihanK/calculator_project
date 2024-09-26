import pytest
from calculator.calculator import Calculator

# Parameterized test for the add function
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected

# Parameterized test for the subtract function
@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (0, 0, 0), (-1, -1, 0)])
def test_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected

# Parameterized test for the multiply function
@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (0, 10, 0), (-1, 5, -5)])
def test_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected

# Parameterized test for the divide function
@pytest.mark.parametrize("a, b, expected", [(6, 2, 3), (10, 5, 2), (-6, -3, 2)])
def test_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)

def test_add_to_history():
    calc = Calculator()
    calc.add_to_history("2 + 2 = 4")
    assert "2 + 2 = 4" in Calculator.get_history()

def test_clear_history():
    calc = Calculator()
    calc.add_to_history("2 + 2 = 4")
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0
