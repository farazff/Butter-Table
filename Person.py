class Person:
    def __init__(self, location, num):
        self.__haveButter = False
        self.__location = location
        self.__num = num

    def setLocation(self, location):
        self.__location = location

    def setHaveButter(self, haveButter):
        self.__haveButter = haveButter

    def setNum(self, num):
        self.__num = num

    def getLocation(self):
        return self.__location

    def getHaveButter(self):
        return self.__haveButter

    def getNum(self):
        return self.__num
