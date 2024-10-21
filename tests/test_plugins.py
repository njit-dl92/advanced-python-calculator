from calculator.plugins.addition import add
from calculator.plugins.subtraction import subtract

def test_add_plugin():
    assert add(2, 3) == 5

def test_subtract_plugin():
    assert subtract(5, 3) == 2
