# A recursive function is defined in terms of itself via self-referential expression

# This means that the function will continue to call itself and repeat its behavior until some condition is met
# to return a result.

# All recursive functions share a common structure made up of two parts.
#   - Recursive case--> Decompose original problem into simpler instances of the same problem.
#   - Base case--> Smallest instance of the same problem.

# Let's go through an example.

'''
n! = n * (n-1) * (n-2) * (n-3) * ..... * 1
n! = n * (n-1)!
'''

def factorial_recursive(n):
    if n <= 1: #base case
        return 1
    return n * factorial_recursive(n-1) #recursive case

a = factorial_recursive
print(a(10))

