# Intro to python

Python is a dynamically typed language, so you don't have to state what the data types of variables are.

#### Variables 
```python
a = 1
b = 2
c = 3.5
hi = "hello world!"

print(a)  # 1
print(b)  # 2
print(c)  # 3.5
print(hi) # "Hello World!"
```
Variables can be overwritten

```python
d = 5
print(d) # 5

d = 7
print(d) # 7
```
#### Data types
 Numerical - _integers, floats or complex numbers_

 String - _characters or text_

 Boolean - _True or False values_
 
**Operators**

_Arithmetic operators_: +, -, /, *, %

_Comparison operators_: >, <, =>, =<, ==, !=

**Numeric data types**
```python
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
print(one_third)     # 0.3333333333
print(one_third * 3) # 1.0

```
**Strings**
```python
single_quotes = 'Look, single quotes'
double_quotes = "Look, double quotes"

# String slicing
hi = "Hello World!"
print(hi[-5:])
```
**String Methods**

Python has built-in functions that can be used on strings

```python
hi = "Hello World!"

# len() - gives a length of a string 
print(len(hi))

# .lower() - lowercase the string
print(hi.lower())

# .upper() - uppercase the string
print(hi.upper())

# .capitalize() - capitalise every word in the string
print(hi.capitalize())

# .strip() - removes spaces at the beginning and the end
white_spaces = "     lot's of white space    "
print(white_spaces.strip())

# .count() - counts specific letter or word
example_text = "Here's some text with lots of text"
print(example_text.count('e'))

# .replace() - replaces a specific letter
print(example_text.replace('e', '3'))
```
**Concatenation and Casting**

This allows to concatenate strings together
```python
x = 2
y = 5.4
z = 'This is a string.'
zz = 'This is also a string'

# Concatenate
print(z + ' ' + zz) # This is a string. This is also a string.

# Casting
print(str(x) + " " + z + " " + zz)

# String to Numeric casting
int_string = "6"
print(int(int_string))
print(type(int(int_string)))
```
**F-String**

```python
name = "lassie"
years = 7
height = 60.2
print(f"{name.upper()} is {years * 7} years old in dog years ")

pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi:.3f}")

# percentage
score = 16
max_score = 26
print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:.0%}")
```
**Boolean**
```python
a = True
b = False

print(a == b)         # False
print(bool(1))        # True
print(a >= True)      # True
print(True and False) # False
print(True or False)  # True
```
**Boolean Methods**
```python
hi = "Hello World!"

print(hi.isalpha())       # False
print(hi.islower())       # False
print(hi.endswith("!"))   # True
print(hi.startswith("H")) # True
```
**The value of 0 in Boolean**
```python
x = 0
y = 10
z = -12

# 0 always False
print(bool(x))  # False
print(bool(y))  # True
print(bool(z))  # True
```
**The value of None in Boolean**

None is a placeholder, which means it is **not 0** neither is **nothing**
```python
x = None
print(bool(None))
print(x == False) # False
print(x == True)  # False

# best practice for checking if something is None
print(x is None)
```
**Task**
```python
name = input("What is your name?: ").capitalize()
age = int(input("How old are you?: "))
address = input("Where do you live?: ").capitalize()
hobby = input("What do you do in your free time?: ")
icecream = input("What is your favourite icecream flavour?: ")

# Casting
print("Hi, my name is " + name + " " + "and I'm " + str(age) + " years old. I live in " + address + ". What I like to do in my free time is " + hobby + ".")

# F-String
print(f"Hi, my name is {name} and I'm {age} years old. I live in {address}. What I like to do in my free time is {hobby} and my favourite ice cream flavour is {icecream}.")
```