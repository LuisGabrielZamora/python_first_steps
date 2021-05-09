# PRACTICE TITLE: Recursive Call Function
# DESCRIPTION: In function you can call the same function with recursion,
# and that function allows us to calculate factorial.
# NOTATION: function(args):
# NOTES:
# 1. In definition function have to call the same function with recursion

def factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print('*************************')
# Get number typping by user
numberFactorial = input('What number do you need to know the factorial? ')
# Operators Overload
numberFactorial = int(numberFactorial)

# Call function
result = factorial(numberFactorial)
print(f'The factorial is: {result}')
