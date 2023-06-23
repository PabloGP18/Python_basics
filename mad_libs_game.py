# aksing the user for input to fill in the blanks and complete te mad libs
import time

print("Welcome to the Mad Libs game!")
time.sleep(1)
print("Please enter the missing words...")
time.sleep(1)

try:
    color = input('Enter a color: ')
    plural_noun = input('Enter a plural noun: ')
    celebrity = input('Enter the name of a celebrity: ')

    print("The result is....")
    time.sleep(1)
    print("**************")  
    time.sleep(1)
    print("**********") 
    time.sleep(1)
    print("******")
    time.sleep(2)

    print(f'Roses are {color}')
    print(f'{plural_noun} are blue')
    print(f'I love {celebrity}')
except Exception as e:
    print("Oops! Something went wrong. Please try again.")
    print(f"Error: {str(e)}")
