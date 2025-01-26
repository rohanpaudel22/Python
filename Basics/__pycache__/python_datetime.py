
'''
-->> A date in python is not a data type of its own, but we can import a module names datetime to work with dates as date objects.
'''

import datetime
x = datetime.datetime.now()
print(x)

# Returning the year and name of weekday:

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects:

'''
->> To create a date, we can use the datetime() class (constructor) of the datetime module.
'''

y = datetime.datetime(2025 , 1  ,26)
print(y)


# The strftime() Method:

'''
-->> formatting date objects into readable strings.

-->> 
'''

z = datetime.datetime(2024 , 5 , 2)

print(z.strftime("%B"))