# PRACTICE TITLE: Set
# DESCRIPTION: Set type doesn´t have order and doesn´t possible to edit or repeat elements , but it is possible to
# create and delete new elements
# NOTATION: variable = {'element 1', 'element 2', 'element 3'}
# NOTES:
# 1. For set collection you have to use {}

# Initializing set variable
planets = {'Marte', 'Júpiter', 'Venus'}
print(planets)

# Verify if one element is present in set
print('Marte' in planets)

# Add new element
planets.add('Tierra')
print(planets)

# Delete element with error
planets.remove('Tierra')
print(planets)

# Delete element without error
planets.discard('Júpiter')
print(planets)

# Clear variable
planets.clear()
print(planets)

# Delete variable
del planets
