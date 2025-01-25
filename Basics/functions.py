# Creating a function:

def my_function():
  print("Hello from a function")
  
# Calling a function:

my_function()

# Arguments:

def my_function1(fname):
  print(fname)
  
my_function1("Rohan")
my_function1("Raman")
my_function1("Roshan")

# Parameters or Arguments??

'''
-->> The terms parameter and argument can be used for the same thing: information that are passed into a function.

--> From a functions perspective:

    -> A parameter is the variable listed inside the parentheses in the function definition.
    -> An argument is the value that is sent to the function when it is called.
'''

# Number of Arguments:

def my_func(fname , lname):
  print(fname + " " + lname)
  
my_func("Rohan", "Paudel")

# Arbitrary Arguments, *args

'''
-->> if we do not know how many arguments that will be passed into our function, add a * before the parameter in the function definition.

->> This way the function will receive a tuple of arguments, and access the items accordingly:
'''

def my_function3(*fname):
  print("First name: " + fname[2])
my_function3("Rabin" , "Rohan" , "Raman")

# Keyword Arguments:
'''
-->> we can also send arguments with key = value syntax
-->> This way the order of the arguments does not matter.
'''

def my_func1(child3 , child2 , child1):
  print("The youngest child is " + child3)
  
my_func1(child1 ="Emil" , child2 = "Tobias" , child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
'''
-->> the function will receive a dictionary of arguments, and can access the items accordingly:
'''
# --> if the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_func2(**kid):
  print("His last name is " + kid["lname"])
  
my_func2(fname = "Tobias" , lname ="Sarki")

# Default Parameter Value:

def my_func3(country = "Norway"):
  print("I am from " + country)
    
my_func3("Sweden")
my_func3("Nepal")
my_func3()
my_func3("USA")

# Passing a List as an Argument:

def func(food):
  for x in food:
    print(x)
    
fruits = ["apple" , "banana" , "cherry"]
func(fruits)

# Return Values:

def func2(x):
  return 5 * x

print(func2(3))
print(func2(5))
print(func2(9))

# Positional-Only Arguments:

'''
->> We can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

-> to specify that a function can have only positional arguments, add , / after the arguments:
'''

def my_function4(x , /):
  print(x)
my_function4(5)

'''
--> without the , / we are actually allowed to use keyword arguments even if the function expects positional arguments:

'''

def my_func4(x):
  print(x)
my_func4(x = 9)

# Keyword-Only Arguments:
'''
--> to specify that a function can have only keyword arguments , add * , before the arguments:
'''

def my_func5(* , x):
  print(x)
my_func5(x = 9)

# Combine Positional-Only and Keyword-Only:

def function(a , b, /, * , c , d):
  print(a + b + c + d)
  
function(5 , 6 , c = 7 , d = 8)

# Recursion:

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k -1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)