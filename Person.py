class Person:
    def __init__(self, location):
        self.__haveButter = False
        self.__location = location

    def setLocation(self, location):
        self.__location = location

    def setHaveButter(self, haveButter):
        self.__haveButter = haveButter

    def getLocation(self):
        return self.__location

    def getHaveButter(self):
        return self.__haveButter
