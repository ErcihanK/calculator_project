import cmath 

class SqrtCommand:
    """Command to calculate the square root of a number, including support for negative numbers."""
    
    def execute(self, x):
        return cmath.sqrt(x)
