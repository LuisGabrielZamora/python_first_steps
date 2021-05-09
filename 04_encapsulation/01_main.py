"""
PRACTICE TITLE: Encapsulation
DESCRIPTION: Disable or hide direct access to class properties and access and modify to properties by methods
NOTATION: self.__property = property
NOTES:
1. To encapsulation property, have to convert in private with double underscore (__)
"""


class NewPeople:
    def __init__(self, name):
        """ Define private property with double underscore """
        self.__name = name

    """ Use get to returns the value in the class """
    def get_name(self):
        return self.__name

    """ Use set to define new value in the class """
    def set_name(self, name):
        self.__name = name


""" Uses and call getters and setters """
p1 = NewPeople('Juan')
print(p1.get_name())

p2 = NewPeople('Karla')
print('People 1: ' + p2.get_name())

p2.set_name('Carlos')
print('People 2: ' + p2.get_name())
