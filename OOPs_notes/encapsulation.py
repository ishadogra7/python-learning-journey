# encapsulation ->>>>> keeping of data and the operations taht work on the data together, while controlling how the data is accessed or modified
# it uses conventions/name mangling

# 1 - Public------A normal variable is public.
class employee:
    def __init__(self):
        self.name = "isha"

emp = Employee("Rahul")

print(emp.name) # directly accessible from outside the class



# 2 protected conventions
class Employee:
    def __init__(self, salary):
        self._salary = salary     # _salary means this is intented for internal/subclass use

dev = Employee(90000)
print(dev._salary)

#  This is intended for internal use or use by subclasses


# 3. private / name mangled-- uses doble underscore to represent private variable

self.__age = 30           # __age is name-mangled, making it harder to access from outside the class
                           # "This is intended for internal use or use by subclasses
""".......................
Public
   ↓
name

Protected
   ↓
_name

Private
   ↓
__name

........................."""
 

# what is name mangling ?
# -->. Name mangling is a mechanism in Python that alters the name of a variable or method to make it harder to access from outside the class. When you define a variable with a double underscore prefix (e.g., __age), Python internally changes its name to include the class name, making it less likely to be accidentally accessed or modified from outside the class. This is done to provide a level of encapsulation and prevent naming conflicts in subclasses.

class Employee:
    def __init__(self, salary):
        self.__salary = salary

emp = Employee(90000)
#print(emp.__salary)   #this wil give an error because __salary is name-mangled and not directly accessible from outside the class.
print(emp._Employee__salary)  # 90000  # This is how you can access the name-mangled variable from outside the class, but it's not recommended as it breaks encapsulation.

"""
You write:

__salary

Python internally stores it as approximately:

_Employee__salary  """


# Why Does Python Do Name Mangling?  usesful in inheritance

# One major reason is avoiding accidental conflicts in subclasses.

class Parent:
    def __init__(self):
        self.__value = "Parent"

class child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "child"

# They don't accidentally overwrite each other.

#  Private Data + Methods -->>> 
class BankAccount:

    def __verify_account(self):
        print("Account verified")

    def withdraw(self, amount):
        self.__verify_account()
        print(f"Withdrawing ₹{amount}") 

account = BankAccount()
account.withdraw(5000)
#Name mangling isn't only for variables.
