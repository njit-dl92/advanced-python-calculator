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
