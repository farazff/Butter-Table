class State:
    def __init__(self, robot, butters):
        self.__robot = robot
        self.__butters = butters

    def getRobot(self):
        return self.__robot

    def getButters(self) -> list:
        return self.__butters

    def setRobot(self, robot):
        self.__robot = robot

    def setButters(self, butters):
        self.__butters = butters
