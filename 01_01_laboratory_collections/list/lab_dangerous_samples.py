"""
CREATED BY: LGZA
CREATED AT: 06 May 2021
"""

""" Process to create database """
import random

"""Initialize database"""
sampleTests = []

"""Initialize constant"""
SAMPLE = 'SAMPLE_'

"""Process to fill database"""
for number_test in range(100):
    if number_test < 9:
        nameTest = SAMPLE + '00' + str(number_test+1)
    else:
        if 9 <= number_test < 99:
            nameTest = SAMPLE + '0' + str(number_test+1)
        else:
            nameTest = SAMPLE + str(number_test+1)

    sampleTests.append(nameTest)

print(f'Database Samples: {sampleTests}')
print('**********************')

"""Initialize database"""
valuesBasic = []

"""Process to fill database"""
for numberTest in range(100):

    """Create the random value"""
    randomValue = random.random()

    """Validate with the instructions"""
    if numberTest < 25:
        valueTest = randomValue
    else:
        valueTest = 0

    """Add value to database"""
    valuesBasic.append(valueTest)

    """Print data to user"""
    print(f' {sampleTests[numberTest]} : {valuesBasic[numberTest]} ')

print('**********************')
print(f'Database Values Basic Samples {valuesBasic}')

"""Initialize the new constant"""
DIVISIBLE_BY_5 = 'DIVISIBLE_5_'

"""Process to change the sample name divisible by 5"""
for numberTest in range(100):

    if numberTest < 9:
        newNumber = '00' + str(numberTest+1)
    else:
        if 9 <= numberTest < 99:
            newNumber = '0' + str(numberTest+1)
        else:
            newNumber = str(numberTest+1)

    if numberTest % 5 == 0:
        sampleTests[numberTest] = SAMPLE + DIVISIBLE_BY_5 + newNumber

print('**********************')
print(f'New Sample Test {sampleTests}')
