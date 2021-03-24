class Robot:
    def __init__(self, location, haveButter=False):
        self.__location = location
        self.__butter = None
        self.__haveButter = haveButter

    def set_location(self, location):
        self.__location = location

    def set_butter(self, butter):
        self.__butter = butter

    def set_haveButter(self, haveButter):
        self.__haveButter = haveButter

    def get_location(self):
        return self.__location

    def get_butter(self):
        return self.__butter

    def get_haveButter(self):
        return self.__haveButter
