'''
->> List comprehension offers a shorter syntax when we want to create a new list based on the values os an existing list

For example:

-->> Based on a list of fruits, we want a new list, containing only the fruits with the letter "a" in the name.

-->> Without list comprehension we will have to write a for statement with a conditional test inside:
'''
fruits = ['apple' , 'banana', 'cherry', 'pineapple' , 'orange', 'kiwi' , 'avocado', 'mango']
newlist =[]

for x in fruits:
  if "l" in x:
    newlist.append(x)
print(newlist)

# with list comprehension we can do all that with only one line of code:

fruits1 = ['apple' , 'banana', 'cherry', 'pineapple' , 'orange', 'kiwi' , 'avocado', 'mango']

newlist1 = [ x for x in fruits1 if "n" in x]
print(newlist1)

# The Syntax
'''
newlist = [expression for item in iterable if condition == True]

->> The return value is a new list, leaving the old list unchanged
'''
# Condition:
'''
->> The condition is like a filter that only accepts the items that valuate to True.
'''
# Example of condition:

newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)
'''
-->> the condition if x != "apple will return True for all elements other than "apple", making the new list contain all fruits except "apple"

->> The condition is optional and can be omitted:
'''
# with no 'if' statement:

newlist3 = [x for x in fruits]
print(newlist3)

# Iterable:

newlist4 = [x for x in range(10)]
print(newlist4)

# with a condition: accept only numbers lower than 5:

newlist5= [x for x in range(10) if x<5]
print(newlist5)

# Expression:
newlist6 = [x.upper() for x in fruits]
print(newlist6)

# setting all values in the new list to 'hello':
newlist7 = ['HELLO' for x in fruits]
print(newlist7)

'''
The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
'''
# Return "orange" instead of "banana":
newlist8 = [x if x != "banana" else "orange" for x in fruits]
print(newlist8)

'''The expression in the example above says:
"Return the item if it is not banana, if it is banana return orange".
'''