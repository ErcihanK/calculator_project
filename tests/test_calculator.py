"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator

# Parameterized test for the add function
@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
def test_add(num1, num2, expected):
    """Test the addition operation."""
    assert Calculator.add(num1, num2) == expected

# Parameterized test for the subtract function
@pytest.mark.parametrize("num1, num2, expected", [(5, 3, 2), (0, 0, 0), (-1, -1, 0)])
def test_subtract(num1, num2, expected):
    """Test the subtraction operation."""
    assert Calculator.subtract(num1, num2) == expected

# Parameterized test for the multiply function
@pytest.mark.parametrize("num1, num2, expected", [(2, 3, 6), (0, 10, 0), (-1, 5, -5)])
def test_multiply(num1, num2, expected):
    """Test the multiplication operation."""
    assert Calculator.multiply(num1, num2) == expected

# Parameterized test for the divide function
@pytest.mark.parametrize("num1, num2, expected", [(6, 2, 3), (10, 5, 2), (-6, -3, 2)])
def test_divide(num1, num2, expected):
    """Test the division operation."""
    assert Calculator.divide(num1, num2) == expected

def test_divide_by_zero():
    """Test division by zero to raise an exception."""
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)

def test_add_to_history():
    """Test adding a calculation to the history."""
    calc = Calculator()
    calc.add_to_history("2 + 2 = 4")
    assert "2 + 2 = 4" in Calculator.get_history()

def test_clear_history():
    """Test clearing the calculator's history."""
    calc = Calculator()
    calc.add_to_history("2 + 2 = 4")
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0
