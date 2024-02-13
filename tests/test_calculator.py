'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(3,3) == 6

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(4,4) == 0
