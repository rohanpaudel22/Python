print(10>9)
print(10==9)
print(10<9)

# when we run a condition in an if statement, Python returns True or False:

a = 20
b = 2

if b>a:
  print("b is greater than a")
  
else:
  print("b is not greater than a")
  
  '''
# Evaluating values and Variables

# ->> The bool function allows us to evaluate any value, and give us True or False in return,
'''
# Evaluating a string and a number
print(bool("Rohan"))
print(bool(15))
print("\n")

# Evaluating two variables":

a = "Rohan"
b = 19

print(bool(a))
print(bool(b))
print("\n")

'''
------ Most Values are True-----

-> Almost any value is evaluated to True if it has some sort of content.

-> Any string is True, except empty strings.

-> Any number is true, except 0.

-> Any list, tuple, set, and dictionary are True, except empty ones.
'''
print(bool("abc"))
print(bool(123))
print(bool(["apple", "Cherry" , "banana"]))
print("\n")

# Some False Values are:

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("\n")

'''
->>> One more value, or object in this case, evaluates to False, and that is if we have an object that is made from a class with a __len__ function that returns 0 or False:
'''

class myclass():
    def __len__(self):
      return 0
    
myobj = myclass()
print(bool(myobj))

# Function can return a Boolean:

def myFunction():
  return True

print(myFunction())

# ->> We can execute code based on the boolean answer of a function:
# ->> Printing 'Yes' if the function returns True, otherwise print "No":

# def myFunction():
#   return False

def myFunction():
  return True

if myFunction():
  print("Yes!!!")
  
else:
  print("No!!!!!")
  
  
# 'isinstance()' function, which can be used to determine if an object is of a certain data type:

d = 3
print(isinstance(d , int))
print(isinstance(d , float))


