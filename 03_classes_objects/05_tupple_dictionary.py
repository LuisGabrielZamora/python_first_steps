"""
PRACTICE TITLE: Tupple Dictionary and Classes Management
DESCRIPTION: Forms to send data types to class in arguments
NOTATION:
NOTES:
"""


class TuppleDictionary:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        self.args = args
        self.kwargs = kwargs

    def print_data(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Tuple: {self.args}')
        print(f'Dictionary: {self.kwargs}')


""" First object without tuple and dictionary """
noTupleAndDictionary = TuppleDictionary('Mateo', 20)
noTupleAndDictionary.print_data()
print('')

""" Second object without dictionary """
noDictionary = TuppleDictionary('Javier', 31, 2, 3, 4)
noDictionary.print_data()
print('')

""" Third complete object """
completeObject = TuppleDictionary('Paula', 20, 8, 9, ML='Machine Learning', DS='Data Science')
completeObject.print_data()
