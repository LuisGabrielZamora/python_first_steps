# PRACTICE TITLE: Classes
# DESCRIPTION: Classes is a very important element for OOP
# NOTATION: class NewClass():
# NOTES:
# 1. All the classes have to use UpperCamelCase convention
# 2. All the code with indentation applies for Class
# 3. For constructor or initializer class, we use: def __init__(self)

class People:
    # Class receive parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Modify class values
People.name = 'Juan'
People.age = 28

# Access to class values
print(People.name)
print(People.age)

# Create new people object or a new instance class
people = People('Karla', 15)
print(people.name)

# Create second object
people2 = People('Carlos', 100)
print(people2.name)
# With id access to memory direction
print(id(people2.name))
