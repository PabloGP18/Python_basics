# A function that says hi
def say_hi(name, age):
    print(f"Hello {name}! Are you {str(age)} old?")

# python jumps up and goes over to the say_hi function
# this is the flow of functions
print('top')

say_hi("Pablo", 35)
say_hi("Kevin", 25)
print("bottom")