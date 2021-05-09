"""
PRACTICE TITLE: Inheritance
DESCRIPTION: Children class, inheritance all methods, attributes and properties for the father class
NOTATION: Children class: Employee, and Father class: People -> Employee(People)
NOTES:
1. With super() access to properties, methods and attributes to father class
2. With super().__init__(params), send all the values and params for the father class
3. In children class have to declare def __init__(self, all_params_that_receives)
"""

"""Father class"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to define the variables to print
    def __str__(self):
        return "Name: " + self.name + ", age: " + str(self.age)


"""Children class"""


class Employee(People):
    def __init__(self, name, age, billing):
        """Pass params to father class"""
        super().__init__(name, age)
        """Define own properties in children class"""
        self.billing = billing

    # Method to define the variables to print
    def __str__(self):
        return super().__str__() + ', billing: ' + str(self.billing)


people = People('Juan', 30)
print(people)

employee = Employee('Karla', 28, 500)
print(employee)


print('********************************')
print(f'Name: {people.name}')
print(f'Employee name: {employee.name}')
print(f'Billing: {employee.billing}')
