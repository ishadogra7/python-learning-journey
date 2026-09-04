# Inheritance allows a child/subclass to reuse functionality from a parent/base class.
# syntax
class Child(Parent):
    pass


# common functionality
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    pass

dev = Developer("John", "Doe", 50000)
print(dev.email)          # John.Doe@email.com
print(dev.pay)          # 50000


# Method Overriding --->> a child class can replce the parrent's behaviour

class teacher:
    def work(self):
       return "teaching"
                            # when we print insted of return then it also print none to complete the function

class student(teacher):
    def work(self):
        return "learning"

e = teacher()
d = student()
print(e.work())         # teaching  
print(d.work())        # learning



## super() function --> allows you to call methods from a parent class inside a child class.
class employee:
    def __init__(self, first ,last , pay):
        self.first = first
        self.last = last
        self.pay = pay

class developer(employee):
    def __init__(self , first ,last, pay , language):
        super().__init__(first , last , pay)   #calls the appropriate parent implementation.
        self.language = language
    
# super() follows Python's Method Resolution Order (MRO).
# That's particularly important with multiple inheritance.
# Python's inheritance system supports multiple base classes and uses MRO to determine the order in which classes are searched.

class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(B):
    pass

c = C()
c.show()

print(C.mro())

# isinstance() -> used to  check wheather an object is an instance of a class
# issubclass() ->checks the relationship between the classes

# Why employees=None Instead of employees=[]? because the same default list can be reused across calls in brakets


#######  types of  inheritance:=
# 1 . single inheritance
class b(a):
    pass

# 2. multilevel inheritance
class b(a):
    pass

class a(c):
    pass

# 3.hierarchical inheritance
class b(a):
    pass

class c(a):
    pass

# 4.multiple inheritance ....Python supports multiple inheritance
class n(a , b):
    pass

# 5 .. hybrid inheritance--> combination of mutiple inheritance structure


################## the diamond problem #################
'''
       A
      / \
     B   C
      \ /
       D   
       
     D inherits from both B and C.

If both eventually inherit from A, which version should Python use?

Python handles this using MRO (Method Resolution Order).

Example:

 #####   print(D.mro()) ---> tells the structure of it

Python's C3 MRO determines the order.

This is one reason super() is preferable to hardcoding parent calls in complex inheritance structures.  
       '''
