# this class wil inherit everything from class Chef
from Chef import Chef

class ChineseChef(Chef):

    #overwriting the same function in Chef, because the ChineseChef has is own special dish
    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")