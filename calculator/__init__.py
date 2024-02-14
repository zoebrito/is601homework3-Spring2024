"""
Calculator class that performs addition, subtraction, multiplication, and division
Uses static methods meaning it doesn't require an instance to be called
"""

from calculator.calculations import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(first_num, second_num):
        calculation = Calculation(first_num, second_num, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(first_num, second_num):
        calculation = Calculation(first_num, second_num, subtract)  # Pass the subtract function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply(first_num, second_num):
        calculation = Calculation(first_num, second_num, multiply)  # Pass the multiply function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(first_num, second_num):
        calculation = Calculation(first_num, second_num, divide)  # Pass the divide function from calculator.operations
        return calculation.get_result()
