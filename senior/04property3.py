# python中的property
class Dog(object):
    def __init__(self):
        self.__color = "black"
    

    @property
    def color(self):
        return self.__color

    
    @color.setter
    def color(self,color):
        self.__color = color


d = Dog()
d.color = "red"
print(d.color)
