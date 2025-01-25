# The while Loop:
'''
with the while loop we can execute a set of statements as long as a condition is true.
'''

i = 1
while i <6:
  print(i)
  i += 1
  
# The break statement:
# ->> with the break statement we can stop the loop even if the condition is true:
  
a = 1
while a < 7:
  print(a)
  if a == 4:
    break
  a +=1
  
#  the continue statement:
# ->> with the continue statement we can stop the current iteration, and continue with the next:

b = 0
while b < 8:
  b +=1
  if b ==3:
    continue
  print(b)
  
# The else statement:
# ->> with the else statement we can run a block of code once when the condition no longer is true

c = 1
while c < 7:
  print(i)
  c += 1
else:
  print("c is no longer less than 7")
  
