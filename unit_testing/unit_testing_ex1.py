import unittest

#Testing projects/code is the most exciting thing you can do.
#gives more confidence in your code.

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x/y


