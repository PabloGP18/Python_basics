# This is a function that return the max num of three numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
# Calling the function
print (max_num(2,3,4))


# This is a function that compairs strings
def compair_string(string):
    if string == "dog":
        return "it's a dog"
    elif string == "cat":
        return "it's a cat"
    else:
       return "it's just an animal!"
    
# Calling the function
print(compair_string('dog'))