class Butter:
    def __init__(self, location, isWithRobot=False):
        self.__location = location
        self.__isWithRobot = isWithRobot

    def set_location(self, location):
        self.__location = location

    def set_isWithRobot(self, isWithRobot):
        self.__isWithRobot = isWithRobot

    def get_location(self):
        return self.__location

    def get_isWithRobot(self):
        return self.__isWithRobot
