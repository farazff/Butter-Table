from Butter import Butter
from Robot import Robot


class State:
    def __init__(self, robot, butters):
        self.__robot = robot
        self.__butters = butters

    def changeButterSituation(self, whichButter, withRobot):
        Butter(self.__butters[whichButter]).setWithRobot(withRobot)

    def getRobot(self) -> Robot:
        return self.__robot

    def getButters(self):
        return self.__butters

    def setRobot(self, robot):
        self.__robot = robot

    def setButters(self, butters):
        self.__butters = butters
