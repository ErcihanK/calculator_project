"""
This module provides basic arithmetic operations:
addition, subtraction, multiplication, and division.
"""

class Calculator:
    """
    Calculator class with static methods for arithmetic operations
    and class methods for managing history.
    """

    history = []

    @staticmethod
    def add(first_number: float, second_number: float) -> float:
        """Return the sum of two numbers."""
        return first_number + second_number

    @staticmethod
    def subtract(first_number: float, second_number: float) -> float:
        """Return the difference between two numbers."""
        return first_number - second_number

    @staticmethod
    def multiply(first_number: float, second_number: float) -> float:
        """Return the product of two numbers."""
        return first_number * second_number

    @staticmethod
    def divide(first_number: float, second_number: float) -> float:
        """
        Return the division of two numbers.
        Raises an error on division by zero.
        """
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number

    @classmethod
    def add_to_history(cls, calculation):
        """Add a calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        """Return the history of all calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the calculation history."""
        cls.history.clear()
