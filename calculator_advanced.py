
# converting from init the number to a number(otherwise it's always a string)
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# without a function
if op == "+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op =="*":
    print(num1 * num2)
elif op =="/":
    print(num1 / num2)
else:
    print("Enter valid operator!")

# with a function & while true
def calculator(num1, op, num2):
    while True:
        if op == 'sum' or op == '+':
            return num1 + num2
        elif op == 'rest' or op == '-':
            return num1 - num2
        elif op == 'multiply' or op == '*':
            return num1 * num2
        elif op == 'divide' or op == '/':
            return num1 / num2
        elif op == 'exit':  # Add condition to terminate the program
            return "Program terminated"
        else:
            op = input("Enter a valid operator (or 'exit' to terminate): ")
            


