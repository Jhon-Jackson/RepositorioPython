
# Define a Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#  Add Methods to Class
    def greet(self):
        return f'Hello, I´m {self.name}'

# Class Variables vs Instance Variables
class Dog:
    species = 'Canine'

    def __init__(self, name):
        sel.name = name

# Inheritance
class Animal:
    def speak(self):
        return 'Sound'

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return super().speak() + " Meow"

class Book:
    def __init__(self, title):
        self.title = title
        def _str_(self):
            return print(f'Book: {self.title}')

# Create an Object
p1 = Person("Jhon", 31)
print(p1.name)
print(p1.age)

# Call Method
print(p1.greet())
print(Dog)
print(Cat)
print(Book)

