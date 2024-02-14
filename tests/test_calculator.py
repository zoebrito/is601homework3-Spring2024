'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(3,3) == 6

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(4,4) == 0

def test_multiplication():
    '''Test that multiplication function works '''
    assert multiply(5,5) == 25

def test_division():
    '''Test that division function works '''
    assert divide(25,5) == 5