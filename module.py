# MODULE=== module is just  a pyhton file containing pyhton code .(functions , variables) that you can inport and use it to you own code
#    ....instead of writing a code from scratch
#   ----- collection of ready made module called the standard library
  

# EXAMPLE OF REAL WORLD ===
#  1.. math ---for math operations
import math

print(math.sqrt(5),'\n', math.ceil(7.9),'\n', math.floor(8.0))


# 2... random---- for generating random values
import random
print(random.randint(1 ,1999))   # random number beteween limit
print(random.choice(['a' , 'b', 'c'])) # random picks from list

#### in OTP GENERATION , SHUFFLING QUIZ QUESTION , GAMES ,TRANING AND TESTING SET IN AI/ML


#  3...datetime--- working with the dates and time
import datetime
now = datetime.datetime.now()  # as it write , it give correct answer
print(now)
today = datetime.date.today()
print(today)

####  timestramping order , logging when data was collected , scheduling
###  in AI/ML --- timestramping order when the model trained


# 4.... os--- interacting with your operating system/files
import os
print(os.getcwd())  # shows currrnt folder path(cwd-- current working directry)
print(os.listdir())  # lists the files in current folder
print(os.__file__)

#### automatically finding /loading dataset files , organising project folder


# 5... json--- reading / writing json data

# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))
ṇ
# back_to_dict = json.loads(json_string)
# print(back_to_dict)
# print(type(back_to_dict))

### almost all the api's

# 6... time=== working with delays/measuring performance
import time
print("start")
time.sleep(5)  # puase time after 5 sec
print("end after the 5 sec")

####  measuring time to train models

#   7... calender module(specially shown in this lecture)

import calendar
print(calendar.month(2026,10))
print(calendar.isleap(2004))
print(calendar.calendar(2026))

# 8... rs--- regular expression is used to search for , match ,or extract specifific parts of text
import re
text = "my email is amit123@gmail.com"
match = re.search(r'\S+@\S' , text)
print(match.group())

# The basic regex symbols you should know (start here, don't learn all of regex at once)
# Symbol	Meaning	Example
# \d 	any digit (0-9)	   ||  \d+ matches "12345"
# \s	any space	       ||  matches blank spaces
# \S	any NON-space	   ||    matches letters/numbers/symbols
# +	one or more	       ||    \d+ matches "123" not just "1"
# *	zero or more	    ||  optional repeats
# .	any single character	||  a.c matches "abc", "axc"
# ^	start of text	    ||   ^Hello — text must start with "Hello"
# $	end of text	          || bye$ — text must end with "bye"

#   9 ... dir() and help()  -->> exploring what inside a module
import random
print(dir(random))  # This lists every function/variable available inside that module — great for discovering what's possible.

help(random.randint)

import os
print(dir(os))