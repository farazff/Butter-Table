class Robot:
    def __init__(self, location, haveButter=False):
        self.__location = location
        self.__butter = None
        self.__haveButter = haveButter

    def setLocation(self, location):
        self.__location = location

    def setButter(self, butter):
        self.__butter = butter

    def setHaveButter(self, haveButter):
        self.__haveButter = haveButter

    def getLocation(self):
        return self.__location

    def getHutter(self):
        return self.__butter

    def getHaveButter(self):
        return self.__haveButter
