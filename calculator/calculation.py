"""
This module provides the Calculation class to handle various mathematical operations.
"""

class Calculation:
    """A class to represent a mathematical operation."""

    def __init__(self, operation: str):
        """Initializes the Calculation with a specified operation."""
        self.operation = operation

    @classmethod
    def create(cls, operation: str):
        """Class method to create a new calculation."""
        return cls(operation)
