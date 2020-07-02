class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return('({}, {}, {})'.format(self.name, self.age, self.salary))


from operator import attrgetter

e1 = Employee('Khan', 29, 70000)
e2 = Employee('Rao', 2, 80000)
e3 = Employee('Mir', 30, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.age

# Lists with classes require a KEY to sort!!
# key can contain any function. Built in or self generated or even LAMBDA functions.!

s_employees = sorted(employees, key=e_sort, reverse=True)
l_employees = sorted(employees, key=lambda e: e.name) #flexible!!
a_employees = sorted(employees, key=attrgetter('salary'))

print(s_employees)
print(l_employees)
print(a_employees)