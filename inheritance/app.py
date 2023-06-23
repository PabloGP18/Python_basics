from Chef import Chef
from ChineseChef import ChineseChef

# storing the object in a variable
myChef = Chef()
MyChineseChef = ChineseChef()

# accessing the functions off the object
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

# accessing a new object that has inheritade everything from chef
MyChineseChef.make_chicken()
MyChineseChef.make_salad()
MyChineseChef.make_special_dish()
MyChineseChef.make_fried_rice()
