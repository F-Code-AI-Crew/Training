import pytest
from exception_handling import process_and_divide

def test_valid_case():
    assert process_and_divide(["10", "abc"], 0, 2) == "Result: 5.0"

def test_index_error():
    assert process_and_divide(["10"], 5, 2) == "Error: Index out of range!"

def test_value_error():
    assert process_and_divide(["10", "abc"], 1, 2) == "Error: 'abc' cannot be parsed into number!"

def test_zero_division():
    assert process_and_divide(["30"], 0, 0) == "Error: Cannot divide by 0!"

# run:
# pytest pytest_demo.py
