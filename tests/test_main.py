import pytest
import logging
from main import main

def test_repl_add(monkeypatch, caplog):
    """Test the REPL with the 'add' command."""
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Result: 5" in caplog.text

def test_repl_subtract(monkeypatch, caplog):
    """Test the REPL with the 'subtract' command."""
    inputs = iter(["subtract 10 2", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Result: 8" in caplog.text

def test_repl_multiply(monkeypatch, caplog):
    """Test the REPL with the 'multiply' command."""
    inputs = iter(["multiply 3 4", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Result: 12" in caplog.text

def test_repl_divide(monkeypatch, caplog):
    """Test the REPL with the 'divide' command."""
    inputs = iter(["divide 9 3", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Result: 3" in caplog.text

def test_repl_divide_by_zero(monkeypatch, caplog):
    """Test the divide command with a divisor of zero."""
    inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Cannot divide by zero" in caplog.text

def test_repl_square(monkeypatch, caplog):
    """Test the REPL with the 'square' command."""
    inputs = iter(["square 4", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Result: 16" in caplog.text

def test_repl_sqrt(monkeypatch, caplog):
    """Test the REPL with the 'sqrt' command."""
    inputs = iter(["sqrt 9", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Result: 3" in caplog.text

def test_repl_invalid_command(monkeypatch, caplog):
    """Test the REPL with an invalid command."""
    inputs = iter(["invalid_command", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "Unknown command" in caplog.text

def test_repl_invalid_input(monkeypatch, caplog):
    """Test the REPL when non-numeric input is provided."""
    inputs = iter(["add a b", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "could not convert string to float: 'a'" in caplog.text

def test_repl_missing_argument(monkeypatch, caplog):
    """Test the REPL with missing arguments for a command."""
    inputs = iter(["add 2", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "add requires 2 numbers" in caplog.text

def test_repl_menu(monkeypatch, caplog):
    """Test the REPL with the 'menu' command."""
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with caplog.at_level(logging.INFO):
        main()

    assert "add" in caplog.text
    assert "subtract" in caplog.text
    assert "multiply" in caplog.text
    assert "divide" in caplog.text
