from collections import namedtuple

color = (55, 155, 255) # --> Regular Tuple (R, G, B), Are immutable

print(color[0])

# Use a dictionary?

color_dct = {
    'red': 55,
    'green': 155,
    'blue': 255
}

print(color_dct['red'])
# Named Tuples are a good compromise to use dictionary type formatting but in a tuple.

Color = namedtuple('Color', ['red', 'green', 'blue'])

color_named = Color(55, 155, 255)
color_n = Color(red=1, blue=101, green=201)
white = Color(255, 255, 255)

print(color_named[0])
print(color_named.red)
print(color_n.red)
print(white.blue)


#A lot more readable, and much more precise than a dictionary.
# A lot more readable than a normal tuple, and more concise than a dictionary.
