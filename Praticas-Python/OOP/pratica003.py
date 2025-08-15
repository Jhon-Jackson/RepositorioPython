class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


d = Dog("Meggy")
c = Cat("Francisco")

d.speak()
c.speak()