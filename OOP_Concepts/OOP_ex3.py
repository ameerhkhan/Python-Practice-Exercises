# Class Methods --> Takes in class as the first argument
# Discover more in the TIME class of python.

import datetime

class Employee_oop3:

    raise_amt = 1.2 #--> This is a class variable. Since it remains same for all instances of the class.
    num_employees = 0

    def __init__(self, first, last, pay): #self --> variable name for created instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)

        Employee_oop3.num_employees += 1 #increases on creation of every new instance.
    

    def fullname(self): #When calling methods use paranthesis at end to print it out.
        return('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        print('New Salary = %i'%self.pay)


    @classmethod #This is a class method and instead of self we use cls as a convention
    def set_raise_amt(cls, amount): #cls --> variable for class instance
        cls.raise_amt = amount
    
    @classmethod #alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod #don't take instance or class as their first argument and behaves just like a normal function would.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    
    


emp_1 = Employee_oop3('Corey', 'Schafer', 50000)
emp_2 = Employee_oop3('John', 'Doe', 60000)

Employee_oop3.set_raise_amt(1.10)

print(Employee_oop3.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#Creating new instances from Strings
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jane-Doe-90000'

new_emp_1 = Employee_oop3.from_string(emp_str_1)
new_emp_2 = Employee_oop3.from_string(emp_str_2)

print(new_emp_1.fullname())

my_date = datetime.date(2020, 6, 20)
print(Employee_oop3.is_workday(my_date))