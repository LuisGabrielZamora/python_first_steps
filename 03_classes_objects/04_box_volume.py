"""
PRACTICE TITLE: Box Volume Class
DESCRIPTION: Allows to request base, height and width to user and returns the box volume
NOTATION:
NOTES:
"""


class BoxVolume:
    def __init__(self, base, height, width):
        self.base = base
        self.height = height
        self.width = width

    def box_volume(self):
        return self.base * self.height * self.width


""" Get values for base, height and width to calculate the box volume """
print('Hello, give us the variables to calculate box volume')
base = input('Give us base value: ')
base = int(base)
height = input('Give us height value: ')
height = int(height)
width = input('Give us width value: ')
width = int(width)

print('..... CALCULATING ......')
""" Generate new instance class to calculate rectangle area """
box = BoxVolume(base, height, width)

""" Print the result """
print(f'Rectangle area is: {box.box_volume()}')
