#Actual usage of Iterator or Iterables.

class MyRange: #lets create an iterator of our own.
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        #iter method returns an iterator.
        return self
    
    def __next__(self):
        #to work through the iterator.
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    

nums = MyRange(1, 10)

for num in nums:
    print(num)

#print(next(nums)) #will raise an exception of StopIteration.


#following is a generator for above class with similar functionality.
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

numbs = my_range(1, 10) #use my_range(1) to loop over one value at a time, indefinitely.

#Maybe useful for new values coming in every few seconds.
#Updating news and stuff.
#can be used for cracking passwords. Attempting brute force attack one attack at a time.
#used for memory efficient programming.

for nums in numbs:
    print(nums)

