class animal: #base class or parent class
    def eat(self):
        print("Animal is eating")

class dog(animal): #derived class or child class
    def bark(self):
        print("Dog is barking")

dog1 = dog()
dog1.eat()  # Output: Animal is eating
dog1.bark()  # Output: Dog is barking