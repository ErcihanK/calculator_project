from calculator.calculation import Calculation

def test_calculation_create():
    """Test the creation of a Calculation instance."""
    calculation = Calculation.create("2 + 2")
    assert calculation.operation == "2 + 2"

def test_calculation_init():
    """Test the initialization of a Calculation instance."""
    calculation = Calculation("3 * 3")
    assert calculation.operation == "3 * 3"
