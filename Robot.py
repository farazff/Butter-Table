class Robot:
    def __init__(self, location, haveButter=False):
        self.__location = location
        self.__haveButter = haveButter

    def set_location(self, location):
        self.__location = location

    def set_isWithRobot(self, haveButter):
        self.__haveButter = haveButter

    def get_location(self):
        return self.__location

    def get_isWithRobot(self):
        return self.__haveButter
