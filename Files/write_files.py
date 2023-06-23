# writing to the file
employee_file = open("Files/employees.txt", "w")

# this is going to overwrite the entire file
employee_file.write("\nYork - Customer Service")

# Creating a new file
employee_file1 = open("Files/employees1.txt", "w")

# this is going to overwrite the entire file
employee_file1.write("\nYork - Customer Service")

# closing the file
employee_file.close()