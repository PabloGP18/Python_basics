# with try except it's possible to handle errors and do something about it!

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
    # Best practice in python is to catch a specific error, otherwise it's to broad
except ZeroDivisionError as err:
    # catching error that 10 can not be divided by 0
    print(err)
except ValueError:
    # catching an invalid input
    print("invalid input")

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except Exception as e:
#     # Exception will explain what kind of error you are encountering
#     print(e)