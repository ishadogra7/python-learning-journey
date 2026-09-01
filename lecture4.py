# lists ---->> store different type of data in a string

courses = ['python' , 'java' , 'c++' , 'c#' , 'js']
print(courses)
print(courses[0:3],'\n')  # it access the range of elements in a list
print(courses[0][2]  , '\n')    # it access the particular char in a string  in a list
# print(courses[10][2])    # when it goes out of thee index then it gives error 
 
 
 
# methods in list ....

# 1.change an element in a list
courses[0] = 'python3'
print(courses ,'\n')

# 2.append an element in a list
courses.append('ruby')
print(courses ,'\n')

# 3. insert an element in a list
courses.insert(1 , 'php')
print(courses ,'\n')

# 4.remove an element in a list
courses.remove('java')
print(courses , '\n')

# 5.pop an element in a list........... only for 1 index or number in a list
courses.pop(0)
print(courses , '\n')

#  for multiple it can be done by the del function 
del courses[0:2]
print (courses , '\n')

# clear a list

# 6.length of a list
print(len(courses),'\n')

# 7.looping through a list
for i in courses:
    print(i)
## ........enumerate function in a list
for index, course in enumerate(courses):
    print(index, course)



# 8.................sort a list
courses.sort()  
print(courses , '\n')

# sort in decending order
courses.sort(reverse = True)

# sorted ---> it does not changes the original list but it returns a new list
new=sorted(courses) 
print(new ,'\n')

# 9.slicing a list .... used to access a range of elements in list
print(courses[1:1],'\n') #empty list when accessing  the range of elements in a list and the range is not available in the list
print(courses[0:4])    #The slice includes the start index (1) but excludes the end index (4)

# 10. no. of list added to the another list through extend method
courses2 = ['go', 'rust']
courses.extend(courses2)
print(courses, '\n')

# 11.reverse a list
courses.reverse()
print(courses , '\n')

# 12. min and max in a list
print(min(courses))
print(max(courses))

# 13. index of an element in a list 
# print(courses.index('artificial intelligence'))......... provides an error
#   .. by truue or false
print('c#' in courses)

# 14.join function in a list
join_fun = ' , '.join(courses)
print( join_fun)

# 15. split function in a list-->convert a string into a list
  #.... split by spaces(default)
words = join_fun.split()
print(words, '\n')
  #....split by comma
words = join_fun.split(',')
print(words ,'\n')
  #...Split using a hyphen
words = join_fun.split('-')
print(words ,'\n')

# 16. count an element in a list/
print(courses.count('python'))