from .animal import Animal

class Dog(Animal):

    def sound(self):
        print("Dog says Bow Bow")

    def eat(self):
        print("Dog eats food")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")

    def eat(self):
        print("Cat eats food")