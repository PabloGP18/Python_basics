# in this guessing game we will use different coding structures
import time
# variable to store secret word
secret_word = "giraffe"

# variable to store all the guesses the user makes
guess = ""

# adding variable for limit of guesses
guess_count= 0
guess_limit= 3

#boolean for when you you are out of guesses
out_of_guesses = False

# while this is true the loop is going to keep looping
# In this case while guess is not equal to secret word it will keep looping
while guess != secret_word and not (out_of_guesses):

    if guess_count < guess_limit:    
    # if guess != secret_word:
        guess = input("Enter guess: ")
        guess_count += 1
        time.sleep(1)
    else: 
        out_of_guesses = True


if out_of_guesses:
    print("Out of Guesses, YOU Lose!")
else:
    print("***************")
    time.sleep(1)
    print("*************")
    time.sleep(1)
    print("***********")
    time.sleep(1)
    print("*********")
    time.sleep(1)
    print("*****")
    time.sleep(1)
    print("You win!")


