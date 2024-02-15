'''
Tests for operations.py
'''

from calculator.operations import Operations

def test_operations():
    ''' method to test operations'''
    assert Operations.add(3, 4) == 7
    assert Operations.subtract(5, 2) == 3
    assert Operations.multiply(2, 6) == 12
    assert Operations.divide(8, 4) == 2

if __name__ == "__main__":
    test_operations()
