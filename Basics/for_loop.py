# with the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple" , "banana" , "cherry"]
for x in fruits:
  print(x)
  
# Looping through a String
# ->> even strings are iterable objects, they contain a sequence of characters:

for x in "banana":
  print(x)
  
#  The break statement 
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# -->> Exit the loop when x is "banana" , but this time the break comes before the print:

for x in fruits:
  if x == "banana":
    break
  print(x)
  
# The continue statement:

for x in fruits:
  if x == "banana":
    continue
print(x)

# The range() function:

for x in range(6):
  print(x)
print("\n")
  
for x in range(2 , 8):
  print(x)
print("\n")
  
'''
->> the range() function defaults to increment the sequence by 1 , however it is possible to specify the increment value by adding a third parameter: range(2 , 30 , 3):
'''
# Increment the sequence with 3:

for x in range(2 , 20 , 3 ):
  print(x)
  
# Else in for loop:
# ->> the else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(8):
  print(x)
else:
  print("Finally finished!!!")
  '''
  -->> the else block will NOT be executed if the loop is stopped by a break statement
  '''
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!!")
  
# Nested Loops:
'''
-->> the "inner loop" will be executed one time for each iteration of the "outer loop":
'''
# Printing each adjective for fruit:

adj = ["red" , "big" , "tasty"]
fruits = ["apple" , "banana" , "cherry"]

for x in adj:
  for y in fruits:
    print(x,y)
    
# The Pass Statement:
# ->> for loops cannot be empty, but if for some reason have a for loop with no content, put in the pass statement to avoid getting an error:

for x in [0,1,2]:
  pass