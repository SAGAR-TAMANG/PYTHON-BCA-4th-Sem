# Function Declaration Example 

def add (x, y):
  pass

# Function Definition

def add(x, y):
  return x+ y

print(add(1, 2))

# Formal, Positional, Default, & Variable Length Arguments

# Formal is the one we have used above

# Belo is Positional argument

def greet(name, greeting):
  print(greeting, name)

greet("Bob", "hi")

# default argument

def greet(name, hello = "greet"):
  print(hello, name)

greet("Sagar")

# Variable Length Argument

def greet(*args):
  for i in args:
    print(i)

greet(1, 2, 3, 4)

# Page number 369, example 11.1 Passing & calling (Built-in) Functions (numconv.py)