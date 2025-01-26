# --> to open a file for reading it is enough to specify the name of the file:

# f = open("filename.txt")
# Another way:
# f = open("filename.txt" , "rt")

'''
--> Because "r" for read, and "t" for text are the default values, we do not need to specify them.
'''

# Open a File on the server:

'''
->> to open the file, use the built-in open() function.

->> the open() function returns a file object, which has a read() method for reading the content of the file
'''

f = open("Basics/casting.py" , "r")
print(f.read())

# returning the 5 first characters of the file:

print(f.read(5))

# Read one line of the file:

print(f.readline())

# Read two lines of the file:

print(f.readline())
print(f.readline())

# Looping through the file line by line:

for x in f:
  print(x)
  
# Close Files:

f.close()