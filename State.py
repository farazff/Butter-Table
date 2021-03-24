from Butter import Butter


class State:
    def __init__(self, robot, butters):
        self.__robot = robot
        self.__butters = butters

    def changeButterSituation(self, whichButter, withRobot):
        Butter(self.__butters[whichButter]).setWithRobot(withRobot)

    def get_robot(self):
        return self.__robot

    def get_butters(self):
        return self.__butters

    def set_robot(self, robot):
        self.__robot = robot

    def set_butters(self, butters):
        self.__butters = butters
