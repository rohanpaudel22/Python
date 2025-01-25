"""
---- Global Variables:

-> variables that are created outside of a function are known as global variables

-> Global variables can be used by everyone, both inside of functions and outside.
"""

# Creating a variables outside of a function, and use it inside the function

x = "good programming language"

def myfunc():
  print('Python is ' + x)
  
myfunc()

"""
  -> if we create a variable with the same name inside a function, this variable will be local, and can only be used the function. The global variable with the same name will remain as it was, global and with the original value. 
"""

# Creating a variable inside a function, with the same name as the global variable

a = "good programming language"

def myfunc1():
  
  a = "awesome programming language"
  print('Python is ' + a)
  
myfunc1()

print('Python is ' +a)

"""
  ----- The Global Keyword:
  
  -> to create a global variable inside a function, we can use the 'global' keyword.

"""

def myFunc2():
  
  global g
  g = "good"
  
myFunc2()

print("Python is " +g)

# We can also use the 'global' keyword if we want to change a global variable inside a function

d = "Rohan"

def myFunc3():
  global d 
  d = "Raman Paudel"
  
myFunc3()

print("My name is " +d)