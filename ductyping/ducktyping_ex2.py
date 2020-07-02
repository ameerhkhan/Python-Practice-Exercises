# Duck Typing and Easier to Ask Forgiveness than Permission (EAFP).

person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
person = {'name': 'Jess', 'age': 23}

# LBYL (Non Pythonic) --> Look Before You Leave
if 'name' in person and 'age' in person and 'job' in person:
    print('{name} {age} {job}'.format(**person))
else:
    print('Missing some keys')

# EAFP (Pythonic) --> Easier to Ask Forgiveness than Permission
try:
    print('{name} {age} {job}'.format(**person)) # --> all Keyword Arguments (kwargs)
except KeyError as e:
    print('Missing {} key'.format(e))

my_list = [1, 2, 3, 4, 5, 6]

#Non Pythonic,
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('List has less than 6 elements.')

#Pythonic,
try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')

# Pythonic examples are more readable and are faster than non pythonic way
# since our program does not have to go through all of them at once to find the error.
# Program keeps running and if catches an error is stopped.
# Non Pythonic ways have their own benefits sometimes as well.


# Another example,
import os

my_file = 'Q:/Hamza/Python/Python_new_exercises/text.txt'

try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read)