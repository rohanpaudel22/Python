list1 = ["a" , "b" , "c"]
list2 = [1, 3 ,5]
list3 = list1 + list2
print(list3)

# Using 'append()' method to join list
list5 = ["d" , "e" , "f"]
list6 = [2, 4 ,6]

for x in list6:
  list5.append(x)
  
print(list5)

# Using 'extend()' method to join list:

list9 = ["g" , "h" , "i"]
list10 = [20, 40 ,60]

list9.extend(list10)
print(list9)