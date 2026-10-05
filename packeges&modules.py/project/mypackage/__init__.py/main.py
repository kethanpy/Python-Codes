from .dog import Dog, Cat

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
    animal.eat()