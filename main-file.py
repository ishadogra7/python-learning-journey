# Step 2 --- create another file in the same folder 

# first way .... to write-----import specific things only
from mymodule import greet, pi_value
print(greet("amit"))
print(pi_value)



# 2nd way to write---- basic import
import mymodule

print(mymodule.greet("Amit"))
print(mymodule.pi_value)

#  3rd way to write --- import with alias(shorter name ) ----commonly used

import mymodule as mm

print(mm.greet("Amit"))
print(mm.pi_value)

#  4th way == import everything (generally discouraged)
from mymodule import *
print(mymodule.pi_value) # discouraged beacuse of it causes name conflict

### wheen you import something , then python searches through a list of folder location called sys.path

import sys
print(sys.path)

## if you dont get when file exist but path not found then you write with append

import sys
sys.path.append("C:/mymodule")


#### __pycache__  folder---------->>compiled version of your module(bytecodee), which lets Python load it faster the next time, instead of re-reading and re-translating your .py file every single time. You never need to touch this folder manually — Python manages it automatically.
# After importing your own module, you'll notice Python automatically creates a folder called __pycache__ with a .pyc file inside.


import antigravity

