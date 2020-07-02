import itertools
import operator


# with open('test_iter.log', 'r') as f:
#     #file is also an iterator
#     header = itertools.islice(f, 3) #for our header. This should grab the first three lines of the file.

#     for line in header:
#         print(line, end='')


#Now lets look at the compress function. Returns an iterator that corresponds to true values in selectors.

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)

for item in result:
    print(item)

#better than filter as it uses function to determine wheter something is True or False,
#For filter you have to create a function. Maybe using lambda, or a dedicated function.

# #other notable functions, 
# ==================================================
# itertools.dropwhile(filtering_function, list)
# itertools.takewhile(filtering_function, list)
# ==================================================


#let's look at another function, called Accumulate,

result_acc = itertools.accumulate(numbers)

for iytem in result_acc:
    print(iytem)
#Above function added the values.
#if we want to multiply,

nums = [1, 2, 3, 4, 5, 6]

result_mul = itertools.accumulate(nums, operator.mul)

for yt in result_mul:
    print(yt)



#Finally Last Function:
#Groups values based on certain key.
#Combines key and value in a tuple.

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Bruce Wayne',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Thor Odinson',
        'city': 'New_Asgard',
        'state': 'Norway'
    },
    {
        'name': 'Valkyrie',
        'city': 'New_Asgard',
        'state': 'Norway'
    }
]

#how will we group all members by state?
#we will use, can be used to group people such as who got As, Bs
#price of cars etcetra


def get_state(person):
    return person['state']

group_by_state = itertools.groupby(people, get_state)


for key, group in group_by_state:
    print(key)#, len(list(group)))
    for person in group:
        print(person)
    print()
    #print(len(list(group)))

#================================================
#how to replicate an iterator??

copy1, copy2 = itertools.tee(group_by_state)
print(copy1)
print(copy2)
