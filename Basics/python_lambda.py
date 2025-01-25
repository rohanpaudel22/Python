'''
->> A lambda function is a small anonymous function

->> A lambda function can take any number of arguments, but can only have one expression.

Syntax:

lambda arguments: expression
''' 

# Adding 10 to argument a , and return the result:

x = lambda a : a+10
print(x(5))

# Multiply argument a with argument b and return the result:

x = lambda a , b : a*b
print(x(5 , 6))

# Summarize argument a , b , c and return the result:

x = lambda a , b , c : a + b + c
print(x(5 , 7 , 2))

# Why use Lambda Functions??

'''
-->> The power of lambda is better shown when we use them as an anonymous function inside another function.

-->> say we have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda a : a *n
'''

# Using that function definition to make a function that always doubles the number we send in:

def my_func(n):
  return lambda a : a * n

mydoubler = my_func(2)

print(mydoubler(11))

