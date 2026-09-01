# os module  --->> pyhton talk to your coputer os directly -->
#   navigating files ,reading file details , changing file details , 

import os
# 1.. Navigating files sysytem
print(os.getcwd())  
os.chdir("d:\\python_code") #change directry
print(os.getcwd())
     
     ## if the folder does'n exist then create a new directry
os.makedirs("d:\\python_code\\mainn" , exist_ok = True)  # make a neww directory if it doesn't exist
# os.chdir("d:\\python_code\\mainn")                       # chaange directory
print(os.getcwd())                                       # shows the current working directory
print(os.listdir())                                      # list files and folders in current directory



## to avoid a crash entirely

# import os
# target = "d:\\python_code\\mainn"

# if os.path.exists(target):
#     os.chdir(target)
#     print(os.getcwd())
# else :
#     print(target)


## 2... creating and removing directory
os.mkdir("nerffffS")            # create one, other folder
os.makedirs("def")          # create nested/inside folders at once
import os
os.remove("nef")             #os.remove() — deletes a file (not a folder!) permanently
os.rmdir("nerf")         #deletes an EMPTY folder
os.removedirs("mainn" )    # deletes NESTED empty folders

import shutil

shutil.rmtree("mainn")   #delete everything, no matter what's inside"

# 3rd ... rename files / folder
import os
os.rename("main.py" ,"main-file.py")

# 4th... getting file information == os.stat()
import os
file_info = os.stat("operators.py")
print(file_info)

# this information in bytecode and convert it into a raw timestramp into a readable date

from datetime import datetime

raw_time = file_info.st_atime
readable_time = datetime.fromtimestamp(raw_time)
print(readable_time)

# walking through folders ===>>os.walk()
####### MOST IMPORTANT TOPIC ###
for dirpath ,dirnames ,filenames in os.walk("d:\\python_code"):
   print("=" * 40)
   print("current path : "  , dirpath)      # which folder it's currently looking at
    print("directories : " ,dirnames)        # what subfolders exist inside that folder
    print("files : " , filenames)            # what files exist inside that folder
 

 ## 6th -->environment variable ====> os.environ
import os
print(os.environ.get("USERNAME"))

# os.path -->safe , cross-platform path handling
file_name = "dataset.csv"
file_path = os.path.join("d:\\python_code", "data", file_name)
print(file_path)

print(os.path.exists(file_path))     # True/False - does it exist
print(os.path.isfile(file_path))     # True if it's a file
print(os.path.isdir(file_path))      # True if it's a folder
print(os.path.basename(file_path))   # dataset.csv (just the filename)
print(os.path.dirname(file_path))    # d:\python_code\data (just the folder)
print(os.path.splitext(file_path))   # ('d:\\python_code\\data\\dataset', '.csv')


#8. Opening a file with its default program (Windows-specific)
os.startfile("loops.py")