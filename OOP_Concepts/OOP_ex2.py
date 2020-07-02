# Class Variables --> Variables shared among all instances of a class.
# Instance varibales --> Variables unique to an Instance

class Employee_oop:

    raise_amt = 1.2 #--> This is a class variable. Since it remains same for all instances of the class.
    num_employees = 0

    def __init__(self, first, last, pay): #self --> variable name for created instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)

        Employee_oop.num_employees += 1 #increases on creation of every new instance.
    

    def fullname(self): #When calling methods use paranthesis at end to print it out.
        return('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        print('New Salary = %i'%self.pay)


emp_1 = Employee_oop('Corey', 'Schafer', 50000)
emp_2 = Employee_oop('John', 'Doe', 60000)

emp_1.apply_raise()
emp_2.apply_raise()

#How to change the Class Variable here?
Employee_oop.raise_amt = 1.10

print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(Employee_oop.num_employees)