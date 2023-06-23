# Here I will create the student (object)

# import class
# the first student is referring to the file
# the second student is referring to the actual student class
from Student import Student

# creating an object of a student class
# A class is an overvall templete that defines what a student is
# This object is an actual student with actual information
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pow", "Art", 2.5, True)

# Accessing the information about the student
print(student1.name)
print(student1.gpa)
print(student2.major)