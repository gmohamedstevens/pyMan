##################
# INITIALIZATION #
##################
import random

MAX_TRIES = 5
DICTIONARY = ("secret", "python", "guess", "clue")

#############
# FUNCTIONS #
#############

# Return a random word from the dictionary
def get_word():
    return random.choice(DICTIONARY)

# Show an intro message to the player
def show_intro():
    print("Welcome to Hangman!")

# Show the current game state to the player
def show_game_prompt():
    print()
    print("Number of tries left: ", tries_left)
    print("The word: ", display_word)
    print("Already guessed letters: ", guessed_letters)
    return input("Please guess a letter: ")

# Return if the passed letter is contained in the passed word
def letter_is_in_word(letter, word):
    return letter in word

# Returns if the guess made is valid
def valid_guess_made():
    if not len(letter_guess) == 1: # Guess must be only one character
        print("Invalid guess, must be only one letter!")
        return False
    else:
        if not letter_guess.isalpha(): # Guess must be in the alphabet
            print("Invalid guess, that is not a letter!")
            return False
        if letter_is_in_word(letter_guess, guessed_letters): # Cannot guess the same letter twice
            print("Invalid guess, you already guessed that letter!")
            return False
    return True

##################
# MAIN GAME LOOP #
##################

# Introduce the player to the game
show_intro()
while True: # Begin main loop 
    secret_word = get_word() # Get a secret word from the dictionary
    tries_left = MAX_TRIES # Reset game variables
    display_word = "_ " * len(secret_word)
    guessed_letters = ""
    player_won = False
    while tries_left > 0 and not player_won: # While there are tries left and the player hasn't won, keep playing
        # Display the current game state
        letter_guess = show_game_prompt().lower() # Convert player guess to lower case
        print()
        if valid_guess_made():
            guessed_letters = guessed_letters + letter_guess + " " # Add guessed letter to list
            if letter_is_in_word(letter_guess, secret_word):
                print("Correct!") # Guess is correct; reveal the hidden letters
                for element in range(0, len(secret_word)):
                    if letter_guess == secret_word[element]:
                        temp_word = list(display_word)
                        temp_word[element * 2] = secret_word[element]
                        display_word = "".join(temp_word)
                if not letter_is_in_word("_", display_word): # If there are no more hidden letters, the player has won
                    print("You guessed the secret word!")
                    player_won = True
            else:
                tries_left -= 1 # Guess is incorrect
                if tries_left > 0:
                    print("Nope! Try again.") # Try again if there are tries left
                else:
                    print("Game over!") # Game over if no tries left
    print("The secret word was \"", secret_word, "\"") # Show the player the secret word
        
