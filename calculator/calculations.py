'''
Constructor with self parameter for calculator class
'''

class Calculation:
    def __init__(self, first_num, second_num, operation):
        self.first_num = first_num
        self.second_num = second_num
        self.operation = operation  # Store the operation function

    def get_result(self):
        # Call the stored operation with first_num and second_num
        return self.operation(self.first_num, self.second_num)