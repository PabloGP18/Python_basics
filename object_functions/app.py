from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Will", "Business", 3.8)

print(student1.on_honor_roll()) # this will return false
print(student2.on_honor_roll()) # this will return true