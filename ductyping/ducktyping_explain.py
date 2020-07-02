# Pythonic --> Below two concepts are crucial in understanding Python's ways of programming.
# DUCK TYPING --> You assume that if an object walks like a duck and quacks like a duck. It is a duck.
# EAFP --> Easier to Ask Forgiveness than Permission.

class DuckT:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('flap, flap!')


class Person:

    def quack(self):
        print('I am quacking like a duck')

    def fly(self):
        print('I am flapping my Arms!')

# The below method is not Pythonic at all.
def quack_and_fly(thing):
    #THE following is not Pythonic.
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
    # The following example is not duck typed and hence non pythonic.
    #if isinstance(thing, DuckT): #
    thing.quack()
    thing.fly()
    #else:
        # print('This has to be a duck!')

    print()

def quack_and_fly_pythonic(thing):
    #Example of DUCK TYPING:
    # thing.quack()
    # thing.fly()
    
    # This is Pythonic as well.
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()



d = DuckT()
quack_and_fly_pythonic(d)

p = Person() # In duck typing if person behaves like a duck (i.e. has quack and fly methods) it is a DUCK!!
quack_and_fly(p)



