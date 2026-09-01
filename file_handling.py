# file handling -->> reading data from files and writing data into files
example ->student.txt
students.csv
model.pkl

# # ##  in ai/ml ,daata cannot always sstay inside python variables....

File/Dataset
     ↓
Read
     ↓
Python / Pandas
     ↓
Preprocessing
     ↓
ML Model
     ↓
Predictions
     ↓
Save Results

#  .. open()  --- most important
syntax---> 
file = open("filename.txt" ,"mode")

example--->
file = open("student.txt", "r")
but in real project prefer....                  with open()
                                                    ↓
                                                Open file
                                                    ↓
                                                Do your work
                                                    ↓
                                                Automatically close

with open("student.txt" ,"r")as file:      # with statement automaticcally closes the file... even if an error occur
    data = file.read()   
    print(data)                   


# File Mode-->
r------read
w------write
a------append
x------create new file
rb-----read binary
wb-----write binary


# 1... read
with open("data.txt","r") as file:
    data = file.read()

# 2... write
with open("data.txt","r")as file:
    file.write("hello")            # overwrite existing data#

# 3... append
with open("data.txt","a") as file:
    file.write("\n Machine Learning")

############ Reading a files -----------have 3 methods...

(A)---- read()------>  read the complete file
with open("data.txt","r") as file:
   data = file.read()
print(data)


(B)----readline()------>  reads one line
with open("data.txt","r")as file:
    print(file.readline())


(C)----readlines()------> reads all lines and give you a list
with open("data.txt","r")as file:
    data = file.readlines()
    print (data)

##########   reading large files---->particulary important for ai/ml

with open("large_data.txt","r")as file:
    for line in file:
        print(line)

#####    write() --> writes a string
with open("data.txt","w")as file:
    file.write('python')
    file.write('\nml')

####     writelines()---> writes multiple string
lines = ["python\n" ,"ai"]
with open("data.txt","w")as file:
    file.writelines(lines)


#  9 filePaths............
suppose your project looks like
...
Student_Project/
│
├── main.py
│
├── data/
│   └── students.csv
│
└── results/


strongly recommend pathlib...   ##pathlib makes path handling cleaner and more portable across operating systems.

from pathlib import path
file_path = Path("data") /"students.csv"
with open(file_path , "r")as file:
    data = file.read()

#####   encoding.... it helps python correctly handle chracters from different languages and avoids amny encoding problem
with open("data.txt","r",encoding="utf-8")as file:
    data = file.read()


## text file and binary file ........
with open("data.txt" ,"r") as file:
    data = file.read()

binary file..........
with open("images.jpg","rb")as file:
    data = file.read()


###############  csv
CSV ->comma separated values

example:

Name,Age,Marks
Isha,21,85
Rahul,22,90
Aman,20,78

you can read it with csv module\

import csv
with open("student.csv" ,"r") as file:
    reader = csv.reader(file)      #In Python, csv.reader is used to read and parse data from a CSV file line by line inside a while loop or for loop. It automatically splits each line of text into a clean list of words, handling tricky elements like commas inside quotation marks for you.
   
    next(reader)  # it genreally reads the next row.............While it is most commonly used with a for loop, you can use it with a while loop by using Python's next() function to manually pull the next row.
    for row in reader:
        print(row)

# for write inside csv 
import csv

with open("students.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(["Name", "Age", "Course"])
    csv_writer.writerow(["Isha", 21, "CS"])
    csv_writer.writerow(["Rahul", 22, "IT"])

####### write in csv file with DictWriter()
import csv

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Course"]

    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()

    csv_writer.writerow({
        "Name": "Isha",
        "Age": 21,
        "Course": "CS"
    })

    csv_writer.writerow({
        "Name": "Rahul",
        "Age": 22,
        "Course": "IT"
    })

# But because you're learning AI/ML, you will very often use Pandas instead:
import pandas as pd
df = pd.read.csv("students.csv")
print(df)

   # saving CSV with pandas
df.to_csv("cleaned_students.csv",index = False)




# JSON   -> USED TO STORE THE DATA PERMANENTLY
EXAMPLE:

{
    "name": "Isha",
    "age": 21,
    "skills": ["Python", "ML"]
}

import json
#read in json
with open("student.json", "r")as file:
    data = json.load(file)
print(data)

# write in json
with open ("student.json","w")as file:
    json.dump(data, file , indent = 4)




############### --------------remnenber-------------
json.load()   → JSON file → Python
json.dump()   → Python → JSON file

and .......
json.loads()  → JSON string → Python
json.dumps()  → Python → JSON string



## exception handling..........An exception is an error that occurs while the program is running.
try:
    # code that might cause an error
except:
    # what to do if error occurs

So:

try → code that might produce an error
except → handles the error



#example:   ---

try:
    with open("data.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File does not exist")


# common exception you should know...
 | Exception           | Example                           |
| ------------------- | --------------------------------- |
| `ZeroDivisionError` | `10 / 0`                          |
| `ValueError`        | `int("abc")`                      |
| `TypeError`         | `"10" + 5`                        |
| `IndexError`        | `arr[10]` when array is smaller   |
| `KeyError`          | Missing dictionary key            |
| `FileNotFoundError` | Opening a file that doesn't exist |
| `NameError`         | Using an undefined variable       |


# try - except - else
try:
    a = 10
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")

here :  
try → attempts the operation
except → runs only if an error occurs
else → runs only if no error occurs
finally runs whether an error happens or not

# finally:  finally runs whether an error happens or not

try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
finally:
    print("Program finished")   -->> this is particularly useful when working with files, databases and resources

# raise :  you can also deliberately create an exception using raise
example:

age = -5
if agee <0 :
    raise ValueError("age cannot be naegative")

############## important example or fie handling
try:
    file = open("data.csv", "r")
    data = file.read()
    print(data)

except FileNotFoundError:
    print("File does not exist")

finally:
    print("File operation completed")


    

########## handle multiple exceptions
try:
    x = int(input("Enter number: "))
    result = 10 / x
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")