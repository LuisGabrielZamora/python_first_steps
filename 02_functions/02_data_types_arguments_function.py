# PRACTICE TITLE: Function Definition Request Dictionary Arguments
# DESCRIPTION: Code structure that enable to execute an specific process and request dictionary arguments
# NOTATION: def my_first_function(**kwargs):
# NOTATION FOR MULTIPLE ARGUMENTS: def multiple_list_terms(type, *args, **kwargs)
# NOTES:
# 1. All the code that corresponds to the function has to be with tabulation
# 2. To execute the function we have to call it with the same "def" tabulation
# 3. For receive a dictionary have to define (**kwargs) in function arguments

# Definition function that receives a dictionary
def list_terms(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')


# Function which receive multiple arguments or data types
def multiple_types(args):
    for arg in args:
        print(arg)


# Call function that receives a dictionary
list_terms(IDE='Integrated Development Environment')

names = ['Juan', 'Karla', 'Ramiro', 'Esteban']

print('')
print('***** String List Parameters *****')
multiple_types(names)

print('')
print('***** String parameter *****')
multiple_types('Carlos')

print('')
print('***** Tuples parameters *****')
multiple_types((8, 9))

print('')
print('***** Integer List parameters *****')
multiple_types([10, 11])
