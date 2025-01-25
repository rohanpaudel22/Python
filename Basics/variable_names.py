"""
 Rules for python variables:
 
 -> variable name must start with letter or the underscore character
 
 -> variable name cannot start with a number
 
 -> variable name can only contain alpha-numeric characters and underscores
 
 -> variable names are case-sensitive
 
 -> variable name cannot be any of the python keywords 
"""

# Example:

myvar = "Rohan"
my_var = "Rohan"
_my_var = "Rohan"
myVar = "Rohan"
MYVAR = "Rohan"
myvar1 = "Rohan"

# Assigning multiple values

# 1. Many values to multiple variables

x , y , z = "Apple" , "Orange" , "Cherry"
print(x)
print(y)
print(z)

# 2. one value to multiple variables

a = b = c = "Banana"
print(a)
print(b)
print(c)


"""
  # Unpacking a Collection
  
  -> if we have a collection of values in a list, tuple etc. Python allows us to extract the values into variables. This is called unpacking.
"""
#Unpacking a list:

fruits = ["Orange" , "Apple" , "Cherry"]
k , l ,m = fruits
print(k)
print(l)
print(m)