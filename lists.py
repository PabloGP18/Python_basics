# A list (arrays in javascript) is a structure to store lists of information, to organize them to keep track of them a lot easier
# This are examples of the basics working with lists

#list of friends
friends = ['Kevin', 'Kim', "Jim", "Oscar", "Toby"] 

#print list
print(friends)

#print list by index
print(friends[0])

#print starting from index and all after the index
print(friends[1:])

#specify a range
#this will print out the value of index 1,2 & 3
print(friends[1:4])

#change value of index
friends[1]="Mike"
print(friends[1])