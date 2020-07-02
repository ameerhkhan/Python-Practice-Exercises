# very good for creating lists easily
# and also help in reading, modifying lists, generators etc.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums]
print(my_list)

# let's complicate

sq_list = [n**2 for n in nums]
print(sq_list)

# or you can use map with lambda in the following way, but more complicated.
sq_list_map = map(lambda n: n**2, nums)
print(list(sq_list_map))

# even more complication?
if_even = [n for n in nums if n%2 == 0]
print(if_even)

# can also use filter/map and lambda for this as well.
if_even_map = filter(lambda n: n%2 == 0, nums)
print(list(if_even_map))


# More complications? Make a letter number pair, for each letter in ABCD paired to each number.
alphas = 'ABCD'
pairing = [(letter, num) for letter in alphas for num in nums]
print(pairing)

# EvEN MORE? How about some superhero stuff zipping through the city? IN A DICTIONARY??

names = ['Bruce', 'Clark', 'Peter', 'Thor', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Odinson', 'Wolverine', 'Deadpool']

super_power = {name:hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(super_power)


# HOW ABOUT SET COMPREHENSIONS? You don't even know what SET is!!
# SET --> A set is like a list but it has all unique values.

numss = [1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10]

# Normal way of doing things.

# my_set = set()
# for n in numss:
#     my_set.add(n)
# print(my_set)

# Comprehension way is much much simpler!!

my_set = {n for n in numss}
print(m_set)

