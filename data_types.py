"""
Data types

Numbers -> float, int, complex, longs(old version)
Strings -> characters or text
Boolean -> True or False
"""

"""
Operators

Arithmetic operators: +, -, /, *, %
Comparison operators: >, <, =>, =<, ==, !=
"""
# Numbers

a = 24
b = 16

print(a + b) # -> 40
print(a - b) # -> 8
print(a / b) # -> 1.5
print(a < b) # -> False

FloatNum = 1.356
IntNum = 4
print(type(FloatNum + IntNum))

one_third = 1 / 3
print(one_third) # -> 0.3333333333
print(one_third * 3) # -> 1.0

# Strings

# single_quotes = 'Look, single quotes'
# double_quotes = "Look, double quotes"
#
# String slicing
# hi = "Hello World!"
# print(hi[-5:])
#
# # String methods
#
# # len()
# print(len(hi))
# # .strip()
# white_spaces = "     lot's of white space    "
# print(white_spaces.strip())
# # .count()
# example_text = "Here's some text with lots of text"
# print(example_text.count('e'))
# # .replace()
# print(example_text.replace('e', '3'))
#
# # concatenation
# x = 2
# y = 5.4
# z = 'This is a string'
# zz = 'This is also a string'
#
# print(z + ' ' + zz)
#
# # String to numeric casting
#
# int_string = "6"
# print(int(int_string))
# print(type(int(int_string)))
#
# # F-string
#
# name = "lassie"
# years = 7
# height = 60.2
#
# print(f"{name.upper()} is {years * 7} years old in dog years ")
#
# pi = 3.14159265359
# print(f"Pi to 3 decimal places: {pi:.5f}")
#
# # percentage
#
# score = 16
# max_score = 26
# print(f"You scored {score/max_score}")
# print(f"You scored {score/max_score:.0%}")
#
# """
# Task
#
# """
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# address = input("Where do you live?: ").capitalize()
# hobbie = input("What do you do in your free time?: ")
# icecream = input("What is your favourite icecream flavour?: ")
# #
# # # casting
# print("Hi, my name is " + name + " " + "and I'm " + str(age) + " years old. I live in " + address + ". My hobbie is " + hobbie + ".")
# # f string
# print(f"Hi, my name is {name} and I'm {age} years old. I live in {address}. My hobbie is {hobbie} and my favourite ice cream flavour is {icecream}.")

# Booleans

# a = True
# b = False
#
# print(a == b) # -> False
# print(bool(1)) # -> True
# print(a >= True) # -> True
#
# print(True or False)

# Boolean with data type

# hi = "Hello World!"
#
# # Boolean methods
# print(hi.isalpha()) # -> False
# print(hi.islower()) # -> False
# print(hi.endswith("!")) # -> True
# print(hi.startswith("H")) # -> True
#
# # The value of 0

# x = 0
# y = 10
#
# # 0 always False
# print(bool(x))
# print(bool(y))

# Value of None - not 0, not nothing ------> It is a placeholder
# x = None
# print(bool(None))
# print(x == False) # -> False
# print(x == True) # -> False
#
# # best practice for checking if something is None
# print(x is None)
#
