# Python Basics

This document provides a brief overview of various topics covered in a Python programming course.

## Introduction

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

## Installing Python

Python can be downloaded and installed from its official website (https://www.python.org/).

## Setup & Hello World

To print a string in Python, we use the `print` function. For example:

```python
print("Hello, World!")
```

## Drawing a Shape

In Python, we can use print statements to draw shapes. For example, to draw a simple triangle:

```python
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
```

## Variables & Data Types

In Python, variables are created when you assign a value to it. Python has the following data types: text type(str), numeric types(int, float, complex), sequence types(list, tuple, range), mapping type(dict), set types(set, frozenset), boolean type(bool), binary types(bytes, bytearray, memoryview).

```python
name = "John"  # str
age = 20  # int
height = 5.6  # float
```

## Working With Strings

Python has a set of built-in methods that you can use on strings. Some of the main methods include lower(), upper(), strip(), replace(), split(), etc.

```python
str1 = "Hello, World!"
print(str1.lower())  # Outputs "hello, world!"
```

## Working With Numbers

Python supports different types of numbers, including int, float and complex. Python also provides built-in functions like abs(), max(), min(), round(), and sum().

```python
x = 5  # int
y = 2.5  # float
z = 1j  # complex
print(round(y))  # Outputs 3
```

## Getting Input From Users

In Python, you can use the `input()` function to get user input.

```python
name = input("Enter your name: ")
print("Hello, " + name)
```

## Building a Basic Calculator

A basic calculator can be created in Python using simple arithmetic operations and the input() function to get the numbers.

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1 + num2)
```

## Mad Libs Game

A Mad Libs game can be created in Python using string concatenation and the input() function.

```python
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
```

## Lists

A list is a collection which is ordered and changeable. Lists are written with square brackets.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Outputs "banana"
```

## List Functions

Python provides several methods that you can use to modify lists. Some of the main methods include append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), copy().

For example:

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Outputs ["apple", "banana", "cherry", "orange"]
```

## Tuples

A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

```python
fruits = ("apple", "banana", "cherry")
print(fruits[1])  # Outputs "banana"
```

## Functions

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.

```python
def greet(name):
  print("Hello, " + name)

greet("John")  # Outputs "Hello, John"
```

## Return Statement

The return statement is used to exit a function and go back to the place from where it was called.

```python
def square(number):
  return number * number

print(square(3))  # Outputs "9"
```

## If Statements

if statements are used to test for particular conditions and respond appropriately. if statements can be nested and you can use elif and else.

```python
temperature = 20
if temperature > 30:
print("It's hot outside")
elif temperature > 15:
print("It's nice outside")
else:
print("It's cold outside")
```

## If Statements & Comparisons

Comparison operators (==, !=, >, <, >=, <=) are used to compare values. It either returns True or False according to the condition.

```python
def max_num(num1, num2, num3):
if num1 >= num2 and num1 >= num3:
return num1
elif num2 >= num1 and num2 >= num3:
return num2
else:
return num3

print(max_num(3, 4, 5)) # Outputs "5"
```

## Building a Better Calculator

You can build a better calculator using if statements and the input() function.

```python
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "*":
  print(num1 * num2)
elif op == "/":
  print(num1 / num2)
else:
  print("Invalid operator")
```

## Dictionaries

A dictionary is a collection which is unordered, changeable and indexed. Dictionaries are written with curly brackets, and they have keys and values.

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(my_dict["brand"])  # Outputs "Ford"
```

## While Loop

With the while loop we can execute a set of statements as long as a condition is true.

```python
i = 1
while i < 6:
print(i)
i += 1
```

## Building a Guessing Game

You can build a simple guessing game using a while loop.

```python
secret_word = "giraffe"
guess = ""
while guess != secret_word:
  guess = input("Enter guess: ")
print("You win!")
```

For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

```python
for x in range(6):
  print(x)  # Outputs 0 to 5
```

## Exponent Function

You can create a function to compute the power of a number.

```python
def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result

print(raise_to_power(3, 2))  # Outputs "9"
```

## 2D Lists & Nested Loops

In Python, you can create a list containing other lists, known as a 2D list. You can use nested for loops to iterate through 2D lists.

```python
number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

for row in number_grid:
  for col in row:
    print(col)
```

## Building a Translator

You can build a simple translator that replaces certain words in a text with your specified words.

```python
def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "aeiou":
      if letter.isupper():
        translation = translation + "G"
      else:
        translation = translation + "g"
    else:
      translation = translation + letter
  return translation

print(translate("Apple"))  # Outputs "GpplG"
```

## Comments

Comments can be used to explain Python code. You can create a comment in Python by using the # symbol.

```python
# This is a comment
print("Hello, World!")
```

## Try / Except

The try block lets you test a block of code for errors. The except block lets you handle the error.

```python
try:
  number = int(input("Enter a number: "))
  print(number)
except:
  print("Invalid input")
```

## Reading Files

Python allows you to read contents of a file using the open() function.

```python
file = open("filename.txt", "r")
print(file.read())
file.close()
```

## Writing to Files

Python allows you to write to a file or append to a file. This can be done using the open() function with the "w" (write) or "a" (append) parameter.

```python
file = open("filename.txt", "a")
file.write("\nHello, World!")
file.close()
```

## Modules & Pip

Modules in Python are simply Python files with the .py extension, which implement a set of functions. Pip is a package manager for Python and is used to install modules.

```python
# Install a module
# pip install module_name

# Using a module
import module_name
```

## Classes & Objects

Classes and objects are the two main aspects of object-oriented programming. A class is a blueprint for the object.

```python
class Student:
  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gpa

student1 = Student("Jim", "Business", 3.1)
print(student1.name)  # Outputs "Jim"
```

Building a Multiple Choice Quiz
You can create a simple multiple choice quiz game using classes.

```python
class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

question_prompts = [
  "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
  "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
]

questions = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c")
]

def run_quiz(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_quiz(questions)
```

## Object Functions

You can define functions within a class that represent operations that are common to all instances of the class.

```python
class Student:
  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gpa

  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False

student1 = Student("Jim", "Business", 3.8)
print(student1.on_honor_roll())  # Outputs True
```

## Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

```python
class Chef:
  def make_chicken(self):
    print("The chef makes a chicken")

class ItalianChef(Chef):
  def make_pasta(self):
    print("The chef makes pasta")

myChef = ItalianChef()
myChef.make_chicken()  # Outputs "The chef makes a chicken"
myChef.make_pasta()  # Outputs "The chef makes pasta"
```
