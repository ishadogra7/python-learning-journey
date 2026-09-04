#1.. python class and objects ====>> before class and objects  , store data in variables and dictionaries ... but OPP's lets you store bundle data and behaviour into a reasonable unit.

'''  2..
Class vs Object
Term   ->	Meaning
Class	-> A blueprint/template for creating objects. Defines attributes & methods.
Object(Instance)	-> A specific realization of a class, with actual values.
'''

class student:
    pass    # skip for now, we will add attributes and methods later

student1 = student()  # creating an object of class student
student2 = student()  # creating another object of class student

print(student1)        # <__main__.student object at 0x000001F2D3A1BFA0>
print(student1 == student2) # False, because they are different objects in memory


# 3.. Creating a class -- __init__(the constructor)------>>>__init__ runs automatically when an object is created. It sets up instance variables (unique to each object).
class student:
    def __init__(self , first , last , age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first +'.'+last+'@school.in'

std1 = student("john" ,"doe",20)
std2 = student("janne" ,"kumar" ,27)

print(std1.age)
print(std2.email)

''' >> self refers to the instance itself. It must be the first parameter of every instance method (Python passes it automatically).
    >> Without __init__, you'd have to set attributes manually on every object one by one — repetitive and error-prone.'''


# real world example
class bankAccount:
    def __init__(self , owner, balance =0):
        self.owner = owner
        self.balance = balance
        
    def deposite(self , amount):
        self.balance += amount

    def withdraw(self , amount):
        if amount > self.balance:
            print("Insufiicient funds")
        else :
            self.balance -= amount

acc =bankAccount("ravi" , 1000)
acc.deposite(500)
acc.withdraw(800)
print(acc.balance)

# 4..instance methods-->>> regular functions defined inside a class that operate on instance data. Always take self as the first argument.

class employee:
    def __init__(self , first , last , pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return f" {self.first} {self.last}"
    
    def apply_raise(self , percent):
        self.pay = int(self.pay*(1 + percent))

emp= employee('John', 'Doe', 50000)
emp.apply_raise(50)
print(emp.pay)

# 5..class variable vs instance variables
# instance variables: unique per object (e.g., name, pay).
# class variable : : shared by ALL instances of the class (same value unless overridden).

# 6...Class Methods vs Static Methods vs Instance Methods
'''
Type	        Decorator	  First Argument	Used When
Instance method 	none	   self	         Needs access to instance data
Class method	 @classmethod	cls	         Needs access to class data / alternative constructors
Static method	@staticmethod	none	    logically related to the class but doesn't touch instance or class 
'''
from datetime import date
class employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first, self.last, self.pay = first, last, pay
    
    @classmethod 
    def set_raise_amount(cls ,amount):
        cls.raise_amount = amount     # changes it for the whole class
    
    @classmethod
    def from_string(cls , emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    
    @staticmethod
    def is_workday(day):
        # doesn't need self or cls -- pure utility function
        return day.weekday() != 5 and day.weekday() != 6


employee.set_raise_amount(1.05)
emp_3 = employee.from_string('Steve-Smith-30000')


print(employee.is_workday(date(2026, 9, 1)))