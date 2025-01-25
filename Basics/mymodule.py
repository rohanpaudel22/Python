'''
-->> Consider a module to be the same as a code library.

-->> A file containing a set of functions we want to include in our application.
'''

# Creating a Module:

# -->> To create a module just save the code we want in a file with the file extension .py:

def greeting(name):
  print("Hello, " + name)
  
# Using a Module:

import mymodule

mymodule.greeting("Rohan")

person1 = {
  
  "name": "John",
  "age": 21,
  "country": "Norway"
  
}

a = mymodule.person1["country"]
print(a)

import mymodule as mx

b = mx.person1["age"]
print(b)

# Built-in Modules:

import platform

x = platform.system()
print(x)

# Using the dir() function:

# ->> There is a built-in function to list all the function names(or variable names) in a module. The dir() function:

x = dir(platform)
print(x)

# Importing only the person1 dictionary from the module:

from mymodule import person1

print (person1["name"])

'''
--->> When importing using the from keyword, do not use the module name when referring to elements in the module. Example:

person1["age"], not ==> mymodule.person["age"]
'''