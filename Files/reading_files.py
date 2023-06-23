
# Open function will just open the file inside our filesystem
# You have to store a open file inside of a variable to access the information

# accessing a file and ("r") reading it
employee_file = open("Files/employees.txt", "r")

# checking if a file is readable
print(employee_file.readable()) # this will giva back a bool true or false

# Reading an individual line inside of the file
print(employee_file.readline())

# Reading all of the lines and put them inside of a list
print(employee_file.readlines())

# accessing a specific line of the array
print(employee_file.readlines()[1])

# looping and printing the context in employee_file with for loop
for employee in employee_file.readlines():
    print(employee)

# printing out the entire content file 
print(employee_file.read())

# You also need to close to file after a the action you want to do with that file
employee_file.close()


# accessing a file and ("w") modify it
open("employees.txt", "w")

# append ("a") information into the end of the file
open("employees.txt", "a")

# read and write ("r+")
open("employees.txt", "r+")


