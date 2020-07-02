#Double underscore methods are called special/magic/dunder methods.

class Employee_spec:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): #Unambigous representation of Object meant for debugging.
        return("Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay))

    def __str__(self): #Representation of Object meant to be seen by an end user.
        return('{} - {}'.format(self.fullname(), self.email))
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())



emp1 = Employee_spec('John', 'Doe', 100000)
emp2 = Employee_spec('Jane', 'Doe', 110000)
emp3 = Employee_spec('Bruce', 'Banner', 2000000)

print(emp1)

#can also use,
print(emp2.__repr__())
print(emp3.__str__())


#There are also other internal ethids available in Python.
#such as, 

#print(int.__add__(1, 2))

#hence we can actually customize ADD method to work in a way we desire,
#A customized add method is given above.

print(emp1 + emp2)

#There are plenty of other examples such as the LEN method. and others.

#so we can basically customize all internal methods.

print(len(emp1))

#other methods included in documentation --> DUNDER METHODS IN PYTHON
#look at the TIME library for practical implementation of customizing dunder methods.