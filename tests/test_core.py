import sys
import os

# Add the path to the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from calculator.core import Calculator

def test_addition():
    calc = Calculator()
    assert calc.evaluate("2 + 2") == 4

def test_subtraction():
    calc = Calculator()
    assert calc.evaluate("5 - 2") == 3

def test_multiplication():
    calc = Calculator()
    assert calc.evaluate("3 * 4") == 12

def test_division():
    calc = Calculator()
    assert calc.evaluate("10 / 2") == 5

def test_division_by_zero():
    calc = Calculator()
    try:
        calc.evaluate("10 / 0")
    except ZeroDivisionError as e:
        assert str(e) == "Division by zero is not allowed."  # Optionally check the message
    else:
        assert False, "Expected ZeroDivisionError not raised" 

