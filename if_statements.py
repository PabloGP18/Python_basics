# If statements are a special structure where we can help our program can make decisions
# You will be able to execute code depending on conditions

is_male = True
is_tall = True 

# using or
if is_male or is_tall:
    print('you are a male or tall or both')
else:
    print('you are not a male or tall')

# using and
if is_male and is_tall:
    print('you are a male & tall')
else:
    print('you are not a male or tall or both')

# using and not/elif
if is_male and is_tall:
    print('you are a male & tall')
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are a tall woman")        
else:
    print('you are not a male and noy tall')