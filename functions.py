############## functions

## def == definition of a function

      # without parameters
def func():
    print('hello')
func()


      # with parameters
def funct(name):    # name  is a parameter
    print(f'hello {name}')
funct("amit".upper())       #  amit is an argument


#  *args --- accepting unlimited positional arguments
#            used when you dont know how many values will be passed in the function

def neeww(*number):      # number  -- collect everything in a tuple
    return sum(number)

print(neeww(1 , 2, 3 ))

# **kwargs --- accepting unlimited keyword arguments
#            used when you dont know how many keyword arguments will be passed in the function
def show_details(**details):
    for key ,value in details.items():
        print(f'{key} : {value}')
show_details(name='ammit' , age =20 , city  = "delhi")


# local variable and the global variable


x = 10   #global variable


def show():
    x = 20  # local variable
    print(f"local  : {x}")
show()
print(f"global : {x}")


# lambda function --- (short one line function)
#     Used for small, throwaway functions — especially common with sorted(), map(), filter() (which you'll use a lot in AI/ML data work).   

square = lambda y : y**2
print(square(5))

dif = lambda y ,b :y % b
print(dif(10,6))

nums = [1 , 2, 3, 4, 7]
square = list(map(lambda y: y**3 , nums))
print(square)


# REAL WORLD EXAMPLE === a discount calculator example

def apply_discount(price , discount = 10):
    discount  = price * discount / 100
    return price - discount

print(apply_discount(1000 , 10))    # by ddefault discount is 10%
print(apply_discount(220, 20))   


#1.... Data cleaning functions (used constantly)
def clean_data(data):
    if data is None or data < 0:
        return 0
    return data
ages = [25 , 89,None , 34,67]
cleaned_ages = [clean_data(a) for a in ages]
print(cleaned_ages)

# 2....reusable preprocessing function

def normalize(value , min_val , max_val):
    return (value - min_val) / (max_val - min_val)
print(normalize(50 , 0 , 100))

# 3.... function with **kwargs - matches how model setting are passed in real ML librariess

def train_model(**setting):
    for key , value in setting.items():
        print(f"{key} : {value}")
train_model(learning_rate = 0.01 , epoches = 10 , batches = 54)