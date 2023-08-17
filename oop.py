# # Create a basic class
# class Person:
#     # Constructor
#     def __init__(self, name, age):
#         if age > 17:
#             self.name = name
#             self.age = age
#     # Methods

#     def __str__(self):
#         return f'{self.name} {self.age}'

#     def greeting(self):
#         return f'Hello {self.name}. You are {self.age}'

# # Inheritance


# class Student(Person):
#     # Constructor
#     def __init__(self, name, age, course):
#         # Parent constructor
#         super().__init__(name, age)
#         self.course = course
#     # Student info method

#     def student_into(self):
#         return f'Hello {self.name}. You are {self.age} and studying {self.course}'


# # Instantiate Person class
# person1 = Person('Sergei', 39)
# print(person1.greeting())
# person2 = Person('Julia', 25)
# print(person2.greeting())

# # Instantiate the extended class (Student)
# student1 = Student('Daniil', 18, 'Programming languages')
# print(student1)
# print(student1.greeting())
# print(student1.student_into())

# Define a class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Methods

    def __str__(self):
        return f'{self.name} {self.age}'

    def greeting(self):
        return f'Hello {self.name}. You are {self.age}'


class SecondaryEducation(Person):
    # Constructor
    def __init__(self, name, age, course):
        # Parent constructor
        super().__init__(name, age)
        self.course = course

    def student_info(self):
        return f'Hello {self.name}. You are {self.age} and studying {self.course}'


class Undergraduate(Person):
    # Constructor
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def learner_info(self):
        return f'Hello {self.name}. You are {self.age} and in the {self.grade} grade of your school'

# Multiple inheritance


class Kid(SecondaryEducation, Undergraduate):
    def __init__(self, name, age, course, grade):
        Undergraduate.__init__(self, name, age, grade)
        SecondaryEducation.__init__(self, name, age, course)
        # self.height = height
        # self.weight = weight

    # def kids_info(self):
    #     return f"This kid has the following information: The name is {self.name}, the age is {self.age}, the height is {self.height} santimetres, the weight is {self.weight} kilos. The kid is in the {self.grade} grade and studies {self.course} subject"


# Instantiate parent and child classes
# person1 = Person('Sergei', 39)
# person2 = Person('Julia', 25)

# print(person1)
# print(person2)

# secondary_education1 = SecondaryEducation('Rob', 18, 'Programming')
# print(secondary_education1.greeting())
# print(secondary_education1.student_info())

# undergraduate1 = Undergraduate('Daniil', 8, 2)
# print(undergraduate1.greeting())
# print(undergraduate1.learner_info())

# undergraduate1 = Undergraduate('Daniil', 8, 2)
# print(undergraduate1)
# print(undergraduate1.learner_info())

kid1 = Kid('Danya', 3, 'Speaking', 2)
print(kid1.learner_info())
