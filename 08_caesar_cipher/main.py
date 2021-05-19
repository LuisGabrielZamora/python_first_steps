"""
Define alphabet variable: All the alphabet appears in two times because is easier to encryption to do its job.
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Import all the final resources
from art import logo
print(f"{logo}")


# FUNCTION ENCRYPT: Function that takes the "text" and "shift" as inputs
def encrypt_decrypt(plain_text, shift_amount, cipher_direction):
    # Initialing variables
    cipher_text = ""

    # Validate cipher direction
    if cipher_direction == 1:
        cipher_direction_text = "encoded"
    else:
        shift_amount *= -1
        cipher_direction_text = "decoded"

    for letter in plain_text:
        # Validate that char is in alphabet
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter

    print(f"The {cipher_direction_text} text is {cipher_text}")


# Question for continue the program
def finish_cipher():
    choice = input("Do you give us a plain text again? Y/N: \n")
    return choice == "Y"


def validate_shift(shift):
    return shift % 26


not_finish = True
while not_finish:
    # User selection or choice
    cipher_direction = int(
        input(
            "\n Press the number 1 o 2, depends on your choice: \n 1. code \n 2. decode \n Give us your response please: \n"))

    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift = validate_shift(shift)

    # Call the function to crypt or encrypt text
    encrypt_decrypt(text, shift, cipher_direction)

    # Assign to variable to finish the process
    not_finish = finish_cipher()
