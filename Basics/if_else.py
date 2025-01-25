'''
python supports the usual logical conditions from mathematics:

->> Equals: a == b
->> Not Equals: a != b
->> Less than: a < b
->> Less than or equal to: a<= b
->> Greater than: a > b
->> Greater than a equal to: a >=b
'''
# if statement
'''a = 22
b = 222
if b>a:
  print("b is greater than a")
  '''
# elif statement
'''
c = 55
d = 55
if d > c:
  print("d is greater than c")
elif c == d:
  print("c and d are equal")
  '''
  
# else statement:

'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  '''
# Short Hand if:
'''
if a > b: print("a is greater than b")
'''
# Short Hand if else:
'''
print("A") if a > b else print("B")
'''
# One line if else statement, with 3 conditions:

'''
c = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
'''

# and keyword

'''
a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are True!!")
'''  
  # or keyword
  
'''
a = 200
b = 33
c = 50

if a > b or c > a:
  print("At least one of the conditions is true!!")
  '''
  
# not keyword:
'''
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  '''
# Nested if statement:

x = 44

if x > 10:
  print("Above ten,")
  if x > 55:
    print("and also above 55!")
  else:
    print("but not above 55.")

# The pass Statement:
'''
if statement cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error..
'''
a = 33
b = 300

if b<a:
  pass