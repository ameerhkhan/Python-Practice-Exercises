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

class Developer_oop(Employee_oop3):
    raise_amt = 1.4

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Or use Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager_oop(Employee_oop3):
    raise_amt = 2.0

    def __init__(self, first, last, pay, employeees=None):
        super().__init__(first, last, pay)
        if employeees is None:
            self.employeees = []
        else:
            self.employeees = employeees
    
    def add_emp(self, emp):
        if emp not in self.employeees:
            self.employeees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employeees:
            self.employeees.remove(emp)

    def print_emps(self):
        for emp in self.employeees:
            print('{}'.format(emp.fullname()))




emp_1 = Employee_oop3('Corey', 'Schafer', 50000)
emp_2 = Employee_oop3('John', 'Doe', 60000)

dev_1 = Developer_oop('Jane','Doe', 70000, 'Python')
dev_2 = Developer_oop('Bruce', 'Banner', 100000, 'Golang')

man_1 = Manager_oop('Tony', 'Stark', 100000000, [dev_1, dev_2, emp_2])


# print(dev_1.email)
# print(dev_2.prog_lang)
# print(man_1.fullname())
# print(man_1.pay)
# man_1.apply_raise()
# print(man_1.pay)

print(man_1.print_emps())

print(isinstance(man_1, Employee_oop3))
print(issubclass(Manager_oop, Employee_oop3))


#Find out Python Whiskey Class to find out more about subclasses and inheritance.
