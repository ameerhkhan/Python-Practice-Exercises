#Use employee class.
#This is basic OOP

#Check WHISKEY Exception class for more info and/or practical application of inheritance.

class Employee_in:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    
    def fullname(self):
        return('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    

class Developer(Employee_in):
    #special developer raise.
    raise_amt = 1.10
    #how to increase arguments for an inheritance:

    def __init__(self, first, last, pay, prog_lang):
        #we'll let employee handle first name last name and pay
        super().__init__(first, last, pay)
        #can also use, 
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee_in):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->\t {}'.format(emp.fullname()))
    


dev_1 = Employee_in('Corey', 'Schafer', 50000)
dev_2 = Developer('John', 'Doe', 100000, 'Python')
dev_3 = Developer('Jane', 'Doe', 30000, 'Java')

#Python has method, isInstance(inherited, main) to check inheritance)
#Python also has, issubclass(inherited, main) to check if a class is a subclass.


# manager_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(manager_1.email)

# manager_1.add_emp(dev_2)

# manager_1.print_emps()

# manager_1.remove_emp(dev_1)
# manager_1.print_emps()



# print(dev_1.pay)
# print(dev_2.pay)
# dev_2.apply_raise()
# dev_1.apply_raise()
# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# print(dev_2.pay)

# print(dev_2.prog_lang)
# print(dev_3.prog_lang)
# print(dev_3.email)