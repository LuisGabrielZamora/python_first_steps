"""
PRACTICE TITLE: Arithmetic Class
DESCRIPTION: Allows to add two operators in a specific class method
NOTATION: Method: def new_method(self):
NOTES:
"""


class Arithmetic:
    """Initializer class or constructor in Python"""

    def __init__(self, operator_one, operator_two):
        self.operator_one = operator_one
        self.operator_two = operator_two

    """Method for add operators"""

    def add(self):
        return self.operator_one + self.operator_two


"""Create new object and get result for add method"""
newAdd = Arithmetic(2, 4)
print(f'Add result: {newAdd.add()}')
