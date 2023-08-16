# Create a basic class
class Person:
    # Constructor
    def __init__(self, name, age):
        if age > 17:
            self.name = name
            self.age = age
    # Methods

    def __str__(self):
        return f'{self.name} {self.age}'

    def greeting(self):
        return f'Hello {self.name}. You are {self.age}'

# Inheritance


class Student(Person):
    # Constructor
    def __init__(self, name, age, course):
        # Parent constructor
        super().__init__(name, age)
        self.course = course
    # Student info method

    def student_into(self):
        return f'Hello {self.name}. You are {self.age} and studying {self.course}'


# Instantiate Person class
person1 = Person('Sergei', 39)
print(person1.greeting())
person2 = Person('Julia', 25)
print(person2.greeting())

# Instantiate the extended class (Student)
student1 = Student('Daniil', 18, 'Programming languages')
print(student1)
print(student1.greeting())
print(student1.student_into())
