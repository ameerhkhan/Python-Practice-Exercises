# Variable scopes --> One of the more important concepts.
# Also helps in debugging specially when a variable doesn't have expected value.
# Variable scope --> Determines where our variable can be accessed from within our program.

# Common Abbreviation for understanding scoping rules in Python
# This is the path Python chooses when finding a variable.

# L E G B
# Local, Enclosing, Global, Built-In

# Local --> Variables defined within a function.
# Enclosing --> Variables in the local scope of an enclosing function
# Global --> Variables defined at the top level or assigned global decorator?
# Built-In --> Variables within Python.

# GLOBAL & LOCAL Scope:

x = 'global x' #This is a global variable.

def test(z): # --> here z is also a local variable within this test function and will only reside within this function.
    global x # --> Allows us to change above global x variable within a function and makes any variable global
             #     Above is not a very good way to assign variables. Use as less times as possible.

    # y = 'Local y' # --> Local variable to test function
    x = 'local x' # --> this local variable resides only in this test function.
    # print(y) 
    # print(x)
    print(z)



test('local z')
test.x = 'Does it work' #NO!!


#BUILT IN:
import builtins

def my_min():            #This will not bypass the builtin module but if you name it only min() builtin module will be bypassed.
    pass
    
m = min([8, 1, 4, 6, 9]) #here min is a built-in function in python.
print(m)

#print(dir(builtins))


#ENCLOSING:

def outer():
    x = 'outer x'     # --> Enclosing scope variable. Not affected by inner()'s assignment of x.

    def inner():
        nonlocal x    # --> Now we can affect x assigned in outer() function.
        x = 'inner x' # --> if this is commented 'outer x' is printed and that is why it is called enclosing scope variable.
        print(x)      # --> prints inner x because python found a local variable.

    inner()
    print(x)

outer()

# Conclusion,
# Python finds the variable using Scopes.
# First it tries to find a variable in Local scope,
# if it doesn't find it there then Python looks in Enclosing scope,
# and then Global scope
# and finally Built-in scope (where it basically looks for an error.)

