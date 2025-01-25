'''
-->> An iterator is an object that contains a countable number of values.

-->> An iterator is an object that can be iterated upon, meaning that we can traverse through all the values,

-->> Technically, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''

# Iterator vs Iterable:

'''
-->> Lists, tuples , dictionaries, and sets are all iterable objects. They are iterable containers which we can get an iterator from.
'''

mytuple = ("apple" , "banana" , "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Iterating objects:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator:
# ->> we can also use a for loop to iterate through an iterable object:

for x in mytuple:
  print(x)
  
# Creating an Iterator:

'''
-->> To create an object/class as an iterator we have to implement the methods __iter__() and __next__() to our object

--> The __iter__() method acts similar, we can do operations(initializing etc.), but must always return the iterator object itself.

->> The __next__() method also allows us to do operations, must return the next item in the sequence.
'''
# Creating an iterator that returns numbers, starting with 1 , and each sequence will increase by one(returning 1,2,3 ,4,5 etc.):

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration:

'''
-->> To prevent the iteration from going on forever, we can use the StopIteration statement.

-->> In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''

# Stop after 20 iterations:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <=20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
    
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)