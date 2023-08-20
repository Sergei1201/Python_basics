# # Decorators
# def my_decorator(func):
#     def wrap_func():
#         print('Hello')
#         func()
#         print('Goodbye')
#     return wrap_func


# @my_decorator
# def my_function():
#     print('I love programming with Python, Javascript, and PHP')


# @my_decorator
# def my_function2():
#     print('I am also a big fan of C++')


# my_function()
# my_function2()

# Decorators with arguments
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('Hello')
#         func(*args, **kwargs)
#         print('Goodbye')
#     return wrap_func


# @my_decorator
# def my_function(param1, emoji=':)'):
#     print(f'I love {param1} {emoji}')


# my_function('programming with Python, JavaScript, and PHP')

# Performance measurement decorator
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} seconds to complete the task')
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i*2
    return i


long_time()
