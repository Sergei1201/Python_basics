# Exploring map, filter, zip, and reduce functions in python
from functools import reduce
# map
my_list = [1, 2, 3, 4, 5, 6, 7]
your_list = [8, 9, 10, 11, 12, 13, 14]
their_list = [15, 16, 17, 18, 19, 20, 21]


# def multiply_by2(item):
#     return item*2


# print(list(map(multiply_by2, my_list)))
# print(my_list)

# # filter


# def even_only(item):
#     return item % 2 == 0


# print(list(filter(even_only, my_list)))

# # zip combines two or more iterables together and creates a tuple
# print(list(zip(my_list, your_list, their_list)))


# def accumulate(acc, item):
#     print(acc, item)
#     return acc + item


# print(reduce(accumulate, my_list, 0))

# lambda functions in python
# lambda function is a small anonymous function that you will run just once to perform an action and after that we won't need this functions anymore
# The result of a lambda function returns automatically, therefore we don't need to return it manually in our script

# Using a lambda function with map
# print(list(map(lambda item: item*2, my_list)))
# print(my_list)

# # Using a lambda function with filter
# print(list(filter(lambda item: item % 2 == 0, my_list)))
# print(my_list)

# # Using a lambda function with reduce
# print(reduce(lambda acc, item: acc + item, my_list, 0))
# print(my_list)

# Lambda funtions exercise
# The task #1: you should create a list and square its elements using a lambda function
# The task #2: you should sort a list of tuples based of tuple's second element using a lambda function

# Squaring
# my_list = [1, 2, 3, 4, 5, 6, 7]
# squared_list = list(map(lambda item: item**2, my_list))
# print(squared_list)
# print(my_list)

# # Sorting
# my_list = [(5, -20), (6, -19), (7, -35), (8, 46)]
# my_list.sort(key=lambda x: x[1])
# print(my_list)

# List comprehensions
# Strings
my_list = [char for char in 'Python programming']
# Numbers
my_list2 = [num for num in range(0, 100)]
# List of number multiplied by 2
my_list3 = [num*2 for num in range(0, 100)]
# List of even powered numbers from 0 to 100
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

# Set comprehensions
my_set = {char for char in 'Python programming'}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num*2 for num in range(0, 100)}
my_set4 = {num**2 for num in range(0, 100) if num % 2 == 0}

# Dictionary comprehensions
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict2 = {x: x*2 for x in [1, 2, 3, 4, 5]}
print(my_dict2)

my_dict3 = {k: v*2 for k, v in my_dict.items()}
print(my_dict3)

my_dict4 = {k: v*2 for k, v in my_dict.items() if v > 1}
print(my_dict4)
