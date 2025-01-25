thislist1 = ["Math" , "Social" , "science"]
print(thislist1)

'''
----- Ordered List-------

->> When we say that list are ordered, it means that the items have a defined order, and that order will not change.

->> Changeable: The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

->> Allow Duplicates: Since lists are indexed, list can have items with the same value:
'''

thislist2 = ["Math" , "Social" , "science","Math" , "Social" , "Science" ]
print(thislist2)

# List length:

thislist3 = ["Math" , "Social" , "science","Math" , "Social" , "Science" ]
print(len(thislist3))

# List items- Data types:
# List items can be of any data types:

list1 =["apple", "banana" , "cherry"]
list2 = [ 1, 4, 6, 8 , 9]
list3 = [ True , False , False]

# A list can contain different data types:

list = ["abc" , 44 , True, 55, "male"]

# type() function:
#  ->> From python perspective, lists are defined as objects with the data type 'list':
# <class 'list'>

mylist = ["Kathmandu" , "Pokhara" , "Sarlahi" , "Morang"]
print(type(mylist))

# List() Constructor:

# thislist = list(("math" , "science" , "Social" , "English"))
# print(thislist)


'''
 -------- Python Collections(Arrays)-----
 
 There are four collection data types in the python programming language:
 
 -> List: is a collection which is ordered and changeable. Allows duplicate members.
 
 -> Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
 
 -> Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members
 
 -> Dictionary: is a collection which is ordered** and changeable. No duplicate members.
 
 *Set items are unchangeable, but we can remove and/or add items whenever we like.
 
 **As of python version 3.7, dictionaries are ordered. In python 3.6 and earlier, dictionaries are unordered.
'''

# Accessing List items:

list6 = ["Apple", "Banana" , "Kiwi" , "Cherry" , "Mango" , "Melon" , "Orange"]

print(list6[4])
print(list6[-1]) # Negative indexing
print(list6[3:5]) # Range of indexes
print(list6[:4])
print(list6[2:])
print(list6[-4:-1])

# Checking if items Exists:

if "Mango" in list6:
  print("Yes, 'Mango' is in the fruits list")
  
  # ---------Changing List items:---------
  
  # 1. Changing item value:
  list7 = ["Apple", "Banana" , "Kiwi" , "Cherry" , "Mango" , "Melon" , "Orange"]
  list7[1] = "blackcurrant"
  print(list7)
  
  # 2. Changing a Range of item values:
  list7[1:3]= ["blackcurrant" ,"watermelon" ]
  print(list7)
  
  # Changing the second value by replacing it with two new values:
  
  list7[1:2]= ["blackcurrant" , "watermelon"]
  print(list7)
  
  # if we insert less items than we replace, the new items will be inserted where we specified, and remaining items will move accordingly:
  
  # Changing the second and third value by replacing it with one value:
  
  list8 = ["apple" , "banana" , "cherry"]
  list8[1:3] = ["watermelon"]
  print(list8)
  
  # Inserting items:
  '''
  ->> TO insert a new list, without replacing any of the existing values, we can use the insert() method.
  
  '''
  
  list9 = ["Apple" , "Banana" , "Cherry"]
  list9.insert(2 , "watermelon")
  print(list9)
  
  # -------- Adding List items:-------
  
  # 1. Append items:
  list10 = ["Apple" , "Banana" , "Cherry"]
  list10.append("orange")
  print(list10)
  
  # Extending List:
  '''
  ->> to append elements from another list to the current list, use the extend() method:
  '''
  
  list11 = ["Apple" , "Banana" , "Cherry"]
  tropical =["Pineapple" ,"papaya" , "Mango" ]
  list11.extend(tropical)
  print(list11)
  
  # Adding any Iterable
  
  '''
  ->> The extend() method does not have to append list, we cam add any iterable object(tuples, sets, dictionaries, etc.)
  '''
  
  thistuple = ("kiwi" , "Orange")
  list11.extend(thistuple)
  print(list11)
  
  # Removing specified item:
  
  list4 = ["apple" , "banana" , "pineapple"]
  list4.remove("banana")
  print(list4)
  
  # Removing specified index:
  # The pop() method removes the specified index
  
  list4.pop(0)
  print(list4)
  
  # If we do not specify the index, the pop() method removes the last item.
  
  list5 = ["Apple" , "Cherry" , "Banana" , "Pineapple" , "Orange" , "Kiwi" , "Watermelon"]
  list5.pop()
  print(list5)
  
  # The 'del' keyword also remove the specified index:
  
  del list5[0]
  print(list5)
  
  # The del keyword can also delete the list completely.
  
  del list4
  
  # Clearing the list:
  
  '''
  ->>> The clear() methods empties the list.
  ->>> the list still remains, but it has no content
  '''
  
  list5.clear()
  print(list5)
  
  # Loop through a list
  
  thislist0 = ["Apple", "Banana" , "Cherry"]
  for x in thislist0:
    print(x)
    
# Loop through the index numbers

'''
Using the range() and len() functions to create a suitable iterable.
'''
thislist22 = ["Math" , "Science" , "Social"]
for i in range(len(thislist22)):
  print(thislist22[i])
  
  
# Using a While Loop

thislist23 = ["Math" , "Science" , "Social"]
i=0
while i< len(thislist23):
  print(thislist23[i])
  i = i+1
  
# Looping Using list Comprehension:

thislist24 = ["Rohan" , "Rabin" , "Raman" , "Roshan"]
[print(x) for x in thislist24]