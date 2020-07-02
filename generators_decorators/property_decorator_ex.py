#Property decorator allows our class attributes getter setter and and deleter functionality like 
#you may have seen in some other languages.
#Property decorator allows us to define a method that we can access like an attribute.

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + '_' + last + '@email.com'

    @property
    def fullname(self):
        return('{} {}'.format(self.first, self.last))
    
    @property #getter
    def email(self):
        return('{}_{}@email.com'.format(self.first, self.last))
    
    #setter --> name same as fullname or what we will get as an input
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter #deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

emp_1.fullname = 'Corey Schafer' #We are going to need a setter for this to happen.


print(emp_1.first)
#print(emp_1.email())
#With @property we don't need to use () to get our email called as an attribute
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname