#  Datetime --> built in python module----- no installation needed

import datetime  #--------->>> import whole module
from datetime import date , datetime, timedelta  #---? import specific parts

### --> datetime  have 5 main classes
datetime module
├── date          → only date (year, month, day)
├── time          → only time (hour, minute, second)
├── datetime      → both date AND time together
├── timedelta     → difference between two dates
└── timezone      → timezone handling


#  1  --> date class 
from datetime import date

######  get today date
today = date.today()
print(today)

###### create specific date
d = date(2026 , 1 ,15)
print(d)

##### access parts separately
print(today.year)
print(today.month)

####   day of week -- monday = 0 , sunday=6
print (today.weekday()) # monday
print(today.isoweekday()) # monnday = 1 , sunday = 7


## convert date into string
print(str(today))
print(today.strftime("%d/%m/%Y"))  # 19/08/2026
print(today.strftime("%B %d , %Y"))


#  2... time class --- only time..
from datetime import time
 
# create time
t = time(14 ,30 , 45)  # hour , min, second
print(t)   

# acess parts
print(t.hour)  #14

# hour format
print(t.strftime("%I:%M %p"))  # 02:30 pm


#  3... datetime class 

from datetime import datetime

# get current date and time
now = datetime.now()
print(now)                # 2026-08-19 14:30:45.123456

# access parts
print(now.year)           # 2026
print(now.month)          # 8
print(now.day)            # 19
print(now.hour)           # 14
print(now.minute)         # 30
print(now.second)         # 45

# create specific datetime
dt = datetime(2026, 1, 15, 10, 30, 0)
print(dt)                 # 2026-01-15 10:30:00


  ############# conversion of time and string into each other


# convert to string using strftime
print(now.strftime("%d/%m/%Y %H:%M:%S"))   # 19/08/2026 14:30:45
print(now.strftime("%B %d, %Y"))           # August 19, 2026


#  strftime -->date to string
strftime means string format time — converts date/time to string.

from datetime import datetime

now = datetime.now()

# Most used format codes
print(now.strftime("%Y"))     # 2026          — 4 digit year
print(now.strftime("%y"))     # 26            — 2 digit year
print(now.strftime("%m"))     # 08            — month number
print(now.strftime("%B"))     # August        — full month name
print(now.strftime("%b"))     # Aug           — short month name
print(now.strftime("%d"))     # 19            — day number
print(now.strftime("%A"))     # Tuesday       — full day name
print(now.strftime("%a"))     # Tue           — short day name
print(now.strftime("%H"))     # 14            — hour 24 format
print(now.strftime("%I"))     # 02            — hour 12 format
print(now.strftime("%M"))     # 30            — minutes
print(now.strftime("%S"))     # 45            — seconds
print(now.strftime("%p"))     # PM            — AM or PM

######## commonly used in ai .ml project

now.strftime("%d/%m/%Y")           # 19/08/2026
now.strftime("%Y-%m-%d")           # 2026-08-19  ← used in your expense tracker
now.strftime("%d %B %Y")           # 19 August 2026
now.strftime("%d/%m/%Y %H:%M")     # 19/08/2026 14:30
now.strftime("%I:%M %p")           # 02:30 PM

# ............. conversion of  string to datetime


from datetime import datetime

# convert string to datetime
date_string = "19/08/2026"
dt = datetime.strptime(date_string, "%d/%m/%Y")
print(dt)                 # 2026-08-19 00:00:00
print(type(dt))           # <class 'datetime.datetime'>

# another example
date_string2 = "August 19, 2026"
dt2 = datetime.strptime(date_string2, "%B %d, %Y")
print(dt2)                # 2026-08-19 00:00:00



# 4 .. timedelta -->represent a duration and difference between two days
from datetime import date, timedelta

today = date.today()
print(today)               # 2026-08-19

# add days
tomorrow    = today + timedelta(days=1)
next_week   = today + timedelta(days=7)
next_month  = today + timedelta(days=30)

print(tomorrow)            # 2026-08-20
print(next_week)           # 2026-08-26
print(next_month)          # 2026-09-18

# subtract days
yesterday   = today - timedelta(days=1)
last_week   = today - timedelta(days=7)

print(yesterday)           # 2026-08-18
print(last_week)           # 2026-08-12

# difference between two dates
date1 = date(2026, 1, 1)
date2 = date(2026, 8, 19)
diff  = date2 - date1
print(diff.days)           # 230 days



# fromisoformat--> string to date
from datetime import date

date_str  = "2026-08-19"
d         = date.fromisoformat(date_str)
print(d)                   # 2026-08-19
print(type(d))             # <class 'datetime.date'>

# you used this in your expense tracker
expense_date = date.fromisoformat(expense_date_str)

# 5  comparision dates
from datetime import date

today     = date.today()
yesterday = today - timedelta(days=1)
past_date = date(2025, 1, 1)

print(today > yesterday)       # True
print(today == yesterday)      # False
print(past_date < today)       # True

# you used this in expense tracker get_date() function
if expense_date == today:
    return "Today"
elif expense_date == yesterday:
    return "Yesterday"





Quick Revision Table
Class/Method	What it does	Example
date.today()	Get today's date	2026-08-19
datetime.now()	Get current date + time	2026-08-19 14:30:45
strftime()	Date to string	"19/08/2026"
strptime()	String to date	date(2026,8,19)
timedelta(days=n)	Add/subtract days	today + timedelta(days=7)
fromisoformat()	ISO string to date	date.fromisoformat("2026-08-19")
.year .month .day	Get parts of date	today.year → 2026
.hour .minute .second	Get parts of time	now.hour → 14





ost Important Format Codes to Remember
Code	Meaning	Example
%Y	4 digit year	2026
%m	Month number	08
%B	Full month name	August
%d	Day number   	19
%A	Full day name	Tuesday
%H	Hour 24 format	14
%I	Hour 12 format	02
%M	Minutes     	30
%S	Seconds     	45
%p	AM or PM	    PM