from Butter import Butter
from Robot import Robot


class State:
    def __init__(self, robotLocation, locationOfButters):
        self.__robot = Robot(robotLocation)
        self.__butters = []
        for locationOfButter in locationOfButters:
            self.__butters.insert(Butter(locationOfButter))

    def changeButterSituation(self, whichButter, isWithRobot):
        Butter(self.__butters[whichButter]).set_isWithRobot(isWithRobot)

    def get_robot(self):
        return self.__robot

    def get_butters(self):
        return self.__butters

    def set_robot(self, robot):
        self.__robot = robot

    def set_butters(self, butters):
        self.__butters = butters
