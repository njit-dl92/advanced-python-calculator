from calculator.core import Calculator

def test_addition():
    calc = Calculator()
    assert calc.evaluate("2 + 2") == 4

def test_subtraction():
    calc = Calculator()
    assert calc.evaluate("5 - 2") == 3
