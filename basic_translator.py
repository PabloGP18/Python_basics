
def translate(phrase):
    translation = ""
    # looping phrase and adding it to translation
    for letter in phrase:
        #checing if the letter is inside in the string
        if letter.lower() in "aeiou":
            if letter.isupper():
            # if the letter is a vowle convert it to a g
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:# this will be when the letters are no vowels.
            translation = translation + letter
    return translation

# calling the function
print(translate(input("Enter a phrase: ")))