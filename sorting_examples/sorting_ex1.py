li = [9, 1, 8, 4, 3, 5, 6, 7, 2]

s_li = sorted(li) # --> waah!! sorting function

print(s_li)
print(li)

# How to sort without creating new variable?
# li.sort() # --> sorting method. returns None. But sorts original list in place.
# print(li)

#Descending?
r_li = sorted(li, reverse=True)

li.sort(reverse=True)

print(r_li)
print(li)

#Sorted function can be used to sort any iterable as opposed to sort method, which works on only lists.

tup = (1,2,4,5,6,2,4,7,9)
s_tup = sorted(tup)
# print(tup.sort()) --> Attribute Error... TUPLE has no object sort!!
print(s_tup)


# Similarly sorting a dictionary's keys can also be performed using SORTED function. and returns them in a list.

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)