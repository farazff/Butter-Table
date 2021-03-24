class Person :
    def __init__(self,location):
        self.__haveButter=False
        self.__location=location

    def set_location(self, location):
        self.__location = location

    def set_haveButter(self, haveButter):
        self.__haveButter = haveButter

    def get_location(self):
        return self.__location

    def get_haveButter(self):
        return self.__haveButter