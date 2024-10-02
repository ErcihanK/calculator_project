"""
This module provides configuration for pytest, including fixtures for generating fake data.
"""

import pytest
from faker import Faker
from calculator.calculator import Calculator

# Initialize Faker
fake = Faker()

def pytest_addoption(parser):
    """Adds an option to specify the number of fake records to generate."""
    parser.addoption(
        "--num_records",
        action="store",
        default=10,
        help="number of fake records to generate"
    )


@pytest.fixture
def num_records(request):
    """Fixture to get the number of records."""
    return int(request.config.getoption("--num_records"))

@pytest.fixture
def fake_data(record_count):  # Use a different name for the parameter
    """Generates fake test data for the calculator."""
    data = []
    for _ in range(record_count):  # Use the renamed variable here
        a = fake.random_number(digits=2, fix_len=False)
        b = fake.random_number(digits=2, fix_len=False)
        operation = fake.random_element(elements=("add", "subtract", "multiply", "divide"))
        if operation == "add":
            expected = Calculator.add(a, b)
        elif operation == "subtract":
            expected = Calculator.subtract(a, b)
        elif operation == "multiply":
            expected = Calculator.multiply(a, b)
        elif operation == "divide":
            expected = a / b if b != 0 else None
        else:
            expected = None
        data.append((a, b, operation, expected))
    return data


def pytest_generate_tests(metafunc):
    """Parametrize test cases with fake data."""
    if {"a", "b", "operation", "expected"} <= set(metafunc.fixturenames):
        # Use the fixture `fake_data` to parametrize the tests
        metafunc.parametrize("a, b, operation, expected", metafunc.config.getoption("fake_data"))
