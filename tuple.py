# Tuple ===>> is used for storing multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# tuple is a collection of diffrent data strucuture but for permanent save
# example === days of a week

days = ('Monday' , 'Tuesday' ,'Wednesday' , 'Thursday' , 'Friday' , "Saturday" , 'Sunday')
print(days ,'\n')

location = {
    (10 , 20) : "Home"  ,
    (30 , 40) : "school"
} 
print(location[(10,20)])

# 1 .count()
print(days.count('Monday'))

# 2 . index()
print(days.index('Tuesday'))

# other build in functions

#  length
print(len(days))

# min
print(min(days))

# max
print(max(days))

# sum only works for the integer
#print(sum(days + ("0",)))

# string Tuple ===> combine all the string by using join
print(" ".join(days))

# sorted
sorted_tuple = tuple(sorted(days))
print(sorted_tuple)


# If you want to add an element to a tuple  by adding another tuple in it
days = days + ('Holiday' ,)
print(days)