class Butter:
    def __init__(self, location, withRobot=False):
        self.__location = location
        self.__withRobot = withRobot

    def setLocation(self, location):
        self.__location = location

    def setWithRobot(self, withRobot):
        self.__withRobot = withRobot

    def getLocation(self):
        return self.__location

    def getWithRobot(self):
        return self.__withRobot
