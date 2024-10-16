import pytest
from main import main

def test_repl_add(monkeypatch, capsys):
    """Test the REPL with the 'add' command."""
    # Simulate user input
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the REPL
    main()

    # Capture the output
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out

def test_repl_subtract(monkeypatch, capsys):
    """Test the REPL with the 'subtract' command."""
    inputs = iter(["subtract 10 2", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Result: 8" in captured.out

def test_repl_multiply(monkeypatch, capsys):
    """Test the REPL with the 'multiply' command."""
    inputs = iter(["multiply 3 4", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Result: 12" in captured.out

def test_repl_divide(monkeypatch, capsys):
    """Test the REPL with the 'divide' command."""
    inputs = iter(["divide 9 3", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Result: 3" in captured.out

def test_repl_divide_by_zero(monkeypatch, capsys):
    """Test the divide command with a divisor of zero."""
    inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out

def test_repl_square(monkeypatch, capsys):
    """Test the REPL with the 'square' command."""
    inputs = iter(["square 4", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Result: 16" in captured.out

def test_repl_sqrt(monkeypatch, capsys):
    """Test the REPL with the 'sqrt' command."""
    inputs = iter(["sqrt 9", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Result: 3" in captured.out

def test_repl_invalid_command(monkeypatch, capsys):
    """Test the REPL with an invalid command."""
    inputs = iter(["invalid_command", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Unknown command" in captured.out

def test_repl_invalid_input(monkeypatch, capsys):
    """Test the REPL when non-numeric input is provided."""
    inputs = iter(["add a b", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "could not convert string to float: 'a'" in captured.out

def test_repl_missing_argument(monkeypatch, capsys):
    """Test the REPL with missing arguments for a command."""
    inputs = iter(["add 2", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "add requires 2 numbers" in captured.out

def test_repl_menu(monkeypatch, capsys):
    """Test the REPL with the 'menu' command."""
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
