import random

feet_in_mile = 5200
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo"]

def get_file_ext(filename):
    return filename[filename.ext(".")+1:]

def roll_dice(num):
    return random.randint(1,num)
    