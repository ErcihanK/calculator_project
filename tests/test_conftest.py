import pytest

def test_num_records_fixture(num_records):
    """Test the num_records fixture."""
    assert isinstance(num_records, int)
    assert num_records > 0

def test_fake_data(fake_data):
    """Test the fake_data fixture."""
    assert isinstance(fake_data, list)
    assert len(fake_data) > 0
    for record in fake_data:
        a, b, operation, expected = record
        assert isinstance(a, int)
        assert isinstance(b, int)
        assert operation in ("add", "subtract", "multiply", "divide")
        if operation == "divide" and b == 0:
            assert expected is None
        else:
            assert expected is not None

def test_pytest_addoption(pytestconfig):
    """Test the pytest_addoption functionality."""
    num_records = pytestconfig.getoption("num_records")
    assert isinstance(num_records, int)  # It should be an integer
    assert num_records > 0  # Ensure it's a positive number

