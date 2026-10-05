# 6. Create a class in a module that uses private attributes and 
# @property / @setter decorators. Import the class into another 
# module and show how encapsulation protects the data while 
# still allowing controlled access. 

class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    @property
    def name(self):
        return self.__name

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")