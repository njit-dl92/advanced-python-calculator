import sys
import os

# Add the path to the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from calculator.plugins.addition import add
from calculator.plugins.subtraction import subtract

def test_add_plugin():
    assert add(2, 3) == 5

def test_subtract_plugin():
    assert subtract(5, 3) == 2
