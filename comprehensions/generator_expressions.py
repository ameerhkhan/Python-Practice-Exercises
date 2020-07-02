nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generators help in save memory required to process as it gives/ yields only one result at a time.

# Normal way
# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# Comprehension

my_gen = (n*n for n in nums) # --> Just use parantheses instead of square brackets.

for i in my_gen:
    print(i)