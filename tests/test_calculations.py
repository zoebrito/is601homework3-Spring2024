'''
Tests for calculations.py
'''

from calculator.calculations import Calculation

def test_calculations():
    '''tests for calculations class'''
    calc = Calculation(10, 5)
    assert calc.add() == 15
    assert calc.subtract() == 5
    assert calc.multiply() == 50
    assert calc.divide() == 2

if __name__ == "__main__":
    test_calculations()
