#Itertools module is a collection of tools that allows us to use iterators in a fast and efficient way.

import itertools

#First method.

counter = itertools.count()
#can create an infinite loop
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


data = [100, 200, 400, 500]

#Now we want to associate above data with a key or similar things.
#for example,

daily_data = list(zip(itertools.count(), data)) #creates a tuple/iterator combining both count and above data.

print(daily_data)
#[(0, 100), (1, 200), (2, 400), (3, 500)]


#to start at a specific count as well as degine stepsize,
counter2 = itertools.count(start=5, step=3)
for count in range(6):
    print(next(counter2))


#let's look at another function ziplongest. pairs iterables together until longest iterable is exhasusted.

daily_data2 = list(zip(range(10), data))

daily_data3 = list(itertools.zip_longest(range(10), data))
print(daily_data3)

#NOW let's look at cycle function in itertools.
#Just cycles through a list repeatedly. Can be used to create functions that act according to situattion
#For example counter3 = itertools.cycle(['On', 'Off'])


counter3 = itertools.cycle([1,2,3])

for i in range(7):
    print(next(counter3))


#Now, Repeat Functions:
#For giving a function a repeat of constant values,
counter4 = itertools.repeat(2, times=3)

for i in range(9):
    try:
        print(next(counter4))
    except StopIteration:
        print('Stop Iteration executed')
    finally:
        pass


#example of repeat,
squares = list(map(pow, range(10), itertools.repeat(2)))
#Pow --> raises a number to a certain power.
#range --> iterator
#constant value.
print(squares)

#starmap --> takes arguments that are already paired together in tuples.

cubes = itertools.starmap(pow, [(0,2), (1,2), (2,2)])
print(list(cubes))


#Combination and Permutations Functions
#Combination --> order does not matter
#Permutation --> order does matter.
#but both of them don't repeat any of those values.

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2) #Basically combination.

for item in result:
    print(item)

print('Now Permutations')

perm_result = itertools.permutations(letters, 2)

for item in perm_result:
    print(next(perm_result))

#What if we wanted to allow repeat?
#can be used to crack passwords with brute attacks.
result_pr = itertools.product(numbers, repeat=4)

for item_pr in result_pr:
    print(item_pr)


result_re = itertools.combinations_with_replacement(numbers, 4)

for ietm in result_re:
    print(ietm)


#Now let's look at the chain function,
#We want to loop over multiple lists.
#we could combine all lists and then loop over them,
#combined = letter + numbers + names
#Above method is majorly computationally inefficient.
#Now we can use chains for much more efficent computing.

combined = itertools.chain(letters, numbers, names)

for iterm in combined:
    print(iterm)

#Slicing on an iterator,
result_5 = itertools.islice(range(10), 1, 5, 2) #list, start, stop, step

for itm in result_5:
    print(itm)

