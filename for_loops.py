# for loop allows us to loop over different collections of items (arrays, numbers, letters in a string,...)

# for every letter inside of pgp academy i want to do something
for letter in "PGP Academy":
    #this is going to print out a different letter with every loop
    print(letter)

# using an array with for loop
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    # printing every element of the array friends 
    print(friend)

#other way to print all the elements of an arrays
for index in range(len(friends)):
    # printing every element of the array friends 
    print(friends[index])

# printing out numbers
for index in range(10):
    print(index)

# printing out all the numbers between 3 & 10
for index in range(3,10+1):
    print(index)

# using logic with for loop

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")