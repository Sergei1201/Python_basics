# # Iterators
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break


# special_for([1, 2, 3, 4, 5])

# # How iterators work under the hood


# class MyGen:
#     current = 0
#     # Constructor

#     def __init__(self, first_number, last_number):
#         self.first_number = first_number
#         self.last_number = last_number

#     # Iterate
#     def __iter__(self):
#         return self

#     # Next
#     def __next__(self):
#         if self.current < self.last_number:
#             num = self.current
#             self.current += 1
#             return num
#         raise StopIteration


# gen = MyGen(5, 20)
# for i in gen:
#     print(i)

# Exercise with fibonacci numbers           temp = 0 a = 1 b = 0 + 1 = 1  temp = 1 a = 1 b = 1 + 1 = 2
# def fib(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp + b


# for x in fib(21):
#     print(x)

# Exercise with fibonacci numbers using a list
def fib(num):
    a = 0
    b = 1
    my_list = []
    for i in range(num):
        my_list.append(a)
        temp = a
        a = b
        b = temp + b
    return my_list


for x in fib(100):
    print(x)
