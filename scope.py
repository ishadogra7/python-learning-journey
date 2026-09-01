# scope--> where variable can be accessed  in your program
# global Keyword

When you want to modify a global variable inside a function — use global keyword.
python
count = 0                # global variable

def increment():
    global count         # tell Python — use the global count
    count = count + 1    # modify global variable

increment()
increment()
increment()
print(count)             # output: 3 ✅

# without global keyword
count = 0

def increment():
    count = count + 1    # ❌ ERROR — Python treats count as local
                         # but local count has no value yet

increment()              # UnboundLocalError

#nonlocal Keyword

Used inside nested functions — to modify variable of outer function.
def outer():
    x = 10               # outer function variable

    def inner():
        nonlocal x       # use outer function's x
        x = 20           # modify it
        print(x)         # output: 20

    inner()
    print(x)             # output: 20 — modified by inner

outer()


# LEGB RULE--> pyhton searches for the variabbele in this order

L → Local       (inside current function)
E → Enclosing   (outer function if nested)
G → Global      (outside all functions)
B → Built-in    (Python built-in names like print, len)

  example :
x = "global x"            # Global

def outer():
    x = "enclosing x"     # Enclosing

    def inner():
        print(x)          # no local x → uses enclosing x

    inner()

outer()
# output: enclosing x









_________________________________________________________________________________-


#  slicing...extracting a portion of sequence such as...string , list , tuple.
basic syntax...  sequence[start:stop:step]

x = "Python"

print(x[1:4])

# positive indexing --> 0 ,1 ,2 ,3 ,4...n from starting to last index

# negative indexing---> -1, -2 ,-3...-n from last to start index


# in slicing .....

#if empty at start..
print(word[:3])     # start from 0

# if end  is empty..
print(word[3:])     # means till end or size of array , list or other

# coping of ssequence
number = [1,23,45,5]
copy  = number[:]
print(copy)               # copy
print(number[:])          # copy


# # shallow copy of list
# list2 = list1[:]


# using step
print(number[0:5:2])  #it can be also write this
print(numbers[::2])

# ########### very important for innterview..
word = 'python'
print(word[::-1])