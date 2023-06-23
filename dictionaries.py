# dictionaries is a special structure in python that allows us to store information in what are called key value pairs (this is like objects in javascript)

# in this example jan is the key and january is the value
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
    }

# Accessing key or value with []
print(monthConversions["Nov"])

# Accessing key or value with get
print(monthConversions.get("Dec"))

# Accessing key or value with get & passing a default value
print(monthConversions.get("aaa", "Not a valid Key"))
