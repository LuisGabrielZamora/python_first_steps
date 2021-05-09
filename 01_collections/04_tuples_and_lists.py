# PRACTICE TITLE: Tuples and Lists
# DESCRIPTION: With specific tuple, user decide the maximum value and the process create new list with lower values
# NOTATION: -
# NOTES: -

# Define the initial list
resultList = []

# Set the initial tuple
initialTuple = (20, 25, 26, 29, 13, 4, 5, 1, 0, 7, 8, 9, 15, 46, 18, 40, 56, 11, 21, 19, 26, 31, 15, 35, 30, 20);

# System request to user the maximum value
maxValue = input(f'Set the maximum value, it have to lower than {max(initialTuple)}: ')
# Convert string to int
maxValue = int(maxValue)

print(' ***** CALCULATING ***** ')
# Process decision to create a new list or finish process
if maxValue > max(initialTuple):
    # Finish process because max value that user sets is bigger than maximum tuple value
    print(f'Your value {maxValue} is bigger than maximum tuple value. Sorry, try it again.')
else:
    # Process execution to fill the list
    for tuple in initialTuple:
        if tuple < maxValue:
            resultList.append(tuple)

print(f'List generate: {resultList}')
print(' ***** FINISH PROCESS ***** ')
