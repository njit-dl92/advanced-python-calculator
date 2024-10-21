import sys
import os

# Add the path to the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from calculator.plugins.addition import add
from calculator.plugins.subtraction import subtract
from calculator.plugins.multiplication import multiply
from calculator.plugins.division import divide

def test_add_plugin():
    assert add(2, 3) == 5

def test_subtract_plugin():
    assert subtract(5, 3) == 2

def test_multiply_plugin():
    assert multiply(3, 4) == 12

def test_divide_plugin():
    assert divide(10, 2) == 5

def test_divide_by_zero_plugin():
    try:
        divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False  # This line should not be reached
