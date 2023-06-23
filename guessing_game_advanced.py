# same guessing game as before but more advanced
# Adding a message when the user guesses and comparing how many letters the users inputs
# User can only have 5 guesses 

import time

def play_guessing_game(secret_word, max_guesses):
    num_guesses = 0
    while num_guesses < max_guesses:
        print("Please guess the secret word!")
        time.sleep(1)
        print("Remember that you can only guess 5 times.")
        time.sleep(1)
        guess = input("Enter your guess: ")
        num_guesses += 1

        if guess == secret_word:
            print("Congratulations, you win!")
            return

        if guess < secret_word:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print("Out of guesses. The secret word was:", secret_word)

secret_word = "giraffe"
max_guesses = 5

play_guessing_game(secret_word, max_guesses)
