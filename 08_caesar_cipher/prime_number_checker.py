""" Prime number are numbers that can only be cleanly divided by itself and 1 """

"""
Function Initialize that calculates the prime number
"""


def prime_checker(number: int):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It´s a prime number")
    else:
        print("It´s not a prime number")


print("*******************************")
print("*******************************")
print("Prime number checker")
print("*******************************")
print("*******************************")
number = input("Give us your number: ")
prime_checker(int(number))
