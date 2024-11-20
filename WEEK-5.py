class Animal:
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        return "Flying through the sky! 🐦"

class Fish(Animal):
    def move(self):
        return "Swimming in the ocean! 🐟"

class Dog(Animal):
    def move(self):
        return "Running on land! 🐕"

# Example Usage
animals = [Bird(), Fish(), Dog()]

for animal in animals:
    print(animal.move())
