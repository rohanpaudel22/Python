fruits = ("apple" , "orange" , "cherry")
(green , yellow , red) = fruits
print(green)
print(yellow)
print(red)
'''
The number of variables must match the number of values in the tuple, if not we must use an asterisk to collect the remaining values as a list.
'''
fruits1 = ("apple" , "banana", "cherry", "pineapple" , "orange", "kiwi" , "avocado", "mango")

(ram , harry ,*roman ) = fruits1
print(ram)
print(harry)
print(roman)

fruits2 = ("apple" , "banana", "cherry", "pineapple" , "orange", "kiwi" , "avocado", "mango")

(ramm , *harryy ,romann ) = fruits2
print(ramm)
print(harryy)
print(romann)