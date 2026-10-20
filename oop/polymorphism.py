class Dog:

    def sound(self):
        print("Bark")

    def eat(self):
        print("Dog is eating")


class Cat:

    def sound(self):
        print("Meow")

    def eat(self):
        print("Cat is eating")


class Cow:

    def sound(self):
        print("Moo")

    def eat(self):  
        print("Cow is eating")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

for animal in animals:
    animal.eat()