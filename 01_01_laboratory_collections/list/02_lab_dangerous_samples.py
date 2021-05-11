"""
Created by: MGR
Created at: 06 May 2021
"""
print('************Exercise 1*********************')
""" Process to create database """
import random

"""Initialize database"""
sampleTest = []

"""initialize constant"""
sample = 'SAMPLE_'

"""Process to fill 'sampleTest' database """
for numberList in range(100):
    if numberList < 9:
        nameList = sample + '00' + str(numberList + 1)
    elif 9 <= numberList < 99:
        nameList = sample + '0' + str(numberList + 1)
    else:
        nameList = sample + str(numberList + 1)
    sampleTest.append(nameList)

print(f'DataBase Samples Laboratory: {sampleTest}')

print('************Exercise 2*********************')

"""Initialize database"""
valuesBasic = []

"""Process to fill 'valuesBasic' database """
for numberList in range(100):

    """Create the random value"""
    randomNumber = random.random()

    """Validate instructions"""
    if numberList < 25:
        valueTest = randomNumber
    else:
        valueTest = 0

    """Add values to 'valuesBasic database'"""
    valuesBasic.append(valueTest)

    """Print data to user"""
    print(f'{sampleTest[numberList]} : {valuesBasic[numberList]}')

print('************Exercise 3*********************')
"""Initialize the new constant"""
DIVISIBLE_BY_5 = 'DIVISIBLE_5_'

"""Process to change the sample name divisible by 5"""
for numberList in range(100):

    if numberList < 9:
        newNumber = '00' + str(numberList + 1)
    else:
        if 9 <= numberList < 99:
            newNumber = '0' + str(numberList + 1)
        else:
            newNumber = str(numberList + 1)

    if numberList % 5 == 0:
        sampleTest[numberList] = sample + DIVISIBLE_BY_5 + newNumber

print(f'New Sample Test {sampleTest}')

print('************Exercise 4*********************')
"""Initialize valuesDangerous database"""
valuesDangerous = []

"""Process to fill 'valuesDangerous' database """
for numberList in range(100):

    """Create the random value"""
    randomNumber = random.randint(20, 100)

    """Validate instructions"""
    if numberList < 25:
        valueTest = 0
    else:
        valueTest = randomNumber

    """Add values to 'valuesBasic database'"""
    valuesDangerous.append(valueTest)

    """Print data to user"""
    print(f'{sampleTest[numberList]} : {valuesDangerous[numberList]}')
