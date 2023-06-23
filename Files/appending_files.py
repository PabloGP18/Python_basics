
# adding text at the end of the file with "a" (append)
employee_file = open("Files/employees.txt", "a")

# appending something to the end of the file
employee_file.write("\nYork - Customer Service")

# closing the file
employee_file.close()