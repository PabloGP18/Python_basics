# insert a new line with \n
print("PGP\nAcademy")

# using \ to tell python i want to print out a "
print("PGP\"Academy")

#using variable and printing it and concatenating
phrase = "PGP Academy"
print(phrase + "is cool")
# or
print(f"{phrase} is cool")

# convert it to lower and uppercase
print(phrase.lower())
print(phrase.upper())

# check if the string is uppercase of lowercase (it will give back false because it checks if the entire phrase is upper of lower)
print(phrase.isupper())
print(phrase.islower())

# combining functions (this will give back true)
print(phrase.upper().isupper())
print(phrase.lower().islower())

#checking how many charachters are inside of the string
print(len(phrase))

#getting individual characthers in the string
print(phrase[0])
#or (this is going the return the index of the firs capital P inside of the string) 
print(phrase.index("P"))

#replace a characther in the string
print(phrase.replace("PGP", "Spanish"))
