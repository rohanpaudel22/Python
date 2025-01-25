# creating a class:

class MyClass:
  x = 5
print(MyClass)

# Creating Object:

p1 = MyClass()
print(p1.x)

#  The __init__()function:

'''
-->All classes have a function called __init__(), which is always executed when the class is being initiated.

-->> Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
''' 
# Creating a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name , age):
    self.name = name
    self.age = age
    
p1 = Person("Rohan" , 21)

print(p1.name)
print(p1.age)
  
# -->> The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() function:

'''
--> this function controls what should be returned when the class object is represented as a string.

-->> if this function is not set, the string representation of the object is returned:
'''

# The string representation of an object without the __str__() function:

class Person1:
  def __init__(self , name , age):
    self.name = name
    self.age = age
    
p2 = Person1("Raman" , 24)
print(p2)

# The string representation of an object with the __str__() function:

class Person2:
  def __init__(self , name , age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"name:{self.name}, age:{self.age}"
    
p3 = Person2("Raman" , 24)
print(p3)

# Object Methods:

class Person3:
  def __init__(self , name , age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)
    
per = Person3("Rohan" , 21)
per.myfunc()

'''
->> The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
'''

# Using the word mysillyobject and abc instead of self:

class Person4:
  def __init__(mysillyobject, name , age):
    mysillyobject.name = name
    mysillyobject.age = age
    
  def myfunc(abc):
    print("Hello my name is " + abc.name)
    # print(abc.age)
    
per1 = Person4("Raman" , 24)
per1.age = 40
del per1.age
per1.myfunc()

# Modify Object Properties:



