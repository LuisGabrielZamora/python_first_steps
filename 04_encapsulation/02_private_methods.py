"""
PRACTICE TITLE: Encapsulation
DESCRIPTION: Disable or hide direct access to class properties and access and modify to properties by methods
NOTATION: self.__property = property
NOTES:
1. To encapsulation property, have to convert in private with double underscore (__)
2. Attributes definition:
        self.name = name -> public (always accessible)
        self._age = age -> protected (medium accessible)
        self.__phone = phone -> private (not accessible, just in the class)
3. Methods definition:
        def method(self) -> public (always accessible)
        def _method(self) -> protected (medium accessible)
        def __method(self) -> private (not accessible, just in the class)
"""


class People:
    """ Constructor or initialize class """

    def __init__(self, name, sur_name, last_name):
        """ Public property """
        self.name = name
        """ Protected property """
        self._sur_name = sur_name
        """ Private property """
        self.__last_name = last_name

    """ Public method """

    def public_method(self):
        self.__private_method()

    """ Private method """

    def __private_method(self):
        print(self.name)
        print(self._sur_name)
        print(self.__last_name)

    """ Get for _sur_name """

    @property
    def sur_name(self):
        return self._sur_name


""" Get object """
p = People('Juan', 'López', 'Pérez')
p.public_method()

print('')
print(p.name)
print(p.sur_name)
