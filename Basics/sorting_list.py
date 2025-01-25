
# sort() method that will sort the list alphanumerically, ascending, by default:
fruits = ['apple' , 'banana', 'cherry', 'pineapple' , 'orange', 'kiwi' , 'avocado', 'mango']
fruits.sort()
print(fruits)

num1 = [100 , 40, 50 , 30 , 10 , 77 ]
num1.sort()
print(num1)

# Sorting in descending order
'''
-->> to sort descending, use the keyword argument: reverse = True
'''
num2 = [4 , 5, 9 , 1 , 2, 0 , 55, 66 , 33 , 100]
num2.sort(reverse= True)
print(num2)

# Customize Sort Function:
'''
->> We can also customize our own function by using the keyword argument: key = function

->> the function will return a number that will be used to sort the list(the lowest number first)
'''
# Example: Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

num3 = [50 , 44 , 52 , 48 , 100 , 51 , 33 ,55]
num3.sort(key = myfunc)
print(num3)

# Case Insensitive Sort
'''
->> By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
'''
# Example

fruits1 = ['Apple' , 'banana', 'cherry', 'Pineapple' , 'Orange', 'kiwi' , 'avocado', 'mango']
fruits1.sort()
print(fruits1)

'''
-->> so if we want a case-insensitive sort function, use: str.lower as a key function:
'''
fruits2 = ['Apple' , 'banana', 'cherry', 'Pineapple' , 'Orange', 'kiwi' , 'avocado', 'mango']
fruits2.sort(key =str.lower)
print(fruits2)

# Reverse order:
fruits3 = ['Apple' , 'banana', 'cherry', 'Pineapple' , 'Orange', 'kiwi' , 'avocado', 'mango']
fruits3.reverse()
print(fruits3)
