# Building a basic calculator  where you get 2 numbers, add them and print them on the screen.
# importing time to delay between the first frase and the input part of the app.
import time

print("Please enter 2 numbers to add up...")
time.sleep(2)
num1 = input("enter a number: ")
num2 = input("enter another number: ")
result = float(num1) + float(num2)
print(f"The sum of the 2 numbers: {result}")
