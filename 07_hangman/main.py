# Set the initial word list
import random
import hangman_art as art
import hangman_list as data_list

# Define the variable from module
word_list = data_list.word_list

# Choose a random word
# random_word = word_list[random.randint(0, (len(word_list) - 1))]
random_word = random.choice(word_list)

# Print the logo for a game
print(art.logo)

# Create an empty list with underscores
display = []
for underscore in range(len(random_word)):
    display.append('_')

# Print letter display
print(f"{' '.join(display)}")

# Variable to manage the user lives
lives = len(art.stages) - 1

# Variable to control de end of game
end_of_game = False
while not end_of_game:

    # Get new letter to user
    guess_letter = input('Guess a letter: ').lower()

    # Checks if letter exists in array
    for position in range(len(random_word)):

        # Get a position letter
        letter = random_word[position]

        # Validation letter and add to display list
        if letter == guess_letter:
            display[position] = letter

    # Calculate the new value to lives
    if guess_letter not in random_word:
        print(f"You guessed {guess_letter}. that's not in the word. You lose a life.")
        lives -= 1

        # Print the stages ASCCI
        print(art.stages[lives])

    if lives == 0:
        end_of_game = True
        print(f'\n GAME OVER, the word was {random_word}')

    # Print letter display
    print(f"{' '.join(display)} \n")

    # Validate if exists blank in list
    if '_' not in display:
        end_of_game = True
        print('\n YOU WIN!!!')
