# python中的property
class Dog(object):
    def __init__(self):
        self.__color = "black"

    def setColor(self,color):
        self.__color = color

    def getColor(self):
        return self.__color

d = Dog()
print(d.getColor())
#d.__color = "white"

print(d.getColor())
