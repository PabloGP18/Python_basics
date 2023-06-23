class Student:
    def __init__(self, name, major, gpa ):
        # assigning values
        self.name= name
        self.major= major
        self.gpa= gpa

    # creating a function for the Student class
    def on_honor_roll(self):
        # in case to have an honor role you must have a gpa of 3.5
        if self.gpa >= 3.5:
            return True
        else:
            return False