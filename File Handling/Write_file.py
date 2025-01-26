# Opening the file "Basics/casting.py" and append content to the file:

f = open("Basics/casting.py" , "a")
f.write("Now the file has more content!!!")
f.close()

# Now open and read the file after the appending:

f = open("Basics/casting.py" , "r")
print(f.read())

# opening the file "sample.txt" and overwrite the content:

f = open("File Handling/sample.txt" , "w")
f.write("Woops! I have deleted the content!!")
f.close()

f = open("File Handling/sample.txt" , "r")
print(f.read())

# Creating a New file:

f = open("File Handling/myfile.txt" , "x")

'''
--> "x" , create-- will create a file, returns an error if the file exists.

--> "a" , Append-- will create a file if the specified file does not exists

--> "w" , Write-- will create a file if the specified file does not exists
'''