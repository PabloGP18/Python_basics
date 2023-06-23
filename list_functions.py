#Different functions that you can apply on a list

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Kim', "Jim", "Oscar", "Toby"] 

#extend function wil take a list and append another list on the end of it
friends.extend(lucky_numbers)
print(friends)

#add individual elements on to a list
# append function will always at at the end of a list
friends.append('Creed')
print(friends)

#Insert function allows you to inster an individual element at choice
friends.insert(1, "Gavi")
print(friends)

#remove function removes an element from the list
friends.remove("Jim")
print(friends)

#Pop function will "pop" an element of the list (the last element)
friends.pop()
print(friends)

#index function will search a value and return index
print(friends.index("Gavi"))

#count function will count how many times the element is in the list
print(friends.count("Gavi"))

#sort function will sort the list in ascending order
friends2 = ['Kevin', 'Kim', "Jim", "Oscar", "Toby"] 
friends2.sort()
print(friends2)

#reverse function will do just that, reverse the list
friends.reverse()
print(friends)

#copy function will copy a list with all the elements
friends3 = friends2.copy()
print("copy of friends2: " + str(friends3))

#Clear function to reset the list
friends.clear()
print(friends)

