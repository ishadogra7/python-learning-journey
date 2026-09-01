# boolean operator --->> true(1) or false(0)
# every condition you write eventually becomes one of these two values 

x = 10 
result = (x > 5)
print(result)
print(type(result))

# Stores True/False directly
is_adult = x >= 18

# if/else statement
if(is_adult): 
    print("hello")
else:
    print("no hello")

# boolean are also secreatly in python : True(1) , False(0)
print(True + 3)   # 4
print(False + 3)  # 3


# These combine multiple Boolean conditions into one final True/False result

# 1..and
age = 20
has_id = True
print(age >= 18 and has_id)

# 2..or
has_id = False
is_vip = True
print(has_id or is_vip)

# 3..not ---> reverse  the value
is_banned = False
print(not is_banned)


# combining multiople conditons
age = 29
is_banned = True
has_ticket = False

if age >=18 and has_ticket == True and is_banned == False:
#if has_ticket  == False:   #(if not has_ticket : )not has_ticket reads as "if has_ticket is NOT true"
    print('permission allowed')
else:
    print('not','\n')

#  demo ==example   === >>> short circuit demo in which the pyhton only reas left to right but it find true or false it return the first one
def left():
    print("this is left")
    return True

def right():
    print('this is right')
    return False

print('Testing and ...')
print(left() and right() , '\n') 

print("Testing or ...")
print(left() or right())

# find id of variables
a = 10
print (id(a))