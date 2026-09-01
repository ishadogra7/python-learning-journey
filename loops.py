# loops and iterations

nums = [1 ,2, 3 ,4 ,5]
for num in nums:
    print(num , end = " ")  # when i put end =' ' it makes gap beteen number and the print in the straight lineprint('\n')

print('\n')


# two keywords are used in the loops and iterations in python

#1... break statements

for num in nums:
    if num == 2:
        print(f"Found {num}")
        break                 # stop the loop immediately when the condittion is met
    print(num)
print('\n')

# 2.. continue statements == skip the current step but keep looping

for num in nums:
    if num ==2:
        print(f"found{num}")
        continue   #skip 2 but print all the other numbers
    print(num)
print('\n')

# 3... pass statement == it is used when the statement is required syntactically but you do not want any command or code to execute
     #  Used when you're writing structure first and will fill in logic later — doesn't affect the loop at all.
for num in nums:
    if num == 3:
        print(f"Found {num}")
        pass  # does nothing, just a placeholder for later codes
    print(num)


# nested loops
for num in nums:
    for letter in 'abc':
        print (f"{num} {letter}")


# range function 
for i in range(4):
    print(i)    # prints 0,1,2,3

for i in range(1, 6):
    print(i)    # prints 1,2,3,4,5 == it include the first one and exclude the last one(start, stop)

for i in range(1 , 10 , 3):
    print(i)    # prints 1,4,7 == it include the first one and exclude the last one(start, stop, step)

# looping over string
for letter in "isha":
    print (letter)   # prints i,s,h,a

# loopin over the dictionary
student = {"name" : "isha" , "age" : 28}
for key , value in student.items():
    print(key , " :" , value)



# while loop  ===> when you don't know how many times , only the condition is true

count = 0
while count < 5 :
    print(count)
    count = count + 1 


###################################

# real world example of using loops

# 1... proceesing every item in a list(shopping cart total)

prices = [10, 500 , 850 ,60 ]
total  = 0 
for price in prices:
    total = total + price
print(f"total amount :{total}")


# 2... repeating until a task successful(login attempts limiter)

attempts = 0
while attempts < 3:
    password = input("Enter your password : ")
    if password == "12345":
        print("Login Successsful")
        break
    attempts +=1
else:
    print("Too many attempts")

# 3... reading  a file line by line

    # STEP 1 : CRETAE A SAMPLE FILE
with open("data.txt", "w") as file:
    file.write("Hello\n")
    file.write("World\n")
    file.write("This is a test file.\n")
    
    # STEP 2 : READ LINE BY LINE
for line in open("data.txt", "r"):
    print(line.strip())  # strip  rmeoves the extra newline

# 4 .. sending emails to the users
users = ["amit@mail.com", "riya@mail.com"]
for user in users:
    print(f"Sending email to {user}")

# 5... building word frequency count (nlp basics)

words = ["cat", "dog", "cat", "bird", "dog", "cat"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word] =1

print(word_count) 