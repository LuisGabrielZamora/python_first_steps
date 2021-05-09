# PRACTICE TITLE: Tuple
# DESCRIPTION: Tuple is an immutable object, means that nothing change the state, position or values object
# NOTATION: variable = ('element 1', 'element 2', 'element 3')
# NOTES:
# 1. For tuples you have to use ()
# 2. For one element in tuple, you can identifying that because has the next notation:
# tuple = ('Element 1',) -> with final comma, next to first element

fruits = ('Naranja', 'Platáno', 'Guayaba')
print(fruits)

# Tuple length
print(f'Tuple length: {len(fruits)}')

# Access one element
print(fruits[0])

# Inverse Access
print(fruits[-1])

# Tuples range
print(fruits[0:1])

# Access tuples with for
for fruit in fruits:
    print(fruit)

# Convert tuple to list
print(f'Tuple: {fruits}')
listFruits = list(fruits)
listFruits[0] = 'Pera'
fruits = tuple(listFruits)
print(f'New Tuple: {fruits}')

# Delete tuple
del fruits
