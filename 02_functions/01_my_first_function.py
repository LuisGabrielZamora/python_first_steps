# PRACTICE TITLE: Function Definition
# DESCRIPTION: Code structure that enable to execute an specific process
# NOTATION: def my_first_function():
# NOTES:
# 1. All the code that corresponds to the function has to be with tabulation
# 2. To execute the function we have to call it with the same "def" tabulation

# Definition to my function
def my_first_function():
    print('Hello from my First Function')


# Function which receives arguments
def arguments_function(name, year):
    print('')
    print(f'My name is: {name} and this year is: {year}')


# Returns result
def add_arguments(a, b):
    return a + b


# Default arguments with the data type to return
def default_minus_arguments(a=100, b=100) -> int:
    return a - b


# Python consider a dynamic parameters that receives like a tuple
# IMPORTANT NOTE: For dynamic arguments in a function have to use with *
def name_list(*names):
    for name in names:
        print(name)


def add_all_arguments(*args: int) -> int:
    total = 0
    for arg in args:
        total = total + arg
    return total


def multiply_all_arguments(*args: int) -> int:
    total = 1
    for arg in args:
        total = total * arg
    return total


# Call the function
my_first_function()

# Call the function with parameters
arguments_function('Gabriel Zamora', 2030)

# Add function
print('')
print(add_arguments(10, 96))

# Minus function
print('')
print(default_minus_arguments(120))
print(default_minus_arguments())

# Function with dynamic parameters
print('')
name_list('Juan', 'Karla', 'Maria', 'Ernesto', 'Javier')


# Function with dynamic add parameters
print('')
print(f'Sum total is: {add_all_arguments(10, 15, 20, 15, 202, 4, 5)}')
print(f'Multiply total is: {multiply_all_arguments(10, 15, 20, 15, 202, 4, 5)}')
