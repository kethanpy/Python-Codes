from module_a import Animal
from module_b import Walkable


class Dog(Animal, Walkable):

    def sound(self):
        print("Dog says Bow Bow")

    def move(self):
        print("Dog is walking")