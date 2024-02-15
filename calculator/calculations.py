# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
'''
Constructor with self parameter for calculator class
'''
from operations import Operations

class Calculation:
    def __init__(self, first_num, second_num):
        # methods automatically converted by Python into MyClass.method(myobject, arg1, arg2)
        self.first_num = first_num
        self.second_num = second_num

def add(self):
        return Operations.add(self.first_num, self.second_num)

def subtract(self):
    return Operations.subtract(self.first_num, self.second_num)

def multiply(self):
    return Operations.multiply(self.first_num, self.second_num)

def divide(self):
    return Operations.divide(self.first_num, self.second_num)
