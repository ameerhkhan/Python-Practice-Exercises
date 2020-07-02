#python object oriented programming.

#1 - Creating and instantiating a Python class

# Allow us to logically group our data and function in a way that's easy to reuse as well as build upon.
# Method --> A function associated with a class

# Attribute --> A variable associated with a class

# classes are blueprints for creating instances.

# Each unique employee is an instance of the Employee_oop class.
class Employee_oop:
    def __init__(self, first, last, pay): #self --> variable name for created instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)
    
    def fullname(self, middle=None): #When calling methods use paranthesis at end to print it out.
        if middle == None:
            return('{} {}'.format(self.first, self.last))
        else:
            return('{} {} {}'.format(self.first, middle, self.last))



emp_1 = Employee_oop('Corey', 'Schafer', 50000)
emp_2 = Employee_oop('John', 'Doe', 60000)

print(emp_1.fullname()) 
print(emp_2.fullname('Jane'))


