a = 10
b = [1, 2, 3, 4, 5, 6, 7]
c = ['a', 'b', 'c']
d = (1,2)
e = 'Another Data Type'

z = lambda q : q**2
#y = lambda q : q%2
#x = lambda q : q == 'a' | q =='b' | q=='c'(q)
w = lambda q : sum(q)
v = lambda q : q.split(' ')

print(z(a))
#y(b)
#x(c)
print(w(d))
print(v(e))
