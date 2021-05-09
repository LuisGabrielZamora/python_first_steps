"""
PRACTICE TITLE: Area Calculate Class
DESCRIPTION: Allows to request base and height to user and returns the rectangle area
NOTATION:
NOTES:
"""


class AreaCalculate:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def rectangle_area(self):
        return self.base * self.height


""" Get values for base and height to calculate the rectangle area """
print('Hello, give us the variables to calculate rectangle area')
base = input('Give us base value: ')
base = int(base)
height = input('Give us height value: ')
height = int(height)

print('..... CALCULATING ......')
""" Generate new instance class to calculate rectangle area """
rectangle = AreaCalculate(base, height)
""" Print the result """
print(f'Rectangle area is: {rectangle.rectangle_area()}')
