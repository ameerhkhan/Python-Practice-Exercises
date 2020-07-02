# What if I has a list of integers and I wanted to sort based on their absolute values?

li = [-6, -5, -4, 1, 2, 3]

s_li = sorted(li) # Normal sorting
print(s_li)

a_li = sorted(li, key=abs) # based on absolute values.
print(a_li)

