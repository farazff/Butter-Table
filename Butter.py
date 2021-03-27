class Butter:
    def __init__(self, location, num, withRobot=False):
        self.__location = location
        self.__withRobot = withRobot
        self.__num = num

    def setLocation(self, location):
        self.__location = location

    def setWithRobot(self, withRobot):
        self.__withRobot = withRobot

    def setNum(self, num):
        self.__num = num

    def getLocation(self):
        return self.__location

    def getWithRobot(self):
        return self.__withRobot

    def getNum(self):
        return self.__num
