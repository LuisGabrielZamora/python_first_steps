# PRACTICE TITLE: Recursive Call Function
# DESCRIPTION: In function you can call the same function with recursion,
# and that function allows us to descending and print the value.
# NOTES:
# 1. In definition function have to call the same function with recursion

def desc_function(maxNumber):
    if maxNumber == 0:
        return 0
    else:
        # Print new value
        print(maxNumber)
        # Call with recursion the same function
        return desc_function(maxNumber - 1)


print('*************************')
# Get number typping by user
maxNumber = input('What number do you type like the max value to descending? ')
# Operators Overload
maxNumber = int(maxNumber)

# Call function
result = desc_function(maxNumber)
