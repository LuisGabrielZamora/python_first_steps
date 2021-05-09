# Create de list with all the numeric values
print('***************************************************************')
print('***************************************************************')
print('Just appear the values divisibles for a number that user assign')
print('')

divisible = input('Assign the number which divide the list: ')
divisible = int(divisible)
print('')

lastNumber = input('Assign the last number for the list: ')
# Converts the value and adds 1 for practising
lastNumber = int(lastNumber) + 1
print(f'... CALCULATING DIVISIBLES BY {divisible} ...')
print('')

for i in range(lastNumber):
    if i % divisible == 0:
        print(f'Number is divisible: {i}')

print('*** FINISH PROCESS ***')