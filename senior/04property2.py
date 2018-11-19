# python中的property
class Dog(object):
    def __init__(self):
        self.__color = "black"

    def setColor(self,color):
        self.__color = color

    def getColor(self):
        return self.__color
    #getColor和setColor不能更换位置
    color = property(getColor,setColor)

d = Dog()
print(d.getColor())
#d.__color = "white"

d.color = "red"
print(d.color)
#print(d.getColor())
