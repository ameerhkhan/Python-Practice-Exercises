#Corey Schafer's Tutorials,

#A list is an iterable but not an iterator.

#Iterable --> something that can be looped over.
nums = [1,2,3]

for num in nums:
    print(num)


#How can we tell if something is iterable?

#for something to be iterable they have to have,

# __iter__(): #this function

#print(dir(nums)) #find if above method exists in the list.

#Iterator --> Has a state that it know where it is in current state.
#An iterator has __next__() method in it.
#A list does not have __next()__ method hence it isn't an iterator.

i_nums = nums.__iter__() #or use iter(nums) #produces a list iterator object. Now this object is an iterator.
# print(i_nums)
# print(dir(i_nums))

#now the iterator object is an iterator and can be used in the following way.
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums)) #will give error StopIteration exception. Since iterator doesn't have any more values.

#can also be used as,

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break









