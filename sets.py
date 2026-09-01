#  set==>set is the collection of the unique and unordered elements

# create a set
fruits ={ 'apple' , 'mango' , "banana"}
print(fruits , '\n') 

# type
s = {}
print(type(s) , '\n')

j = set()
print(type(j))

# sets not allowed index accessing by using the index function 
   # only access through thee loop
for x in fruits:
    print(fruits ,'\n')

# add elements
fruits.add("lichi")
print(fruits)


# add multiple elements through update function
fruits.update(["graapes" , "oranges"])
print(fruits)

# remove 
fruits.remove("banana")
print(fruits)

# discard
fruits.discard("banana")

#pop
fruits.pop()
print(fruits)

# clear===> clear all elements in set
 
# length

# copy

# membership == for true or false

print('banana' in fruits)

### set operations

A = {1, 2, 3}
B = {3, 4, 5}

# 1.. union
print(A|B)

# 2.. intersection
print(A & B)

# 3.. difference
print(A-B)

# 4..symmetric diffrence--->Elements in either set, but not both {print all elements except the similar one}
print( A^ B)