# Creating a Parent Class:

class Person:
  def __init__(self, fname , lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self):
    print(self.firstname , self.lastname)
    
# Using the Person class to create an object, and then execute the printname method:

x = Person("John" , "Doe")
x.printname()

# Creating a Child Class:

class Student(Person):
  pass

x = Student("Rohan" , "Paudel")
x.printname()

# Add the __init__() function:

class Student(Person):
  def __init__(self , fname , lname):
    # add properties etc.
    
    '''
-->> when we add the __init__() function , the child class will no longer inherit the parents __init__() function

--->>> The child's __init__() function overrides the inheritance of the parent's __init__() function:
'''

class Student(Person):
  def __init__(self , fname , lname):
    Person.__init__(self , fname , lname)
    
x = Student("Aayush" , "Tharu")
x.printname()

# Use the super() function:

'''
-->> python also has a super() function that will make the child class inherit all the methods and properties from its parent:
'''

class Employee(Person):
  def __init__(self , fname, lname):
    super().__init__(fname , lname)
    
x = Employee("Ram" , "Sarki")
x.printname()

'''
-->> by using super() function, we do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
'''


class Student(Person):
  def __init__(self , fname, lname):
    super().__init__(fname , lname)
    self.graduationyear = 2022
    
x = Student("Mike" , "Olsen")
print(x.graduationyear)
   
   
class Student(Person):
  def __init__(self, fname , lname , year):
    
    super().__init__(fname, lname)
    self.graduationyear = year
    
x = Student("Mike" , "Olsen" , "2019") 
print(x.graduationyear)

# Adding Method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
 
x = Student("Rohan" , "Paudel" , 2025)   
x.welcome()