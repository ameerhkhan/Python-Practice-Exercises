#Video --> Python Tutorial: Generators-How to use them and the benefits you recieve. by Corey Schafer

#This is an example I found on youtube to implement Generators in Python.
#Generators can be used to generate lists in which each element is generated when it is asked to be.
#Hence instead of comprehending a complete list in one go GENERATORS allow us to generate one element of a list at a time.
#This helps in parallel processing so that for example the next command that operates on a single element of a list
#Doesn't have to wait for the list to be complete.

#Instead it can work on that single generated element.

#This not only saves processing time but also requires waaaaayy less memory allocation as compared to list comprehension in one go!

#Let's start off with a normal way to return lists.
def square_numbers(nums):
    results = []
    for i in nums:
        results.append(i*i)
    return results
print('Using normal way')
my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

#now let's take a look at how we can do this using generators.
def square_gen(nums):
    for i in nums:
        yield(i*i)

print('Let\'s see our generator element')
gen_nums = square_gen([1,2,3,4,5])
#This returns a generator object. This doesn't hold the entire result but instructions to generate the list(generator element) element by element as asked
print(gen_nums)

#Following is the proper way to get our results.
print('Now using Generators')
print(next(gen_nums))
print(next(gen_nums))
#print(next(gen_nums))
#print(next(gen_nums))
#print(next(gen_nums))

#Once we have generated all elements the generator object cannot produce any more and no result will be output.
#if we use the above method as well as the for loop to generate numbers, the for loop will not print out anything
#OR use a loop.. Simple
print('Using a loop')

for num in gen_nums:
    print(num)

#Generators can also be used in the same way as list comprehensions
#Just use round brackets instead of sqaure brackets, for example,
nums = [1,2,3,4,5]
gen_nums_com = (i*i for i in nums)

#now use same way to print
#Generator elements can also be converted into lists using,

gen_nums_lst = list(gen_nums_com)
print('The list generated')
print(gen_nums_lst)
#The above example is just a preview of what a generator can do.
#Generators are especially useful when you have hundreds of thousands of elements to work on with.
#Using GENERATORS can not only save memory but will allow for a more efficient overall code.