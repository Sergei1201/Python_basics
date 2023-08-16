# is_old = False
# if is_old:
#     print('You are old enough to drive a car')
# else:
#     print('You are too young to drive a car')
# is_old = True
# is_licenced = True

# if is_old and is_licenced:
#     print('You are eligible to drive a car')
# elif is_old and not is_licenced:
#     print("You don't have a driver's licence and can't drive a car")
# else:
#     print('You are too young to drive a car')

# Ternary operator
# is_friend = True
# can_message = 'Messaging is allowed' if is_friend else 'Messaging is forbidden'
# print(can_message)

# Conditionals
# is_magician = False
# is_expert = False

# # Check if the user is both magician and expert
# if is_magician and is_expert:
#     print('You have truly mastered the game. You are a wizard')
# elif is_magician and not is_expert:
#     print("At least you're getting there")
# elif not is_magician and is_expert:
#     print('You an expert in the game')
# else:
#     print('You need to practise more often to obtain a certain level in the game')

# For Loops
# for item in 'This is a string in Python':
#     print(item)

# Looping through a list
# for item in [1, 2, 3, 4, 5]:
#     print(item)
# # Looping through a set
# for item in {1, 2, 3, 4, 5}:
#     print(item)
# # Looping through a touple
# for item in (1, 2, 3, 4, 5):
#     print(item)

# Nested loops
# for item in [1, 2, 3, 4, 5]:
#     for x in ['a', 'b', 'c']:
#         print(item, x)

# Looping over dictionaries/ objects
# person = {
#     'first_name': "John",
#     'last_name': 'Doe',
#     'age': 35
# }

# # # Looping through the keys of a dictionary/object
# for item in person.keys():
#     print(item)

# # Looping through the values of a dictionary
# for item in person.values():
#     print(item)

# # Looping through the items of a dictionary
# for item in person.items():
#     print(item)

# # Looping through the items of a dictionary - second method
# for k, v in person.items():
#     print(k, v)

# Exercise finding duplicates in a list
# my_list = ['a', 'b', 'c', 'c', 'a', 'd',
#            'e', 'f', 'f', 'g', 'm', 'n', 'a', 'm']
# duplicates = []
# for value in my_list:
#     if my_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
# print(duplicates)

# Functions with parameters
# def say_hello(name):
#     print(f'Hello {name}')

# # Passing an argument into the function when calling it
# say_hello('Sergei')

# Clean code
# def is_even(num):
#     return num % 2 == 0


# print(is_even(53))

# args and kwargs
# *args are represented in a form of a tuple
# ** kwargs on the other hand, are represented as a dictionary
# *args are represented as a tuple
# **kwargs on the other hand, are represented in form of a dictionary which we can iterate through
# *args are positional arguments in a function
# **kwargs are keyword arguments in a function
# def args_and_kwargs(*args, **kwargs):
#     total = 0
#     # Add kwargs values
#     for item in kwargs.values():
#         total += item
#     print(kwargs)
#     return sum(args) + total


# print(args_and_kwargs(1, 2, 3, 4, 5, 6, 7, num7=8, num8=9, num10=10))

# Create a function that finds the max and min numbers in a given list
# def find_min_odd_number(li):
#     odd_list = []
#     for item in li:
#         if item % 2 != 0:
#             odd_list.append(item)
#     return min(odd_list)


# print(find_min_odd_number([100, 50, 90, 101, 25, 19, 27, 18, 55]))


# def find_max_even_number(li):
#     even_list = []
#     for item in li:
#         if item % 2 == 0:
#             even_list.append(item)
#     return max(even_list)


# print(find_max_even_number([3, 7, 22, 35, 37, 99, 101, 102, 96, 206, 301]))
# print(type(True))
