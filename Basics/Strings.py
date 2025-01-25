print("Hello bruhh!!")
print('Hello there!!')


# Quotes inside Quotes

print("It's alright")
print("He is called 'Raman'")
print('He is called "Rohan"')

# Assigning string to a variable

a = "Hello"
print(a)

# Multiline Strings----- using double quotes

b = """This is the best programming language for the beginner to learn.This programming language follow the simple english but we have to care about indentation of this programming language which can also consider as the syntax for the python programming(as it does not have complex syntax rule comparing to other programming languages...) """

print(b)

# Multiline strings ---- using single quotes:

c = '''This is the best programming language for the beginner to learn, this programming language follow the simple english but we have to care about indentation of this programming language which can also consider as the syntax for the python programming(as it does not have complex syntax rule comparing to other programming languages...) '''

print(c)

# ------String are Arrays:-------

"""
  -> Strings in python are arrays of bytes representing unicode characters..
  
  -> Python does not have a character data type, a single character is simply a string with a length of 1
"""

# Getting the character at position 1:

d = "Rohan,Paudel"
print(d[1])


# ----Looping through a String:-----

# Looping through the letters in the word "apple":

for x in "apple":
  print(x)


# ------String Length:------

# The len() function returns the length of the string:

y = "Rohan Paudel"
print(len(y))

# ----- Check Strings-----
""" To check if a certain phrase or character is present in a string, we can use the keyword 'in'"""

# Checking if "life" is present in the following text:

txt = "The best things in life are free!"
print("life" in txt)

# Using it in an 'if' statement:

txt1 = "The best things in life are free!"
if "life" in txt1:
    print("Yes, 'life' is present")
    
    
# Check if NOT:

txt2 = "The best things in life are free!"
print("better" not in txt2)

txt3= "The best things in life are free!"
if "better" not in txt3:
    print("No, 'better' is not present")
    
    
# ----- Slicing Strings-----

# Getting the characters from position 2 and 5(not included):

z = "Rohan, Paudel!!"
print(z[2:5])

# Slicing form the Start:

# -> Getting the characters from the start to position 5(not included):

m = "Hello, siri"
print(m[:5])

# Slicing form the end:

# -> Getting the characters from position 2 , and all the way to the end:

n = "Hello, google!!!"
print(n[2:])

# Negative Indexing:
""" 
-> Using negative indexes to starts the slice from the end of the string.

-> Getting the characters:

      -> from: "o" in "World" (position -5)
      -> to , but not included: "d" in "world!" (position -2):

"""

h = "Hello, World!"
print(h[-5:-2])

# ----Modifying Strings------

# Upper Case:

q = "This is python programming language"
print(q.upper())

# Lower case:

l= 'ROHAN PAUDEL'
print(l.lower())

# Removing Whitespaces:

# -> WhiteSpace is the space before and/or after the actual text, and very often wee want to remove the space.

w = " Wavy, Wavy , Wavy , blallala! "
print(w.strip())


# Replacing String

r = "Hello, chicks!!!"
print(r.replace("H" , "I"))

# Split String:

# -> The split() method returns a list where the text between the specified separator becomes the list items.

s = "Hello, World!"
print(s.split(",")) # returns ['Hello' , 'World!']

# -----String Concatenation----

# -> Merging variable g with variable i into variable p:

g = "Raman"
i = "Paudel"

p = g +i
print(p)

#-> Adding space between word:
g = "Raman"
i = "Paudel"

p = g + " "+i
print(p)
