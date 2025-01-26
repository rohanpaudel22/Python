# --> To delete a file, we must import the OS module, and run its os.remove() function:

import os
# os.remove("File Handling/myfile.txt")

# Check if File exist:

if os.path.exists("File Handling/myfile.txt"):
  os.remove("File Handling/myfile.txt")
  
else:
  print("The file does not exist")
  
  # Delete Folder
  # ->> we can only remove empty folders.
  
  os.rmdir("foldername")