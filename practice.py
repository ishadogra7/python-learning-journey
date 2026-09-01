import os
from datetime import datetime
#  1 ... where am i ?
print(os.getcwd() , '\n')  # get current working directory

# 2...what's here ?
print(os.listdir() ,'\n')

# 3... create a practise folder
os.makedirs("prac_folder",exist_ok = True)
print(os.path.exists("prac_folder"))

#  4 .. build a safe file path
path = os.path.join("prac_folder" ,"double.txt")
print(path)

# 5.. create a file to test with
with open(path ,'w') as f:
    f.write("hello maddhav , i am sure you are fine...")

print(os.getcwd())

# 6 .. get file info
info = os.stat(path)
print(info ,'\n ')

# 7.. walk through the folder
# for dirpath , dirnames , filenames in os.walk('python_code'): # when you write like this python_code then it find the file inside directory
for dirpath , dirnames , filenames in os.walk("d:\\python_code"):
     print(dirpath , "|||" , filenames ,"||||" , dirnames)

# 8 .. environment variable
print(os.environ.get("USERNAME"))    # FOR WINDOW
