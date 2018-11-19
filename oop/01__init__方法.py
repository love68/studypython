class Animal(object):
    
    def __init__(self,name):
        self.__name = name
    
    def work(self):
        print(self.__name)

animal = Animal("动物1")

animal.work()



