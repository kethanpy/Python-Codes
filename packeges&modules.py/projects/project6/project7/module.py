class Engine:
    def start(self):
        print("Engine started")


# Composition
class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")



class Vehicle:
    def start(self):
        print("Vehicle started")


class Bike(Vehicle):
    def ride(self):
        self.start()
        print("Bike is riding")