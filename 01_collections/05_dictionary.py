# PRACTICE TITLE: Dictionary
# DESCRIPTION: Dictionary represents an object with key and value
# NOTATION: dictionary = {'key' : 'value}
# NOTES:
# 1. For dictionary you have to use { 'key' : 'value }
# 2. Everything immutable type can use by key (int, float, bool, str, etc)

# Initializing dictionary
dictionary = {
    'IDE'   : 'Integrated Development Environment',
    'OOP'   : 'Object Oriented Programming',
    'DBMS'  : 'Database Management System',
}

# Print dictionary
print(dictionary)

# Dictionary Length
print(len(dictionary))

# Get specific element
print(dictionary['IDE'])

# Other form to get specific element
print(dictionary.get('OOP'))

# Modifying elements
dictionary['IDE'] = 'integrated development environment'
print(dictionary)

# Get elements with for loop
for key, value in dictionary.items():
    print(key, value)

# Find element in dictionary
print('IDE' in dictionary)

# Add new element to dictionary
dictionary['PK'] = 'Primary Key'
print(dictionary)

# Remove element
dictionary.pop('DBMS')
print(dictionary)

# Clear dictionary
dictionary.clear()
print(dictionary)

# Delete dictionary
del dictionary
